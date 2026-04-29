import os
import asyncio
from google.genai import Client

async def main():
    client = Client(vertexai=True, project="truiz-agent-builder", location="global")
    response = await client.aio.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Hi"
    )
    print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
