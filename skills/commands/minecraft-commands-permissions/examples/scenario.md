# Evaluation scenario

Create a purchase command with optional quantity and suggestions without allowing unauthorized console-equivalent actions.

## Context

```json
{
  "edition": "java",
  "minecraft": null,
  "platform": null
}
```

## Expected behavior

- Resolve missing target facts before version-dependent generation.
- Use matching inspected evidence for material API/format claims.
- Preserve scope and report actual checks separately from unavailable checks.
- Task-specific verification: Exercise player, console and denied sender paths; malformed numbers, stale targets and tab completion. Ensure the same forbidden action is rejected through its GUI entry point.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
