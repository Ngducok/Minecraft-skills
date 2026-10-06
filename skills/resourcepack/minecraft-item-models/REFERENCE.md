# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper data components](https://docs.papermc.io/paper/dev/data-component-api/) — registry ID `components`; inspected 2026-10-06. Component APIs are version-specific; prefer stable metadata interfaces where sufficient.
- [Minecraft Java 1.21.11 release notes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-11) — registry ID `release-12111`; inspected 2026-10-06. Historical example only: release notes record resource/data format changes and item/block atlas constraints; not a global target version.
- [Fabric data generation](https://docs.fabricmc.net/develop/data-generation/setup) — registry ID `datagen`; inspected 2026-10-06. Datagen produces version-specific JSON for recipes, tags and assets; generated output is still validated by the game.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
