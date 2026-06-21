#!/usr/bin/env python3
"""Validate an AI-DLC maturity assessment JSON file against the bundled schema."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:
    raise SystemExit("Missing dependency: run `pip install -r scripts/requirements.txt`.") from exc


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_assessment.py assessment.json", file=sys.stderr)
        return 2

    assessment_path = Path(sys.argv[1])
    if not assessment_path.exists():
        print(f"Assessment file not found: {assessment_path}", file=sys.stderr)
        return 2

    schema_path = Path(__file__).resolve().parents[1] / "schemas" / "maturity-assessment.schema.json"
    with schema_path.open("r", encoding="utf-8") as f:
        schema = json.load(f)
    with assessment_path.open("r", encoding="utf-8") as f:
        assessment = json.load(f)

    try:
        jsonschema.validate(instance=assessment, schema=schema)
    except jsonschema.ValidationError as exc:
        print(f"Invalid assessment JSON: {exc.message}", file=sys.stderr)
        return 1

    print("Assessment JSON is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
