import json

from loguru import logger
from tortoise.exceptions import IncompleteInstanceError, IntegrityError

from src.models.message import MQTTMessage
from src.models.tortoise import Message


async def save(message: MQTTMessage) -> None:
    message_db = Message(created_at=message.created_at, payload=json.dumps(message.payload))
    try:
        await message_db.save()
    except (IntegrityError, IncompleteInstanceError) as ex:
        logger.error(f"An error occurred while trying to save message {message_db} to db: {ex}")


async def get_all(limit: int | None = None) -> list[MQTTMessage]:
    messages: list[MQTTMessage] = []
    if limit:
        async for message in Message.all().limit(limit).values("created_at", "payload"):
            messages.append(MQTTMessage(**message))
    else:
        async for message in Message.all().values("created_at", "payload"):
            messages.append(MQTTMessage(**message))
    return messages
