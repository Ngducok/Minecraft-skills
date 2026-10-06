# Read-only MCP stdio adapter

```sh
python -m tools.mcp_server
```

Configure the host with this checkout as working directory and its Python executable. stdout carries newline-delimited JSON-RPC only; no shell execution, writes, network listener or arbitrary paths. Tools: catalog, skill (name + document enum), resolve (project context). The adapter supports MCP 2025-06-18 stdio; unknown protocol versions negotiate that version. Client must disconnect if unsupported.

Test coverage exercises subprocess initialize, discovery, read, traversal rejection and compatibility resolution. It does not certify every MCP host. [Transport specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports). Limits: 1 MiB per inbound message; oversized input closes the session. Streamable HTTP, authentication, notifications beyond initialization and executable operations are intentionally absent.
