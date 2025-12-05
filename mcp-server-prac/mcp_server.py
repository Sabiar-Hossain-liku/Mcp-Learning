from mcp.server.fastmcp import FastMCP

# Create the FastMCP server instance
mcp = FastMCP("mcp-doc-server-prac")

@mcp.tool()
def get_documentation_from_database() -> dict:
    """
    Returns mocked documentation data from a database.
    """
    return {
        "title": "Sample Project Documentation",
        "body": "This is a mocked documentation entry from the database. It demonstrates how to expose tools via MCP.",
        "source": "mocked_database"
    }

if __name__ == "__main__":
    mcp.run("stdio")
