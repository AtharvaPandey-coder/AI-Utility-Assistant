from mcp.server.mcpserver import MCPServer
import os
from dotenv import load_dotenv
from groq import Groq
mcp=MCPServer("Ai Utility Assistant")

load_dotenv()
groq_client=Groq(api_key=os.getenv('GROQ_API_KEY'))
# Addittion
@mcp.tool()
def add(a:int,b:int)->int:
    """Add two numbers"""
    if abs(a) > 10000000 or abs(b) > 10000000:
        raise ValueError("Numbers must be in a allowed range")

    return a + b

#Multiplication
@mcp.tool()
def multiplication(a:int,b:int)->int:
    """Multiplication the two numbers"""

    if abs(a) > 10000000 or abs(b)> 10000000:
        raise ValueError("Numbers must be in the allowed range")

    return a * b 


@mcp.tool()
def count_words(text:str)-> int:
    """Count the number of words in a text"""

    if not text.strip():
        raise ValueError("Text cannot be empty")

    return len(text.strip())

@mcp.tool()
def analyze_text(text:str)->dict:
    """Analyze the text and return basic statistics"""

    if not text.strip():
        raise ValueError("Text cannot be empty")

    words=text.split()

    return {
        "word count":len(words),
        "character_count":len(text),
        "sentence count":sum(text.count(mark) for mark in ".!?"),
    }

@mcp.tool()
def summarize_text(text:str)->str:
    """Summarixe length text into small summary"""

    if not text.strip():
        raise ValueError("Text cannot be empty")

    response=groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role":"system",
                "content":"Summarize the given text clearly.Preserve its important information."
            },
            {
                'role':'user',
                'content':text
            }
        ]
    )
    return response.choices[0].message.content

@mcp.tool()
def sentiment_analysis(text:str)->str:
    """Analyze the text and give a sentiment and possible emotions"""

    if not text.strip():
        raise ValueError("Text cannot be empty .Enter a valid a text")

    if len(text) > 10000:
        raise ValueError("text length is too long.")

    response =groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role":"system",
                "content":"""
                You are a text sentiment and emotion analysis assistant.

                Analyze the user's text and identify:
                1. Sentiment: Positive, Negative, or Neutral.
                2. Possible emotion: Stress, sadness, happiness,
                frustration, excitement, worry, or calmness.
                3. Explanation: Briefly explain which words or
                expressions indicate this sentiment and emotion.

                 Important:
                - Identify possible emotions expressed in the text.
                - Do not diagnose mental health conditions.
                - Do not assume you know the user's actual mental state.
                - If there is insufficient information, say so.

                Return your response in this format:

                Sentiment:
                Possible Emotion:
                Explanation:

"""
            },
            {
                "role":"user",
                "content":text
            }
        ]
    )
    result=response.choices[0].message.content
    if not result:
        raise RuntimeError("Sentiment analysis returned an empty response.")

    return result.strip()


if __name__ == "__main__":
    mcp.run()


