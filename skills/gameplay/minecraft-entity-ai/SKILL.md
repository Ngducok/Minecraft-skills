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

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
