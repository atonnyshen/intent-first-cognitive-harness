#!/usr/bin/env python3
"""Validate the small public working-brief contract without third-party packages."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = ("raw_request", "subject", "user_job", "desired_outcome", "deliverable", "readiness")
READINESS = {"PASS_THROUGH", "READY", "ASK", "BLOCKED_USER_INPUT"}


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["brief must be a JSON object"]
    for key in REQUIRED:
        if key not in data:
            errors.append(f"missing required field: {key}")
    for key in ("raw_request", "subject", "desired_outcome", "deliverable"):
        if key in data and (not isinstance(data[key], str) or not data[key].strip()):
            errors.append(f"{key} must be a non-empty string")
    if "user_job" in data and not isinstance(data["user_job"], dict):
        errors.append("user_job must be an object")
    if data.get("readiness") not in READINESS:
        errors.append("readiness must be one of PASS_THROUGH, READY, ASK, BLOCKED_USER_INPUT")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} BRIEF.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read brief: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
