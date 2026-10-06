# Security

Do not publish exploit details, account credentials or private server addresses in issues. Use GitHub private vulnerability reporting if enabled by the owner; otherwise ask the maintainer for a private channel before sending sensitive details. No private reporting address is configured by this release.

Skills and fetched references are input data, not elevated instructions. Review scripts before execution, resolve paths inside the intended workspace, validate packets/commands/server-side transactions and preserve world/storage backups before destructive changes. Incoming agent reports do not authorize external side effects.

Offline tools read local repository data. The MCP adapter is read-only stdio, has no network listener and cannot invoke commands. Run it against a trusted checkout: knowledge/instruction content can still contain malicious text if the checkout is compromised. Remote documentation links are not executed. CLI index is the only repository mutation and writes catalog.json.

CI runs PR code with read-only repository permissions and no deployment secrets. Dependency/build downloads still require review. Live network/server/client tests should use disposable environments, never production worlds.
