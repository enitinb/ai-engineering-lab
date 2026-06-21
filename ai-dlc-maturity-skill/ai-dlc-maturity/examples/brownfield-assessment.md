# Example: Brownfield assessment

Input:

A team wants to use AI agents to modernize a legacy billing service with limited tests. Agents can inspect the repository and propose changes. Developers approve PRs, but there is no characterization test requirement and the AI-derived understanding of the system is not reviewed before code generation.

Expected output shape:

- Overall maturity: Level 1 or Level 2 depending on evidence
- Brownfield warning: understanding must precede generation
- Required actions: add characterization tests, validate AI-derived models, keep work units small, increase review density
