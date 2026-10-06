# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [WorldEdit clipboard and schematic API](https://worldedit.enginehub.org/en/latest/api/examples/clipboard/) — registry ID `worldedit`; inspected 2026-10-06. Clipboard origin, transforms, format readers and EditSession lifetime matter when pasting.
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/) — registry ID `worldguard`; inspected 2026-10-06. Use flag-aware protection queries; bypass handling is separate from region membership.
- [ChunkGenerator contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/generator/ChunkGenerator.html) — registry ID `worldgen`; inspected 2026-10-06. Versioned example: generation callbacks need thread safety and must not recursively fetch their generating chunk.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
