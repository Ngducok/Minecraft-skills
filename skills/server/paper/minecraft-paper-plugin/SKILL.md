---
name: minecraft-paper-plugin
description: "Create or maintain Bukkit/Paper plugins, plugin descriptors, service boundaries and startup/shutdown behavior."
---

# Paper plugin lifecycle and structure

Inspect the existing build and descriptor before adding classes. Keep supported public APIs first; use internal server access only for a demonstrated gap and pin it to the target build.

- Let JavaPlugin wire dependencies and register behavior. Keep event handlers thin and domain rules testable without inventing an interface for one implementation.
- Choose plugin.yml or paper-plugin.yml to match actual bootstrap/dependency needs. Do not convert descriptor formats just to follow a newer example.
- Keep UI, gameplay handlers and build artifacts separate when the repository already does. Namespaces and player UUIDs are stable identifiers; names and menu captions are presentation.
- Initialize configuration and storage before enabling entry points. If initialization fails, stop the affected feature instead of continuing with partially initialized state.
- On disable, cancel owned tasks, reject new transactions, settle pending state and close owned resources. Do not assume another plugin's classloader or singleton remains valid across restarts.

## Verification

Inspect the packaged JAR for descriptor/resources. Start and stop an isolated server; verify commands, listener registration and absence of duplicate tasks.

## Example request

Add a small plugin feature while retaining the existing build and keeping startup failure recoverable.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
