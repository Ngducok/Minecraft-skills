---
name: minecraft-hosting
description: "Set up or debug Minecraft server startup, local/public resource-pack hosting, ports, scripts and restart behavior on Windows or Linux."
---

# Server and pack hosting operations

Inspect actual process, executable paths, working directory and shell before changing launch scripts. PowerShell and cmd quoting are not interchangeable; local versus public client networks need different URLs.

- Choose the Java runtime required by the target release. Resolve executable paths before launch; avoid versioned installation paths guessed from an older machine.
- Use a direct ZIP response with stable bytes, correct content and matching hash. Check redirects, authentication/HTML pages, caching and reachability from the intended client.
- Keep server and host process ownership explicit. A launcher may stop its own helper on exit; do not kill unrelated Java processes or restart the live server without authorization.
- Choose one pack delivery/configuration owner rather than combining server.properties delivery and plugin delivery accidentally.
- Test ports and startup failures. Background Windows helpers should run hidden unless a visible console was requested; logs must remain inspectable.
- Bind to the intended interface and expose only necessary services. Admin/RCON/management endpoints need authentication and network restrictions; publishing them is a separate deployment action.

## Verification

Start from a path containing spaces, verify served bytes/hash, test an occupied port and exit cleanup. For public hosting, test from another network/client.

## Example request

Create portable cmd/PowerShell launchers without assuming the server and client share localhost.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
