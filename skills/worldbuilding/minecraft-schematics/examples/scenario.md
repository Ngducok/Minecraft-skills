# Evaluation scenario

A generated starter .litematic imports as empty; validate its schema, palette and packed state array.

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
- Task-specific verification: Round-trip mixed states, containers, negative regions and a palette large enough to change bit width. Inspect the imported world at known coordinates and confirm DataVersion handling.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
