# Paper plugin example

Explicit target: Paper API 1.21.11-R0.1-SNAPSHOT, Java 21. This is an example target, not a global default. SNAPSHOT coordinates are mutable; record resolved timestamp/build/checksum for reproducible releases.

```sh
mvn -f examples/paper-plugin/pom.xml -B package
```

Output: build/paper-example/agent-check-1.0.0.jar. Only plugin code and plugin.yml are packaged; Paper API is provided by server. Install only in a disposable matching server. `/agentcheck` succeeds for authorized players/console, rejects extra arguments and requires `agentcheck.use`.

Compile and descriptor inspection do not establish live permission behavior. Test op/non-op permission, startup/shutdown and reconnect manually. No persistent state or scheduler is needed for this example.
