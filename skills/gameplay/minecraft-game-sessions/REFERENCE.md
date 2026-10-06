# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/) — registry ID `events`; inspected 2026-10-06. Cancellation and priorities affect cooperation with other plugins; observer handlers should not mutate results.
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/) — registry ID `scheduler`; inspected 2026-10-06. Ticks are simulation time; normal Bukkit world access is not made safe merely by moving it off-thread.
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/) — registry ID `database`; inspected 2026-10-06. Embedded and standalone database choices differ; JDBC is an API and does not supply every database driver.
- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/) — registry ID `pdc`; inspected 2026-10-06. Namespaced metadata belongs on supported holders; normal blocks and item lore are not equivalent storage mechanisms.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
