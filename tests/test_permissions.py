"""Tests for Permission."""

from x4.core import Permission


def test_permission_allow() -> None:
    p = Permission.check("agent", "read", "./workspace", allow=True)
    assert p.allowed is True
    p.raise_if_denied()  # must not raise


def test_permission_deny() -> None:
    p = Permission.check("agent", "write", "/etc", allow=False)
    assert p.allowed is False
    try:
        p.raise_if_denied()
        assert False, "Expected PermissionError"
    except PermissionError:
        pass
