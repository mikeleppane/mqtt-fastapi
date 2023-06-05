from fastapi import APIRouter

router = APIRouter()


@router.get("/v1/health_check")
async def health_check() -> dict[str, str]:
    return {"message": "OK"}
