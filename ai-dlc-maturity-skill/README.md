# AI-DLC Maturity Advisor Skill

**Assess whether your AI-enabled SDLC is ready to be trusted at scale.**

AI-DLC Maturity Advisor is a vendor-neutral Claude Skill for customer-facing and internal assessments of AI-assisted coding and AI-driven software delivery practices. It helps teams answer a practical question: "We are using AI in our SDLC. Are we doing it the right way, and what should we improve next?"

The Skill treats the AI-enabled delivery practice as the workload. It reviews people, process, engineering controls, evidence, governance, security, reliability, cost, operations, and improvement loops across the software delivery lifecycle.

## What it assesses

The Skill reviews an AI-enabled delivery practice across:

- lifecycle maturity
- people and process alignment
- operational excellence
- security
- reliability
- performance efficiency
- cost optimization
- sustainability
- evidence quality
- improvement loops
- brownfield readiness when legacy systems are involved

## Slash command

```text
/ai-dlc-maturity
```

First-time usage with no arguments explains the Skill, the maturity model, and the assessment artifact workflow.

## Natural workflow

The Skill is designed to work naturally rather than require many flags.

If a user provides enough context, the Skill produces an assessment directly:

```text
/ai-dlc-maturity Our team uses AI coding assistants for implementation and unit test drafting. Developers review PRs manually. CI runs tests and linting, but prompts and agent rules are personal, not versioned. We do not track cost or trace shipped changes back to intent.
```

If a user gives a broad prompt such as "we are using AI in our SDLC, are we doing it right?", the Skill starts a living Markdown assessment artifact. When file access is available, the default artifact path is `outputs/ai-dlc-maturity-assessment.md`. If file access is not available, the same artifact is shown in the chat.

The artifact is designed to persist from the first question through the completed assessment. It keeps the questions, customer answers, evidence notes, maturity assessment, people/process findings, gaps, priority actions, assumptions, and inline JSON snapshot in one Markdown document.

## Assessment artifact

The assessment artifact is a reusable Markdown document. It helps teams collect the information that matters and keep the final assessment in the same place, including:

- assessment scope
- where AI is used in the SDLC
- people and process alignment
- human decision points
- engineering controls
- traceability and evidence
- security and governance
- cost and measurement
- operations and learning
- known concerns and leadership trust criteria

This makes the assessment useful for workshops, customer conversations, architecture reviews, team retrospectives, follow-up reviews, and versioned evidence gathering.

## Helpful modes

```text
/ai-dlc-maturity --help
/ai-dlc-maturity --framework
/ai-dlc-maturity --questions
/ai-dlc-maturity --evidence
/ai-dlc-maturity --well-architected
/ai-dlc-maturity --brownfield
/ai-dlc-maturity --card-only <description>
/ai-dlc-maturity --json-only <description>
```

Default output includes a readable maturity assessment followed by inline JSON. The JSON is shown in the response and is not saved anywhere unless the user explicitly asks.

## Install locally in a project

```bash
mkdir -p .claude/skills
cp -R ai-dlc-maturity .claude/skills/
```

## Install globally for your user

```bash
mkdir -p ~/.claude/skills
cp -R ai-dlc-maturity ~/.claude/skills/
```

Use a project-local install when a repository needs its own assessment rules or examples. Use a global install when you want the generic Skill available across projects.

## Repository structure

```text
ai-dlc-maturity-skill/
  README.md
  QUICKSTART.md
  LICENSE
  ai-dlc-maturity/
    SKILL.md
    references/
    schemas/
    scripts/
    outputs/
    examples/
    tests/
    docs/
```

## Design choices

- The Skill recommends maturity findings and improvement actions, not named vendors or specific tools.
- `SKILL.md` is intentionally concise and uses supporting files for progressive disclosure.
- All references are one level deep from `SKILL.md`.
- The default output is readable for humans and structured enough for downstream use.
- People and process alignment is treated as a first-class maturity dimension.
- The Markdown assessment artifact persists from discovery questions through answers, findings, actions, and inline JSON.
- Evidence beats assurance. If the user claims a practice exists without artifacts, the Skill marks it as partial evidence.

## Optional JSON validation

If you copy the inline JSON to a file and want to validate it locally:

```bash
cd ai-dlc-maturity
pip install -r scripts/requirements.txt
python scripts/validate_assessment.py assessment.json
```

## License

MIT
