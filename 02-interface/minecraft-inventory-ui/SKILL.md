---
name: minecraft-inventory-ui
description: "Create chest-style Minecraft menus or fix click, drag, shift-click and inventory-transfer behavior."
---

# Inventory menus and safe transfers

Identify the menu using its holder/session, not a translated or user-editable title. Decide which slots are decorative, interactive, player storage or explicit escrow before writing handlers.

- Map raw slots to the actual top/bottom inventories; out-of-window and null inventory clicks are legitimate cases. Inspect click type and InventoryAction rather than assuming left-click.
- Handle drag, shift movement, hotbar-number swaps, offhand swaps, double-click collection and creative actions according to menu policy.
- Cancel prohibited mutations before processing custom actions. Schedule menu replacement after the event when its transaction timing requires it.
- Transfer using actual item similarity, metadata and maximum stack sizes. Model partial capacity and leftovers; never silently drop valuable items because a GUI slot is full.
- On close, logout, death and disable, account for every held item exactly once. If only presentation changes are requested, avoid rebuilding the trade engine.

## Verification

Use a transfer matrix covering all click actions, inventory full, cursor occupied and interrupted close. Assert total items before/after plus deliberate sales or costs.

## Example request

A sell basket duplicates items under shift-click and loses leftovers on close; repair its transfer policy.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Custom InventoryHolders](https://docs.papermc.io/paper/dev/custom-inventory-holder/)
- [InventoryClickEvent contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/inventory/InventoryClickEvent.html)
