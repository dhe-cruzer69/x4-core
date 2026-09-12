#!/usr/bin/env python3
"""60-second example for x4-core."""

from x4 import Config, EventBus, Logger, Permission

def main() -> None:
    config = Config.load({"env": "demo"})
    logger = Logger("demo", level=config.get("log_level", "INFO"))
    events = EventBus()
    permissions = Permission()

    permissions.grant("demo-agent", "filesystem.read", "./workspace")

    def on_ready(payload):
        logger.info("runtime ready", **payload)

    events.on("runtime.ready", on_ready)
    events.emit("runtime.ready", {"version": "0.1.0", "env": config.get("env")})

    check = permissions.check("demo-agent", "filesystem.read", "./workspace")
    logger.info("permission check", allowed=check.allowed, reason=check.reason)

    denied = permissions.check("demo-agent", "filesystem.write", "./workspace")
    logger.info("write attempt", allowed=denied.allowed, reason=denied.reason)

if __name__ == "__main__":
    main()
