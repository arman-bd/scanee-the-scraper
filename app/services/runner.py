import os

async def run_module(module_name, module_type: str = "py", module_method : str = "main", query_params: dict = None):

    # Module Path
    module_path = os.path.join(os.path.dirname(
        __file__), "..", "modules", module_type, module_name + "." + module_type)
    
    # Check If Module File Exists
    if not os.path.isfile(module_path):
        print("> Module Not Found: " + module_path)
        return False

    # If No Type is Specified, Try to Guess
    if module_type == None:
        py_file = os.path.join(os.path.dirname(
            __file__), "..", "modules", "py", module_name + "." + "py")
        js_file = os.path.join(os.path.dirname(
            __file__), "..", "modules", "js", module_name + "." + "js")

        # Check If Python Module File Exists
        if os.path.isfile(py_file):
            module_type = "py"

        if os.path.isfile(js_file):
            module_type = "js"

        # Check Which Module is Newer

        if os.path.isfile(py_file) and os.path.isfile(js_file):
            py_time = os.path.getmtime(py_file)
            js_time = os.path.getmtime(js_file)

            if py_time > js_time:
                module_type = "py"
            else:
                module_type = "js"
        elif os.path.isfile(py_file):
            module_type = "py"
        elif os.path.isfile(js_file):
            module_type = "js"
        else:
            module_type = None

    if module_type == None:
        print("> Module Not Found: " + module_path)
        return False

    if module_type == "py":
        return await run_python_module(module_name, module_method, query_params)

    if module_type == "js":
        return await run_js_module(module_name, module_method, query_params)

    return False


async def run_python_module(name: str, module_method: str = "main", query_params: dict = None):
    """ Run a Python Module

    Args:
        name (str): Module Name
        module_method (str, optional): Module Method. Defaults to "main".
        params (dict, optional): Module Parameters. Defaults to None.

    Returns:
        str: Output of the Module
    """
    
    # Prepare Module Path
    module_path = os.path.join(os.path.dirname(
        __file__), "..", "modules", "py", name + "." + "py")
    
    # Chek If Module File Exists
    if not os.path.isfile(module_path):
        print("> Module Not Found: " + module_path)
        return False
    
    # Run Module and Get Output
    output = os.popen('python3 ' + module_path + ' ' +
                      module_method + ' ' + str(query_params)).read()
    
    # Return Output
    return output


async def run_js_module(name: str, module_method: str = "main", query_params: dict = None):
    """ Run a JavaScript Module

    Args:
        name (str): Module Name
        module_method (str, optional): Module Method. Defaults to "main".
        params (dict, optional): Module Parameters. Defaults to None.

    Returns:
        str: Output of the Module
    """
    
    # Prepare Module Path
    module_path = os.path.join(os.path.dirname(
        __file__), "..", "modules", "js", name + "." + "js")

    # Chek If Module File Exists
    if not os.path.isfile(module_path):
        print("> Module Not Found: " + module_path)
        return False
    
    # Run Module and Get Output
    output = os.popen('node ' + module_path + ' ' +
                      module_method + ' ' + str(query_params)).read()
    
    # Return Output
    return output
