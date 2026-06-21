# Asset Map

AI Route Advisor is a Claude Skill backed by a small policy and schema library. The skill is designed to be useful as a standalone Claude workflow and as a technical artifact that can be adapted into intake forms, architecture reviews, governance boards, or automated workflows.

## Runtime path

```text
User AI use case
  -> ai-route-advisor/SKILL.md
  -> references/task-taxonomy.yaml
  -> references/data-classification.yaml
  -> references/model-tiers.yaml
  -> references/governance-controls.yaml
  -> references/eval-scorecards.yaml
  -> references/cost-controls.yaml
  -> schemas/recommendation.schema.json
  -> R.E.S.E.T. recommendation card
```

## File purposes

| File or folder | Used for |
| --- | --- |
| `SKILL.md` | Skill trigger, decision process, output contract, and style rules |
| `references/task-taxonomy.yaml` | Generic task classification across any use case |
| `references/data-classification.yaml` | Data sensitivity classification and default controls |
| `references/model-tiers.yaml` | Generic AI route recommendation rules |
| `references/governance-controls.yaml` | Guardrail selection for governed workflows |
| `references/eval-scorecards.yaml` | Eval level and evaluation-dimension guidance |
| `references/cost-controls.yaml` | Cost-control recommendations by pattern |
| `schemas/recommendation.schema.json` | Machine-readable output contract |
| `examples/` | Golden examples for style and behavior |
| `scripts/validate_recommendation.py` | Local validation of JSON recommendations |
| `scripts/estimate_cost.py` | Vendor-neutral cost estimation with user-provided assumptions |
| `scripts/requirements.txt` | Optional local dependencies for validation scripts |
| `tests/skill-eval-cases.jsonl` | Manual eval cases for trigger, routing, and output quality checks |

## Design principle

The skill recommends route types, not named tools. It helps teams think clearly before implementation by classifying the work, identifying the risk, defining the proof required, and choosing the smallest safe route that can clear the quality bar.
