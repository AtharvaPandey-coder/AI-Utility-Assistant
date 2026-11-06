import asyncio
from mcp import Client,StdioServerParameters

async def main():
    server_params=StdioServerParameters(
        command="python",
        args=['server.py']
    )

    async with Client(server_params) as client:

        tools=await client.list_tools()

        print("Avaliabel tools")
        print("name",[tool.name for tool in tools.tools])

        #Test Addition
        result=await client.call_tool(
            "add",{"a":20,"b":50}
        )

        print("Addition content")
        print(result.content)

        result1=await client.call_tool(
            "multiplication",
            {"a":3,"b":5}
        )
        print(result1.content)

        result2=await client.call_tool(
            "count_words",
            {"text":"MCP Connects Ai application with external tools"}
        )

        print("words Count")
        print(result2.content)

if __name__ == '__main__':
    asyncio.run(main())








