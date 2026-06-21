# AI Route Advisor

**Choose the right AI route before you choose the model.**

AI Route Advisor is a vendor-neutral Claude Skill powered by the [**R.E.S.E.T. framework**](https://www.linkedin.com/pulse/stop-chasing-model-start-choosing-nitin-eusebius-jpufc/). It helps teams classify AI use cases, recommend the right route type, identify required guardrails, define evaluation needs, and control cost before a model is selected or a workflow reaches production.

It does not recommend specific vendors, products, or models by default. The skill recommends generic AI route types so each organization can map the guidance to its own approved stack, governance rules, and cost structure.

## Why this exists

Model selection used to be a technical choice. Now it is an operating decision shaped by cost, security, governance, latency, data sensitivity, evaluation quality, and the risk of switching too often.

AI Route Advisor gives teams a repeatable way to answer one question before implementation starts:

> What kind of AI route does this work deserve?

The output is a practical recommendation card plus an inline JSON mirror that can be copied into architecture reviews, AI governance discussions, product planning, design docs, engineering intake, or workflow automation. The skill does not save JSON anywhere unless the user explicitly asks for a file.

## How the skill uses the repository

Every retained folder has a purpose in the skill. `SKILL.md` is the Claude entry point. The `references/` files provide the reusable decision logic for taxonomy, sensitivity, route selection, guardrails, evals, and cost controls. The `schemas/` folder defines the optional machine-readable recommendation format. The `examples/` folder gives expected behavior patterns. The `scripts/` folder provides optional local validation and cost-estimation utilities when users want to operationalize the recommendation.

This makes the repo more than a prompt. It is a small, vendor-neutral decision system for the R.E.S.E.T. framework.


## Claude Skill best-practice alignment

This package follows current Claude Skill authoring guidance:

- `SKILL.md` contains focused instructions and points to supporting files instead of carrying every rule inline.
- The YAML frontmatter uses the required `name` and `description` fields, with a specific third-person description for skill discovery.
- Reference files stay one level deep from `SKILL.md` for easier loading.
- Scripts are optional, deterministic, local utilities. They are not required for normal recommendations.
- Script dependencies are documented in `ai-route-advisor/scripts/requirements.txt`.
- Manual eval cases are included in `tests/skill-eval-cases.jsonl`.
- The skill avoids time-sensitive model rankings and named-provider defaults so the decision logic stays durable.

## What the skill produces

Given a use case, the skill returns a structured R.E.S.E.T. recommendation card first, followed by inline JSON for copy/paste or automation:

```text
R.E.S.E.T. Recommendation

Use case:
Summarize customer support calls and draft CRM follow-up notes.

Classification:
Task type: customer support summarization and drafting
Complexity: medium
Data sensitivity: customer
Volume: high
Latency need: batch
Business impact: medium

Recommended AI route:
approved enterprise route

Why this route:
The workflow is not deep reasoning, but it uses customer conversations and possible PII, so governance requirements should constrain model choice before cost optimization.

Required guardrails:
PII handling, approved route, audit logging, retention review, human review for low-confidence outputs

Evaluation plan:
Summary accuracy, missed action items, privacy leakage, human edit rate, cost per completed note

Cost controls:
Batch processing, output caps, reusable instructions, sampled QA, escalation only for disputed cases

Escalation rule:
Move to a stronger tier only when evaluation results or human review show the current route is below the quality bar.

Decision:
Pilot with an approved mid-tier route and promote only after the eval results meet the quality and governance bar.
```

## R.E.S.E.T. framework

AI Route Advisor uses five decision lenses:

| Lens | What it checks |
| --- | --- |
| **R: Right-size** | Task type, complexity, risk, volume, and whether the work needs a small, mid, frontier, approved, or human-reviewed route |
| **E: Evaluate** | Whether the task needs a light eval, required eval, red-team testing, or human review before production |
| **S: Spend** | Cost per correct outcome, including retries, context size, output size, latency, batching, caching, and review effort |
| **E: Enforce** | Governance controls such as data handling, access restrictions, retention review, audit logging, approval points, and monitoring |
| **T: Test** | Whether a new route should enter the eval queue before replacing an existing workflow |

## Design goals

- **Vendor-neutral:** no named providers, products, or models unless the user supplies an approved catalog
- **Scalable:** classifies any use case through stable dimensions instead of a fixed use-case list
- **Governance-first:** treats sensitive data, regulated data, customer impact, source code, and external actions as routing constraints
- **Eval-driven:** recommends what to test before production instead of relying on demos or public benchmarks
- **Cost-aware:** uses cost per correct outcome rather than only token price
- **Implementation-ready:** produces a recommendation card and inline JSON that can flow into design docs, intake forms, or workflow automation without saving files

## Route types

The skill recommends route types, not named models:

| Route type | Meaning |
| --- | --- |
| `low_cost_tier` | Simple, low-risk, high-volume work such as extraction, formatting, tagging, and short summaries |
| `mid_tier` | Routine business work such as drafting, longer summarization, support assistance, and structured analysis |
| `frontier_or_reasoning_tier` | Complex reasoning, architecture review, strategy, complex coding, or high-impact synthesis |
| `approved_enterprise_route` | Sensitive, customer, confidential, regulated, or governed workflows that must follow approved paths |
| `human_review_route` | Work where a human must approve, verify, or own the final decision before use |
| `evaluation_queue` | A task or route that should be tested before production or before replacing the current workflow |

## Repository structure

```text
ai-route-advisor-skill/
  ai-route-advisor/
    SKILL.md
    references/
      task-taxonomy.yaml
      data-classification.yaml
      model-tiers.yaml
      governance-controls.yaml
      eval-scorecards.yaml
      cost-controls.yaml
      positioning.md
    schemas/
      recommendation.schema.json
    scripts/
      validate_recommendation.py
      estimate_cost.py
    examples/
      customer-support-summary.md
      architecture-review.md
      marketing-copy.md
  docs/
    asset-map.md
    slash-command-usage.md
    best-practices-notes.md
  QUICKSTART.md
  README.md
```

## Install as a local project skill

Use a local install when one repository or project needs its own data rules, governance policy, evaluation standards, or route definitions.

From the root of your project:

```bash
mkdir -p .claude/skills
cp -R ai-route-advisor .claude/skills/
```

Expected structure:

```text
your-project/
  .claude/
    skills/
      ai-route-advisor/
        SKILL.md
        references/
        schemas/
        scripts/
        examples/
```

Then run Claude Code from that project and invoke:

```text
/ai-route-advisor We want to summarize customer support calls and create CRM follow-up notes. The data includes customer conversations and possible PII. Volume is high and latency is not critical.
```

## Install as a global personal skill

Use a global install when you want the generic R.E.S.E.T. logic available across projects.

```bash
mkdir -p ~/.claude/skills
cp -R ai-route-advisor ~/.claude/skills/
```

Then invoke it from any Claude Code project:

```text
/ai-route-advisor <your AI use case>
```

## Local vs global policy

A useful pattern is to keep the global skill generic and vendor-neutral, then create local project copies only when a team needs project-specific rules.

| Scope | Best for | What to customize |
| --- | --- | --- |
| Global | Personal use, demos, broad AI intake, generic R.E.S.E.T. guidance | Usually nothing |
| Local | Product teams, governed projects, security reviews, enterprise workflows | Data classification, approved route definitions, guardrails, eval scorecards |

## Example prompts

```text
/ai-route-advisor We want to generate CRM follow-up notes from customer support calls. Data includes customer conversations and PII. High volume, batch is fine.
```

```text
/ai-route-advisor Evaluate whether we should replace our current summarization route for internal meeting notes. Data is internal and volume is medium.
```

```text
/ai-route-advisor Classify this AI idea: a coding assistant that can open pull requests and run tests against internal repositories.
```

```text
/ai-route-advisor We want an AI assistant to review vendor contracts and flag risky clauses. Legal will review the final output.
```


## Slash command flags

Use these optional flags to control the response:

| Flag | Behavior |
| --- | --- |
| `--help` | Explains what the skill does, when to use it, and what input to provide |
| `--reset` | Explains the R.E.S.E.T. framework |
| `--schema` | Shows the JSON fields and what each field means |
| `--examples` | Shows sample use cases and likely route types |
| `--card-only` | Returns only the human-readable recommendation card |
| `--json-only` | Returns only the inline JSON object |
| `--validate-json` | Validates pasted JSON against the bundled schema when local execution is available |
| `--estimate-cost` | Estimates rough cost when token, volume, and pricing assumptions are provided |

Default behavior is **recommendation card plus inline JSON**. The JSON is shown in the response and is not saved to a file.

## Recommendation schema

The skill returns inline JSON by default after the readable card. The canonical field is `recommended_ai_route` because the result is a decision route, not a vendor or model name. The JSON mirrors the card and should not introduce new recommendations that were not explained in the readable section.

```json
{
  "use_case": "Summarize customer support calls and draft CRM follow-up notes",
  "task_type": "customer_support_summarization",
  "complexity": "medium",
  "data_sensitivity": "customer",
  "volume": "high",
  "latency_need": "batch",
  "business_impact": "medium",
  "recommended_ai_route": "approved_enterprise_route",
  "why_this_route": "Customer conversations may include PII, so governance should constrain the route before cost optimization.",
  "required_guardrails": ["pii_handling", "audit_logging", "retention_review"],
  "evaluation_plan": ["summary_accuracy", "missed_action_items", "privacy_leakage", "human_edit_rate"],
  "cost_controls": ["batching", "output_caps", "sampled_quality_review"],
  "escalation_rule": "Escalate only when quality falls below the eval threshold or human review flags repeated misses.",
  "decision": "Pilot with an approved mid-tier route and promote only after evaluation passes."
}
```

Validate a pasted or copied recommendation JSON locally by saving it yourself and running:

```bash
python ai-route-advisor/scripts/validate_recommendation.py recommendation.json
```

## Optional cost estimator

The cost estimator is intentionally generic. You provide your own assumed prices and workload profile.

```bash
python ai-route-advisor/scripts/estimate_cost.py \
  --input-tokens 5000 \
  --output-tokens 1000 \
  --requests 10000 \
  --input-price-per-million 1.0 \
  --output-price-per-million 5.0 \
  --retry-rate 0.05
```

## Customizing for a team

Keep `SKILL.md` stable and generic. Put team-specific decisions in reference files:

```text
references/model-tiers.yaml
references/data-classification.yaml
references/governance-controls.yaml
references/eval-scorecards.yaml
references/cost-controls.yaml
```

This keeps the skill reusable while allowing each team to define its own approved route types, data classes, review requirements, and evaluation standards.

## What this is not

AI Route Advisor is not a model leaderboard, model gateway, benchmark runner, vendor recommendation engine, or automatic production router. It is a pre-flight decision skill that helps teams think clearly before model selection.

## Optional scripts

The scripts are not required for normal skill use. They are included so teams can turn the recommendation into a more technical workflow.

- `validate_recommendation.py` validates JSON output against the bundled schema.
- `estimate_cost.py` estimates route cost from user-provided token counts, request volume, and pricing assumptions.

The scripts do not call external services and do not include model or vendor pricing.

## Safety note

Review all skill files before use. This package includes only simple local scripts and no outbound network calls. Treat any third-party skill as code that should be reviewed before installation.

## Positioning

**AI Route Advisor** helps teams move from model chasing to model discipline. It classifies the work, identifies the risk, recommends the route, defines the proof needed, and keeps governance close to the decision.

**Stop chasing models. Route the work.**

## Manual testing

Use `tests/skill-eval-cases.jsonl` to test the skill before sharing it. Each case has an input use case and expected recommendation behavior. Run the cases in Claude Code or claude.ai and confirm the skill triggers, produces the recommendation card plus inline JSON by default, avoids named vendors, and recommends the right route type, guardrails, eval plan, and cost controls.

For JSON validation, save a recommendation as `recommendation.json`, then run:

```bash
cd ai-route-advisor
python -m pip install -r scripts/requirements.txt
python scripts/validate_recommendation.py recommendation.json
```


## First-time experience

When someone runs the skill without a use case, it should not produce a recommendation or JSON. It should briefly explain what AI Route Advisor does, define the R.E.S.E.T. framework, and show one example command.

```text
/ai-route-advisor
```

Expected behavior:

```text
AI Route Advisor helps teams classify AI work before choosing a model. It recommends a generic AI route, required guardrails, eval needs, and cost controls.

R.E.S.E.T. means Right-size, Evaluate, Spend, Enforce, and Test. It is a pre-flight model-selection framework that helps teams route work intentionally instead of chasing every new model.

Example:
/ai-route-advisor We want to summarize customer calls and draft CRM follow-up notes. The data may include PII. Volume is high.
```
