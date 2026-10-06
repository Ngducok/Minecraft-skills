# Resource pack smoke example

Target: Java client 1.21.11, resource format 75.0. Copy this folder into client resourcepacks, enable it and inspect reload logs. Select English (US) for this single-locale example; additional locales need their own translation entries.

On a test server with permission, run:

```mcfunction
/tellraw @s {"translate":"agentcheck.status"}
```

Expected text: Agent resource pack active. No Mojang textures/binaries are distributed. JSON parsing proves syntax only; translation resolution needs an actual matching client. A server cannot infer the client's visual result from an API compile.
