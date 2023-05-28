from fastapi import APIRouter

from src.database.services.message_service import get_all
from src.models.message import MQTTMessage

router = APIRouter()


@router.get("/", response_model=list[MQTTMessage])
async def read_all_messages() -> list[MQTTMessage]:
    return await get_all()
