# Output format

Default output has two parts: a readable card followed by inline JSON.

## Readable card

Use this structure:

# AI-DLC Maturity Assessment

**Scope:** [team/product/workflow]
**Overall maturity:** [level]
**Summary:** [2 to 4 sentences]

## Lifecycle assessment

| Lifecycle area | Maturity | Why |
|---|---|---|
| Intent-to-Work | [level] | [evidence-based reason] |
| Build-and-Validate | [level] | [evidence-based reason] |
| Run-and-Learn | [level] | [evidence-based reason] |

## Dimension assessment

List the six dimensions with concise findings.

## People and process alignment

State maturity, strengths, gaps, and priority actions.

## Top gaps

Rank the highest-risk gaps.

## Priority actions

Give 3 to 7 actions ordered by impact.

## Assumptions

List assumptions only when details were missing.

## Inline JSON

Include a fenced `json` block matching `schemas/maturity-assessment.schema.json`, unless the user asked for `--card-only`.


## Persistent artifact format

When maintaining the living Markdown artifact, preserve the original questions and answers. Add or update the assessment sections below the intake sections. Keep the inline JSON in the `Structured Assessment Snapshot` section of the same Markdown file rather than saving JSON separately.

Default artifact path when file write access is available: `outputs/ai-dlc-maturity-assessment.md`.
