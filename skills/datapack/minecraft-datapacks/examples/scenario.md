# Evaluation scenario

Port an old datapack to a newer release without resetting player quest state.

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
- Task-specific verification: Load on a disposable matching world, inspect parsing logs and list enabled packs. Exercise load/tick functions twice, reload and restart without duplicating state.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
