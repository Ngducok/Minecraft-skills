# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/) — registry ID `paper-setup`; inspected 2026-10-06. Rolling examples use newer dependency coordinates; pin API and toolchain to requested release.
- [Paper vanilla compatibility](https://docs.papermc.io/paper/vanilla/) — registry ID `paper-vanilla`; inspected 2026-10-06. Paper can differ from vanilla simulation; technical contraptions and adventure maps need target-runtime testing.
- [Litematica author repository](https://github.com/maruohon/litematica) — registry ID `litematica`; inspected 2026-10-06. Author implementation is authoritative for litematic serialization; exact packing/version constants must be read from the target branch before writing a serializer.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
