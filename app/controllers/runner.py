from ..services import runner as RunnerService

async def run_module(module_name: str, module_type: str, module_method: str, query_params: dict):
    return await RunnerService.run_module(module_name, module_type, module_method, query_params)
