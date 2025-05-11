import os
import tempfile
import time
import subprocess
import sys
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Ask-MCP", "0.2.1")
temp_file = os.path.join(tempfile.gettempdir(), "ask_message_res_user.txt")

def read_message_from_file(filename):
    while not os.path.exists(filename):
        time.sleep(0.1)
    with open(filename, "r") as f:
        message = f.read()
    os.remove(filename)
    return message

# Add an addition tool
@mcp.tool("Ask", "Ask the user a question and get a response.")
def ask(question: str, predictedAnswer: str | None = None) -> str:
    """Ask a question and get a response from the user."""
    subprocess.Popen([
        "cmd", "/c", "start", "", sys.executable, "C:\\Users\\samue\\Documents\\dev\\python\\AskMCPServer\\ask-terminal.py", temp_file, question, predictedAnswer if predictedAnswer is not None else "No answer provided."
    ])
    print(f"Parent: Waiting for message from child... {temp_file}")
    message = read_message_from_file(temp_file)
    print(f"Parent received: {message}")
    return message + "(from Ask MCP Server)"