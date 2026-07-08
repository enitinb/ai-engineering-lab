#!/usr/bin/env python3
"""Validate a R.E.S.E.T. recommendation JSON file against the bundled schema."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:
    raise SystemExit("Missing dependency: run `pip install -r scripts/requirements.txt`.") from exc

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "recommendation.schema.json"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_recommendation.py recommendation.json", file=sys.stderr)
        return 2

    data_path = Path(sys.argv[1])
    if not data_path.exists():
        print(f"Recommendation file not found: {data_path}", file=sys.stderr)
        return 2

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Recommendation file is not valid JSON: {exc.msg} (line {exc.lineno})", file=sys.stderr)
        return 1

    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.ValidationError as exc:
        print(f"Invalid R.E.S.E.T. recommendation: {exc.message}", file=sys.stderr)
        return 1

    print(f"Valid R.E.S.E.T. recommendation: {data_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
