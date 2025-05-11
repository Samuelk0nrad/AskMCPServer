import os
import tempfile
import time
import subprocess
import sys
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Ask2.1", "0.2.5")
temp_file = os.path.join(tempfile.gettempdir(), "ask_message_res_user.txt")

def read_message_from_file(filename):
    while not os.path.exists(filename):
        time.sleep(0.1)
    with open(filename, "r") as f:
        message = f.read()
    os.remove(filename)
    return message

# Add an addition tool
@mcp.tool(
    "ASK",
    "Ask a question if you are not sure what the user means"
    "or if you want to confirm something. "
    "add defaultAnswer to the question to show the user what you think the answer is."
    "you can also provide choices as a list to create a multiple choice question."
    "you can provide context to give the user more information about your question."
    )
def ask(question: str, defaultAnswer: str | None = None, choices: list[str] | None = None, context: str | None = None) -> str:
    """Ask a question and get a response from the user."""
    args = [
        sys.executable,  # Python executable
        "C:\\dev\\src\\python\\MCP\\AskMCPServer\\ask-terminal.py",  # Script path
        temp_file,  # Temporary file path
        question,  # Question to ask
        defaultAnswer if defaultAnswer is not None else "No answer provided.",  # Default answer
    ]
    if choices:
        args.append("\";\"".join(choices))  # Join choices with ';'
    
    if context:
        args.append(context)  # Add context if provided

    print(f"Parent: Starting child process with args: {args}")

    subprocess.Popen(["cmd", "/c", "start", "", *args])  # Use *args to unpack the list
    print(f"Parent: Waiting for message from child... {temp_file}")
    message = read_message_from_file(temp_file)
    print(f"Parent received: {message}")
    return message + "(from Ask MCP Server)"