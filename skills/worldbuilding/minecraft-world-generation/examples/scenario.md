# Evaluation scenario

Replace a test Overworld with a void map while keeping player data and a usable rollback.

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
- Task-specific verification: Generate chunks in different orders and compare results. Test negative coordinates, boundary chunks, spawn/respawn and restore to an isolated server.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
