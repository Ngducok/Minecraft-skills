# Evaluation scenario

A Java custom crop shop needs a usable Bedrock path without changing its economic rules.

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
- Task-specific verification: Run Java and Bedrock clients through purchase, sale, reconnect and custom item interactions. Inspect both pack logs and mapping failures.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
