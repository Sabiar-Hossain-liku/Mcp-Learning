# MCP Server Practice Example

This folder contains a minimal MCP server using the FastMCP Python SDK. It exposes a single tool:

- `get_documentation_from_database`: Returns mocked documentation data from a database.

## How to Run

1. Install FastMCP (and dependencies):

```powershell
pip install fastmcp
```

2. Run the server:

```powershell
python mcp_server.py
```

The server will start in stdio mode and expose the tool to MCP-compatible clients.

## Example Tool Output

```
{
  "title": "Sample Project Documentation",
  "body": "This is a mocked documentation entry from the database. It demonstrates how to expose tools via MCP.",
  "source": "mocked_database"
}
```
