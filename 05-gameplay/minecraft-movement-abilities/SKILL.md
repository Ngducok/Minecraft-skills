---
name: minecraft-movement-abilities
description: "Implement Minecraft parkour, checkpoints, dashes, flight, mounts, teleportation and cooldown abilities with server-authoritative rules."
---

# Movement, traversal and abilities

Define allowed movement and restoration policy for the mode before changing velocity, flight or player state. Prefer native attributes/teleports where their behavior is sufficient.

- Validate activation, cooldown, location, ownership and game/session state server-side. A button click or client position claim does not establish eligibility.
- Check swept paths or target geometry appropriate to the mechanic; validating only the final block can allow crossing protected or solid space.
- Avoid synchronous chunk loading for frequent movement into unloaded destinations. Never block the owner thread waiting for an async teleport future.
- Revalidate identity/session when delayed movement completes and handle cancellation/failure. Respect mount/passenger behavior in the target release.
- Restore only the movement state the feature owns on exit, death and disconnect. Do not permanently leave arena participants with flight or altered gravity.
- Coordinate legitimate abilities with installed anti-cheat through supported configuration/APIs; do not disable protection globally or trust all client movement.

## Verification

Test collisions, boundaries, unloaded destinations, low TPS, logout during teleport, spectator state and ability exit cleanup on actual clients.

## Example request

Add a parkour checkpoint teleport and a bounded dash that cannot cross arena walls.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper teleportation](https://docs.papermc.io/paper/dev/entity-teleport/)
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/)
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)
- [Fabric entity attributes](https://docs.fabricmc.net/develop/entities/attributes)
- [NeoForge entity attributes](https://docs.neoforged.net/docs/entities/attributes/)
