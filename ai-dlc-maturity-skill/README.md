# AI-DLC Maturity Advisor Skill

**Assess whether your AI-enabled SDLC is ready to be trusted at scale.**

AI-DLC Maturity Advisor is a vendor-neutral Claude Skill for customer-facing and internal assessments of AI-assisted coding and AI-driven software delivery practices. It helps teams answer a practical question: "We are using AI in our SDLC. Are we doing it the right way, and what should we improve next?"

The Skill treats the AI-enabled delivery practice as the workload. It reviews people, process, engineering controls, evidence, governance, security, reliability, cost, operations, and improvement loops across the software delivery lifecycle.

## What it assesses

The Skill reviews an AI-enabled delivery practice across:

- lifecycle maturity
- people and process alignment
- observability and traceability
- security and governance
- reliability and verification
- execution efficiency
- cost management
- resource stewardship
- evidence quality
- improvement loops
- brownfield readiness when legacy systems are involved

## Slash command

```text
/ai-dlc-maturity
```

First-time usage with no arguments explains the Skill, the maturity model, and the assessment artifact workflow.

## Sample prompts and scenarios

Copy any of these to try the Skill. Natural language works best; the flags are shortcuts for a specific output.

**Discovery: "are we doing this right?"**
```text
/ai-dlc-maturity We are using AI in our SDLC. Are we doing it the right way?
```
Starts a fillable Markdown assessment artifact covering scope, lifecycle, people/process, controls, traceability, security, cost, and evidence. It does not score until you provide answers or enough context.

**Assess directly from context**
```text
/ai-dlc-maturity Our team uses AI coding assistants for implementation and unit test drafting. Developers review PRs manually. CI runs tests and linting, but prompts and agent rules are personal, not versioned. We do not track token cost or trace shipped changes back to intent.
```
Produces a readable maturity card plus an inline JSON snapshot, scored conservatively with gaps and priority actions.

**Prepare an artifact for a team to fill out**
```text
/ai-dlc-maturity Please prepare a Markdown assessment artifact for our platform team to fill out.
```

**Continue from a completed intake**
```text
Continue the AI-DLC maturity assessment from this completed intake: [paste filled Markdown]
```

**Learn the model first (no scoring)**
```text
/ai-dlc-maturity --framework
/ai-dlc-maturity --questions
/ai-dlc-maturity --evidence
```

**Structured maturity review for architects and leaders**
```text
/ai-dlc-maturity --review Assess our AI-DLC practice. We use AI across requirements, coding, test generation, PR review, and release notes. We have CI gates but no standard audit schema for model identity, prompt version, rule version, approval, and linked tests.
```

**Legacy / brownfield systems**
```text
/ai-dlc-maturity --brownfield We are applying AI to a large legacy system with poor test coverage and want to modernize it safely.
```

**Control the output shape**
```text
/ai-dlc-maturity --card-only Our team versions prompts and rules, runs CI gates on AI changes, and tracks cost by workflow.
/ai-dlc-maturity --json-only Our team versions prompts and rules, runs CI gates on AI changes, and tracks cost by workflow.
```

These same scenarios are encoded as test cases in `ai-dlc-maturity/tests/skill-eval-cases.jsonl` (see `ai-dlc-maturity/tests/README.md` for how to run them).

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

The Skill works best with natural language, but these modes are available when you want a specific type of output.

| Command | What it does | When to use it |
|---|---|---|
| `/ai-dlc-maturity --help` | Explains the Skill, available modes, and example usage. | Use this when someone is new to the Skill. |
| `/ai-dlc-maturity --framework` | Explains the AI-DLC maturity model, lifecycle stages, maturity levels, review dimensions, and people/process dimension. | Use this before an assessment when the audience wants the model first. |
| `/ai-dlc-maturity --questions` | Shows the assessment questions grouped by lifecycle, dimensions, and people/process alignment. | Use this to prepare a workshop or review the questionnaire without running an assessment. |
| `/ai-dlc-maturity --evidence` | Lists evidence to collect, such as rule files, PR samples, CI logs, security scans, approvals, cost dashboards, incidents, and trace links. | Use this when a team needs to prepare artifacts before scoring maturity. |
| `/ai-dlc-maturity --review` | Frames the assessment as a structured maturity review of the AI-enabled delivery practice. | Use this with architects, governance teams, platform teams, or leaders who prefer a structured review format. |
| `/ai-dlc-maturity --brownfield` | Adds legacy-system and existing-codebase questions, including understanding-before-generation, characterization tests, and earned autonomy. | Use this when AI is being applied to existing systems, legacy code, or poorly tested applications. |
| `/ai-dlc-maturity --card-only <description>` | Produces only the readable maturity assessment card. | Use this when you want a clean human-facing answer without the JSON snapshot. |
| `/ai-dlc-maturity --json-only <description>` | Produces only the structured JSON snapshot. | Use this when another workflow, dashboard, or automation needs machine-readable output. |
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
