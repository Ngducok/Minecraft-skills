---
name: minecraft-combat-rules
description: "Implement Minecraft PvP/PvE damage, equipment effects, friendly fire, attribution and encounter rules without assuming an RPG stat system."
---

# Damage, combat and encounter rules

Write the requested damage/interaction policy before adding attributes. Preserve native combat when enough; custom stats, classes and phases are optional mechanics.

- Identify attacker, projectile/source owner, defender, world/session and protection context. Environmental and reflected damage need explicit attribution policies.
- Use the target damage/attribute event model; avoid cancelling then reapplying damage recursively without a guarded and tested reason.
- Define ordering of armor, effects, blocking, invulnerability and custom modifiers. Do not apply the same bonus in both native attributes and a damage listener.
- Enforce friendly-fire, spectator and safe-zone rules server-side. Visual team labels and collision settings do not fully define combat authorization.
- Check death, assists, simultaneous kills and disconnect at reward time. One death must not generate duplicate score or rewards across observers.
- Test actual client/server combat and platform differences. Attribute names, ranges and formulas require target verification rather than copied tables.

## Verification

Exercise melee, projectile, indirect/environmental damage, cancelled protection events and concurrent lethal hits. Compare intended versus actual damage and attribution.

## Example request

Add a friendly-fire rule to a team arena while preserving vanilla armor and attack cooldowns.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [EntityDamageByEntityEvent](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/entity/EntityDamageByEntityEvent.html)
- [Paper Team API: versioned example](https://jd.papermc.io/paper/1.21.11/org/bukkit/scoreboard/Team.html)
- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/)
- [Fabric entity attributes](https://docs.fabricmc.net/develop/entities/attributes)
- [NeoForge entity attributes](https://docs.neoforged.net/docs/entities/attributes/)
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)
