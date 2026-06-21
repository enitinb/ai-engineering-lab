# Example: Persistent artifact, brownfield assessment

This example shows how the skill handles existing systems, where the main risk is allowing AI to generate changes before the team has validated the system understanding.

## User prompt

```text
/ai-dlc-maturity We want to use AI agents to modernize a legacy billing service with limited tests. Agents can inspect the repository and propose changes. Are we ready?
```

## Expected skill behavior

The skill should start or update the persistent assessment artifact and include brownfield-specific questions. It should ask for evidence before recommending broad agent autonomy.

## Brownfield questions to include in the artifact

```md
## Brownfield and Legacy-System Readiness

Does understanding precede generation? Describe how the team validates the current system behavior before AI proposes code changes.

Answer:

Are characterization tests created for untested or poorly understood code before modification?

Answer:

Are AI-derived static and dynamic models reviewed by developers before implementation work begins?

Answer:

How small are AI-assisted work units, and how is review density adjusted for legacy risk?

Answer:
```

## Completed intake snippet

```md
Answer:
Agents can inspect the repository and propose changes. Developers approve PRs, but there is no characterization test requirement and the AI-derived understanding of the system is not reviewed before code generation.
```

## Expected assessment output appended to the artifact

```md
## Brownfield Assessment

Brownfield readiness: Level 1, Ad hoc

The current workflow lets AI propose changes before the team has validated system behavior, which is risky for a legacy billing service with limited tests. In brownfield work, the first maturity step is not faster code generation; it is reliable understanding.

## Highest-Risk Gaps

1. No requirement to validate AI-derived system understanding before generation.
2. No characterization tests for untested behavior.
3. Agent autonomy is not earned gradually through smaller work units and higher review density.

## Priority Actions

1. Require an understanding artifact before code generation starts.
2. Add characterization tests for the touched behavior before modification.
3. Keep work units narrow until the team has enough evidence to expand scope.
4. Require developer validation of AI-derived models and assumptions.
```
