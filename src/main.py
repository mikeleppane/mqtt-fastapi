import asyncio

from fastapi import FastAPI
from loguru import logger

from src.api import health_check
from src.services.mqtt_service import create_mqtt_service
from src.util.task_manager import TaskManager


def create_application() -> FastAPI:
    application = FastAPI(title="MQTT - FastAPI", version="0.1.0")
    application.include_router(health_check.router)

    return application


app = create_application()
task_manager = TaskManager()


@app.on_event("startup")
async def startup_event() -> None:
    logger.info("Starting up...")
    task_manager.add(asyncio.create_task(create_mqtt_service()))


@app.on_event("shutdown")
async def shutdown_event() -> None:
    logger.info("Cancelling all running tasks...")
    await task_manager.cancel_all()
    logger.info("Shutting down...")
