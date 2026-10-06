# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Fabric networking](https://docs.fabricmc.net/develop/networking) — registry ID `fabric-net`; inspected 2026-10-06. Logical client/server payload handling and validation are separate from singleplayer appearance.
- [NeoForge payload registration](https://docs.neoforged.net/docs/networking/payload/) — registry ID `neoforge-net`; inspected 2026-10-06. Payload registration, execution thread and size limits are explicit versioned contracts.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
