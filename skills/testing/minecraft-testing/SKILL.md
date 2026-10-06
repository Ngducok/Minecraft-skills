---
name: minecraft-testing
description: "Test Minecraft plugin/mod/data changes with pure checks, matching isolated runtimes and real-client validation where needed."
---

# Minecraft verification and regression checks

Choose evidence by failure surface. Arithmetic and state machines can use small pure checks; registries/events need a matching runtime; rendering and pointer behavior need an actual client.

- Reuse existing tests and build scripts before adding a test framework. Leave one meaningful runnable check for non-trivial new logic, not assertions that merely mirror implementation text.
- Test boundaries and failure paths: overflow, full inventories, stale callbacks, cancellation, unload and interrupted commits. Use deterministic seeds where distributions need reproducibility.
- Mocks help isolate API consumers but cannot prove packet handling, native Dialog behavior or every registry lifecycle. Match the MockBukkit/version coverage before relying on it.
- Run isolated servers in a separate working directory and port, with owned process IDs and disposable data. Stop only the process this test created; never terminate arbitrary Java processes.
- Package validation includes JSON references, JAR descriptors, classpath/runtime compatibility and exact ZIP hashes. Do not install a build that failed its relevant gate.
- Label simulations and screenshots accurately. State which clients/GUI scales were tested rather than claiming a generated preview verifies gameplay.

## Verification

Report changed behavior, checks run and remaining limits. Avoid broad repeated tests once checks pass unless new edits or unresolved risks justify them.

## Example request

Verify a resource-pack shop and harvest change without restarting the user's live server.

## Focused reference

Read [references/verification-levels.md](references/verification-levels.md) when handling the detailed cases above.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
