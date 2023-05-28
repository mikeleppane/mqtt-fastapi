from fastapi import APIRouter

from src.database.services.message_service import get_all
from src.models.tortoise import MessageSchema

router = APIRouter()


@router.get("/", response_model=list[MessageSchema])
async def read_all_messages() -> list[MessageSchema]:
    return await get_all()
