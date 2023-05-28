import asyncio
from typing import Any

import asyncio_mqtt as aiomqtt
from loguru import logger

from src.database.services.message_service import save
from src.models.message import MQTTMessage
from src.util.deserialize import deserialize

MOSQUITTO_HOSTNAME = "mosquitto"
RECONNECT_INTERVAL_SECS = 5
TOPIC = "humidity/outside"


def build_mqtt_client(hostname: str = MOSQUITTO_HOSTNAME) -> aiomqtt.Client:
    return aiomqtt.Client(hostname=hostname)


async def handle_incoming_message(message: Any) -> None:
    if payload := deserialize(message.payload):
        mqtt_message = MQTTMessage.from_payload(payload)
        mqtt_message.dump()
        await save(message=mqtt_message)


async def listen(client: aiomqtt.Client) -> None:
    while True:
        try:
            async with client as mqtt_client:
                async with mqtt_client.messages() as messages:
                    await mqtt_client.subscribe("#")
                    async for message in messages:
                        if message.topic.matches(TOPIC):
                            await handle_incoming_message(message)
        except aiomqtt.MqttError as error:
            logger.error(f'Error "{error}". Reconnecting in {RECONNECT_INTERVAL_SECS} seconds.')
            await asyncio.sleep(RECONNECT_INTERVAL_SECS)


async def create_mqtt_service() -> asyncio.Task:
    async with asyncio.TaskGroup() as tg:
        return tg.create_task(listen(build_mqtt_client("mosquitto")))
