# MCP AI Utility Assistant 🤖

An AI-powered utility assistant built using **Python, Model Context Protocol (MCP), and Groq LLM**. This project demonstrates how an LLM can dynamically discover, select, and execute external Python tools through an MCP client-server architecture.

The assistant supports mathematical operations, text analysis, AI-powered summarization, sentiment analysis, and wellness suggestions. It also implements **multi-round tool orchestration**, allowing the LLM to execute multiple tools across multiple interaction rounds to handle complex user requests.

The project is also being extended with **SQLite database integration**, allowing CSV datasets to be imported into a database and their schemas to be discovered automatically.

---

## 🚀 Project Overview

Traditional AI applications often implement tool functionality directly inside their application logic.

This project explores a more modular approach using the **Model Context Protocol (MCP)**.

An MCP server exposes reusable Python tools, while an MCP client connects to the server and makes those tools available to a Groq-powered LLM.

The LLM understands the user's request, selects appropriate tools, provides the required arguments, receives execution results, and generates a natural-language response.

Unlike a basic single-round tool-calling implementation, this assistant supports **multi-round tool orchestration**, allowing the LLM to request additional tools based on the results of previous executions.

Additionally, the project includes a database integration component that imports CSV datasets into SQLite and automatically inspects their database structure.

## ✨ Features

### MCP and AI Features

- **MCP Client-Server Architecture:** Separates AI application logic from external tool functionality.
- **Dynamic Tool Discovery:** Automatically discovers available tools from the MCP server.
- **LLM-Based Tool Selection:** Uses Groq LLM to select appropriate tools based on user requests.
- **Dynamic Schema Conversion:** Converts MCP tool input schemas into Groq-compatible function schemas.
- **Multi-Tool Execution:** Supports multiple MCP tool calls within a single LLM response.
- **Multi-Round Tool Orchestration:** Allows the LLM to request additional tools across multiple interaction rounds.
- **Mathematical Operations:** Supports addition and multiplication.
- **Text Analysis:** Calculates word count, character count, and sentence count.
- **AI-Powered Summarization:** Uses Groq LLM to generate concise summaries.
- **Sentiment Analysis:** Identifies positive, negative, or neutral sentiment.
- **Emotion Identification:** Identifies possible emotions expressed in user-provided text.
- **Wellness Support:** Provides practical, non-clinical wellness suggestions based on the analyzed text.
- **Input Validation:** Includes validation for mathematical and text-processing operations.
- **Error Handling:** Handles tool execution exceptions and passes error information back to the LLM.
- **Execution Limit:** Uses a maximum iteration limit to prevent endless tool-calling loops.

### Database Integration Features

- **CSV Import:** Imports CSV datasets into SQLite using Pandas.
- **Automatic Table Creation:** Creates database tables using CSV filenames.
- **Database Schema Inspection:** Discovers available tables and their columns.
- **Column Metadata Extraction:** Retrieves column names, data types, NOT NULL constraints, default values, and primary-key metadata.
- **Structured Schema Representation:** Stores discovered database information in Python dictionaries.

---

## 🧰 Available MCP Tools

The MCP server currently exposes six tools.

| Tool | Description |
|---|---|
| `add` | Adds two numbers |
| `multiplication` | Multiplies two numbers |
| `count_words` | Counts the number of words in a text |
| `analyze_text` | Returns word count, character count, and sentence count |
| `summarize_text` | Generates a concise summary using Groq LLM |
| `sentiment_analysis` | Identifies sentiment and possible emotions and provides wellness suggestions |

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

**4. Sentiment analysis and wellness support**

Input:

```text
I have too much work, my exams are approaching, and I feel overwhelmed.
```

The assistant selects `sentiment_analysis` to:

- Classify the sentiment.
- Identify possible emotions.
- Explain the classification.
- Provide practical wellness suggestions.
- Recommend one small action to try today.

**Note:** This feature provides general wellness suggestions. It does not diagnose mental health conditions or replace professional support.

---

## 🔄 Multi-Round Tool Orchestration

One of the key features of this project is multi-round tool orchestration using Groq and MCP.

