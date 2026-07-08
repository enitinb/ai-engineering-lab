# Claude Skill best-practice notes used in this package

This package follows current Claude Skill guidance and is structured for progressive disclosure.

## What this package follows

- `SKILL.md` is concise and points to supporting files instead of embedding every taxonomy, control, and example.
- The YAML frontmatter uses the required `name` and `description` fields only.
- The skill name is lowercase kebab-case and avoids reserved words.
- The description is third-person, specific, and trigger-oriented.
- Reference files are linked one level deep from `SKILL.md`.
- Paths use forward slashes.
- Scripts are optional, local, deterministic utilities and are not required for normal recommendation cards.
- Script dependencies are listed in `scripts/requirements.txt` and referenced from `SKILL.md`.
- The repo includes concrete eval cases in `tests/skill-eval-cases.jsonl` using the Anthropic eval shape (`skills`, `query`, `expected_behavior`), with `tests/validate_eval_cases.py` for an offline structure check and `tests/README.md` for the run workflow.
- The core logic avoids time-sensitive model rankings, named-provider defaults, and vendor-specific decisions.

## Recommended manual checks

1. Ask Claude when it would use `ai-route-advisor` and confirm it mentions AI use-case classification, model-tier intake, governance guardrails, eval planning, and cost controls.
2. Run the cases in `tests/skill-eval-cases.jsonl` and grade each response against its `expected_behavior` rubric (see `tests/README.md`).
3. Check that routine requests produce a recommendation card without reading every reference file.
4. Check that JSON validation scripts run only when explicitly requested.
5. Iterate if Claude ignores a key reference, overuses a reference, or asks unnecessary follow-up questions.
