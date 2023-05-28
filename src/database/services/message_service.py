import json
from typing import Any

from src.models.message import MQTTMessage
from src.models.tortoise import Message


async def save(message: MQTTMessage) -> None:
    message = Message(created_at=message.created_at, payload=json.dumps(message.payload))
    await message.save()


async def get_all() -> list[dict[str, Any]]:
    return await Message.all().values("created_at", "payload")