Instead of stopping after one round of tool execution, the application allows the LLM to receive tool results, evaluate them, and request additional tools when necessary.

### Key Capabilities

- Supports multiple MCP tool calls within a single user request.
- Executes tools dynamically based on the LLM's decisions.
- Sends tool execution results back to the LLM.
- Allows additional tool calls across multiple interaction rounds.
- Uses previous tool results to support subsequent decisions.
- Combines multiple tool outputs into one final response.
- Includes a maximum iteration limit to prevent endless tool execution.
- Handles tool execution exceptions and returns error information to the LLM.

### Workflow

```text
User Input
    |
    v
Groq LLM
    |
    v
Tool Selection
    |
    v
MCP Client
    |
    v
MCP Server
    |
    v
Tool Execution
    |
    v
Tool Results
    |
    v
Groq LLM
    |
    +----> Additional Tool Calls (if needed)
    |               |
    |               v
    |          MCP Server
    |               |
    |               v
    |          Tool Results
    |               |
    +---------------+
    |
    v
Final Response
```

This enables the assistant to handle complex requests that require multiple tools and multiple execution rounds.

### Example Multi-Tool Request

```text
Analyze this text, identify its sentiment and emotions,
and summarize it:

I am struggling with assignments and deadlines.
I feel stressed and sometimes doubt my abilities,
but I am trying to stay motivated.
```

Depending on the LLM's tool-selection decisions, it can use tools such as:

- `analyze_text`
- `sentiment_analysis`
- `summarize_text`

The results are returned to Groq, which generates a combined response.

---

## 🗄️ Database Integration

The project includes a SQLite database integration component that converts CSV datasets into structured database tables.

The purpose is to make the application capable of understanding different datasets through automatic database schema inspection.

### 1. CSV to SQLite Conversion

CSV files are imported using Pandas and stored as tables inside an SQLite database.

The database creation script automatically:

- Reads CSV files from the `data/` directory.
- Uses CSV filenames as table names.
- Creates corresponding SQLite tables.
- Imports the CSV records into the database.

### 2. Automatic Schema Inspection

The project includes a schema inspection script that discovers the structure of the generated SQLite database.

It retrieves:

- Database table names.
- Column names.
- Column data types.
- NOT NULL constraints.
- Default values.
- Primary-key metadata.

The discovered information is stored in a structured Python dictionary, making it reusable by other application components.

### Database Directory Structure

```text
database/
│
├── create_database.py
├── inspect_schema.py
└── pizza_sales.db
```

### Create the SQLite Database

Run the following command from the project root:

```bash
python database/create_database.py
```

### Inspect the Database Schema

Run:

```bash
python database/inspect_schema.py
```

The script discovers the available tables and displays their column information.

**Note:** The SQLite database is generated locally and is excluded from Git tracking. CSV datasets should only be redistributed when their licenses permit it.

### Current Development Status

The CSV-to-SQLite import and schema inspection components have been implemented and tested.

MCP integration for database schema discovery and dynamic SQL execution is planned as the next development stage.

---

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
           +--------+--------+
           |        |        |
           v        v        v
         Math     Text    AI-Powered
         Tools    Tools     Tools
           |        |        |
           +--------+--------+
                   |
                   v
               Tool Results
                   |
                   v
                 GROQ LLM
                   |
           Additional Tool Calls
               (if needed)
                   |
                   v
               Final Response
                   |
                   v
              USER OUTPUT
```

### Database Processing Architecture

```text
             CSV DATASETS
                   |
                   v
             Pandas Import
                   |
                   v
              SQLite DB
                   |
                   v
          Schema Inspection
                   |
                   v
          Structured Schema
                   |
                   v
        Planned MCP Integration
                   |
                   v
       Dynamic SQL Analytics
