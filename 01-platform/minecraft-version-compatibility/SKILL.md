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

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper server requirements](https://docs.papermc.io/paper/getting-started/)
- [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/)
- [Fabric project setup](https://docs.fabricmc.net/develop/getting-started/creating-a-project)
- [NeoForge project setup](https://docs.neoforged.net/docs/gettingstarted/)
- [Minecraft Java 1.21.11 release notes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-11)
