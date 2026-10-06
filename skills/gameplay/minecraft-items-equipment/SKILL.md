---
name: minecraft-items-equipment
description: "Implement Minecraft item identities, equipment effects, durability, consumables, optional rarity and item lifecycle across gameplay modes."
---

# Items, equipment and custom identity

Separate server-authoritative item identity from lore, names, models and translated presentation. Use supported namespaced metadata/components for the target platform.

- Define schema, legal values and migration for custom items. Client-visible components and formatted rarity labels are not proof of provenance.
- Decide stackability and whether traits belong to an item, stack or instance. Split/merge/storage must not reroll traits, duplicate charges or lose durability.
- Apply modifiers with stable ownership and remove only feature-owned effects when equipment changes. Repeated equip/reconnect must not stack duplicate bonuses.
- Respect interaction hand, native cooldown, consumption and cancellation behavior. Both-hand events must not trigger one action twice.
- Support vanilla items and old schemas according to the requested design. Malformed metadata must not silently become a privileged or high-value item.
- Preserve full item data during save, transfer, death and display. Lore stripping or model replacement must not destroy custom state.

## Verification

Test equip/unequip, two hands, stack split/merge, repeated reconnect, cancelled use, death and restart. Compare identity and charges before/after transfers.

## Example request

Add a charged utility item usable in survival and arena kits without assuming random rarity rolls.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
