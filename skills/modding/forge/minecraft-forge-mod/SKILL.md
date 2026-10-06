---
name: minecraft-forge-mod
description: "Build Forge mods using version-matched MDK, registries, event buses and physical-side separation."
---

# Forge Mod

Start from the MDK for the requested Forge/Minecraft pair, preserving wrapper and toolchain. Forge and NeoForge are separate targets: do not mix imports, descriptors or registration APIs. Pin mappings and consult matching docs/source. Keep client rendering/input classes out of dedicated-server initialization. Validate packet data server-side. Build, run dedicated server and matching client separately; build success proves neither side safe.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
