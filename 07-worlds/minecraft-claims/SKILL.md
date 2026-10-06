---
name: minecraft-claims
description: "Implement Minecraft island/region authorization or integrate protection checks for building, harvesting, fluids, entities and machines."
---

# Claims, protection and world edits

Use the installed protection platform and its policy queries before adding another parallel claim system. Define ownership, team rights, visitors, automation and administrative bypass explicitly.

- Check flags through supported APIs rather than interpreting region membership as permission. Handle documented bypass separately; default-deny when authoritative protection data is unavailable for a valuable mutation.
- Cover non-player paths: pistons, explosions, fluids, hoppers, projectiles, breeding and machine area operations. Verify the entire target set, not only the initiating block.
- Preserve cancellation from other plugins and choose event priority appropriately. MONITOR handlers observe; they must not reverse protection decisions.
- Revalidate permissions for delayed/batched edits because ownership can change after preview. Cross-world and negative-coordinate boundaries must use the same claim rule.
- Protect shared buffers and containers as well as terrain. A protected farm can still leak products through an unguarded transfer path.
- Keep the allowed/denied reason visible to the player without exposing private owner/account data.

## Verification

Exercise outsider/member/owner/bypass roles across boundaries, including automation and already-cancelled events. Confirm delayed actions respect ownership changes.

## Example request

An area hoe respects its clicked block but harvests a neighbor island; validate every affected location.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)
- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/)
