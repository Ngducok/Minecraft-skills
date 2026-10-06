---
name: minecraft-pack-delivery
description: "Build, host or debug Minecraft Java resource-pack metadata, URLs, hashes, required-pack status and client compatibility."
---

# Pack compatibility and delivery

Read the target release's metadata schema and pack format. A resource pack and datapack have different format histories; do not carry a copied compatibility range across an untested release boundary.

- ZIP the pack root with pack.mcmeta and assets directly inside; verify namespace case and every referenced file. Match the exact hosted bytes to the advertised hash.
- Assign pack identity consistently and use the server/plugin delivery owner already present. Avoid duplicate prompts from overlapping delivery mechanisms.
- Use a direct-download URL reachable from the player's network. Localhost means the player's machine, not the remote server. Prefer immutable release URLs when caching is involved.
- Handle decline, download failure, apply failure and success separately. Required-pack UX needs clear instructions and a fallback/disconnect policy chosen by the user.
- Treat client status as presentation readiness, not a cryptographic attestation for valuable actions. Keep gameplay validation server-side even when a client reports success.

## Verification

Download from a second client/network, compare ZIP hash and inspect the client log. Test stale cache, redirect/HTML response and each terminal status.

## Example request

A pack works from the resource-pack folder but fails when sent by a server; trace delivery and exact ZIP bytes.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Adventure resource-pack delivery](https://docs.papermc.io/adventure/resource-pack/)
- [Minecraft Java 1.21.9 pack changes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-9)
- [Minecraft Java 1.21.11 release notes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-11)
