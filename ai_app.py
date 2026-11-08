import asyncio
import os 
import json

from dotenv import load_dotenv
from groq import AsyncGroq
from mcp import Client,StdioServerParameters

load_dotenv()
model='openai/gpt-oss-20b'
client_ai=AsyncGroq(api_key=os.getenv('GROQ_API_KEY'))

async def main():
    server=StdioServerParameters(
        command="python",
        args=['server.py']
    )

    async with Client(server) as mcp_client:

        tools_response=await mcp_client.list_tools()

        mcp_tools=tools_response.tools


        groq_tools=[]
        for tool in mcp_tools:
            groq_tools.append({
                'type':'function',
                'function':{
                    'name':tool.name,
                    'description':tool.description,
                    'parameters':tool.input_schema
                }
            })
        for tool in mcp_tools:
            if tool.name == 'multiplication':
                print("schema")
                print(tool.input_schema)


        user_input = input("Ask your AI Utility Assistant: ")

        messages =[
            {
                "role":"system",
                "content":(
                    "You are an intelligent AI Utility Assistant. "
                    "Understand the user's request carefully. "
                    "Use available MCP tools whenever needed. "
                    "You can call multiple tools in one turn or across "
                    "multiple turns. "
                    "Use the results of previous tools to decide whether "
                    "additional tools are required. "
                    "Combine tool results into one clear response. "
                    "Never invent tool execution results. "
                    "If a tool fails, explain the error clearly. "
                    "If no tool is required, answer directly."
                )
            },
            {
                "role":"user",
                "content":user_input
            }
        ]
        max_iterations=5

        for iteration in range(max_iterations):
            response=await client_ai.chat.completions.create(
            model=model,
            messages=messages,
            tools=groq_tools,
            tool_choice="auto"
        )
            assistant_message=response.choices[0].message
        #check wheter grok wants to call the tool
            if not assistant_message.tool_calls:
                print("Ask your AI Utility Assistant : ")
                print(assistant_message.content)
                break

        #save assistant tool calls message
            messages.append(
            assistant_message.model_dump(exclude_none=True)
        )   

        #Execute all requested tools
            for tool_call in assistant_message.tool_calls:
                
                
                tool_name=tool_call.function.name
                arguments=json.loads(tool_call.function.arguments)

                print(f"executing tool : {tool_name}")
                try:
                    result=await mcp_client.call_tool(
                    tool_name,arguments
                )
                    #extract the output
                    content="\n".join(item.text for item in result.content if hasattr(item,"text"))

                    if not content:
                        content ="Tool returned no text output"
                        
                    messages.append({
                    'role':'tool',
                    'tool_call_id':tool_call.id,
                    'content':content
                    })
                except Exception as e:
                    error_message=f"Tool execution failed : {str(e)}"

                    messages.append({
                        'role':'tool',
                        'tool_call_id':tool_call.id,
                        'content':error_message
                    })
        else:
            print("\n Maximum Tool execution reached")
        

if __name__=="__main__":
    asyncio.run(main())





