"""Typed configuration loader."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Config:
    """Simple, explicit configuration container."""

    data: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def load(cls, overrides: dict[str, Any] | None = None) -> "Config":
        """Load config from environment with optional overrides."""
        data: dict[str, Any] = {
            "env": os.getenv("X4_ENV", "development"),
            "log_level": os.getenv("X4_LOG_LEVEL", "INFO"),
            "debug": os.getenv("X4_DEBUG", "0") == "1",
        }
        if overrides:
            data.update(overrides)
        return cls(data=data)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def require(self, key: str) -> Any:
        if key not in self.data:
            raise KeyError(f"Required config key missing: {key}")
        return self.data[key]
