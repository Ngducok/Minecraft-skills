---
name: minecraft-spigot-plugin
description: "Build Spigot/Bukkit plugins with target-specific APIs and descriptors."
---

# Spigot Plugin

Resolve exact Spigot revision and Java from target documentation. Use public Bukkit/Spigot APIs, plugin.yml and the project's build tool. Paper Adventure, Dialog, scheduling and registry APIs are not Spigot APIs. If server internals are unavoidable, pin mappings/build and isolate the dependency. Use BuildTools only when actually required, in an isolated directory. Test startup, permissions and teardown on Spigot, not merely Paper.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
