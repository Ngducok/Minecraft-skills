# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/) — registry ID `worldguard`; inspected 2026-10-06. Use flag-aware protection queries; bypass handling is separate from region membership.
- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/) — registry ID `events`; inspected 2026-10-06. Cancellation and priorities affect cooperation with other plugins; observer handlers should not mutate results.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
