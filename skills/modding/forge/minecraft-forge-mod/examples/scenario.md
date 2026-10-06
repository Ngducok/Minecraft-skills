# Evaluation scenario

Build Forge mods using version-matched MDK, registries, event buses and physical-side separation.

## Context

```json
{
  "edition": "java",
  "minecraft": null,
  "platform": "forge"
}
```

## Expected behavior

- Resolve missing target facts before version-dependent generation.
- Use matching inspected evidence for material API/format claims.
- Preserve scope and report actual checks separately from unavailable checks.
- Task-specific verification: Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
