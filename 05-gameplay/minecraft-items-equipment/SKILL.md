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

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/)
- [Paper data components](https://docs.papermc.io/paper/dev/data-component-api/)
- [InventoryClickEvent contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/inventory/InventoryClickEvent.html)
- [Fabric entity attributes](https://docs.fabricmc.net/develop/entities/attributes)
- [NeoForge entity attributes](https://docs.neoforged.net/docs/entities/attributes/)
