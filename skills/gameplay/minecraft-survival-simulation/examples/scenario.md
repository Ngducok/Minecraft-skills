# Evaluation scenario

Change animal population rules and crop timing on an SMP while retaining vanilla drops and player contraptions.

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
- Task-specific verification: Test loaded/unloaded chunks, native/random interaction paths, reset/restart and cancelled protection events. Measure timings on the stated runtime instead of converting ticks blindly to seconds.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
