from fastapi import FastAPI
from loguru import logger

from src.api import health_check, messages
from src.database.db import init_db
from src.services.mqtt_service import start_mqtt_service
from src.util.task_manager import TaskManager


def create_application() -> FastAPI:
    application = FastAPI(title="MQTT - FastAPI", version="0.1.0")
    application.include_router(health_check.router)
    application.include_router(messages.router)
    return application


app = create_application()
task_manager = TaskManager()


@app.on_event("startup")
async def startup_event() -> None:
    logger.info("Starting up...")
    init_db(app)
    await start_mqtt_service(task_manager)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    logger.info("Cancelling all running tasks...")
    await task_manager.cancel_all()
    logger.info("Shutting down...")
