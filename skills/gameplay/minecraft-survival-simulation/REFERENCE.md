# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper vanilla compatibility](https://docs.papermc.io/paper/vanilla/) — registry ID `paper-vanilla`; inspected 2026-10-06. Paper can differ from vanilla simulation; technical contraptions and adventure maps need target-runtime testing.
- [Block Ageable](https://jd.papermc.io/paper/1.21.11/org/bukkit/block/data/Ageable.html) — registry ID `age`; inspected 2026-10-06. Crop age is block data, distinct from entity Ageable; use material-specific maximum age.
- [EntityBreedEvent](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/entity/EntityBreedEvent.html) — registry ID `breed`; inspected 2026-10-06. Breeding can be observed/cancelled; persistence, attribution and custom traits remain application responsibilities.
- [PlayerHarvestBlockEvent](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/player/PlayerHarvestBlockEvent.html) — registry ID `harvest`; inspected 2026-10-06. Right-click harvest has a distinct event; block break is not every crop interaction.
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/) — registry ID `scheduler`; inspected 2026-10-06. Ticks are simulation time; normal Bukkit world access is not made safe merely by moving it off-thread.
- [Bedrock World API](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/world?view=minecraft-bedrock-stable) — registry ID `bedrock-world`; inspected 2026-10-06. Native dimensions, events and world access differ from Java platforms and have lifecycle restrictions.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
