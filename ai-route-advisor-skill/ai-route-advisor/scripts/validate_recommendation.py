#!/usr/bin/env python3
"""Validate a R.E.S.E.T. recommendation JSON file against the bundled schema."""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Missing dependency: jsonschema. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "recommendation.schema.json"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_recommendation.py recommendation.json", file=sys.stderr)
        return 2
    data_path = Path(sys.argv[1])
    schema = json.loads(SCHEMA.read_text())
    data = json.loads(data_path.read_text())
    jsonschema.validate(data, schema)
    print(f"Valid R.E.S.E.T. recommendation: {data_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
