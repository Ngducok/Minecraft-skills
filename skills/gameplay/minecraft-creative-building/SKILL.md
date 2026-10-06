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

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
