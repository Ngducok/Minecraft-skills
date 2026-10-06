---
name: minecraft-proxy-security
description: "Configure or debug Minecraft Velocity/Bungee-style proxy identity forwarding and protected backend connections."
---

# Proxies, forwarding and backend security

Determine proxy/platform versions, forwarding mode and network topology before changing authentication. Explain security-sensitive steps clearly rather than giving ambiguous shorthand.

- Match forwarding mode and backend settings to supported versions. Treat forwarding secrets as secrets; never print them into shared logs or commit them to source.
- If a backend uses offline mode for a proxy, ensure only the trusted proxy can connect. Bind locally when co-located or use firewall/tunnel restrictions across hosts.
- Modern forwarding does not replace backend network isolation. An IP check inside a late plugin event is not equivalent to preventing direct unauthenticated login.
- Verify stable forwarded UUID/IP identity because permissions, wallets, bans and player data depend on it. Switching modes can make players appear as different accounts.
- Keep plugin channels scoped and authenticate valuable cross-server requests; player-originated channel data must not act as an admin message.
- Preserve the authorized deployment boundary. Firewall changes and live network cutovers need the user's actual scope, a reachable fallback and explicit impact description.

## Verification

Confirm legitimate proxy login works, direct backend login fails and saved player identity survives reconnect. Test shared-secret mismatch without exposing its value.

## Example request

A proxy network lets users bypass the proxy and impersonate offline-mode accounts; close the backend path.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
