import time
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Define Static and Templates
templates = Jinja2Templates(directory="app/templates")

async def index():
    """Index Page: Home Page

    Args:
        None

    Returns:
        index.html (HTMLResponse): Home Page
    """
    return templates.TemplateResponse("index.html", {"request": {"time": time.time()}})



async def dashboard():
    """Dashboard Page: Displays the dashboard

    Args:
        None

    Returns:
        dashboard.html (HTMLResponse): The dashboard page
    """
    return templates.TemplateResponse("dashboard.html", {"request": {"time": time.time()}})



async def ping():
    """Ping: Check if the server is running

    Args:
        None

    Returns:
        JSON: str
    """
    return {"status": "OK", "message": "Pong", "time": time.time()}