# x4-core

**Core runtime and shared infrastructure for the X4 open-source ecosystem.**

Provides the foundational primitives used by every other X4 project:

- Configuration
- Structured logging
- Event bus
- Telemetry
- Authentication / Authorization primitives
- Permission model
- Plugin system
- Shared schemas & adapters

## Status

Early foundation (v0.1). Architecture and public API are stabilizing.

## Quick start (planned)

```python
from x4.core import X4

x4 = X4()
x4.config.load()
x4.logger.info("agent started")
x4.events.emit("task.created", {"task_id": "123"})
x4.permissions.check(actor="agent", action="filesystem.write")
```

## Related

- [x4-agents](https://github.com/dhe-cruzer69/x4-agents) — flagship agent runtime
- [x4-ai](https://github.com/dhe-cruzer69/x4-ai)
- [x4-memory](https://github.com/dhe-cruzer69/x4-memory)
- [x4-sandbox](https://github.com/dhe-cruzer69/x4-sandbox)

## License

MIT (see LICENSE)

## Security

See [SECURITY.md](SECURITY.md)
