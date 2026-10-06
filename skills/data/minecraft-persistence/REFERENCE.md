# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/) — registry ID `pdc`; inspected 2026-10-06. Namespaced metadata belongs on supported holders; normal blocks and item lore are not equivalent storage mechanisms.
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/) — registry ID `database`; inspected 2026-10-06. Embedded and standalone database choices differ; JDBC is an API and does not supply every database driver.
- [NeoForge data attachments](https://docs.neoforged.net/docs/datastorage/attachments/) — registry ID `attachments`; inspected 2026-10-06. Persistent and synchronized attachments differ; death cloning and End return must not duplicate state.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
