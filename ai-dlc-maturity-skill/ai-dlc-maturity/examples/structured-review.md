# Example: Persistent artifact, structured maturity review

This example shows how the skill uses a structured review lens without tying the assessment to a specific cloud, vendor, or tool.

## User prompt

```text
/ai-dlc-maturity --review Assess our AI-DLC practice. We use AI across requirements elaboration, coding, test generation, PR review, and release notes. We have CI gates, but no standard audit schema for model identity, prompt version, rule version, approval, and linked tests.
```

## Expected skill behavior

The skill should create or update the persistent assessment artifact and organize findings across lifecycle stages and review dimensions. It should preserve the user's answers, then append a maturity assessment, top gaps, and priority actions.

## Expected assessment structure

```md
## Structured Review Summary

Overall maturity: Level 2, Repeatable

## Lifecycle Scores

- Intent-to-Work: Level 2, Repeatable
- Build-and-Validate: Level 2, Repeatable
- Run-and-Learn: Level 1, Ad hoc

## Dimension Findings

### Observability & Traceability

The team has AI activity across the lifecycle, but the practice lacks a standard audit schema for model identity, prompt version, rule version, approvals, and linked tests.

### Security & Governance

Security maturity cannot be confirmed without evidence of prompt data controls, access boundaries, and enforcement points.

### Reliability & Verification

CI gates exist, which is a strength, but the absence of traceability weakens confidence in AI-generated changes after they leave the PR.

### Execution Efficiency

Assess whether task scope, context size, and analysis depth are chosen deliberately rather than left to individual habits.

### Cost Management

Add cost attribution by team, workflow, and lifecycle stage before expanding usage.

### Resource Stewardship

Right-sizing and context reuse should be tracked as part of cost and efficiency metrics.

## Priority Actions

1. Define a standard audit schema for AI-assisted work.
2. Link intent, prompt or rule version, model context, PR, test evidence, approval, and release.
3. Add cost and usage attribution by workflow.
4. Feed production learnings back into shared rules, prompts, tests, and gates.
```
