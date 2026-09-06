#!/usr/bin/env python3
"""Build a public tree from the checked-in allowlist.

The script uses only the Python standard library and is intentionally fail-closed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

FORBIDDEN_PARTS = {".DS_Store", "__pycache__", ".pyc", "task_plan.md", "findings.md", "progress.md"}
_WEB_CORPUS = "web_" + "questions.jsonl"
_MASTER_PROMPT = "00_" + "MASTER_PROMPT"
_USERS_ROOT = "/" + "Users/"
_HOME_ROOT = "/" + "home/"
_WINDOWS_USERS = "C:" + "\\Users\\"
FORBIDDEN_SUBSTRINGS = (_WEB_CORPUS, _MASTER_PROMPT, _USERS_ROOT, _HOME_ROOT, _WINDOWS_USERS)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?:ghp|github_pat)_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?:sk|rk)-[A-Za-z0-9_-]{20,}"),
)


def manifest_paths(manifest: Path) -> list[str]:
    paths: list[str] = []
    in_paths = False
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if line.strip() == "paths:":
            in_paths = True
            continue
        if in_paths and line.startswith("  - "):
            paths.append(line[4:].strip().strip('"\''))
    if not paths:
        raise ValueError("manifest contains no paths")
    return paths


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"unsafe manifest path: {value}")
    return path


def scan_bytes(relative: str, content: bytes) -> list[str]:
    errors: list[str] = []
    if any(part in FORBIDDEN_PARTS or part.endswith(".pyc") for part in Path(relative).parts):
        errors.append(f"forbidden artefact: {relative}")
    text = content.decode("utf-8", errors="replace")
    for marker in FORBIDDEN_SUBSTRINGS:
        if marker in text or marker in relative:
            errors.append(f"forbidden marker {marker!r}: {relative}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            errors.append(f"secret-like content: {relative}")
    return errors


def build(package_root: Path, output: Path, force: bool) -> dict:
    manifest = package_root / "open-source" / "public-release-manifest.yaml"
    source_root = package_root / "open-source" / "public"
    paths = manifest_paths(manifest)
    if output.exists():
        if not force:
            raise FileExistsError(f"output exists; use --force to replace: {output}")
        if output.is_dir() and not output.is_symlink():
            shutil.rmtree(output)
        else:
            output.unlink()
    output.mkdir(parents=True)
    errors: list[str] = []
    records: list[dict] = []
    for raw in paths:
        relative = safe_relative(raw)
        source = source_root / relative
        destination = output / relative
        if not source.is_file() or source.is_symlink():
            errors.append(f"missing or symlinked source: {relative}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        content = source.read_bytes()
        errors.extend(scan_bytes(raw, content))
        destination.write_bytes(content)
        records.append({"path": raw, "sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)})
    if errors:
        raise RuntimeError("public build rejected:\n" + "\n".join(f"- {error}" for error in errors))
    manifest_record = {"schema_version": "0.1", "source_manifest": "open-source/public-release-manifest.yaml", "files": records}
    (output / "public-repo-manifest.json").write_text(json.dumps(manifest_record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [f"{record['sha256']}  {record['path']}" for record in records]
    (output / "public-repo-sha256.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return manifest_record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    record = build(args.package_root.resolve(), args.output.resolve(), args.force)
    print(f"built {len(record['files'])} public files at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
