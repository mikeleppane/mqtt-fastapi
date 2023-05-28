import json
from typing import Any

from loguru import logger


def deserialize(payload: bytes) -> Any | None:
    try:
        return json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as ex:
        logger.error(f"Deserializing MQTT payload failed: {ex}")
        return None
