# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Custom InventoryHolders](https://docs.papermc.io/paper/dev/custom-inventory-holder/) — registry ID `inventory`; inspected 2026-10-06. Menu identity can be carried by a holder rather than guessed from display titles.
- [InventoryClickEvent contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/inventory/InventoryClickEvent.html) — registry ID `inventory-event`; inspected 2026-10-06. Versioned reference example: menu mutations during a click require attention to event transaction timing.
- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/) — registry ID `pdc`; inspected 2026-10-06. Namespaced metadata belongs on supported holders; normal blocks and item lore are not equivalent storage mechanisms.
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/) — registry ID `database`; inspected 2026-10-06. Embedded and standalone database choices differ; JDBC is an API and does not supply every database driver.
- [VaultAPI author repository](https://github.com/MilkBowl/VaultAPI) — registry ID `vault`; inspected 2026-10-06. Vault bridges economy providers; withdrawal responses and provider availability must be checked.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
