---
name: minecraft-version-detection
description: "Detect exact Minecraft releases, loader builds, Java and content formats from project artifacts."
---

# Version Detection

Compare dependency coordinates, lockfiles, manifests, startup logs and executable Java version. A plugin api-version is a minimum API declaration, not the running server build. Client protocol compatibility does not prove resource-pack or API compatibility. Report conflicting evidence instead of selecting latest. Resolve pack major/minor versions independently. Use pinned Javadocs or dependency inspection for every unfamiliar API symbol.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
