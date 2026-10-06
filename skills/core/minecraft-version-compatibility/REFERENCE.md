# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper server requirements](https://docs.papermc.io/paper/getting-started/) — registry ID `paper-start`; inspected 2026-10-06. Version table separates Java 21-era Minecraft releases from Java 25-era releases; never copy current defaults into older targets.
- [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/) — registry ID `paper-setup`; inspected 2026-10-06. Rolling examples use newer dependency coordinates; pin API and toolchain to requested release.
- [Fabric project setup](https://docs.fabricmc.net/develop/getting-started/creating-a-project) — registry ID `fabric`; inspected 2026-10-06. Generator accepts target Minecraft version; loader/API/Loom and mappings must be selected together.
- [NeoForge project setup](https://docs.neoforged.net/docs/gettingstarted/) — registry ID `neoforge`; inspected 2026-10-06. Use the target-version toolchain and event model; Fabric and NeoForge APIs are not drop-in replacements.
- [Minecraft Java 1.21.11 release notes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-11) — registry ID `release-12111`; inspected 2026-10-06. Historical example only: release notes record resource/data format changes and item/block atlas constraints; not a global target version.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
