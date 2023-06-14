import asyncio
import os
from datetime import datetime, timedelta
from typing import Any
from unittest.mock import patch

import asyncio_mqtt as aiomqtt
import pytest
from fastapi import status

from src.models.tortoise import Message


async def wait_for_db_sync(expected_count: int, timeout: float = 3):
    start = datetime.now()
    elapsed = start + timedelta(seconds=timeout)
    while True:
        if await Message.all().count() == expected_count:
            return
        await asyncio.sleep(0.1)
        if datetime.now() > elapsed:
            raise AssertionError("Timeout elapsed while waiting for db to sync")


async def publish_message(client: aiomqtt.Client, message: Any, topic: str):
    async with client as m_client:
        await m_client.publish(topic=topic, payload=message)


@pytest.mark.asyncio
async def test_read_messages_with_empty_db(test_app_with_db):
    """
    GIVEN
    WHEN health check endpoint is called with GET method
    THEN response with status 200 and body OK is returned
    """
    response = await test_app_with_db.get("/v1/messages")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 0


@pytest.mark.asyncio
async def test_read_messages_with_one_message_in_db(test_app_with_db, get_mqtt_client):
    """
    GIVEN one message is published to broker and wait for them to be stored in a db
    WHEN messages endpoint is called with GET method
    THEN response with status 200 and response length is 1
    """

    await publish_message(get_mqtt_client, 55, os.environ["TOPIC"])
    await wait_for_db_sync(1)

    response = await test_app_with_db.get("/v1/messages")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["payload"] == 55


@pytest.mark.asyncio
async def test_read_messages_with_two_messages_in_db(test_app_with_db, get_mqtt_client):
    """
    GIVEN two messages are published to broker and wait for them to be stored in a db
    WHEN messages endpoint is called with GET method
    THEN response with status 200 and response length is 2
    """

    await publish_message(get_mqtt_client, 55, os.environ["TOPIC"])
    await publish_message(get_mqtt_client, '{"hum": 0.66}', os.environ["TOPIC"])
    await wait_for_db_sync(2)

    response = await test_app_with_db.get("/v1/messages")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
    assert response.json()[0]["payload"] == {"hum": 0.66}
    assert response.json()[1]["payload"] == 55


@pytest.mark.asyncio
async def test_read_messages_with_limit(test_app_with_db, get_mqtt_client):
    """
    GIVEN two messages are published to broker and wait for them to be stored in a db
    WHEN messages endpoint is called with GET method and query param limit is set to 1
    THEN response with status 200 and response length is 1
    """

    await publish_message(get_mqtt_client, 55, os.environ["TOPIC"])
    await publish_message(get_mqtt_client, 65, os.environ["TOPIC"])
    await wait_for_db_sync(2)

    response = await test_app_with_db.get("/v1/messages?limit=1")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_read_messages_should_return_messages_in_correct_order(test_app_with_db, get_mqtt_client):
    """
    GIVEN two messages are published to broker and wait for them to be stored in a db
    WHEN messages endpoint is called with GET method
    THEN response with status 200, response length is 2 and payload order is descending by timestamp
    """

    await publish_message(get_mqtt_client, 55, os.environ["TOPIC"])
    await publish_message(get_mqtt_client, 65, os.environ["TOPIC"])
    await wait_for_db_sync(2)

    response = await test_app_with_db.get("/v1/messages")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
    assert response.json()[0]["payload"] == 65


@pytest.mark.asyncio
async def test_read_messages_should_return_400_error_if_limit_is_not_positive(test_app_with_db):
    """
    GIVEN
    WHEN messages endpoint is called with GET method query param limit is set to -1
    THEN response with status is 400
    """

    response = await test_app_with_db.get("/v1/messages?limit=-1")

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
@patch('src.api.messages.get_all', autospec=AssertionError("DB operation failed"))
async def test_read_messages_should_return_500_error_if_db_transaction_fails(mock_get_all, test_app_with_db):
    """
    GIVEN get_all function mocked to raise an error when called
    WHEN messages endpoint is called with GET method
    THEN response with status is 500
    """

    response = await test_app_with_db.get("/v1/messages")

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


@pytest.mark.asyncio
async def test_read_messages_should_return_empty_if_published_message_is_not_valid(test_app_with_db, get_mqtt_client):
    """
    GIVEN one message with invalid payload is published to broker
    WHEN
    THEN message is not stored to db and messages endpoint returns empty
    """

    await publish_message(get_mqtt_client, '\\', os.environ["TOPIC"])

    with pytest.raises(AssertionError):
        await wait_for_db_sync(1, 0.5)

    response = await test_app_with_db.get("/v1/messages")
    assert len(response.json()) == 0
