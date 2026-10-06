# Evaluation scenario

Add a small plugin feature while retaining the existing build and keeping startup failure recoverable.

## Context

```json
{
  "edition": "java",
  "minecraft": null,
  "platform": "paper"
}
```

## Expected behavior

- Resolve missing target facts before version-dependent generation.
- Use matching inspected evidence for material API/format claims.
- Preserve scope and report actual checks separately from unavailable checks.
- Task-specific verification: Inspect the packaged JAR for descriptor/resources. Start and stop an isolated server; verify commands, listener registration and absence of duplicate tasks.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
