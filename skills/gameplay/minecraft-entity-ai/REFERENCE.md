# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper mob goals](https://docs.papermc.io/paper/dev/mob-goals/) — registry ID `mob-goals`; inspected 2026-10-06. Goal priorities, behavior types and lifecycle matter; goals are constrained by mob capabilities.
- [Paper entity pathfinder](https://docs.papermc.io/paper/dev/entity-pathfinder/) — registry ID `pathfinder`; inspected 2026-10-06. Navigation requests can fail; native movement rules still apply.
- [Display entities](https://docs.papermc.io/paper/dev/display-entities/) — registry ID `display`; inspected 2026-10-06. Displays provide visual transforms/interpolation; they do not automatically provide gameplay interaction or collision.
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/) — registry ID `scheduler`; inspected 2026-10-06. Ticks are simulation time; normal Bukkit world access is not made safe merely by moving it off-thread.
- [Fabric project setup](https://docs.fabricmc.net/develop/getting-started/creating-a-project) — registry ID `fabric`; inspected 2026-10-06. Generator accepts target Minecraft version; loader/API/Loom and mappings must be selected together.
- [NeoForge project setup](https://docs.neoforged.net/docs/gettingstarted/) — registry ID `neoforge`; inspected 2026-10-06. Use the target-version toolchain and event model; Fabric and NeoForge APIs are not drop-in replacements.
- [Bedrock server Script API](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server?view=minecraft-bedrock-stable) — registry ID `bedrock-script`; inspected 2026-10-06. Stable and preview Script API surfaces need matching module dependencies and engine support.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
