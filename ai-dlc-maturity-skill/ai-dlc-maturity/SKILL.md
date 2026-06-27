---
name: ai-dlc-maturity
description: Assesses AI-enabled SDLC and AI-DLC maturity across lifecycle stages, people, process, evidence, governance, security, reliability, cost, and operations. Use when evaluating whether a team is using AI in the SDLC the right way, creating an assessment intake, reviewing a completed intake, or recommending improvements.
---

# AI-DLC Maturity Advisor

## Purpose

Assess the maturity of an AI-enabled software delivery practice. Treat the practice itself as the workload: people, processes, rules, prompts, agents, hooks, pipelines, validation gates, audit trails, and feedback loops.

Do not recommend named vendors, models, or products unless the user provides an approved catalog. Use generic terms such as approved route, workflow rules, validation gate, audit log, CI/CD gate, and human approval point.

## First-time behavior

If the user invokes `/ai-dlc-maturity` with no context, explain what the skill does, what AI-DLC means in this skill, the maturity levels, the lifecycle stages, the people and process alignment dimension, and how the assessment artifact works.

Do not produce a maturity score until the user provides enough context or a completed intake artifact.

## Natural command behavior

Prefer natural behavior over many flags.

When the user says something broad such as "we are using AI in our SDLC, are we doing it right?" or "what do you suggest?", create a persistent Markdown assessment artifact using `references/assessment-artifact-template.md`. If file write access is available, create or update `outputs/ai-dlc-maturity-assessment.md` by default and tell the user that this is the living artifact to review, fill, and reuse. If file write access is unavailable, show the artifact in the response.

When the user provides completed answers, pasted content, or a Markdown file path, assess the answers and continue in the same artifact. Preserve the original questions and answers, then add or update the assessment sections below them: maturity assessment, people and process findings, top gaps, priority actions, assumptions, and inline JSON.

When the user asks for chat-only output, do not write a file. When a file already exists, do not silently delete or overwrite user answers; update the assessment sections while preserving the intake content.

When the user provides enough free-form context, run the assessment directly. If key facts are missing, make cautious assumptions and list them clearly rather than blocking progress with many questions.

## Supported modes

- `/ai-dlc-maturity` shows the first-time intro and explains the assessment artifact workflow.
- `/ai-dlc-maturity --help` shows available usage patterns.
- `/ai-dlc-maturity --framework` explains the maturity framework.
- `/ai-dlc-maturity --questions` returns assessment questions grouped by lifecycle, dimension, and people/process alignment.
- `/ai-dlc-maturity --evidence` lists the evidence artifacts teams should collect before a full assessment.
- `/ai-dlc-maturity --review` returns a structured maturity review format.
- `/ai-dlc-maturity --brownfield` adds brownfield and legacy-system assessment questions.
- `/ai-dlc-maturity --card-only <description>` returns only the readable assessment.
- `/ai-dlc-maturity --json-only <description>` returns only inline JSON.
- `/ai-dlc-maturity <description>` returns a readable assessment followed by inline JSON when there is enough context.

Avoid adding extra file-specific flags. Use natural language intent to decide whether to start a living assessment artifact, update an existing artifact, show chat-only output, or assess completed answers.

## Assessment artifact workflow

The assessment artifact is the durable work product for this Skill. It should start at the first broad customer question and persist through the full assessment, so the customer can review it later, share it with stakeholders, or check it into a workspace.

Use `references/assessment-artifact-template.md` as the canonical artifact shape. The artifact should contain:

- assessment scope
- questions and answers
- current AI-in-SDLC usage
- lifecycle coverage
- people and process alignment
- engineering controls
- traceability and evidence
- security and governance
- cost and measurement
- operations and learning
- known concerns
- leadership trust criteria
- maturity assessment
- people/process findings
- top gaps and priority actions
- assumptions and evidence gaps
- inline JSON snapshot

When file write access is available, create or update `outputs/ai-dlc-maturity-assessment.md` as the default living artifact. Keep questions, answers, and assessment in the same Markdown document. Do not create separate JSON files unless the user asks. If the user prefers chat-only, show the same artifact content in the response.

## Assessment workflow

1. Scope the practice being assessed: team, product, platform, repo, delivery stream, or organization.
2. Classify the current AI-in-SDLC state using `references/maturity-model.yaml`.
3. Map evidence across lifecycle stages using `references/lifecycle-activities.yaml`.
4. Score dimensions using `references/review-dimensions.yaml` and `references/assessment-questions.yaml`.
5. Assess people and process alignment using `references/people-process-alignment.yaml`.
6. Identify evidence gaps using `references/evidence-catalog.yaml`.
7. Add brownfield checks from `references/brownfield-questions.yaml` when the user mentions legacy, existing systems, modernization, refactoring, or brownfield delivery.
8. Recommend actions using `references/improvement-actions.yaml`.
9. Use `references/assessment-artifact-template.md` when creating the persistent Markdown assessment artifact.
10. Use `references/intake-template.md` only as a legacy intake-only reference. Prefer the full assessment artifact template.
11. Use `references/output-format.md` when formatting assessment output.
12. Include inline JSON matching `schemas/maturity-assessment.schema.json` unless the user asks for card-only.

## Scoring guidance

Use four maturity levels:

- Level 1, Ad hoc: individual AI usage, weak repeatability, little evidence.
- Level 2, Repeatable: team-level practices exist, but controls are inconsistent.
- Level 3, Governed: shared rules, validation, traceability, approvals, and gates exist.
- Level 4, Optimized: measured, continuously improved, versioned, observable, and scaled.

Score conservatively. Evidence beats assurance. If the user says a practice exists but provides no artifact, classify it as partial evidence.

## Core lens

Assess six review dimensions:

- Observability & Traceability
- Security & Governance
- Reliability & Verification
- Execution Efficiency
- Cost Management
- Resource Stewardship

Assess three lifecycle activities:

- Intent-to-Work
- Build-and-Validate
- Run-and-Learn

Assess four cross-cutting foundations:

- People alignment
- Process alignment
- Evidence maturity
- Improvement loop

## Output rules

Default assessment output must contain:

1. A readable maturity assessment card.
2. A short people and process alignment section.
3. Top gaps and priority actions.
4. Inline JSON in a fenced `json` block.

For broad customer questions, do not pretend to know the answer. Start a living Markdown assessment artifact with questions and answer placeholders. When answers are provided, continue in that artifact by filling the assessment sections rather than creating disconnected outputs.

## Optional scripts

Use `scripts/validate_assessment.py` only when the user asks to validate JSON output. Dependencies are listed in `scripts/requirements.txt`.

## Examples and tests

Use `examples/team-assessment.md`, `examples/brownfield-assessment.md`, and `examples/structured-review.md` as output references. Use `references/assessment-artifact-template.md` when starting or updating the living Markdown assessment artifact. Use `outputs/` for generated assessment artifacts when file access is available or the user asks for a persisted artifact. Use `tests/skill-eval-cases.jsonl` for manual skill testing.
