"""Unit tests for x4-core primitives."""

from x4 import Config, EventBus, Logger, Permission


def test_config_load_and_get():
    cfg = Config.load({"env": "test", "debug": True})
    assert cfg.get("env") == "test"
    assert cfg.get("debug") is True
    assert cfg.get("missing", "default") == "default"


def test_config_require_raises():
    cfg = Config.load()
    try:
        cfg.require("does_not_exist")
        assert False, "should have raised"
    except KeyError:
        pass


def test_event_bus():
    bus = EventBus()
    received = []

    def handler(payload):
        received.append(payload)

    bus.on("test.event", handler)
    bus.emit("test.event", {"ok": True})
    assert received == [{"ok": True}]


def test_permission_grant_and_check():
    perm = Permission()
    perm.grant("agent", "filesystem.read", "./workspace")
    result = perm.check("agent", "filesystem.read", "./workspace")
    assert result.allowed is True

    denied = perm.check("agent", "filesystem.write", "./workspace")
    assert denied.allowed is False


def test_logger_smoke():
    log = Logger("test", level="DEBUG")
    log.info("hello", key="value")
    log.debug("debug message")
