---
name: minecraft-crafting-automation
description: "Implement or debug Minecraft crafting, redstone interactions, processing queues and storage logistics using native mechanics where possible."
---

# Crafting, redstone and item processing

Determine whether the goal is native technical compatibility, a recipe change or a new machine. Keep vanilla redstone/hoppers/crafters first when they solve the task.

- Verify behavior on the target runtime and configuration. Paper may alter technical builds; a redstone-current event is not a complete account of item movement.
- For custom processing, define input reservations, progress, energy/consumable costs, pending output and delivery ownership. Inventory capacity can change during work.
- Preserve item conservation through partial transfer, full output, interruption and machine removal. Retry output delivery without consuming fresh inputs again.
- Bound network scans and queued work; chunk/region boundaries need an explicit ownership contract. Do not force-load all connected machines to simplify logic.
- Offline progress is optional and requires a stated resource/catch-up policy. A server plugin cannot replicate a client-side mod merely by using similar models.
- Keep recipe IDs and metadata checks compatible with the selected platform. Test automation entry paths as well as manual crafting.

## Verification

Test manual and automated inputs, full outputs, unload/restart, removal during work and representative technical circuits. Assert declared consumption/production across failures.

## Example request

Fix a hopper-fed processor that consumes inputs again when its output chest is full.

## Focused reference

Read [references/machine-conservation.md](references/machine-conservation.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper recipes](https://docs.papermc.io/paper/dev/recipes/)
- [Paper BlockRedstoneEvent: versioned example](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/block/BlockRedstoneEvent.html)
- [Paper vanilla compatibility](https://docs.papermc.io/paper/vanilla/)
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/)
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/)
- [Create author repository](https://github.com/Creators-of-Create/Create)
