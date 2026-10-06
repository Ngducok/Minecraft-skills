# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [NeoForge project setup](https://docs.neoforged.net/docs/gettingstarted/) — registry ID `neoforge`; inspected 2026-10-06. Use the target-version toolchain and event model; Fabric and NeoForge APIs are not drop-in replacements.
- [NeoForge data attachments](https://docs.neoforged.net/docs/datastorage/attachments/) — registry ID `attachments`; inspected 2026-10-06. Persistent and synchronized attachments differ; death cloning and End return must not duplicate state.
- [NeoForge payload registration](https://docs.neoforged.net/docs/networking/payload/) — registry ID `neoforge-net`; inspected 2026-10-06. Payload registration, execution thread and size limits are explicit versioned contracts.

Shared source records: [knowledge/sources.json](../../../../knowledge/sources.json).
