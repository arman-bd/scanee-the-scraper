from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Routers
from .routers import index as IndexRouter
from .routers import extract as ExtractRouter
from .routers import runner as RunnerRouter

# Create FastAPI Instance
app = FastAPI()

# Mount Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/storage", StaticFiles(directory="/storage"), name="storage")

# Attach Routers
app.include_router(IndexRouter.router)
app.include_router(ExtractRouter.router)
app.include_router(RunnerRouter.router)