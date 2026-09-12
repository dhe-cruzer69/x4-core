"""Tests for EventBus."""

from x4.core import EventBus


def test_event_bus_emit() -> None:
    bus = EventBus()
    received: list[dict] = []

    def handler(payload: dict) -> None:
        received.append(payload)

    bus.on("test.event", handler)
    bus.emit("test.event", {"ok": True})
    assert received == [{"ok": True}]


def test_event_bus_clear() -> None:
    bus = EventBus()
    bus.on("x", lambda p: None)
    bus.clear()
    assert True  # no error
