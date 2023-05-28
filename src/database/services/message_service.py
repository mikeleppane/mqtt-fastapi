import json

from loguru import logger
from tortoise.exceptions import IntegrityError, IncompleteInstanceError

from src.models.message import MQTTMessage
from src.models.tortoise import Message, MessageSchema


async def save(message: MQTTMessage) -> None:
    message = Message(created_at=message.created_at, payload=json.dumps(message.payload))
    try:
        await message.save()
    except (IntegrityError, IncompleteInstanceError) as ex:
        logger.error(f"An error occurred while trying to save message {message} to db: {ex}")


async def get_all() -> list[MessageSchema]:
    return await Message.all().values("created_at", "payload")
