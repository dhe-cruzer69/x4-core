# Contributing to x4-core

Thank you for your interest in contributing to the X4 ecosystem.

## Development setup

```bash
git clone https://github.com/dhe-cruzer69/x4-core.git
cd x4-core
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Guidelines

- Open an issue before large changes
- Keep PRs focused and small
- Add tests for new behaviour
- Update documentation when changing public APIs
- Follow existing code style

## Pull Request checklist

- [ ] Tests pass
- [ ] Documentation updated
- [ ] No secrets committed
- [ ] Changelog entry (if user-facing)
