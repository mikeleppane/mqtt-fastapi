from fastapi import APIRouter, HTTPException

from src.database.services.message_service import get_all
from src.models.message import MQTTMessage

router = APIRouter()


@router.get("/v1/messages", response_model=list[MQTTMessage])
async def read_all_messages(limit: int | None = None) -> list[MQTTMessage]:
    if limit and limit < 0:
        raise HTTPException(status_code=400, detail="Limit parameter should be non-negative number")
    try:
        return await get_all(limit=limit)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error") from None
