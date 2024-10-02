"""
   This module provides functionality to execute batch scripts and system commands.
"""

import subprocess
import platform

def run_script(script: str) -> str: 
    """
    Run a script in the system's default shell.

    Args:
        script: The script to run

    Returns:
        str: The output of the script
    """
    try:
        if platform.system() == "Windows":
            shell = "cmd.exe"
            shell_arg = "/c"
        else:
            shell = "/bin/sh"
            shell_arg = "-c"
        
        result = subprocess.run([shell, shell_arg, script], check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as err:
        return f"Error occurred: {str(err)}"

# class RunBatchScriptArgsSchema(BaseModel):
#     script: str

# run_batch_script_tool = Tool.from_function(
#     name="run_batch_script",
#     description="Run a batch script in the integrated terminal.",
#     func=run_batch_script,
#     args_schema=RunBatchScriptArgsSchema
# )

# format = {
#     "type": "function",
#     "function": {
#         "name": "run_batch_script",
#         "description": "Run a batch script in the integrated terminal.",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "script": {
#                             "type": "string",
#                             "description": "The batch script to run"
#             }
#         }
#     },
#         "required": ["script"]
#     }
# }
