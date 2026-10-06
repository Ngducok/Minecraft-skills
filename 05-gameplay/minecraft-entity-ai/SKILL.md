---
name: minecraft-entity-ai
description: "Implement Minecraft mob/NPC/pet behavior, navigation, spawning and entity lifecycle on the chosen plugin/mod/add-on platform."
---

# Entities, navigation and behavior

Choose native goals/navigation when supported. Separate behavior, ownership, visuals and interaction; a display entity is not automatically a colliding or thinking mob.

- Check entity type capabilities and valid targets. A successful API call does not prove that a path is reachable or that an attribute affects that entity.
- Assign goal priorities and control types deliberately. Remove only behavior owned by the feature; deleting all goals can erase essential native behavior.
- Bound search/path updates and handle blocked paths, unloaded destinations and removed targets without retrying every tick indefinitely.
- Persist stable identity/traits only when required and reacquire live entities safely. Spawn reason, despawn rules and caps affect population beyond custom AI.
- Keep entity mutation on the current owner thread. Cross-region movement invalidates assumptions under region-threaded servers.
- Verify the platform's actual hooks for modded or Bedrock behavior. Paper goal APIs do not map directly to another loader's entity code.

## Verification

Test unreachable destinations, competing native goals, owner logout, entity removal, unload/reload and multiple active actors. Measure pathfinding cost under the intended population.

## Example request

Make a guide NPC follow its player without stripping unrelated mob behavior or flooding path requests.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper mob goals](https://docs.papermc.io/paper/dev/mob-goals/)
- [Paper entity pathfinder](https://docs.papermc.io/paper/dev/entity-pathfinder/)
- [Display entities](https://docs.papermc.io/paper/dev/display-entities/)
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/)
- [Fabric project setup](https://docs.fabricmc.net/develop/getting-started/creating-a-project)
- [NeoForge project setup](https://docs.neoforged.net/docs/gettingstarted/)
- [Bedrock server Script API](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server?view=minecraft-bedrock-stable)
