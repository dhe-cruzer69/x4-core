# x4-core Architecture

## Purpose

x4-core is the shared foundation for the entire X4 ecosystem. It provides boring, reliable primitives so higher-level projects (x4-agents, x4-ai, x4-sandbox, etc.) do not re-implement configuration, logging, events, permissions, or plugin loading.

## Package layout

```
x4-core/
├── packages/
│   ├── config/          # typed configuration loading & validation
│   ├── logger/          # structured logging
│   ├── errors/          # error taxonomy & structured exceptions
│   ├── events/          # in-process event bus
│   ├── telemetry/       # metrics & traces hooks
│   ├── auth/            # identity primitives
│   ├── permissions/     # least-privilege checks
│   ├── plugins/         # plugin discovery & lifecycle
│   └── runtime/         # process lifecycle helpers
├── schemas/              # shared JSON Schema / Pydantic models
├── adapters/             # external system adapters
├── tests/
├── examples/
└── docs/
```

## Design principles

1. **Typed first** — public APIs prefer strong types.
2. **No hidden globals** — explicit dependency injection where practical.
3. **Fail closed** — permission denials and config errors are explicit.
4. **Observable** — structured logs and optional telemetry hooks.
5. **Thin** — business logic lives in higher packages (agents, research, etc.).

## Dependency direction

```
x4-agents / x4-ai / x4-sandbox / x4-mcp-gateway / x4-research
                    │
                    ▼
                 x4-core
```

Higher packages may depend on x4-core. x4-core must not depend on them.
