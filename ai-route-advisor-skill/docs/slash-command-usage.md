# Slash command usage

This skill can be installed either locally in a project or globally for your Claude Code user profile.

## Local project install

Use local installation when a repository or project needs its own R.E.S.E.T. policy.

```bash
mkdir -p .claude/skills
cp -R ai-route-advisor .claude/skills/
```

Claude Code will see the skill when you are working inside that project.

Invoke it with:

```text
/ai-route-advisor <your use case>
```

## Global personal install

Use global installation when you want the same skill available across projects.

```bash
mkdir -p ~/.claude/skills
cp -R ai-route-advisor ~/.claude/skills/
```

Invoke it from any Claude Code session:

```text
/ai-route-advisor <your use case>
```

## Expected folder name

The slash command name follows the skill folder name. This package should be installed as:

```text
ai-route-advisor/SKILL.md
```

That creates:

```text
/ai-route-advisor
```

## Flags

```text
/ai-route-advisor --help
/ai-route-advisor --reset
/ai-route-advisor --schema
/ai-route-advisor --examples
/ai-route-advisor --card-only <your use case>
/ai-route-advisor --json-only <your use case>
```

Default behavior is a readable recommendation card followed by inline JSON. The skill should not save JSON to a file unless the user explicitly asks.

## Examples

```text
/ai-route-advisor We want to generate CRM follow-up notes from customer support calls. Data includes customer conversations and PII. High volume, batch is fine.
```

```text
/ai-route-advisor Evaluate whether we should replace our current summarization model for internal meeting notes. Data is internal and volume is medium.
```

```text
/ai-route-advisor Classify this AI idea: a coding assistant that can open pull requests and run tests against internal repos.
```

Claude may also invoke the skill automatically when a user asks about model-tier selection, governance controls, evaluation planning, or the R.E.S.E.T. framework.
