# MCP AI Utility Assistant 🤖

An AI-powered utility assistant built using **Python, Model Context Protocol (MCP), and Groq LLM**. The project demonstrates how an LLM can dynamically discover, select, and execute external Python tools through an MCP client-server architecture.

The assistant supports mathematical operations, text analysis, and AI-powered text summarization through reusable MCP tools.

---

## 🚀 Project Overview

Traditional AI applications often implement tool functionality directly inside their application logic.

This project explores a more modular approach using the **Model Context Protocol (MCP)**.

An MCP server exposes reusable Python tools, while an MCP client connects to the server and makes those tools available to a Groq-powered LLM.

The LLM understands the user's request, selects an appropriate tool, provides the required arguments, and receives the execution result to generate a natural-language response.

## ✨ Features

- **MCP Client-Server Architecture:** Separates AI application logic from external tool functionality.
- **Dynamic Tool Discovery:** Automatically discovers available tools from the MCP server.
- **LLM-Based Tool Selection:** Uses Groq LLM to select appropriate tools based on user requests.
- **Dynamic Schema Conversion:** Converts MCP tool input schemas into Groq-compatible function schemas.
- **Tool Execution:** Executes selected Python functions through the MCP client.
- **Mathematical Operations:** Supports addition and multiplication.
- **Text Analysis:** Calculates word count, character count, and sentence count.
- **AI-Powered Summarization:** Uses Groq LLM to generate concise summaries of text.
- **Input Validation:** Includes basic validation to handle invalid inputs.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| MCP | Standardized communication between AI applications and tools |
| Groq API | LLM integration and text summarization |
| AsyncIO | Asynchronous client operations |
| python-dotenv | Environment variable management |
| JSON | Tool schema conversion and argument handling |

## 🧰 Available MCP Tools

The MCP server currently exposes five tools.

| Tool | Description |
|---|---|
| `add` | Adds two numbers |
| `multiplication` | Multiplies two numbers |
| `count_words` | Counts the number of words in a text |
| `analyze_text` | Returns word count, character count, and sentence count |
| `summarize_text` | Generates a concise summary using Groq LLM |

### Example Tool Usage

**1. Mathematical operation**

Input:
```text
Multiply 25 by 40.
```

Selected MCP tool:
```text
multiplication
```

Arguments:
```json
{
  "a": 25,
  "b": 40
}
```

Result:
```text
1000
```

**2. Text analysis**

Input:
```text
Analyze this text: MCP connects AI applications with external tools.
```

The assistant can select `analyze_text` to calculate basic text statistics.

**3. Text summarization**

Input:
```text
Summarize this text: Artificial Intelligence is transforming many industries...
```

The assistant selects `summarize_text`, which uses Groq to generate a concise summary.

## 🏗️ System Architecture

```text
              USER
                |
                v
         AI APPLICATION
             (ai_app.py)
                |
                v
           GROQ LLM
                |
        Tool Selection
                |
                v
           MCP CLIENT
                |
          MCP Protocol
                |
                v
           MCP SERVER
             (server.py)
                |
        +-------+-------+
        |       |       |
        v       v       v
      Math    Text    Summary
      Tools   Tools    Tool
                        |
                        v
                    GROQ LLM
                        |
                        v
                 Summary Result
                        |
                        v
                 MCP CLIENT
                        |
                        v
                 AI APPLICATION
                        |
                        v
                 FINAL RESPONSE
```

## ⚙️ How It Works

1. The user submits a natural-language request.
2. The MCP client connects to the MCP server.
3. Available tools are discovered dynamically using MCP.
4. MCP tool schemas are converted into Groq-compatible function schemas.
5. The Groq LLM analyzes the request and selects an appropriate tool.
6. The application extracts the tool name and arguments.
7. The MCP client executes the selected tool on the MCP server.
8. The tool result is returned to the LLM.
9. Groq generates the final natural-language response.

For summarization, the `summarize_text` MCP tool independently calls Groq to process the supplied text.
## 🔧 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AtharvaPandey-coder/MCP-AI-Utility-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd MCP-AI-Utility-Assistant
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from the Groq developer console:

https://console.groq.com/

**Important:** Never upload your `.env` file or expose your API key publicly.

## ▶️ Running the Project

### Test the MCP server tools

Run:

```bash
python client.py
```

This connects to the MCP server and allows you to test the available tools.

### Run the AI Utility Assistant

Run:

```bash
python ai_app.py
```

Enter a natural-language request and let the LLM select and execute the appropriate MCP tool.

## 🔐 Security and Validation

The project includes basic input validation for mathematical and text-processing operations.

Examples include:

- Restricting the allowed numerical input range.
- Rejecting empty text inputs.
- Keeping API credentials in environment variables.
- Avoiding hardcoded API keys in source code.

These are basic safeguards for a learning project, not a complete production security implementation.

## 📚 Learning Outcomes

Through this project, I explored:

- MCP fundamentals and client-server communication.
- MCP tool registration and dynamic discovery.
- Calling external tools through an MCP client.
- Converting MCP tool schemas into LLM-compatible function schemas.
- Integrating Groq with MCP.
- LLM-based function calling and argument extraction.
- Returning tool execution results to an LLM.
- Asynchronous Python programming.
- Input validation and basic error handling.

## 🔮 Future Improvements

Planned enhancements:

- [ ] Groq-powered sentiment analysis.
- [ ] Multi-tool execution for complex user requests.
- [ ] Python code explanation and debugging assistant.
- [ ] PDF document analysis and RAG integration.
- [ ] Conversation history and session memory.
- [ ] Continuous conversation with an exit command.
- [ ] Improved error handling and user interface.

## 👨‍💻 Author

**Atharva Pandey**

AI/ML and Generative AI Enthusiast

- GitHub: [AtharvaPandey-coder](https://github.com/AtharvaPandey-coder)

---

⭐ If you find this project interesting, consider giving the repository a star!
