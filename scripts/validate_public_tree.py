#!/usr/bin/env python3
"""Validate the generated public tree without network access."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

FORBIDDEN_NAMES = {".DS_Store", "__pycache__", "task_plan.md", "findings.md", "progress.md"}
_WEB_CORPUS = "web_" + "questions.jsonl"
_MASTER_PROMPT = "00_" + "MASTER_PROMPT"
_USERS_ROOT = "/" + "Users/"
_HOME_ROOT = "/" + "home/"
_WINDOWS_USERS = "C:" + "\\Users\\"
FORBIDDEN_SUBSTRINGS = (_WEB_CORPUS, _MASTER_PROMPT, _USERS_ROOT, _HOME_ROOT, _WINDOWS_USERS)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f"symlink is not allowed: {relative}")
            continue
        if any(part in FORBIDDEN_NAMES or part.endswith(".pyc") for part in relative.parts):
            errors.append(f"forbidden artefact: {relative}")
            continue
        if path.is_file():
            data = path.read_bytes()
            text = data.decode("utf-8", errors="replace")
            for marker in FORBIDDEN_SUBSTRINGS:
                if marker in text or marker in str(relative):
                    errors.append(f"forbidden marker {marker!r}: {relative}")
    skill = root / "SKILL.md"
    if not skill.is_file() or not re.search(r"^name:\s*intent-first-cognitive-harness\s*$", skill.read_text(encoding="utf-8"), re.MULTILINE):
        errors.append("SKILL.md has no neutral public name")
    for readme in (root / "README.md", root / "README.zh-TW.md"):
        if not readme.is_file():
            errors.append(f"missing README: {readme.name}")
        else:
            for target in LINK_RE.findall(readme.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not (readme.parent / target).resolve().is_file():
                    errors.append(f"unresolved README link: {readme.name} -> {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        print("INVALID")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
