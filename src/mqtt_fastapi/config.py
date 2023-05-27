import sys
from functools import lru_cache

from loguru import logger
from pydantic import BaseSettings

config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
    ],
}
logger.configure(**config)


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)


@lru_cache
def get_settings() -> BaseSettings:
    logger.info("Loading config settings from the environment...")
    return Settings()
