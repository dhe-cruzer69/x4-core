# x4-core

**Core runtime and shared infrastructure for the X4 open-source ecosystem**

Provides the common primitives used by every X4 project: configuration, logging, events, telemetry, authentication, permissions, plugins and schemas.

## Status

Early foundation (v0.1). API is experimental and will evolve.

## Install (planned)

```bash
pip install x4-core
# or
npm install @x4/core
```

## Design Goals

- Type-safe, minimal surface area
- Zero heavy dependencies where possible
- Explicit configuration over magic
- Observability built-in
- Plugin system for extension

## Architecture

```
x4-core/
├── packages/
│   ├── config/
│   ├── logging/
│   ├── errors/
│   ├── events/
│   ├── telemetry/
│   ├── auth/
│   ├── permissions/
│   └── plugins/
├── schemas/
├── adapters/
├── tests/
└── docs/
```

## Related

- [x4-agents](https://github.com/dhe-cruzer69/x4-agents) — consumes x4-core
- [x4-ai](https://github.com/dhe-cruzer69/x4-ai)
- [x4-memory](https://github.com/dhe-cruzer69/x4-memory)

## License

Apache-2.0 (or MIT — final decision pending)

## Security

See [SECURITY.md](SECURITY.md). Report vulnerabilities privately.
