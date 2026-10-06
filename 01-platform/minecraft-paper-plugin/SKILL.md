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

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper plugin descriptors](https://docs.papermc.io/paper/dev/plugin-yml/)
- [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/)
- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/)
