# Evaluation scenario

Release a custom-item update with a pack and schema migration while retaining a valid restore point.

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
- Task-specific verification: Exercise upgrade and restoration with representative saved items/profiles. Verify pack reachability, version logs and a minimal gameplay smoke check after restart.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
