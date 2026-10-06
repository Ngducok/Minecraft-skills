---
name: minecraft-creative-building
description: "Build Minecraft creative/building workflows, selection tools, blueprints, batch edits and undo with ownership and bounded world changes."
---

# Creative tools and reversible edits

Prefer installed WorldEdit/native features over a replacement editor. Determine exact selection, affected world, protection context and whether the operation edits templates or live player work.

- Validate bounds, coordinates, material/data compatibility and ownership before editing. Preview counts and resource limits for large operations.
- Use supported edit sessions/clipboard formats and close owned resources. Preserve block entities and transforms deliberately rather than replacing all blocks with bare material IDs.
- Bound each batch and handle cancellation, unload and failure. Partial edits need an explicit progress/undo contract.
- Undo applies to the captured operation, not arbitrary later player changes. Avoid overwriting intervening edits without detecting conflict.
- Separate creative item supply from survival inventory/economy. A builder preview or temporary mode must not leak privileged items into ordinary play.
- Reuse existing permissions and claim services. Reversible does not mean unbounded or authorized outside the selected area.

## Verification

Test asymmetric selections, protected boundaries, block entities, cancellation mid-edit and conflicting edits before undo. Inspect actual placement and saved template round-trip.

## Example request

Add a blueprint preview and bounded paste to a creative plot editor with conflict-aware undo.

## Focused reference

Read [references/map-cases.md](references/map-cases.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [WorldEdit clipboard and schematic API](https://worldedit.enginehub.org/en/latest/api/examples/clipboard/)
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)
- [ChunkGenerator contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/generator/ChunkGenerator.html)
