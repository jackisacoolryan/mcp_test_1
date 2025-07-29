from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Run with Streamable HTTP transport; recommended over SSE
    mcp.run(transport="http", host="0.0.0.0", port=8000, path="/mcp")
