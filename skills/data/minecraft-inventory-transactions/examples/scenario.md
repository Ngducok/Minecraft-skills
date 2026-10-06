# Evaluation scenario

A loadout swap overwrites items when inventory is full; preserve both equipment and remainder.

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
- Task-specific verification: Test full destinations, exact/partial stacks, duplicate activation, cancelled events, disconnect and interruption between effects. State which recovery boundaries are proven.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
