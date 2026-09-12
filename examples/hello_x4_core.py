#!/usr/bin/env python3
"""Minimal example — run with: python examples/hello_x4_core.py"""

from x4.core import Config, Logger, EventBus, Permission

def main() -> None:
    config = Config.load({"app": "hello-x4"})
    logger = Logger("hello")
    events = EventBus()

    def on_ready(payload: dict) -> None:
        logger.info(f"Runtime ready: {payload}")

    events.on("runtime.ready", on_ready)
    logger.info("Starting x4-core example")
    events.emit("runtime.ready", {"version": "0.1.0", "app": config.get("app")})

    perm = Permission.check("demo", "read", "./workspace", allow=True)
    perm.raise_if_denied()
    logger.info("Permission check passed")

if __name__ == "__main__":
    main()
