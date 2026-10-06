# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper teleportation](https://docs.papermc.io/paper/dev/entity-teleport/) — registry ID `teleport`; inspected 2026-10-06. Async teleport avoids blocking chunk loads; blocking its future on the tick thread can deadlock.
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/) — registry ID `scheduler`; inspected 2026-10-06. Ticks are simulation time; normal Bukkit world access is not made safe merely by moving it off-thread.
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/) — registry ID `worldguard`; inspected 2026-10-06. Use flag-aware protection queries; bypass handling is separate from region membership.
- [Fabric entity attributes](https://docs.fabricmc.net/develop/entities/attributes) — registry ID `fabric-attributes`; inspected 2026-10-06. Attribute registration and modifiers depend on target mappings and game release.
- [NeoForge entity attributes](https://docs.neoforged.net/docs/entities/attributes/) — registry ID `neoforge-attributes`; inspected 2026-10-06. Attribute applicability, registration and synchronization require version-aware verification; do not copy every table claim as a tested formula.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
