---
name: ai-route-advisor
description: Classifies AI use cases before model selection. Use for AI route tier, model-tier intake, sensitivity, governance guardrails, eval plans, cost controls, or R.E.S.E.T. decisions.
---

# AI Route Advisor

Choose the right AI route before you choose the model. Powered by R.E.S.E.T.: Right-size, Evaluate, Spend, Enforce, and Test.

AI Route Advisor helps teams decide how an AI use case should be handled before choosing a model, provider, or implementation path. It classifies the work, assesses sensitivity and complexity, recommends an AI route type, identifies required controls, and suggests an evaluation plan.

## Core rule

Recommend the smallest safe model tier that can meet the quality bar. Governance comes before cost optimization when the work involves sensitive data, regulated information, customer impact, source code, or external actions.

## Use this workflow

1. Infer the use case, task type, data sensitivity, complexity, volume, latency need, and business impact from the user's description.
2. Ask a follow-up only when a missing detail would materially change the recommendation. If there is enough information, proceed and mark uncertainty.
3. Classify the work using `references/task-taxonomy.yaml`.
4. Classify sensitivity using `references/data-classification.yaml`.
5. Select a generic route type using `references/model-tiers.yaml`.
6. Apply guardrails from `references/governance-controls.yaml` before cost optimization.
7. Recommend eval dimensions using `references/eval-scorecards.yaml`.
8. Recommend cost controls using `references/cost-controls.yaml`.
9. Return a human-readable recommendation card first, then an inline JSON block that follows `schemas/recommendation.schema.json`.
10. Do not save JSON to a file unless the user explicitly asks for a file. The JSON block is for copy/paste, automation, or downstream intake.
11. Use `examples/` only as style and output references, not as fixed templates.

## Supporting files

This skill is intentionally generic and scalable. Keep the core workflow in this file and load supporting files only when the recommendation needs more detail. This follows progressive disclosure so routine recommendations stay focused while specialized guidance remains available.

- `references/task-taxonomy.yaml`: task categories and complexity signals.
- `references/data-classification.yaml`: public, internal, confidential, customer, employee, regulated, and unknown sensitivity classes.
- `references/model-tiers.yaml`: generic AI route types and when to use or avoid each route.
- `references/governance-controls.yaml`: controls for sensitive data, external actions, review, monitoring, and production change.
- `references/eval-scorecards.yaml`: light, required, and red-team evaluation dimensions.
- `references/cost-controls.yaml`: batching, caching, output caps, retrieval limits, sampled QA, validation, and escalation controls.
- `schemas/recommendation.schema.json`: canonical machine-readable recommendation format.
- `examples/`: reference examples for expected recommendation style and scope.
- `scripts/validate_recommendation.py`: optional local validation when a user provides or requests JSON validation.
- `scripts/estimate_cost.py`: optional local cost estimation when a user provides token counts, request volume, and route pricing assumptions.
- `scripts/requirements.txt`: optional package requirements for local validation.

Do not recommend named vendors, products, or specific models unless the user explicitly provides an approved model catalog or asks for named options.

## Invocation modes and flags

When the user invokes `/ai-route-advisor` without a use case, treat it as a first-time experience. Do not produce a recommendation or JSON. Introduce AI Route Advisor in a compact way, explain that it helps teams classify AI work before model selection, recommend a generic AI route, identify guardrails, define eval needs, and control cost. Explain R.E.S.E.T. in one short paragraph, then show one usage example.

Support these user-facing flags:

- `--help`: Explain what the skill does, when to use it, what input to provide, and show two short examples.
- `--reset`: Explain the R.E.S.E.T. framework: Right-size, Evaluate, Spend, Enforce, and Test.
- `--schema`: Show the JSON fields and what each field means, without creating a file.
- `--examples`: Show three sample use cases and the route type each would likely receive.
- `--card-only`: Return only the human-readable recommendation card, with no JSON block.
- `--json-only`: Return only the JSON object that follows `schemas/recommendation.schema.json`.
- `--validate-json`: Validate JSON that the user pastes in the chat. Use `scripts/validate_recommendation.py` only if local execution is available and the user asks for validation.
- `--estimate-cost`: Estimate rough cost only when the user provides token counts, request volume, and route pricing assumptions. Use `scripts/estimate_cost.py` only when needed.

Default behavior is card plus inline JSON. Do not write files, create artifacts, or save JSON unless the user explicitly asks.


