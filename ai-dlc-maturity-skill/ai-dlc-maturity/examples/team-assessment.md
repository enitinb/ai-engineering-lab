# Example: Persistent artifact, team assessment

This example shows the preferred workflow. The skill starts a living Markdown assessment artifact, the team fills in answers and evidence, and the skill appends the maturity assessment to the same artifact.

## User prompt

```text
/ai-dlc-maturity We are using AI coding assistants in our SDLC. Developers use them for implementation and unit test drafting. Are we doing it the right way?
```

## Expected skill behavior

The skill should not jump straight to a final maturity score unless enough evidence is already provided. It should start a persistent Markdown artifact with questions, answer sections, evidence prompts, and assessment placeholders.

When file access is available, the artifact can be created or updated at:

```text
outputs/ai-dlc-maturity-assessment.md
```

When file access is not available, the same artifact should be shown in the response for the user to copy, review, fill, and bring back.

## Example artifact excerpt

```md
# AI-DLC Maturity Assessment

## Assessment Status

Status: Draft intake started

## 1. Assessment Scope

What teams, applications, or delivery workflows are in scope?

Answer:

## 2. Current AI Usage in the SDLC

Where is AI used today across requirements, design, coding, review, testing, CI/CD, deployment, operations, documentation, and maintenance?

Answer:

## 3. People and Process Alignment

Who is accountable for AI-generated work after it is merged or released?

Answer:

Where are human decision points required?

Answer:
```

## Completed intake snippet

```md
## 2. Current AI Usage in the SDLC

Answer:
The product team uses AI coding assistants for implementation and unit test drafting. Developers review pull requests manually. CI runs unit tests and linting. Prompts and agent rules are personal, not versioned. There is no cost attribution, audit trail, or clear feedback loop from incidents into shared rules.
```

## Expected assessment output appended to the artifact

```md
## Assessment Summary

Overall maturity: Level 2, Repeatable

The team has moved beyond ad hoc individual experimentation because AI-generated work still passes through PR review and CI checks. The practice is not yet governed because prompts, rules, and decision records are not shared, versioned, or traceable, and production learnings do not consistently update the AI workflow.

## People and Process Findings

Strengths:
- Human review exists before merge.
- AI usage is visible within the team.

Gaps:
- Ownership for AI-generated work after merge is not explicit.
- Review and escalation expectations vary by person.
- Personal prompts and rules have not become shared team practice.

## Top Gaps

1. AI workflow rules are not version-controlled.
2. Shipped changes are not consistently traceable to intent, model context, approval, and test evidence.
3. Incident and defect learnings do not feed back into shared rules or gates.

## Priority Actions

1. Move prompts, rules, and agent configuration into reviewed version control.
2. Add trace metadata from intent to PR, CI evidence, approval, and release.
3. Define human ownership and escalation points for AI-generated work.
4. Feed incidents, defects, and review findings back into rules, tests, and workflow gates.
```
