"""Structured logger."""

from __future__ import annotations

import logging
import sys
from typing import Any


class Logger:
    """Thin structured logger wrapper."""

    def __init__(self, name: str = "x4", level: str = "INFO") -> None:
        self._logger = logging.getLogger(name)
        if not self._logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
            )
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)
        self._logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    def debug(self, msg: str, **kwargs: Any) -> None:
        self._logger.debug(self._format(msg, kwargs))

    def info(self, msg: str, **kwargs: Any) -> None:
        self._logger.info(self._format(msg, kwargs))

    def warning(self, msg: str, **kwargs: Any) -> None:
        self._logger.warning(self._format(msg, kwargs))

    def error(self, msg: str, **kwargs: Any) -> None:
        self._logger.error(self._format(msg, kwargs))

    @staticmethod
    def _format(msg: str, kwargs: dict[str, Any]) -> str:
        if not kwargs:
            return msg
        extra = " ".join(f"{k}={v!r}" for k, v in kwargs.items())
        return f"{msg} | {extra}"
