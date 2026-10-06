# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper recipes](https://docs.papermc.io/paper/dev/recipes/) — registry ID `recipes`; inspected 2026-10-06. Namespaced recipe registration is available; ingredient behavior must match the chosen recipe interface.
- [Paper BlockRedstoneEvent: versioned example](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/block/BlockRedstoneEvent.html) — registry ID `redstone`; inspected 2026-10-06. Current-change events are one hook; they are not a complete simulation/transfer log.
- [Paper vanilla compatibility](https://docs.papermc.io/paper/vanilla/) — registry ID `paper-vanilla`; inspected 2026-10-06. Paper can differ from vanilla simulation; technical contraptions and adventure maps need target-runtime testing.
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/) — registry ID `scheduler`; inspected 2026-10-06. Ticks are simulation time; normal Bukkit world access is not made safe merely by moving it off-thread.
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/) — registry ID `database`; inspected 2026-10-06. Embedded and standalone database choices differ; JDBC is an API and does not supply every database driver.
- [Create author repository](https://github.com/Creators-of-Create/Create) — registry ID `create`; inspected 2026-10-06. Automation design reference; Create is a mod and cannot be installed as an ordinary Paper plugin.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
