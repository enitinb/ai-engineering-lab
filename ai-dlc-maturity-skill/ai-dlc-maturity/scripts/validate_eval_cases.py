#!/usr/bin/env python3
"""Validate the structure of the skill eval cases file (tests/skill-eval-cases.jsonl).

Each line must be a JSON object with:
- skills: non-empty list of skill names (must include "ai-dlc-maturity")
- query: non-empty string
- expected_behavior: non-empty list of non-empty strings (checkable criteria)

This checks structure only. It does not run the skill; use the criteria in
expected_behavior as the rubric when grading model output (see tests/README.md).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

EXPECTED_SKILL = "ai-dlc-maturity"
DEFAULT_CASES = Path(__file__).resolve().parents[1] / "tests" / "skill-eval-cases.jsonl"


def validate_case(case: object, line_no: int) -> list[str]:
    errors: list[str] = []
    if not isinstance(case, dict):
        return [f"line {line_no}: not a JSON object"]

    skills = case.get("skills")
    if not isinstance(skills, list) or not skills:
        errors.append(f"line {line_no}: 'skills' must be a non-empty list")
    elif EXPECTED_SKILL not in skills:
        errors.append(f"line {line_no}: 'skills' should include '{EXPECTED_SKILL}'")

    query = case.get("query")
    if not isinstance(query, str) or not query.strip():
        errors.append(f"line {line_no}: 'query' must be a non-empty string")

    behaviors = case.get("expected_behavior")
    if not isinstance(behaviors, list) or not behaviors:
        errors.append(f"line {line_no}: 'expected_behavior' must be a non-empty list")
    elif any(not isinstance(b, str) or not b.strip() for b in behaviors):
        errors.append(f"line {line_no}: every 'expected_behavior' item must be a non-empty string")

    return errors


def main() -> int:
    cases_path = Path(sys.argv[1]) if len(sys.argv) == 2 else DEFAULT_CASES
    if not cases_path.exists():
        print(f"Eval cases file not found: {cases_path}", file=sys.stderr)
        return 2

    errors: list[str] = []
    count = 0
    with cases_path.open("r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            if not raw.strip():
                continue
            count += 1
            try:
                case = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: invalid JSON ({exc.msg})")
                continue
            errors.extend(validate_case(case, line_no))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"\n{len(errors)} problem(s) found across {count} case(s).", file=sys.stderr)
        return 1

    print(f"All {count} eval case(s) are well-formed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
