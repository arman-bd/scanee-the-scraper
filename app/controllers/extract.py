from ..includes import webdriver as wd
from ..services import extract as ExtractService

async def wikipedia_metadata(tag: str):
    try:
        driver = wd.create_driver()
        return await ExtractService.wikipedia_metadata(driver, tag, 3)
    except Exception as e:
        return {"error": str(e)}

async def youtube_metadata(id: str):
    try:
        driver = wd.create_driver()
        return await ExtractService.youtube_metadata(driver, id, 3)
    except Exception as e:
        return {"error": str(e)}


async def googleplay_metadata(package: str):
    try:
        driver = wd.create_driver()
        return await ExtractService.googleplay_metadata(driver, package, 5)
    except Exception as e:
        return {"error": str(e)}

    