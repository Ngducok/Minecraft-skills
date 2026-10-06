---
name: minecraft-neoforge-mod
description: "Create or port NeoForge Minecraft Java mods, registries, event buses, data attachments and distribution-specific behavior."
---

# NeoForge mod development

Select the target-version NeoForge toolchain and APIs. Forge, NeoForge and Fabric have overlapping concepts but distinct loading, registration and event contracts.

- Separate mod lifecycle registration from game events using the correct event bus for the target. Do not solve a missing callback by registering everything on both buses.
- Keep client-only rendering/screens out of dedicated-server initialization. Verify required distribution before resolving client classes.
- Use supported registry/attachment systems for content and state. Persistence, synchronization and copy-on-death are separate choices; document which each field needs.
- Handle player clone/death and dimension return without duplicating state. Avoid copying already-existing values twice after End return or respawn.
- Preserve stable registry IDs through a port and define mapping/migration for renamed content. A compiling JAR does not prove an old world can load safely.
- Use the exact payload and threading APIs from the chosen release; large assets do not belong in ad-hoc gameplay packets.

## Verification

Run dedicated server and client, reload a saved world, exercise death/respawn and dimension changes. Check missing registry warnings and attachment survival.

## Example request

Port a NeoForge player progression attachment while preserving XP after death and avoiding duplicate End-return rewards.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
