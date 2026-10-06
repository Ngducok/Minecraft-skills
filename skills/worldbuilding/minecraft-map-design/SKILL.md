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

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
