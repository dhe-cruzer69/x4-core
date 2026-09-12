"""Simple in-process event bus."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable

Handler = Callable[[dict[str, Any]], None]


class EventBus:
    """Lightweight pub/sub event bus."""

    def __init__(self) -> None:
        self._handlers: dict[str, list[Handler]] = defaultdict(list)

    def on(self, event: str, handler: Handler) -> None:
        self._handlers[event].append(handler)

    def emit(self, event: str, payload: dict[str, Any] | None = None) -> None:
        data = payload or {}
        for handler in self._handlers.get(event, []):
            handler(data)

    def clear(self) -> None:
        self._handlers.clear()
