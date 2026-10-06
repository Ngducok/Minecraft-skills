---
name: minecraft-version-compatibility
description: "Select compatible Minecraft versions, loaders, Java toolchains and APIs when starting, upgrading or diagnosing a Minecraft project."
---

# Version and platform compatibility

Identify edition, exact game release, server/loader build, supported clients and Java runtime from actual artifacts. Do not assume the current documentation default is the user's target.

- Distinguish Paper plugins, vanilla datapacks, client/server mods and Bedrock add-ons before choosing implementation. A Java resource pack changes presentation; it cannot register a new server block type by itself.
- Build a small compatibility matrix: game, platform, Java, mappings, dependencies, pack formats and client requirements. Record which combinations were actually exercised.
- Prefer release-specific docs, API signatures and bundled assets. Treat rolling docs and snapshots as leads that require target-version verification.
- Keep protocol translators separate from feature support: accepting a connection does not prove Dialog, item-component or asset compatibility.
- Preserve a working build when upgrading; do not move the game, loader and every dependency simultaneously unless the requested migration needs it.

## Verification

Compile against pinned dependencies, start a matching isolated runtime and exercise one affected feature per supported client. State unsupported combinations explicitly.

## Example request

A plugin compiles on a newer API but fails on an older server; find the first incompatible symbol and smallest compatible change.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
