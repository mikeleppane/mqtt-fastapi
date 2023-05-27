from fastapi import FastAPI
from loguru import logger

from src.api import health_check

app = FastAPI()


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(health_check.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event() -> None:
    logger.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event() -> None:
    logger.info("Shutting down...")
