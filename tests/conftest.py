import os
from asyncio import get_event_loop

import asyncio_mqtt as aiomqtt
import pytest
import pytest_asyncio
from httpx import AsyncClient
from starlette.testclient import TestClient
from tortoise import Tortoise

from src import main
from src.config import get_settings, Settings
from src.main import create_application
from src.models.tortoise import Message


def get_settings_override():
    return Settings(testing=bool(1), database_url=os.environ.get("DATABASE_URL"))


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:
        yield test_client


@pytest_asyncio.fixture(scope="module")
async def get_mqtt_client(hostname="mosquitto"):
    client = aiomqtt.Client(hostname=hostname)
    try:
        yield client
    finally:
        await client.disconnect()


@pytest_asyncio.fixture(scope="function")
async def test_app_with_db():
    # set up
    app = create_application()
    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={'models': ['src.models.tortoise']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
    await Message.all().delete()

    app.dependency_overrides[get_settings] = get_settings_override

    async with AsyncClient(app=app, base_url="http://localhost:8800") as client:
        yield client

    await Tortoise.close_connections()


@pytest.fixture(scope="module")
def event_loop():
    loop = get_event_loop()
    yield loop
    loop.close()
