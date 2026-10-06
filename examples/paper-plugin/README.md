# Paper plugin walkthrough

Example target: Paper 1.21.11, Java 21. This is a documented example, not a global default. No plugin source, build file or JAR is included.

In a user's project, resolve the exact Paper API artifact and build system, use the API as a provided dependency, and register a small authorized `/agentcheck` command through the appropriate descriptor. Check permission and arguments before behavior.

Compile within that project; inspect the JAR for its descriptor/entrypoint and absence of bundled server APIs. In a disposable matching server, test authorized and denied command execution, extra arguments, startup/shutdown and reconnect. A compile pass does not prove live permissions or client behavior. Record resolved SNAPSHOT timestamp/build/checksum when reproducibility matters.
