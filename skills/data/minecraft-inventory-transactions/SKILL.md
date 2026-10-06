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

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
