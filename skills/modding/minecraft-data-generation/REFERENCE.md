# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Fabric data generation](https://docs.fabricmc.net/develop/data-generation/setup) — registry ID `datagen`; inspected 2026-10-06. Datagen produces version-specific JSON for recipes, tags and assets; generated output is still validated by the game.
- [Paper recipes](https://docs.papermc.io/paper/dev/recipes/) — registry ID `recipes`; inspected 2026-10-06. Namespaced recipe registration is available; ingredient behavior must match the chosen recipe interface.
- [Paper data components](https://docs.papermc.io/paper/dev/data-component-api/) — registry ID `components`; inspected 2026-10-06. Component APIs are version-specific; prefer stable metadata interfaces where sufficient.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
