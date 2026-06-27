# Quickstart

## 1. Install

Project-local install:

```bash
mkdir -p .claude/skills
cp -R ai-dlc-maturity .claude/skills/
```

Global install:

```bash
mkdir -p ~/.claude/skills
cp -R ai-dlc-maturity ~/.claude/skills/
```

## 2. First-time intro

```text
/ai-dlc-maturity
```

This explains the Skill, the maturity model, lifecycle stages, people/process alignment, and the assessment artifact workflow.

## 3. Start with a broad customer question

```text
/ai-dlc-maturity We are using AI in our SDLC. Are we doing it the right way?
```

The Skill should start a persistent Markdown assessment artifact. When file access is available, it can create or update `outputs/ai-dlc-maturity-assessment.md`. If file access is not available, it shows the same artifact in the chat so the team can fill it out, review it, and bring it back for assessment.

## 4. Run an assessment from enough context

```text
/ai-dlc-maturity Our team uses AI coding assistants for implementation and test generation. CI runs tests, but prompts are personal, rules are not versioned, and cost is not tracked.
```

## 5. Continue from a completed artifact

Paste the filled Markdown intake back into Claude and ask:

```text
Continue the AI-DLC maturity assessment from this completed intake.
```

When file access is available, you can also point Claude to the completed Markdown file in the workspace.

## 6. Helpful modes

```text
/ai-dlc-maturity --framework
/ai-dlc-maturity --questions
/ai-dlc-maturity --evidence
/ai-dlc-maturity --brownfield <description>
/ai-dlc-maturity --card-only <description>
/ai-dlc-maturity --json-only <description>
```

## 7. Output behavior

Default assessment output is:

1. human-readable maturity card
2. lifecycle and dimension scores
3. people and process alignment
4. top gaps and priority actions
5. inline JSON

The Skill does not save JSON or completed assessments anywhere unless explicitly asked.
