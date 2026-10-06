# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [ChunkGenerator contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/generator/ChunkGenerator.html) — registry ID `worldgen`; inspected 2026-10-06. Versioned example: generation callbacks need thread safety and must not recursively fetch their generating chunk.
- [WorldEdit clipboard and schematic API](https://worldedit.enginehub.org/en/latest/api/examples/clipboard/) — registry ID `worldedit`; inspected 2026-10-06. Clipboard origin, transforms, format readers and EditSession lifetime matter when pasting.
- [Paper recipes](https://docs.papermc.io/paper/dev/recipes/) — registry ID `recipes`; inspected 2026-10-06. Namespaced recipe registration is available; ingredient behavior must match the chosen recipe interface.
- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/) — registry ID `pdc`; inspected 2026-10-06. Namespaced metadata belongs on supported holders; normal blocks and item lore are not equivalent storage mechanisms.
- [Bedrock World API](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/world?view=minecraft-bedrock-stable) — registry ID `bedrock-world`; inspected 2026-10-06. Native dimensions, events and world access differ from Java platforms and have lifecycle restrictions.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
