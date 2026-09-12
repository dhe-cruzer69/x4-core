"""Structured logger."""

from __future__ import annotations

import logging
import sys
from typing import Any


class Logger:
    """Thin wrapper around stdlib logging with a consistent name."""

    def __init__(self, name: str = "x4", level: int = logging.INFO) -> None:
        self._logger = logging.getLogger(name)
        if not self._logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(
                logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")
            )
            self._logger.addHandler(handler)
        self._logger.setLevel(level)

    def info(self, msg: str, **kwargs: Any) -> None:
        self._logger.info(msg, extra=kwargs or None)

    def warning(self, msg: str, **kwargs: Any) -> None:
        self._logger.warning(msg, extra=kwargs or None)

    def error(self, msg: str, **kwargs: Any) -> None:
        self._logger.error(msg, extra=kwargs or None)

    def debug(self, msg: str, **kwargs: Any) -> None:
        self._logger.debug(msg, extra=kwargs or None)
