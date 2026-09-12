"""Typed configuration loading."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Config:
    """Simple typed configuration container."""

    data: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def load(cls, defaults: dict[str, Any] | None = None) -> "Config":
        """Load configuration from environment with optional defaults."""
        cfg = dict(defaults or {})
        # Environment variables prefixed with X4_ override defaults
        for key, value in os.environ.items():
            if key.startswith("X4_"):
                cfg[key[3:].lower()] = value
        return cls(data=cfg)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def require(self, key: str) -> Any:
        if key not in self.data:
            raise KeyError(f"Required config key missing: {key}")
        return self.data[key]
