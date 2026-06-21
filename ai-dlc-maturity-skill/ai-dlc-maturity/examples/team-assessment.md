# Example: Team assessment

Input:

A product team uses AI coding assistants for implementation and unit test drafting. Developers review pull requests manually, but prompts and rules are not versioned. CI runs unit tests and linting, but there is no cost attribution, audit trail, or clear feedback loop from incidents into agent rules.

Expected output shape:

- Overall maturity: Level 2, Repeatable
- Strongest area: Build-and-Validate
- Highest-risk gap: traceability and unversioned workflow rules
- People/process gap: human review exists, but ownership and escalation are not fully explicit
- Priority actions: version rules, add trace metadata, add AI usage audit trail, add incident feedback loop
