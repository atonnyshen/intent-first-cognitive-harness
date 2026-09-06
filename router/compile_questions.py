#!/usr/bin/env python3
"""Compile a small route JSON document into observable question pools."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def compile_route(route: dict) -> dict:
    pools = {"analysis_questions": [], "research_questions": [], "user_questions": [], "critic_questions": []}
    for question in route.get("questions", []):
        if not isinstance(question, dict) or not question.get("text"):
            continue
        kind = question.get("kind", "analysis")
        target = {
            "analysis": "analysis_questions",
            "research": "research_questions",
            "user": "user_questions",
            "critic": "critic_questions",
        }.get(kind)
        if target is not None:
            pools[target].append({"id": question.get("id", f"q{len(pools[target]) + 1}"), "text": question["text"]})
    unresolved = [item for item in route.get("required_inputs", []) if item not in route.get("resolved_inputs", [])]
    return {"status": "NEEDS_INPUT" if unresolved else "READY", "unresolved": unresolved, **pools}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("route", type=Path)
    args = parser.parse_args()
    route = json.loads(args.route.read_text(encoding="utf-8"))
    print(json.dumps(compile_route(route), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
