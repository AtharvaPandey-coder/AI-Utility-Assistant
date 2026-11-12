from mcp.server.mcpserver import MCPServer
import os
from dotenv import load_dotenv
from groq import Groq
from database.inspect_schema import inspect_schema
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
def sentiment_analysis(text: str) -> str:
    """Analyze sentiment, identify possible emotions, and provide personalized wellness suggestions."""

    if not text.strip():
        raise ValueError("Text cannot be empty")

    if len(text) > 10000:
        raise ValueError("Text is too long. Maximum 10000 characters allowed.")

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": """
                You are an AI Sentiment Analysis and Wellness Assistant.

                Analyze the user's text and provide the following:

                1. SENTIMENT:
                   Classify the sentiment as Positive, Negative, or Neutral.

                2. POSSIBLE EMOTION:
                   Identify the possible emotion expressed, such as
                   stress, sadness, happiness, frustration,
                   excitement, worry, or calmness.

                3. EXPLANATION:
                   Briefly explain why you identified this sentiment
                   and possible emotion.

                4. WELLNESS SUGGESTIONS:
                   Provide 4-5 practical wellness tips based on
                   the user's expressed feelings and situation.

                5. ACTION FOR TODAY:
                   Suggest one small action the user can try today.

                IMPORTANT GUIDELINES:
                - Be empathetic, supportive, and non-judgmental.
                - Give practical and realistic suggestions.
                - Do not diagnose mental health conditions.
                - Do not claim to know the user's actual mental state.
                - Do not recommend medication or medical treatment.
                - Do not guarantee that suggestions will solve problems.
                - If the user expresses immediate risk of self-harm,
                  prioritize immediate support from trusted people
                  and local emergency or crisis services.

                Use clear headings and bullet points in your response.
                """
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    result = response.choices[0].message.content

    if not result:
        raise RuntimeError("Wellness analysis returned an empty response.")

    return result.strip()

@mcp.tool()
def get_database_schema():
    """
    Retrieve the schema of the connected SQLite database.
    Returns table names, column names, data types and constraints.
    
    """
    schema=inspect_schema()

    return schema



if __name__ == "__main__":
    mcp.run()


