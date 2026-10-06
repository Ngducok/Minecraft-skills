# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/) — registry ID `pdc`; inspected 2026-10-06. Namespaced metadata belongs on supported holders; normal blocks and item lore are not equivalent storage mechanisms.
- [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/) — registry ID `paper-setup`; inspected 2026-10-06. Rolling examples use newer dependency coordinates; pin API and toolchain to requested release.

Shared source records: [knowledge/sources.json](../../../../knowledge/sources.json).
