import sys
from functools import lru_cache

from loguru import logger
from pydantic import AnyUrl, BaseSettings

handlers = [
    {"sink": sys.stdout, "format": "{time} - {message}"},
]

logger.configure(handlers=handlers)


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl | None = None


@lru_cache
def get_settings() -> BaseSettings:
    logger.info("Loading config settings from the environment...")
    return Settings()
