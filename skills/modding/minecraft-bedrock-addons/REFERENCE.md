# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Bedrock add-on introduction](https://learn.microsoft.com/en-us/minecraft/creator/documents/gettingstarted?view=minecraft-bedrock-stable) — registry ID `bedrock-start`; inspected 2026-10-06. Bedrock resource/behavior packs and add-on packaging differ from Java assets and datapacks.
- [Bedrock server Script API](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server?view=minecraft-bedrock-stable) — registry ID `bedrock-script`; inspected 2026-10-06. Stable and preview Script API surfaces need matching module dependencies and engine support.
- [Geyser resource packs](https://geysermc.org/wiki/geyser/packs/) — registry ID `geyser-packs`; inspected 2026-10-06. Java resource packs are not automatically converted to Bedrock packs.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
