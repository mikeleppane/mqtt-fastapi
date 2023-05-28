from fastapi import APIRouter

router = APIRouter()


@router.get("/health_check")
async def health_check() -> dict[str, str]:
    return {"message": "OK"}
