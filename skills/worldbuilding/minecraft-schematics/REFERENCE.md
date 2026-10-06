# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Sponge schematic v3 specification](https://github.com/SpongePowered/Schematic-Specification/blob/master/versions/schematic-3.md) — registry ID `sponge`; inspected 2026-10-06. Sponge format is its own schema; it is not interchangeable with Litematica or vanilla structure NBT.
- [Litematica author repository](https://github.com/maruohon/litematica) — registry ID `litematica`; inspected 2026-10-06. Author implementation is authoritative for litematic serialization; exact packing/version constants must be read from the target branch before writing a serializer.
- [WorldEdit clipboard and schematic API](https://worldedit.enginehub.org/en/latest/api/examples/clipboard/) — registry ID `worldedit`; inspected 2026-10-06. Clipboard origin, transforms, format readers and EditSession lifetime matter when pasting.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
