# Asset map

This Skill uses progressive disclosure. `SKILL.md` contains routing and workflow instructions. Supporting files provide assessment content only when needed.

| Asset | Purpose |
|---|---|
| `references/maturity-model.yaml` | Maturity levels and scoring rules |
| `references/lifecycle-activities.yaml` | Intent-to-Work, Build-and-Validate, Run-and-Learn checks |
| `references/review-dimensions.yaml` | Six review dimensions and evidence examples |
| `references/people-process-alignment.yaml` | People, ownership, decision rights, process, and feedback loop checks |
| `references/assessment-questions.yaml` | Review questions grouped by lifecycle and dimension |
| `references/brownfield-questions.yaml` | Legacy and brownfield-specific checks |
| `references/evidence-catalog.yaml` | Strong and weak evidence examples |
| `references/improvement-actions.yaml` | Recommended improvement actions |
| `references/assessment-artifact-template.md` | Canonical living Markdown artifact containing questions, answers, assessment, actions, and inline JSON |
| `references/intake-template.md` | Legacy intake-only reference kept for compatibility |
| `references/output-format.md` | Readable card and JSON output shape |
| `schemas/maturity-assessment.schema.json` | Inline JSON schema |
| `scripts/validate_assessment.py` | Optional local JSON validation |
| `examples/` | Concrete output references |
| `tests/skill-eval-cases.jsonl` | Manual evaluation cases |

## Assessment artifact workflow

`references/assessment-artifact-template.md` is used when the customer starts broadly, such as “we are using AI in our SDLC, are we doing it right?” The Skill should start one living Markdown artifact, preferably at `outputs/ai-dlc-maturity-assessment.md` when file access is available.

The same artifact persists through the workflow. First it contains questions and answer placeholders. After the customer fills it, the Skill updates the assessment sections below the answers with maturity findings, people/process findings, top gaps, priority actions, assumptions, and an inline JSON snapshot.

## Generated outputs

`outputs/` is available for the living assessment artifact. The Skill should not create separate JSON files unless the user explicitly requests an export.
