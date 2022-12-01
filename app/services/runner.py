import os
import sys


async def run_module(name, module_type="py", module_method="main", params=None, timeout=10, max_tries=1, delay=0, do_async=False, job_id=None, log=None, log_level=None, **kwargs):

    # Check If Module File Exists
    # Path: app/modules/<type>/<name>.<type>
    module_path = os.path.join(os.path.dirname(
        __file__), "..", "modules", module_type, name + "." + module_type)
    if not os.path.isfile(module_path):
        print("> Module Not Found: " + module_path)
        return False

    if type == None:
        py_file = os.path.join(os.path.dirname(
            __file__), "..", "modules", "py", name + "." + "py")
        js_file = os.path.join(os.path.dirname(
            __file__), "..", "modules", "js", name + "." + "js")

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
        return await run_python_module(name, module_method, params, timeout, max_tries, delay, do_async, job_id, log, log_level, **kwargs)
    
    if module_type == "js":
        return await run_js_module(name, module_method, params, timeout, max_tries, delay, do_async, job_id, log, log_level, **kwargs)
    
    return False

async def run_python_module(name, module_method="main", params=None, timeout=10, max_tries=1, delay=0, do_async=False, job_id=None, log=None, log_level=None, **kwargs):

    # Check If Module File Exists
    # Path: app/modules/py/<name>.py
    module_path = os.path.join(os.path.dirname(
        __file__), "..", "modules", "py", name + "." + "py")
    if not os.path.isfile(module_path):
        print("> Module Not Found: " + module_path)
        return False
    
    # Run Python Script and Return Result
    output = os.popen('python3 ' + module_path + ' ' + module_method + ' ' + str(params)).read()
    return output

async def run_js_module(name, module_method="main", params=None, timeout=10, max_tries=1, delay=0, do_async=False, job_id=None, log=None, log_level=None, **kwargs):
    
    # Check If Module File Exists
    # Path: app/modules/js/<name>.js
    module_path = os.path.join(os.path.dirname(
        __file__), "..", "modules", "js", name + "." + "js")
    
    
    if not os.path.isfile(module_path):
        print("> Module Not Found: " + module_path)
        return False

    # Run Python Script and Return Result
    output = os.popen('node ' + module_path + ' ' + module_method + ' ' + str(params)).read()
    return output