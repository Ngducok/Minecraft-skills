---
name: minecraft-map-design
description: "Design or validate Minecraft maps, arenas, hubs, adventure levels, creative plots and starter spaces for the chosen gameplay."
---

# Maps, arenas and playable spaces

Define intended player actions, participant count, reset/persistence scope and edition before selecting terrain or a prefab. A minimal survival starter, competitive arena and building plot need different constraints.

- Map routes, sightlines, resource access, safe spawns, checkpoints and boundaries around the requested mode. Symmetry is a design option, not proof of fair spawns.
- Check traversal with actual abilities, equipment and collision geometry. Decorative scale does not establish readable navigation or reachable objectives.
- Make spawn/respawn safe under concurrent joins and failed pastes. Verify headroom, hazard timing and fallback destinations.
- Separate source templates from live player-edited worlds. Reset only the intended instance/region and preserve authorized persistent state.
- Validate schematic dimensions, origin, block entities and contents before allocation. A filename or non-air count does not prove playability.
- Protect creation and edits through existing region/world ownership. Do not assume all maps need islands, currencies or a prebuilt base.

## Verification

Walk representative routes, check alternate movement paths and run a spawn/reset cycle. For arenas test multiple participants; for adventure test progression locks; for plots test boundary edits.

## Example request

Prepare a reusable arena template and a creative plot template with different reset and ownership rules.

## Focused reference

Read [references/map-cases.md](references/map-cases.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [WorldEdit clipboard and schematic API](https://worldedit.enginehub.org/en/latest/api/examples/clipboard/)
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)
- [ChunkGenerator contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/generator/ChunkGenerator.html)
- [Paper teleportation](https://docs.papermc.io/paper/dev/entity-teleport/)
