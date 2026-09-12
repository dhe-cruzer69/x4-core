# x4-core

**Core runtime and shared infrastructure for the X4 open-source ecosystem.**

Shared primitives used by every X4 project: configuration, logging, events, telemetry, authentication, permissions, plugins, and schemas.

## Status

Early foundation (v0.1.0-dev). Designed to be the boring, reliable base layer so agent, AI, memory, MCP and sandbox projects do not re-implement infrastructure.

## Goals

- Type-safe configuration and validation
- Structured logging + event bus
- Permission and policy primitives
- Plugin loading and lifecycle
- Telemetry hooks (no vendor lock-in)
- Zero business logic (agents live elsewhere)

## Quick Start

```bash
pip install -e ".[dev]"   # once packaging is complete
```

```python
from x4.core import Config, Logger, EventBus, Permission

config = Config.load()
logger = Logger(name="x4")
bus = EventBus()

bus.emit("runtime.started", {"version": "0.1.0"})
logger.info("x4-core ready")
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

## Security

See [SECURITY.md](SECURITY.md). Report vulnerabilities privately.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache-2.0 (see LICENSE).

## Roadmap

See [ROADMAP.md](ROADMAP.md).

---

Part of the [X4 ecosystem](https://github.com/dhe-cruzer69) by ARIEX4Ops.
