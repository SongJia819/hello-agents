from app.mcp.server_app import mcp
from app.mcp.cluster_tools import *

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8001,
    )