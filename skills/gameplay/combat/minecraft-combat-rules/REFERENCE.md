# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [EntityDamageByEntityEvent](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/entity/EntityDamageByEntityEvent.html) — registry ID `damage`; inspected 2026-10-06. Damage event exposes source interactions; protection and projectile attribution need separate handling.
- [Paper Team API: versioned example](https://jd.papermc.io/paper/1.21.11/org/bukkit/scoreboard/Team.html) — registry ID `team`; inspected 2026-10-06. Presentation teams expose friendly-fire and collision options but do not replace authoritative group membership/permissions.
- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/) — registry ID `events`; inspected 2026-10-06. Cancellation and priorities affect cooperation with other plugins; observer handlers should not mutate results.
- [Fabric entity attributes](https://docs.fabricmc.net/develop/entities/attributes) — registry ID `fabric-attributes`; inspected 2026-10-06. Attribute registration and modifiers depend on target mappings and game release.
- [NeoForge entity attributes](https://docs.neoforged.net/docs/entities/attributes/) — registry ID `neoforge-attributes`; inspected 2026-10-06. Attribute applicability, registration and synchronization require version-aware verification; do not copy every table claim as a tested formula.
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/) — registry ID `worldguard`; inspected 2026-10-06. Use flag-aware protection queries; bypass handling is separate from region membership.

Shared source records: [knowledge/sources.json](../../../../knowledge/sources.json).
