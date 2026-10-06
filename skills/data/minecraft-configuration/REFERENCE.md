# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Plugin configuration](https://docs.papermc.io/paper/dev/plugin-configurations/) — registry ID `config`; inspected 2026-10-06. Malformed/missing configuration can otherwise resemble an empty configuration; distinguish configuration failure from defaults.
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/) — registry ID `database`; inspected 2026-10-06. Embedded and standalone database choices differ; JDBC is an API and does not supply every database driver.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
