# Evaluation scenario

Split an authorized crossplay review into Java UI and Bedrock mapping checks, then reconcile their evidence.

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
- Task-specific verification: Confirm task boundaries, source-backed results and non-overlapping edits. Test the combined result; report unavailable delegation honestly and perform the work locally when feasible.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
