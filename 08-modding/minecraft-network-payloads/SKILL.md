---
name: minecraft-network-payloads
description: "Design or debug Fabric/NeoForge custom network payloads, menu synchronization and validated client requests."
---

# Mod payloads and client authority

Treat a client message as a request, not proof of inventory, permission, price or cooldown. Define direction, channel identity, codec/schema, size limit and handler ownership for each payload.

- Verify registration/handshake requirements and byte limits on the target loader. Validate lengths, ranges, identifiers and remaining state before performing an action.
- Read the documented execution thread; marshal world/player mutation only when necessary onto its owner. Do not blindly enqueue or assume every handler is already safe.
- Send only state the client needs to render or act on. Never send secrets or implement economic validation solely in the screen.
- Include session/version or sequence where stale messages could act on another menu/job. Rate-limit repeated requests and make valuable operations replay-safe.
- Resolve positions/entities within the authenticated player's permitted scope. A packet containing an entity ID does not authorize editing that entity.
- Separate server authoritative state from optimistic visual feedback. Correct the display on denial, reconnect and out-of-order synchronization.

## Verification

Test malformed/oversized payloads, stale sessions, duplicate messages and unsupported clients. Exercise high latency and a dedicated server with client code absent.

## Example request

A modded purchase screen sends price and amount; validate a product request server-side instead.

## Focused reference

Read [references/network-cases.md](references/network-cases.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Fabric networking](https://docs.fabricmc.net/develop/networking)
- [NeoForge payload registration](https://docs.neoforged.net/docs/networking/payload/)
