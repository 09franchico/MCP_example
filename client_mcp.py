import asyncio
import os
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    
    # Create configuration dictionary
    config = {
        "mcpServers": {
            "fastapi-mcp": {
            "url": "http://localhost:8000/mcp"
            }
        }
    }

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatOllama(model="qwen2.5:3b")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Hello word",
    )
    print(f"\nResultado ---------------> : {result}")

if __name__ == "__main__":
    asyncio.run(main())