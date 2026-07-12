"""
=========================================================
DeTLeng BigQuery MCP Server
=========================================================
 
Purpose:
    Expose Business Intelligence tools to AI through MCP.

Responsibilities:
    - Create MCP Server
    - Register Business Tools
    - Register Health Tool
    - Start MCP Server

This module must NOT contain:

    - SQL Queries
    - Business Logic
    - Prompt Engineering
=========================================================
"""

from fastmcp import FastMCP

from config import (
    APP_NAME,
    HOST,
    MCP_TRANSPORT,
    PORT,
    VERSION,
    PROJECT_ID,
    DATASET_ID,
)
from executor import list_registered_tools as get_registered_tools
from registry import register_mcp_tools

# =========================================================
# MCP Server
# =========================================================

mcp = FastMCP(APP_NAME)

# =========================================================
# Health Check
# =========================================================

@mcp.tool
def server_status():
    """
    Return current server status.
    """

    return {
        "server": "running",
        "application": APP_NAME,
        "version": VERSION,
        "project": PROJECT_ID,
        "dataset": DATASET_ID
    }


@mcp.tool
def list_registered_tools():
    """
    Return registered Business Intelligence tool names.
    """

    return {
        "tools": get_registered_tools()
    }


# =========================================================
# Business Intelligence Tools
# =========================================================

register_mcp_tools(mcp)


# =========================================================
# Run Server
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print(f"Starting {APP_NAME} v{VERSION}")
    print("=" * 60)

    import fastmcp

    print("FastMCP Version :", fastmcp.__version__)
    print("Transport       :", MCP_TRANSPORT)
    print("Host            :", HOST)
    print("Port            :", PORT)

    mcp.run(
        transport=MCP_TRANSPORT,
        host=HOST,
        port=PORT,
        show_banner=True,
    )
