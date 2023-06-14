from fastapi import APIRouter, HTTPException, Query

from src.database.services.message_service import get_all
from src.models.message import MQTTMessage

router = APIRouter()


@router.get("/v1/messages", response_model=list[MQTTMessage])
async def read_all_messages(
    limit: int = Query(100, ge=0), offset: int = Query(0, ge=0)
) -> list[MQTTMessage]:
    try:
        return await get_all(limit=limit, offset=offset)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error") from None
