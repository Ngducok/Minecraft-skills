# Evaluation scenario

A modded purchase screen sends price and amount; validate a product request server-side instead.

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
- Task-specific verification: Test malformed/oversized payloads, stale sessions, duplicate messages and unsupported clients. Exercise high latency and a dedicated server with client code absent.

Manual or authorized external-agent review only. This document is not an executable test or evidence of a passed evaluation.
