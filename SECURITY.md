# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

Please report security vulnerabilities privately.

- Do **not** open a public issue for security problems.
- Preferred: open a private security advisory on this repository, or contact the maintainers via the profile contact methods.

We aim to acknowledge reports within 72 hours and provide a remediation timeline as soon as the issue is confirmed.

## Scope

x4-core provides shared primitives (config, logging, events, permissions, plugins). Security-sensitive areas include:

- Permission evaluation correctness
- Plugin loading isolation
- Configuration secret handling
- Telemetry data leakage

Agent-level execution, sandboxing, and MCP tool policy live in sibling projects (`x4-agents`, `x4-sandbox`, `x4-mcp-gateway`).
