---
name: minecraft-inventory-transactions
description: "Implement Minecraft item transfers, crafting commits, loadout swaps, trades and optional economy effects with loss/duplication protection."
---

# Item transfers and atomic effects

Identify all stores affected and one authoritative owner for each effect. Use native inventory operations and existing providers first; add a durable journal only when required failure guarantees justify it.

- Validate actor, session, exact item identity, amount and destination capacity at commit. Client text, lore and previewed prices are not trusted state.
- Account for partial insertion and preserve the exact remainder. Define what happens when a destination fills, an actor logs out or a feature disables.
- Serialize conflicting operations and reject stale/replayed requests. An inventory event cancellation is not itself a database transaction.
- Distinguish ordinary in-thread rollback from crash durability. External providers, inventories and databases rarely share one atomic commit.
- If outcomes are ambiguous, preserve an unresolved claim for reconciliation rather than blindly repeating delivery or compensation.
- Currency is optional. Creative loadouts, crafting reservations, reward chests and player trades still require item conservation and clear ownership.

## Verification

Test full destinations, exact/partial stacks, duplicate activation, cancelled events, disconnect and interruption between effects. State which recovery boundaries are proven.

## Example request

A loadout swap overwrites items when inventory is full; preserve both equipment and remainder.

## Focused reference

Read [references/durable-trades.md](references/durable-trades.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Custom InventoryHolders](https://docs.papermc.io/paper/dev/custom-inventory-holder/)
- [InventoryClickEvent contract](https://jd.papermc.io/paper/1.21.11/org/bukkit/event/inventory/InventoryClickEvent.html)
- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/)
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/)
- [VaultAPI author repository](https://github.com/MilkBowl/VaultAPI)
