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

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
