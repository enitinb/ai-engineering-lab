# Quickstart

AI Route Advisor is a Claude Skill for AI model-selection intake. It uses the R.E.S.E.T. framework to classify a use case, recommend a generic AI route, identify guardrails, and define what should be evaluated before production.

## Install locally for one project

```bash
mkdir -p .claude/skills
cp -R ai-route-advisor .claude/skills/
```

Use local install when a project has its own governance rules, route definitions, or evaluation standards.

## Install globally for your user

```bash
mkdir -p ~/.claude/skills
cp -R ai-route-advisor ~/.claude/skills/
```

Use global install when you want the generic skill available across projects.

## Run

```text
/ai-route-advisor We want to summarize customer support calls and create CRM follow-up notes. The data includes customer conversations and possible PII. Volume is high and latency is not critical.
```

## What you get

The skill returns a R.E.S.E.T. recommendation card plus inline JSON with:

- use case classification
- complexity and data sensitivity
- recommended AI route
- required guardrails
- evaluation plan
- cost controls
- escalation rule
- final decision

The recommendation is vendor-neutral by default. It recommends route types, not specific providers or models. The JSON is displayed inline for copy/paste and is not saved anywhere unless you explicitly ask for a file.


## Useful flags

```text
/ai-route-advisor --help
/ai-route-advisor --reset
/ai-route-advisor --schema
/ai-route-advisor --examples
/ai-route-advisor --card-only <your use case>
/ai-route-advisor --json-only <your use case>
```

Default output is a readable card plus inline JSON. Use `--card-only` when you want a cleaner human response, and `--json-only` when you want only the machine-readable object.

## Test before sharing

Run the examples in `tests/skill-eval-cases.jsonl` after installing the skill. Confirm that Claude triggers `/ai-route-advisor`, returns a R.E.S.E.T. recommendation card plus inline JSON by default, stays vendor-neutral, and only uses scripts when validation or cost estimation is explicitly requested.


## First-time command

Run this when you want the skill to explain itself and the R.E.S.E.T. framework:

```text
/ai-route-advisor
```

This should return a short intro, the meaning of R.E.S.E.T., and one example. It should not return JSON unless a use case is provided.
