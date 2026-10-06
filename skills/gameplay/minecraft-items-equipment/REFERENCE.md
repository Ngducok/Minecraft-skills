# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/) — registry ID `pdc`; inspected 2026-10-06. Namespaced metadata belongs on supported holders; normal blocks and item lore are not equivalent storage mechanisms.
- [Paper data components](https://docs.papermc.io/paper/dev/data-component-api/) — registry ID `components`; inspected 2026-10-06. Component APIs are version-specific; prefer stable metadata interfaces where sufficient.
- [InventoryClickEvent contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/inventory/InventoryClickEvent.html) — registry ID `inventory-event`; inspected 2026-10-06. Versioned reference example: menu mutations during a click require attention to event transaction timing.
- [Fabric entity attributes](https://docs.fabricmc.net/develop/entities/attributes) — registry ID `fabric-attributes`; inspected 2026-10-06. Attribute registration and modifiers depend on target mappings and game release.
- [NeoForge entity attributes](https://docs.neoforged.net/docs/entities/attributes/) — registry ID `neoforge-attributes`; inspected 2026-10-06. Attribute applicability, registration and synchronization require version-aware verification; do not copy every table claim as a tested formula.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
