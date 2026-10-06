# Evaluation scenario

Add a growth-rate setting without changing existing prices or silently accepting NaN.

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
- Task-specific verification: Test missing versus malformed files, unknown item IDs, invalid probabilities and failed reload. Verify the prior valid configuration still serves requests after rejection.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
