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
        result3=await client.call_tool(
            "summarize_text",
            {
            "text": """
            Artificial Intelligence is transforming many industries.
            Machine learning allows computers to learn patterns from data.
            Natural Language Processing helps computers understand human language.
            Large Language Models can generate text, answer questions,
            summarize documents, and assist users with complex tasks.
            """
            }
        )

        result4=await client.call_tool(
            "sentiment_analysis",
            {
                "text": "I have too much work, my exams are approaching, and I feel overwhelmed."
            }
        )

        print([item.text for item in result4.content if hasattr(item,"text")])

        print([item.text for item in result3.content if hasattr(item, "text")])

        print("words Count")
        print(result2.content)

if __name__ == '__main__':
    asyncio.run(main())








