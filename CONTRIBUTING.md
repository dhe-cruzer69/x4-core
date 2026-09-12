# Contributing to x4-core

Thank you for your interest in contributing.

## Development setup

```bash
git clone https://github.com/dhe-cruzer69/x4-core.git
cd x4-core
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Guidelines

- Keep the core free of agent-specific or provider-specific logic.
- Prefer small, focused PRs.
- Add tests for new public APIs.
- Update docs and CHANGELOG for user-visible changes.
- Follow the existing code style (ruff + mypy once configured).

## Pull requests

1. Fork and create a feature branch.
2. Ensure tests and lint pass.
3. Open a PR with a clear description of the change and motivation.

## Code of Conduct

Be respectful. Harassment or discrimination is not tolerated.
