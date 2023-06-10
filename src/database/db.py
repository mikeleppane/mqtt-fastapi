import os

from fastapi import FastAPI
from loguru import logger
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["src.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["src.models.tortoise", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def generate_schema() -> None:
    logger.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["../models/tortoise"]},
    )
    logger.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


# new
if __name__ == "__main__":
    run_async(generate_schema())
