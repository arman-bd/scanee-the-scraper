from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from ..controllers import index as IndexController

# Define Router
router = APIRouter(
    responses={404: {"description": "Endpoint Not Found"}},
)

@router.get("/", response_class=HTMLResponse)
async def index():
    return await IndexController.index()
    


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return await IndexController.dashboard()


@router.get("/ping")
async def ping():
    return await IndexController.ping()