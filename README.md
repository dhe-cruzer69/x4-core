# x4-core

**Core runtime and shared infrastructure for the X4 open-source ecosystem.**

Config • Logging • Events • Permissions • Plugins (coming)

[![CI](https://github.com/dhe-cruzer69/x4-core/actions/workflows/ci.yml/badge.svg)](https://github.com/dhe-cruzer69/x4-core/actions)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

Part of [ARIEX4Ops / X4](https://github.com/dhe-cruzer69).

## Status

**v0.1.0** — Foundation with working primitives and tests.

## Installation

```bash
pip install -e ".[dev]"   # from source
```

## 60-second example

```bash
python examples/hello_x4_core.py
```

```python
from x4 import Config, Logger, EventBus, Permission

config = Config.load({"env": "demo"})
logger = Logger("demo")
events = EventBus()
perm = Permission()

perm.grant("agent", "filesystem.read", "./workspace")
events.on("ready", lambda p: logger.info("ready", **p))
events.emit("ready", {"version": "0.1.0"})

print(perm.check("agent", "filesystem.read", "./workspace"))
# PermissionResult(allowed=True, reason='granted')
```

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md).

```
x4-core
├── Config          typed configuration
├── Logger          structured logging
├── EventBus        in-process pub/sub
└── Permission      least-privilege checks
```

Higher packages (x4-agents, x4-ai, x4-sandbox …) depend on x4-core.
x4-core never depends on them.

## Development

```bash
pip install -e ".[dev]"
ruff check .
pytest -q
```

## Related projects

| Project | Role |
|---------|------|
| [x4-agents](https://github.com/dhe-cruzer69/x4-agents) | Flagship agent runtime |
| [x4-ai](https://github.com/dhe-cruzer69/x4-ai) | Provider-agnostic AI |
| [x4-memory](https://github.com/dhe-cruzer69/x4-memory) | Local-first memory |
| [x4-sandbox](https://github.com/dhe-cruzer69/x4-sandbox) | Sandboxed execution |
| [x4-mcp-gateway](https://github.com/dhe-cruzer69/x4-mcp-gateway) | Secure MCP gateway |
| [x4-research](https://github.com/dhe-cruzer69/x4-research) | Evidence-first research |

## License

Apache-2.0

## Security

See [SECURITY.md](SECURITY.md).

## Support

[GitHub Sponsors](https://github.com/sponsors/dhe-cruzer69)
