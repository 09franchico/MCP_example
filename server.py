from fastapi import FastAPI
from fastapi_mcp import FastApiMCP


# Create (or import) a FastAPI app
app = FastAPI()

# Create an MCP server based on this app
mcp = FastApiMCP(app)

# Mount the MCP server directly to your app
mcp.mount()


# Add new endpoints after MCP server creation
@app.get("/hello", operation_id="hello word")
async def new_endpoint():
    return {"message": "Hello, world!"}

# Refresh the MCP server to include the new endpoint
mcp.setup_server()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)