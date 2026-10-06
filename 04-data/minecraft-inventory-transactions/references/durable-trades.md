# Trades across failure boundaries

Use when items and money cross inventory, database or external provider boundaries.

In-tick compensation and crash durability are different guarantees. Database
transactions do not atomically include a Minecraft inventory or a Vault provider.
Writing a prepared operation record alone cannot prove a later external debit was
or was not applied after a crash.

Validate ownership, quantity, provenance, current quote and capacity on the owning
thread. Serialize conflicting operations per account/session. Assign a stable
operation ID; retries must not create another trade. Store intent and sufficient
evidence for reconciliation before crossing a durable boundary.

Track prepared, effects observed, settled, compensated or unresolved states as
appropriate to the actual provider. Prefer provider-supported idempotency/querying
when available. If an effect's outcome is ambiguous, quarantine/reconcile rather
than blindly repeat a deposit, withdrawal or item delivery. Compensation can also
fail; preserve the claim and log the operation ID without exposing private data.

For sell escrow, retain an exact item snapshot including components/metadata. One
owner must hold each stack at each stage. Close/logout/disable returns valuables to
inventory or durable recovery storage; overflow is not permission to discard them.
Test provider rejection, partial insertion, duplicate callback, logout, shutdown and
crash between each irreversible effect. Claim exactly the durability demonstrated.
