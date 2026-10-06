---
name: minecraft-exploration-content
description: "Implement Minecraft exploration routes, structures, encounters, discoveries and renewable resource locations without assuming a mining or RPG server."
---

# Exploration, structures and world content

Define why the player travels and which discoveries should persist. Distinguish procedural generation, template placement and replenishment of existing content.

- Prefer target-version worldgen/datapack features or existing map APIs before a custom generator. Check generation callbacks and chunk ownership before placement.
- Keep positions reproducible where needed with explicit seed/version inputs. Reloads and regeneration must not duplicate unique structures or rewards.
- Scope discovery and loot claims per player/team/world according to the design. A mined or harvested block replaced by a player must not inherit renewable-node rewards unintentionally.
- Make objectives reachable with intended traversal and provide recovery from unsafe spawn or unreachable placement. Do not force a hub, island or dungeon topology.
- Bound scanning and replenishment; avoid synchronous loads over unexplored terrain. Define unloaded-content behavior explicitly.
- Test actual biome, terrain and structure interactions on the target release. Seed parity across edition/runtime changes is not guaranteed by a matching numeric seed.

## Verification

Test repeated loading, player replacement, regeneration, multiple discoverers, negative coordinates and safe approach paths. Verify contents and reward ownership in the actual world.

## Example request

Place discoverable landmarks and renewable resources in an exploration world without granting repeatable unique loot.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
