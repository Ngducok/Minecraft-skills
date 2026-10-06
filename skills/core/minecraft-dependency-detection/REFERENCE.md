# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/) — registry ID `paper-setup`; inspected 2026-10-06. Rolling examples use newer dependency coordinates; pin API and toolchain to requested release.
- [Fabric project setup](https://docs.fabricmc.net/develop/getting-started/creating-a-project) — registry ID `fabric`; inspected 2026-10-06. Generator accepts target Minecraft version; loader/API/Loom and mappings must be selected together.
- [NeoForge project setup](https://docs.neoforged.net/docs/gettingstarted/) — registry ID `neoforge`; inspected 2026-10-06. Use the target-version toolchain and event model; Fabric and NeoForge APIs are not drop-in replacements.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
