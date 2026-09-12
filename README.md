# x4-core

**Core runtime and shared infrastructure for the X4 open-source ecosystem.**

Provider-agnostic primitives used by every X4 project: configuration, logging, events, errors, telemetry, authentication, authorization, permissions, plugins, schemas and adapters.

## Status

Early foundation (v0.1.0). Stable API surface is the current goal.

## Features

- Type-safe configuration
- Structured logging + telemetry
- Event bus
- Plugin system
- Permission and policy primitives
- Schema validation helpers
- Clean adapter interfaces for AI, memory, MCP and tools

## Quick Start

```bash
pip install -e .
# or
npm install @x4/core
```

```python
from x4_core import config, logger, events

cfg = config.load()
log = logger.get("x4.core")
bus = events.EventBus()
```

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md).

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

Apache-2.0

## Support

[Sponsor X4](https://github.com/sponsors/dhe-cruzer69)
