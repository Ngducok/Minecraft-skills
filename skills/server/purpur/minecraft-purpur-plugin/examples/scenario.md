# Evaluation scenario

Develop Purpur features while distinguishing inherited Paper APIs and Purpur-specific behavior.

## Context

```json
{
  "edition": "java",
  "minecraft": null,
  "platform": "purpur"
}
```

## Expected behavior

- Resolve missing target facts before version-dependent generation.
- Use matching inspected evidence for material API/format claims.
- Preserve scope and report actual checks separately from unavailable checks.
- Task-specific verification: Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
