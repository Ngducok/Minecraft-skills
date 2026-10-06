---
name: minecraft-dependency-detection
description: "Resolve installed dependencies, pinned API artifacts and build-tool compatibility without speculative additions."
---

# Dependency Detection

Read Maven/Gradle files, wrappers, catalogs, lockfiles and plugin descriptors. Keep game, loader, mappings, Java and API versions distinct. Prefer existing dependency or native API. Check repository provenance and license before adding an artifact; never invent Maven coordinates. Compile against the exact target and verify packaging scope, shading/relocation and service declarations. Do not bundle server APIs into plugin JARs.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
