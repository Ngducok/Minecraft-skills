---
name: minecraft-plugin-apis
description: "Integrate existing Minecraft economy, island, protection or content plugins without redundant services or unsafe lifecycle assumptions."
---

# Economy, island and plugin API integration

Inventory existing dependencies and public integration points before introducing another library or replacing a working subsystem. Choose one owner for wallet, islands, claims and resource-pack delivery.

- Compile against the intended API with runtime dependency declarations. Detect provider presence and compatible versions before exposing features that require it.
- Use supported services/events rather than scraping command output or parsing lore. Keep adapters small and only abstract when genuinely supporting multiple implementations.
- Economy responses can fail; compare balances, rounding and provider currencies deliberately. Vault is a bridge, not proof that an economy provider exists.
- Island framework data, team roles and blueprint lifecycle must remain authoritative when integrated. Do not maintain a shadow ownership list that drifts after transfers/resets.
- Handle dependency disable/reload or document a restart-only contract. Clean up callbacks and cached provider objects owned by expired plugin instances.
- Test conflicts between feature owners. Avoid double-selling, duplicate harvest listeners, overlapping HUD updates or two pack prompts.

## Verification

Run with dependency present, absent and misconfigured. Verify provider failure leaves valuables intact and existing plugin-owned progression survives the integration.

## Example request

Connect a shop to the existing economy and island API instead of adding a second wallet and claim database.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [VaultAPI author repository](https://github.com/MilkBowl/VaultAPI)
- [BentoBox documentation](https://docs.bentobox.world/en/latest/)
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)
- [Paper plugin descriptors](https://docs.papermc.io/paper/dev/plugin-yml/)
