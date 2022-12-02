from fastapi import APIRouter, Request
from ..controllers import runner as RunnerController

# Define Router
router = APIRouter(
    prefix="/runner",
    responses={404: {"description": "Endpoint Not Found"}},
)

# Run Module
# Method: GET
# Path: /runner/run/<module_type>/<module_name>/<module_method>
# Example: /runner/run/py/hello_world/main

@router.get("/run/{module_type}/{module_name}/{module_method}")
async def run_module(module_name: str, module_type: str,  module_method: str, request: Request):
    query_params = request.query_params
    return RunnerController.run_module(module_name, module_type, module_method, query_params)