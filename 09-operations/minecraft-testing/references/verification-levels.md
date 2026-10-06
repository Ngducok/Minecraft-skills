# Evidence levels

Use to choose checks and accurately report what they establish.

| Check | Establishes | Does not establish |
| --- | --- | --- |
| Pure runnable checks | Arithmetic, ranges, state transitions | Native events or rendering |
| Mock runtime | Covered API/event behavior | Unimplemented native internals |
| Matching dedicated server | Load, registries, lifecycle, server behavior | Client geometry or focus |
| Actual client with pack | Assets, click bounds, GUI scale, interaction | Crash recovery or real load |
| Failure/restore drill | Tested persistence boundary and restore path | Every possible crash timing |
| Representative load profile | Measured bottleneck for stated workload | Capacity under other workloads |

Select the smallest check that covers the changed behavior. Keep one runnable check
for nontrivial arithmetic/state logic; avoid tests that merely repeat implementation
wording. Native mechanics and rendering need the corresponding runtime/client.

Report exact target/build, relevant setup, observable result and remaining limit.
An unperformed client check stays unverified even if compilation and JSON parsing
pass. A restart test alone does not prove interruption-safe inventory transactions.
