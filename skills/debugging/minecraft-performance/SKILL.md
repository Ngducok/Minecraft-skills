---
name: minecraft-performance
description: "Diagnose Minecraft tick lag, memory growth or plugin throughput using reproducible profiling and bounded workload design."
---

# Profiling and bounded server work

Gather matching build, hardware, active player count and reproduction/load conditions before suggesting tuning flags. Profile while the issue is present, with a duration appropriate to the incident.

- Use the installed supported profiler; modern Paper often bundles spark. Interpret tick time, allocation/GC, worker backlog and blocking I/O separately.
- Find the hot path from evidence before reducing gameplay fidelity. Avoid blaming a plugin by name solely because it appears in a stack.
- Bound per-tick scans, pathfinding, particles, scheduled callbacks and chunk tickets. Event-driven dirty sets or work queues often beat one task per crop/machine/entity.
- Distinguish TPS from wall-clock production and user-visible latency. Async work can still cause memory/backlog pressure or violate API ownership.
- Measure the same workload after one focused change. Server-wide config changes and JVM flags are not a substitute for removing an unbounded loop.
- Keep logs/metrics bounded and redact sensitive player/account data before sharing a report externally.

## Verification

Compare before/after MSPT percentiles, allocation and feature throughput under equivalent load. Verify saved state and gameplay behavior remain correct.

## Example request

A custom farm plugin scans all islands every tick; identify measured costs and replace the unbounded scan.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