## Script usage rules

Do not run scripts for normal recommendation cards. Run scripts only when the user asks for JSON validation, cost estimation, or local operationalization. If a script dependency is missing, say to install local requirements with `python -m pip install -r scripts/requirements.txt`. Use forward-slash paths only.

- Validate JSON: `python scripts/validate_recommendation.py recommendation.json`
- Estimate cost: `python scripts/estimate_cost.py --input-tokens 2000 --output-tokens 500 --requests 1000 --input-price-per-million 1 --output-price-per-million 5`

## R.E.S.E.T. decision process

### R: Right-size the request

Classify the task before recommending a route. Simple work usually includes extraction, classification, formatting, tagging, short summarization, and simple rewriting. Medium work usually includes longer summarization, business drafting, customer support assistance, structured analysis, and routine decision support. High-complexity work usually includes deep reasoning, architecture review, complex coding, strategy, multi-document synthesis, high-stakes analysis, and agentic workflows.

### E: Evaluate on the user's data

Recommend an evaluation level based on risk and impact. Low-risk internal workflows may need a lightweight eval, while customer-facing, regulated, coding, financial, legal, healthcare, or high-impact workflows require stronger evaluation before production.

### S: Spend by tier

Recommend an AI route type, not a named vendor or model. Use generic routes: low-cost tier, mid-tier, frontier or reasoning tier, approved enterprise route, human-review route, and evaluation queue. Frame cost as cost per correct outcome, including retries, review effort, latency, context size, caching, batching, and escalation.

### E: Enforce guardrails

If the work involves customer data, employee data, confidential documents, source code, financial records, legal content, healthcare data, regulated information, or external actions, recommend controls before optimization.

### T: Test before you tear out

When the user is considering a new model or changing an existing workflow, recommend testing before switching. The new route should be compared against the current route using the same evaluation criteria.

## Output format

Use this output by default: a readable card first, followed by an inline JSON object. The JSON must be shown in the chat response only. Do not save it anywhere unless the user explicitly asks.

If the user passes `--card-only`, omit the JSON. If the user passes `--json-only`, omit the card.

# R.E.S.E.T. Recommendation

**Use case:**  
[Brief description]

**Classification:**
- Task type:
- Complexity:
- Data sensitivity:
- Volume:
- Latency need:
- Business impact:

**Recommended AI route:**  
[Low-cost tier, mid-tier, frontier or reasoning tier, approved enterprise route, human-review route, or evaluation queue]

**Why this route:**  
[Clear explanation tied to risk, complexity, cost, and quality]

**Required guardrails:**
- [Control 1]
- [Control 2]
- [Control 3]

**Evaluation plan:**
- [Eval dimension 1]
- [Eval dimension 2]
- [Eval dimension 3]

**Cost controls:**
- [Cost control 1]
- [Cost control 2]

**Escalation rule:**  
[When to move up or down a tier]

**Decision:**  
[One clear recommendation]

## JSON output

After the recommendation card, include this section by default:

```json
{
  "use_case": "brief use case summary",
  "task_type": "extraction | classification | summarization | drafting | coding | research | strategy | legal | finance | healthcare | agentic | other",
  "complexity": "low | medium | high",
  "data_sensitivity": "public | internal | confidential | customer | employee | regulated | unknown",
  "volume": "low | medium | high | unknown",
  "latency_need": "real_time | interactive | batch | unknown",
  "business_impact": "low | medium | high | unknown",
  "recommended_ai_route": "low_cost_tier | mid_tier | frontier_or_reasoning_tier | approved_enterprise_route | human_review_route | evaluation_queue",
  "why_this_route": "short rationale",
  "required_guardrails": ["guardrail 1", "guardrail 2"],
  "evaluation_plan": ["eval dimension 1", "eval dimension 2"],
  "cost_controls": ["cost control 1", "cost control 2"],
  "escalation_rule": "when to move up, move down, block, or require review",
  "decision": "one clear recommendation"
}
```

The JSON is a machine-readable mirror of the card. It should not introduce new recommendations that were not explained in the readable card.

## Style rules

Use clear executive language. Avoid hype, leaderboard claims, product names, vendor names, and specific model names unless the user explicitly provides an approved catalog. Do not mention multi-model deliberation unless the user specifically asks. Keep the recommendation practical and reusable across organizations. Prefer fuller, natural paragraphs for explanations and use bullets only in the recommendation card where they help scanning.