```

---

## ⚙️ How It Works

### MCP Workflow

1. The user submits a natural-language request.
2. The MCP client connects to the MCP server.
3. Available tools are discovered dynamically using MCP.
4. MCP tool schemas are converted into Groq-compatible function schemas.
5. The Groq LLM analyzes the request and selects appropriate tools.
6. The application extracts the tool names and arguments.
7. The MCP client executes the selected tools on the MCP server.
8. Tool execution results are returned to the LLM.
9. The LLM can request additional tools based on previous results.
10. The process continues until the LLM generates a final response or the maximum iteration limit is reached.

For summarization and sentiment analysis, the corresponding MCP tools independently use Groq to process the supplied text.

### Database Workflow

1. CSV datasets are placed inside the `data/` directory.
2. The database creation script reads the CSV files.
3. Pandas imports their contents into SQLite tables.
4. The schema inspection script discovers the available tables and column metadata.
5. The discovered schema is stored in a reusable Python dictionary.
6. Database schema discovery will subsequently be exposed through MCP tools.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Model Context Protocol (MCP) | Standardized communication between AI applications and tools |
| Groq API | LLM integration and AI-powered text processing |
| AsyncIO | Asynchronous client operations |
| JSON | Tool schema conversion and argument handling |
| python-dotenv | Environment variable management |
| Pandas | CSV processing and database import |
| SQLite | Lightweight relational database |
| SQL | Database querying and analysis |

---

## 🔧 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AtharvaPandey-coder/MCP-AI-Utility-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd MCP-AI-Utility-Assistant
```

### 3. Create a virtual environment

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

Make sure your `requirements.txt` includes:

```text
mcp
groq
python-dotenv
pandas
```

### 5. Configure environment variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from the Groq developer console:

https://console.groq.com/

**Important:** Never upload your `.env` file or expose your API key publicly.

---

## ▶️ Running the Project

### Test MCP server tools

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

Enter a natural-language request and let the LLM select and execute the appropriate MCP tools.

### Create the SQLite Database

Place your CSV datasets inside the `data/` directory and run:

```bash
python database/create_database.py
```

### Inspect Database Schema

Run:

```bash
python database/inspect_schema.py
```

This displays the discovered database tables and their column metadata.

---

## 🔐 Security and Validation

The project includes basic input validation and error handling for tool operations.

Examples include:

- Restricting allowed numerical input ranges.
- Rejecting empty text inputs.
- Limiting the maximum input length for text-processing operations.
- Keeping API credentials in environment variables.
- Handling tool execution exceptions.
- Limiting the maximum number of tool-calling rounds.

Database query validation and read-only SQL execution are planned for a future development stage.

These safeguards are intended for a learning and development project and do not represent a complete production security implementation.

---

## 📚 Learning Outcomes

Through this project, I explored:

- MCP fundamentals and client-server communication.
- MCP tool registration and dynamic discovery.
- Calling external tools through an MCP client.
- Converting MCP tool schemas into LLM-compatible function schemas.
- Integrating Groq with MCP.
- LLM-based function calling and argument extraction.
- Multi-tool execution and multi-round orchestration.
- Returning tool execution results to an LLM.
- Asynchronous Python programming.
- Input validation and basic error handling.
- Building AI-powered text analysis and summarization tools.
- Importing CSV datasets into SQLite.
- Inspecting database schemas programmatically.
- Working with SQL database metadata.
- Organizing database information using Python dictionaries.

---

## 🔮 Future Improvements

- [ ] Expose database schema inspection through MCP tools.
- [ ] Implement safe, read-only SQL query execution.
- [ ] Generate SQL dynamically using natural-language questions.
- [ ] Support multiple uploaded CSV datasets.
- [ ] Discover and validate relationships between database tables.
- [ ] Add database query result interpretation.
- [ ] Generate charts and visualizations from query results.
- [ ] Conversation history and session memory.
- [ ] Context-aware follow-up questions.
- [ ] Advanced business analytics.
- [ ] Improved security, validation, and logging.
- [ ] AI response evaluation and testing.
- [ ] Streamlit chat interface.
- [ ] Application deployment.
- [ ] MySQL integration.

---

## 👨‍💻 Author

**Atharva Pandey**

AI/ML and Generative AI Enthusiast

- GitHub: [AtharvaPandey-coder](https://github.com/AtharvaPandey-coder)

---

**Project Status:** Actively under development.

More capabilities will be added as the project evolves into a more comprehensive MCP-powered AI Data Analytics Assistant.
