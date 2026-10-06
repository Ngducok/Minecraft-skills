# Evaluation scenario

A Fabric feature works in singleplayer but crashes a dedicated server by loading a screen class.

## Context

```json
{
  "edition": "java",
  "minecraft": null,
  "platform": "fabric"
}
```

## Expected behavior

- Resolve missing target facts before version-dependent generation.
- Use matching inspected evidence for material API/format claims.
- Preserve scope and report actual checks separately from unavailable checks.
- Task-specific verification: Run both development client and dedicated server. Build a distribution JAR, verify entrypoints/resources and test only the declared required-side installation.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
