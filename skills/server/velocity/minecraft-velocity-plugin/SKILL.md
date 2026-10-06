---
name: minecraft-velocity-plugin
description: "Implement Velocity proxy plugins and secure proxy/backend integration."
---

# Velocity Plugin

Resolve proxy version independently from backend Minecraft versions and Java requirements. Use Velocity plugin annotation, dependency injection, events and scheduler rather than JavaPlugin. Never treat proxy events as world/entity access. Validate plugin messages and forwarding trust; keep backend ports inaccessible publicly and secrets out of logs. Test player connection, backend unavailable, reconnect and shutdown paths.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
