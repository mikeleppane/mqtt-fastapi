from loguru import logger
from tortoise.exceptions import IncompleteInstanceError, IntegrityError

from src.models.message import MQTTMessage
from src.models.tortoise import Message


async def save(message: MQTTMessage) -> None:
    try:
        await Message(created_at=message.created_at, payload=message.payload).save()
    except (IntegrityError, IncompleteInstanceError) as ex:
        logger.error(f"An error occurred while trying to save message to db: {ex}")


async def get_all(limit: int | None = None) -> list[MQTTMessage]:
    if limit:
        return [
            MQTTMessage(**message)
            async for message in Message.all().limit(limit).values("created_at", "payload")
        ]
    return [
        MQTTMessage(**message) async for message in Message.all().values("created_at", "payload")
    ]
