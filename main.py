import os
import tempfile
import time
import subprocess
import sys
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Ask MCP", "1.0.0")
temp_file = os.path.join(tempfile.gettempdir(), "ask_message_res_user.txt")

# Add an addition tool
@mcp.tool()
def ask(question: str) -> str:
    subprocess.Popen([
        "cmd", "/c", "start", "", sys.executable, "C:\\Users\\samue\\Documents\\dev\\python\\AskMCPServer\\ask-terminal.py", temp_file, question
    ])
    time.sleep(10)
    return "Samuel Liu"