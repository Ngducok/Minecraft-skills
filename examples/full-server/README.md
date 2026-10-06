# Disposable server verification walkthrough

1. Resolve an exact server build, Minecraft/client release and Java runtime. Create an isolated test directory; keep production worlds and credentials separate. Review the EULA before accepting it yourself.
2. Generate test configuration, stop normally and bind localhost when testing locally. Preserve authenticated player identity and explicit command permissions.
3. Build requested plugin/mod/pack artifacts in the user's project. Install only those artifacts into the disposable matching environment.
4. Check startup logs, authorized/denied commands, content reload and matching client behavior. Record version/build/checksums and actual observations.
5. Stop, restart, reconnect and verify recovery. Keep compile, runtime and client results separate.

This is written guidance only. No server distribution, startup script, installer or automatic EULA acceptance is included. No game genre is preconfigured.
