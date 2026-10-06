# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Custom InventoryHolders](https://docs.papermc.io/paper/dev/custom-inventory-holder/) — registry ID `inventory`; inspected 2026-10-06. Menu identity can be carried by a holder rather than guessed from display titles.
- [InventoryClickEvent contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/inventory/InventoryClickEvent.html) — registry ID `inventory-event`; inspected 2026-10-06. Versioned reference example: menu mutations during a click require attention to event transaction timing.

Shared source records: [knowledge/sources.json](../../../../knowledge/sources.json).
