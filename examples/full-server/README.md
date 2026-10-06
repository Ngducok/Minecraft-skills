# Disposable full-server test recipe

1. Create an empty test directory outside production. Download an official Paper build for Minecraft 1.21.11 and record build ID/checksum. Use Java 21. Review Minecraft's EULA yourself before accepting it; this repository does not accept it automatically.
2. Start once to generate configuration, then stop normally. Bind server.properties to 127.0.0.1 for local-only testing. Keep online-mode=true. Do not copy production worlds, tokens or player data.
3. Build the Paper example, copy its JAR to plugins/, and put examples/datapack under the generated world's datapacks. Enable examples/resourcepack on the matching Java client. No automated resource-pack hosting is included.
4. Start, join, grant only the test account required command permissions, check `/agentcheck`, `/datapack list`, `/function agentcheck:load` and the resource-pack translation. Check denied permissions with a non-op test account and extra command arguments.
5. Stop/restart, reconnect and repeat checks. Record server build, client version, Java, dependency resolution, logs and observed visuals. Keep compile, server and client results separate.

This recipe is manual and opt-in. Offline CI does not start Minecraft, download a server or accept EULA. No game genre, economy or farming system is preconfigured.
