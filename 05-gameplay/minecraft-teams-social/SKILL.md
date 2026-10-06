---
name: minecraft-teams-social
description: "Build Minecraft parties, teams, guilds, cooperative ownership and role changes with authoritative membership and scoped access."
---

# Teams, cooperation and shared ownership

Separate persistent social membership, temporary match teams and scoreboard presentation. Use existing group/claim services instead of parallel lists when they own the feature.

- Use stable player/group IDs and specify invite, join, leave, kick, transfer and disband rules. Offline members and expired invites need deterministic handling.
- Recheck effective roles and ownership at each valuable action. Menu visibility, a team prefix and a stale invitation are not authorization.
- Scope friendly fire, collision, shared storage and objective credit independently. Scoreboard options do not replace persistent membership or claim rules.
- Make leadership transfer and simultaneous membership changes atomic within the chosen store. Prevent orphaned ownership and duplicate group rewards.
- Preserve player progress and shared valuables under the requested leave/disband policy. Do not infer that leaving a party should wipe personal state.
- Send external notifications only when authorized. Player-facing messages should describe current state and the next available action.

## Verification

Test expired invitations, concurrent joins/kicks, leader logout, transfer/disband and context-sensitive permissions. Verify persistent identity after reconnect and scoreboard replacement.

## Example request

Let a cooperative team share build rights without granting members global administrative permissions.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper Team API: versioned example](https://jd.papermc.io/paper/1.21.11/org/bukkit/scoreboard/Team.html)
- [LuckPerms developer API](https://github.com/LuckPerms/LuckPerms/wiki/Developer-API)
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/)
- [Safe dynamic MiniMessage replacements](https://docs.papermc.io/adventure/minimessage/dynamic-replacements/)
