"""Least-privilege permission checks."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Permission:
    """Simple allow/deny permission primitive."""

    actor: str
    action: str
    resource: str
    allowed: bool = True

    @classmethod
    def check(cls, actor: str, action: str, resource: str, *, allow: bool = True) -> "Permission":
        """Create a permission decision."""
        return cls(actor=actor, action=action, resource=resource, allowed=allow)

    def raise_if_denied(self) -> None:
        if not self.allowed:
            raise PermissionError(
                f"Permission denied: actor={self.actor!r} action={self.action!r} resource={self.resource!r}"
            )
