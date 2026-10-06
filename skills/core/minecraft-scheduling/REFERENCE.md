# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/) — registry ID `scheduler`; inspected 2026-10-06. Ticks are simulation time; normal Bukkit world access is not made safe merely by moving it off-thread.
- [Paper and Folia scheduling](https://docs.papermc.io/paper/dev/folia-support/) — registry ID `folia`; inspected 2026-10-06. Entity, region, global and async responsibilities differ; setting support metadata does not establish safety.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
