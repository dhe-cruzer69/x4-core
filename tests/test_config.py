"""Tests for Config."""

from x4.core import Config


def test_config_load_defaults() -> None:
    cfg = Config.load({"mode": "test"})
    assert cfg.get("mode") == "test"
    assert cfg.get("missing", "fallback") == "fallback"


def test_config_require_raises() -> None:
    cfg = Config.load({})
    try:
        cfg.require("nonexistent")
        assert False, "Expected KeyError"
    except KeyError:
        pass
