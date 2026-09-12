# x4-core

**Core runtime and shared infrastructure for the X4 open-source ecosystem.**

Config • Logging • Events • Telemetry • Auth • Permissions • Plugins • Schemas

Part of [ARIEX4Ops / X4](https://github.com/dhe-cruzer69).

## Status

Early foundation (v0.1.x). API is experimental and may change.

## Installation

```bash
pip install x4-core   # or: pip install -e .
```

## Quick start

```python
from x4.core import Config, Logger, EventBus, Permission

config = Config.load()
logger = Logger("x4")
events = EventBus()

logger.info("x4-core started")
events.emit("runtime.ready", {"version": "0.1.0"})

# Permission check example
allowed = Permission.check(actor="agent", action="filesystem.write", resource="./workspace")
```

## Architecture

```
x4-core/
├── packages/
│   ├── config/
│   ├── logging/
│   ├── events/
│   ├── telemetry/
│   ├── auth/
│   ├── permissions/
│   ├── plugins/
│   └── schemas/
├── adapters/
├── tests/
├── examples/
└── docs/
```

## Related projects

- [x4-agents](https://github.com/dhe-cruzer69/x4-agents) — flagship agent runtime
- [x4-ai](https://github.com/dhe-cruzer69/x4-ai) — provider-agnostic AI layer
- [x4-memory](https://github.com/dhe-cruzer69/x4-memory) — local-first agent memory
- [x4-sandbox](https://github.com/dhe-cruzer69/x4-sandbox) — sandboxed tool execution
- [x4-mcp-gateway](https://github.com/dhe-cruzer69/x4-mcp-gateway) — secure MCP gateway

## License

Apache-2.0

## Security

See [SECURITY.md](SECURITY.md). Report vulnerabilities privately.

## Support

[GitHub Sponsors](https://github.com/sponsors/dhe-cruzer69)
