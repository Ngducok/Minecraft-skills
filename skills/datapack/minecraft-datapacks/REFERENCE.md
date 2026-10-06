# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Java Edition 1.21.9 release notes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-9) — registry ID `release-1219`; inspected 2026-10-06. Official rolling documentation; resolve target release before using symbols.
- [Minecraft Java 1.21.11 release notes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-11) — registry ID `release-12111`; inspected 2026-10-06. Historical example only: release notes record resource/data format changes and item/block atlas constraints; not a global target version.
- [Paper recipes](https://docs.papermc.io/paper/dev/recipes/) — registry ID `recipes`; inspected 2026-10-06. Namespaced recipe registration is available; ingredient behavior must match the chosen recipe interface.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
