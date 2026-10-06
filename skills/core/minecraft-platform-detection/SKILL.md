---
name: minecraft-platform-detection
description: "Distinguish Java server platforms, proxies, mod loaders and Bedrock execution environments."
---

# Platform Detection

Inspect descriptors, imports and launch arguments. Distinguish Bukkit/Paper server plugins from Velocity proxy plugins, client-only mods, dedicated-server mods and Bedrock scripting. Paper inheritance does not prove Purpur-only API portability; Folia support requires ownership-safe scheduling. Identify hybrid platforms as separate unverified targets, not a union of supported APIs. Keep crossplay client behavior separate from backend platform.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
