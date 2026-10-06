---
name: minecraft-scheduling
description: "Fix Minecraft scheduling, asynchronous I/O, task cancellation or Paper/Folia thread-ownership bugs."
---

# Scheduling, threads and Folia ownership

Identify the owner of each operation before changing threads. Separate immutable computation/I/O from live world, inventory and entity mutation.

- On conventional Paper, capture safe inputs on the owning server thread, perform blocking work outside the tick path and apply results on the correct thread after revalidation.
- Under Folia, use entity scheduling for entities that move and region scheduling for location-owned work. Global work is not a substitute for access to arbitrary regions.
- Treat tick delays as simulation time. For offline elapsed time, use persisted timestamps with bounded catch-up rather than assuming a fixed TPS-to-wall-clock conversion.
- Handle logout, entity retirement, unloaded chunks and plugin disable before applying delayed results. Cancel tasks owned by expired sessions.
- Batch work and cap backlog; a task per block or item often turns a small feature into unbounded scheduler overhead. Mark Folia support only after verifying ownership and cross-region behavior.

## Verification

Test delayed completion after logout and disable, slow I/O and cancellation. For Folia support, exercise two players in different regions and an entity crossing region boundaries.

## Example request

Move database work off the tick thread without reading inventories asynchronously or losing a pending result.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
