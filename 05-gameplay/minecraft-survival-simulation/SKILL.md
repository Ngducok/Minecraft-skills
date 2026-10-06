---
name: minecraft-survival-simulation
description: "Tune Minecraft survival simulation, growth, breeding, spawning, hunger, weather and renewable resources while preserving target-runtime behavior."
---

# Native simulation and renewable systems

Determine which native rules should change and which must remain compatible. Use target gamerules, block/entity data and existing events before creating a parallel simulator.

- Separate random ticks, scheduled ticks, entity ticks and wall-clock time. Chunk availability and server load alter observed timing; do not promise a universal real-time growth interval.
- Treat crops, breeding, decay, weather and regeneration as examples of state transitions, not a mandatory farming system. Check material/entity-specific limits rather than fixed age constants.
- Define unloaded/offline behavior explicitly. Catch-up simulation must be bounded and preserve required inputs; vanilla inactivity is also a valid policy.
- Account for harvest, break, explosion, fluid, tool and cancelled-event paths relevant to the change. Native and custom reward owners must not both issue drops.
- Test renewability and failure recovery when designing survival starts. Avoid making custom rarity/weight or currencies prerequisites for ordinary survival.
- Check Paper configuration differences and other listeners before diagnosing broken native behavior. Do not globally disable safeguards merely to match a technical build.

## Verification

Test loaded/unloaded chunks, native/random interaction paths, reset/restart and cancelled protection events. Measure timings on the stated runtime instead of converting ticks blindly to seconds.

## Example request

Change animal population rules and crop timing on an SMP while retaining vanilla drops and player contraptions.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper vanilla compatibility](https://docs.papermc.io/paper/vanilla/)
- [Block Ageable](https://jd.papermc.io/paper/1.21.11/org/bukkit/block/data/Ageable.html)
- [EntityBreedEvent](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/entity/EntityBreedEvent.html)
- [PlayerHarvestBlockEvent](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/player/PlayerHarvestBlockEvent.html)
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/)
- [Bedrock World API](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/world?view=minecraft-bedrock-stable)
