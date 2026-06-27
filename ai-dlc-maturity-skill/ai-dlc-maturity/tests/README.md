# Evals for the AI-DLC Maturity Advisor skill

`skill-eval-cases.jsonl` is the source of truth for measuring whether the skill
behaves correctly. Each line follows the Anthropic Agent Skills eval shape:

```json
{
  "skills": ["ai-dlc-maturity"],
  "query": "the user message that should exercise the skill",
  "expected_behavior": ["checkable criterion 1", "checkable criterion 2"]
}
```

`expected_behavior` is a rubric: a list of concrete, independently checkable
statements about a correct response. There is no built-in runner for skill
evals, so you grade output against these criteria. The cases cover every mode:
first-time intro, `--help`, `--framework`, `--questions`, `--evidence`, a broad
discovery question, artifact preparation, a full assessment from context,
continuing from a completed intake, `--review`, `--brownfield`, `--card-only`,
and `--json-only`.

## 1. Check the eval file is well-formed (offline)

```bash
cd ai-dlc-maturity
python scripts/validate_eval_cases.py
```

This checks structure only (valid JSON, required fields, the skill name). It does
not run the skill.

## 2. Run the cases against a model

Install the skill (see the project QUICKSTART), then for each case:

1. Start a fresh session with the skill loaded.
2. Send the `query`.
3. Grade the response against every item in `expected_behavior`. A case passes
   only when all criteria hold.

You can grade manually, or automate it with an LLM judge: prompt a model with the
response plus the `expected_behavior` list and ask it to return pass/fail per
criterion. Either way, `expected_behavior` is the rubric.

## 3. Validate any generated JSON output

Cases that produce inline JSON (the full-assessment and `--json-only` cases)
should conform to the schema. Copy the JSON to a file and run:

```bash
cd ai-dlc-maturity
pip install -r scripts/requirements.txt
python scripts/validate_assessment.py assessment.json
```

## 4. Test across models

Per Anthropic's skill best practices, run the cases on each model you plan to use
(for example Haiku, Sonnet, and Opus). Guidance that is enough for a stronger
model may need more detail for a faster one. Note any case that regresses on a
given model and refine the skill instructions accordingly.
