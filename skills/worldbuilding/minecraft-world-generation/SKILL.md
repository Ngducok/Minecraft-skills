---
name: minecraft-world-generation
description: "Create Minecraft void/custom worlds, dimension generators or safely replace an existing playable world."
---

# World generation and dimension changes

Determine whether the task concerns new chunks, a new world or replacement of existing data. Changing a generator does not erase already generated terrain.

- Prefer an existing compatible generator or native configuration when sufficient. Custom generation should be deterministic from seed/coordinates and use only the generation context allowed by the platform.
- Do not recursively fetch the chunk being generated. Generator callbacks can run concurrently; mutable shared caches and live-world calls need explicit ownership.
- Specify terrain, biome, structures, decoration and spawn policy independently. A void generator with default structures or unsafe spawn is not a finished void world.
- For world replacement, establish a stopped/saved state, exact world/dimension paths and restorable backup. Preserve player inventories/profiles unless resetting them is explicitly part of the request.
- Account for world UUID references in claims, teleports, crop indexes and player saves. A folder rename does not automatically migrate external identities.
- Avoid broad deletion or copying live worlds. Stage new data, validate spawn and only then switch the authorized world reference.

## Verification

Generate chunks in different orders and compare results. Test negative coordinates, boundary chunks, spawn/respawn and restore to an isolated server.

## Example request

Replace a test Overworld with a void map while keeping player data and a usable rollback.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
