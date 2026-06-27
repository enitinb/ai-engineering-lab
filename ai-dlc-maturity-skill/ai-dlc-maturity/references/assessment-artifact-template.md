# AI-DLC Maturity Assessment Artifact

This is the living assessment artifact for an AI-enabled SDLC or AI-DLC practice. Use it from the first discovery conversation through the final assessment. Fill the answers first, then let the AI-DLC Maturity Advisor complete the assessment sections.

**Artifact status:** Draft
**Assessment date:**
**Assessment owner:**
**Team / product / platform:**
**Review participants:**

---

## Contents

Intake sections (fill these first):
- 1. Assessment Scope
- 2. Current AI Usage in the SDLC
- 3. People and Process Alignment
- 4. Intent-to-Work
- 5. Build-and-Validate
- 6. Run-and-Learn
- 7. Security and Governance
- 8. Cost, Efficiency, and Resource Use
- 9. Evidence Available
- 10. Known Concerns

Assessment sections (completed by the advisor):
- Review Status
- Lifecycle Assessment
- Dimension Assessment
- People and Process Alignment
- Top Gaps
- Priority Actions
- Evidence Gaps and Assumptions
- Structured Assessment Snapshot
- Assessment Notes and Change Log

---

## 1. Assessment Scope

What team, product, platform, application, repo, delivery stream, or organization is being assessed?

**Answer:**

Who should be included in the review, such as engineering, product, QA, security, architecture, operations, or leadership?

**Answer:**

What is the goal of the assessment?

**Answer:**

---

## 2. Current AI Usage in the SDLC

Where is AI used today? Mark all that apply and add details.

- [ ] Requirements or story refinement
- [ ] Architecture or design
- [ ] Coding
- [ ] Code review
- [ ] Test generation
- [ ] CI/CD assistance
- [ ] Security review
- [ ] Release notes or documentation
- [ ] Deployment support
- [ ] Incident response or operations
- [ ] Maintenance or modernization
- [ ] Other

**Details:**

Which teams or roles use AI today?

**Answer:**

Is usage individual, team-standardized, or organization-wide?

**Answer:**

---

## 3. People and Process Alignment

Who is accountable for AI-generated or AI-assisted work after it is merged or shipped?

**Answer:**

Where are human decision points required across intent, design, implementation, review, deployment, and remediation?

**Answer:**

Are AI usage rules, prompts, agent instructions, hooks, or workflow conventions shared and version-controlled, or personal to each engineer?

**Answer:**

How are product, engineering, QA, security, architecture, and operations involved in AI-assisted delivery?

**Answer:**

How are uncertain, risky, or low-confidence AI outputs escalated?

**Answer:**

---

## 4. Intent-to-Work

Are requirements captured as durable specifications with acceptance criteria, or are they mainly in chat history and tickets?

**Answer:**

Is ambiguity validated before AI begins implementation work?

**Answer:**

Can a shipped change be traced back to the original intent, requirement, or design decision?

**Answer:**

---

## 5. Build-and-Validate

Do AI-generated changes pass the same review, test, lint, type, security, and CI gates as human-written changes?

**Answer:**

Are work units kept small enough for reliable review?

**Answer:**

Are generated dependencies, APIs, and packages validated before merge?

**Answer:**

Do agents or assistants consume CI results and rework against them, or does a human handle all fixes manually?

**Answer:**

---

## 6. Run-and-Learn

Can you identify which AI-assisted changes are running in production?

**Answer:**

Are deployments, rollbacks, feature flags, canaries, or approvals still intact for AI-assisted changes?

**Answer:**

Do incidents, defects, postmortems, or review findings update prompts, rules, tests, gates, or workflow guidance?

**Answer:**

---

## 7. Security and Governance

What data can AI tools or agents access, such as source code, tickets, logs, secrets, PII, customer data, regulated data, production telemetry, or deployment systems?

**Answer:**

Are access permissions scoped by role, repo, environment, and task?

**Answer:**

Are prompts, context sources, tool use, and agent actions logged or auditable?

**Answer:**

Are any actions auto-approved? If yes, which ones?

**Answer:**

---

## 8. Cost, Efficiency, and Resource Use

Do you track AI usage, token cost, inference cost, review effort, defect rate, rework, or productivity impact?

**Answer:**

Do you use smaller routes, cached context, narrow prompts, batching, or other cost controls where appropriate?

**Answer:**

Is productivity measured by outcome, such as time to value, quality, reliability, or reduced toil, rather than activity alone?

**Answer:**

---

## 9. Evidence Available

List evidence that can support this assessment, such as rule files, PR samples, CI logs, security scans, approval records, cost dashboards, incident reports, architecture decisions, prompt files, agent configuration, or workflow documentation.

**Answer:**

Where is the strongest evidence today?

**Answer:**

Where is evidence missing?

**Answer:**

---

## 10. Known Concerns

What worries the team most about AI in the SDLC today?

**Answer:**

What would make leadership trust the practice more?

**Answer:**

What are the top three improvements the team already suspects are needed?

**Answer:**

---

## Review Status

- [ ] Drafted
- [ ] Reviewed by engineering
- [ ] Reviewed by product or business owner
- [ ] Reviewed by security or governance
- [ ] Ready for AI-DLC maturity assessment
- [ ] Assessment completed

---

# AI-DLC Maturity Assessment

Complete this section after the answers above are filled.

**Overall maturity:**

**Summary:**

## Lifecycle Assessment

| Lifecycle area | Maturity | Evidence-based rationale |
|---|---|---|
| Intent-to-Work |  |  |
| Build-and-Validate |  |  |
| Run-and-Learn |  |  |

## Dimension Assessment

| Dimension | Maturity | Evidence-based rationale |
|---|---|---|
| Observability & Traceability |  |  |
| Security & Governance |  |  |
| Reliability & Verification |  |  |
| Execution Efficiency |  |  |
| Cost Management |  |  |
| Resource Stewardship |  |  |

## People and Process Alignment

**Maturity:**

**Strengths:**

**Gaps:**

**Priority actions:**

## Top Gaps

1.
2.
3.

## Priority Actions

1.
2.
3.

## Evidence Gaps and Assumptions

**Evidence gaps:**

**Assumptions:**

## Structured Assessment Snapshot

```json
{}
```

---

## Assessment Notes and Change Log

Use this section to capture follow-up notes, review comments, or reassessment history.

