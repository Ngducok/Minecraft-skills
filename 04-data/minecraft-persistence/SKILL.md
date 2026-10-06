---
name: minecraft-persistence
description: "Design or repair Minecraft player, island, item and transaction persistence, migrations and recovery after restart or crash."
---

# Persistent state and recovery

Identify authoritative state and durability needs before choosing storage. PDC suits metadata on supported holders; queryable/shared accounts may require a database. JDBC drivers are dependencies, not part of Java's standard library.

- Choose stable UUID/key ownership and schema versioning. Distinguish an item instance, stack quantity, player profile and island account; do not use names or lore as identifiers.
- Ordinary blocks do not expose item-style PDC. Store custom plant state using a persistent world/chunk/coordinate index and remove it when blocks change.
- Capture immutable snapshots on the owner thread; persist off-thread with ordered writes. A stale asynchronous save must not overwrite newer state.
- Use transactions/constraints for money or shared balances when available. Saving a player and saving an external ledger are not one atomic operation.
- For file storage, write a temporary file and use an appropriate atomic replacement where supported. Preserve previous data on parse failure; migration must be rerunnable or guarded.
- Back up consistent database/world/account state and test restoration. Include WAL/auxiliary files correctly rather than copying a live database file blindly.

## Verification

Inject failure between commits, retry a migration and simulate out-of-order saves. Restore into an isolated runtime and reconcile balances/items.

## Example request

A balance reverts after logout because an older asynchronous save finishes last.

## Focused reference

Read [references/durable-trades.md](references/durable-trades.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/)
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/)
- [NeoForge data attachments](https://docs.neoforged.net/docs/datastorage/attachments/)
