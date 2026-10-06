# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Fabric project setup](https://docs.fabricmc.net/develop/getting-started/creating-a-project) — registry ID `fabric`; inspected 2026-10-06. Generator accepts target Minecraft version; loader/API/Loom and mappings must be selected together.
- [Fabric networking](https://docs.fabricmc.net/develop/networking) — registry ID `fabric-net`; inspected 2026-10-06. Logical client/server payload handling and validation are separate from singleplayer appearance.
- [Fabric data generation](https://docs.fabricmc.net/develop/data-generation/setup) — registry ID `datagen`; inspected 2026-10-06. Datagen produces version-specific JSON for recipes, tags and assets; generated output is still validated by the game.

Shared source records: [knowledge/sources.json](../../../../knowledge/sources.json).
