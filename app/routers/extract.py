from fastapi import APIRouter
from ..controllers import extract as ExtractController

# Define Router
router = APIRouter(
    prefix="/extract",
    responses={404: {"description": "Endpoint Not Found"}},
)

@router.get("/wikipedia/{tag}")
async def wikipedia_metadata(tag: str):
    return await ExtractController.wikipedia_metadata(tag)

@router.get("/youtube/{id}")
async def youtube_metadata(id: str):
    return await ExtractController.youtube_metadata(id)

@router.get("/google-play/{package}")
async def googleplay_metadata(package: str):
    return await ExtractController.googleplay_metadata(package)