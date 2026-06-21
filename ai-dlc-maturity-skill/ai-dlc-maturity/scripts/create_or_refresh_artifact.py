#!/usr/bin/env python3
"""Create the default AI-DLC maturity assessment artifact if it does not exist.

This helper is optional. Claude can also create or update the Markdown file directly.
It preserves an existing artifact by default.
"""
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = ROOT / "references" / "assessment-artifact-template.md"
DEFAULT_OUTPUT = ROOT / "outputs" / "ai-dlc-maturity-assessment.md"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--force", action="store_true", help="overwrite existing artifact")
    args = parser.parse_args()

    output = Path(args.output)
    if output.exists() and not args.force:
        print(f"Artifact already exists: {output}")
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(DEFAULT_TEMPLATE.read_text(), encoding="utf-8")
    print(f"Created artifact: {output}")


if __name__ == "__main__":
    main()
