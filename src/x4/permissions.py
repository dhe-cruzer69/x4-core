"""Least-privilege permission checks."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PermissionResult:
    allowed: bool
    reason: str = ""


class Permission:
    """Explicit permission checker."""

    def __init__(self) -> None:
        # actor -> set of "action:resource" patterns
        self._rules: dict[str, set[str]] = {}

    def grant(self, actor: str, action: str, resource: str = "*") -> None:
        key = f"{action}:{resource}"
        self._rules.setdefault(actor, set()).add(key)

    def check(self, actor: str, action: str, resource: str = "*") -> PermissionResult:
        rules = self._rules.get(actor, set())
        exact = f"{action}:{resource}"
        wildcard = f"{action}:*"
        if exact in rules or wildcard in rules or f"*:{resource}" in rules or "*:*" in rules:
            return PermissionResult(allowed=True, reason="granted")
        return PermissionResult(
            allowed=False,
            reason=f"actor={actor!r} denied action={action!r} resource={resource!r}",
        )
