# Test MCP Server Using Streamable HTTP

This sample project demonstrates a minimal FastMCP server using the **Streamable HTTP** transport, which has become the recommended default for remote MCP servers. It exposes a single `greet` tool that returns a friendly greeting.

## Files

- `server.py`: Defines and runs the FastMCP server. At runtime, it calls `mcp.run(transport="http")` to launch the server on `0.0.0.0:8000/mcp`. Adjust host, port or path as needed.
- `requirements.txt`: Contains `fastmcp` as the only dependency.

## Running Locally

Ensure you have Python 3.10+ installed and a virtual environment set up. Then install dependencies and run the server:

```
pip install -r requirements.txt
python server.py
```

The server will start at `http://localhost:8000/mcp`. You can inspect it using an MCP client or inspector tool.

## Deploying to Render

1. **Create a new repository** in GitHub and add these files. Link it to a new Web Service on Render.
2. **Environment variables:** None are strictly required for this simple example, but you can add `READ_ONLY=true` or `MCP_PORT` as needed.
3. **Build and start commands** (Streamable HTTP):
   - Build command: `pip install -r requirements.txt`
   - Start command: `python server.py`
4. Once deployed, your MCP server endpoint will be `https://<render-app-url>/mcp`. Use this URL when registering the server as a connector in ChatGPT when that feature becomes available.

## Why Streamable HTTP?

The Model Context Protocol has been transitioning away from **Server-Sent Events (SSE)** due to limitations in scalability, reliability and bidirectional communication. The **Streamable HTTP** transport uses a single endpoint for both sending and receiving messages, dynamically upgrading to streaming when needed, which simplifies connection management and enhances robustness.
