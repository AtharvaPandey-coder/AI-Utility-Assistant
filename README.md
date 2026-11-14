# MCP AI Utility Assistant 🤖

An AI-powered assistant built using **Python, Model Context Protocol (MCP), Groq LLM, and SQLite**.

The project demonstrates how an LLM can dynamically discover, select, and execute external Python tools through an MCP client-server architecture.

It supports mathematical operations, text analysis, AI-powered summarization, sentiment analysis, and database querying tools.

## 🚀 Features

### MCP and AI
- MCP client-server architecture.
- Dynamic discovery of MCP tools.
- LLM-based tool selection using Groq.
- Dynamic conversion of MCP schemas into Groq-compatible function schemas.
- Multiple tool calls in a single interaction.
- Multi-round tool orchestration.
- Addition and multiplication.
- Text analysis: word, character, and sentence counts.
- AI-powered text summarization.
- Sentiment and emotion analysis.
- General wellness suggestions.
- Input validation and error handling.
- Maximum iteration limit to prevent endless tool calls.

### Database Integration
- Import CSV datasets into SQLite using Pandas.
- Automatically create database tables from CSV filenames.
- Dynamically inspect database schemas.
- Retrieve table names and column metadata.
- Expose database schema inspection through an MCP tool.
- Execute read-only SQL queries through an MCP tool.
- Return query results with column names and row counts.
- Limit returned query results to 1,000 rows.

## 🧰 Available MCP Tools

| Tool | Description |
|---|---|
| `add` | Adds two numbers |
| `multiplication` | Multiplies two numbers |
| `count_words` | Counts words in text |
| `analyze_text` | Calculates basic text statistics |
| `summarize_text` | Summarizes text using Groq |
| `sentiment_analysis` | Analyzes sentiment and possible emotions |
| `get_database_schema` | Retrieves database schema information |
| `execute_sql_query` | Executes read-only SQL queries |

## 🔄 How It Works

1. The user submits a natural-language request.
2. The MCP client discovers available tools.
3. MCP tool schemas are converted into Groq-compatible schemas.
4. Groq selects the appropriate tool and generates its arguments.
5. The AI application extracts the tool name and arguments.
6. The MCP client calls the selected server tool.
7. The MCP server executes the corresponding Python function.
8. Results are returned to the AI application.
9. Groq can request additional tools if needed.
10. The LLM generates the final response.

## 🗄️ Database Workflow

1. CSV files are placed inside the `data/` directory.
2. `create_database.py` imports CSV data into SQLite.
3. `inspect_schema.py` discovers tables and column metadata.
4. `get_database_schema` exposes schema information through MCP.
5. `execute_sql_query` executes read-only SQL queries.
6. Query results are returned to the calling application.

The database tools are designed to work with different CSV datasets rather than being limited to one dataset.

## 🏗️ Project Structure

```text
MCP-AI-Utility-Assistant/
│
├── data/
│   ├── orders.csv
│   ├── order_details.csv
│   ├── pizzas.csv
│   └── pizza_types.csv
│
├── database/
│   ├── create_database.py
│   └── inspect_schema.py
│
├── server.py
├── client.py
├── ai_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

The SQLite database is generated locally and is excluded from Git tracking.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| MCP | Communication between AI applications and tools |
| Groq API | LLM integration and text processing |
| AsyncIO | Asynchronous operations |
| Pandas | CSV processing |
| SQLite | Database storage |
| SQL | Database queries |
| JSON | Tool schemas and arguments |
| python-dotenv | Environment variable management |

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/AtharvaPandey-coder/MCP-AI-Utility-Assistant.git
cd MCP-AI-Utility-Assistant
```

**2. Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure your API key**

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from https://console.groq.com/.

Never upload your `.env` file or expose your API key.

## ▶️ Running the Project

**Run the MCP client:**

```bash
python client.py
```

**Run the AI application:**

```bash
python ai_app.py
```

**Create the SQLite database:**

```bash
python database/create_database.py
```

**Inspect the database schema:**

```bash
python database/inspect_schema.py
```

## 🔐 Security

- API credentials are stored in environment variables.
- Input validation is applied to tool operations.
- Tool execution errors are handled.
- Tool-calling iterations are limited.
- SQLite connections use read-only mode for SQL queries.
- SQLite query-only mode provides an additional write restriction.
- Query results are limited to 1,000 returned rows.

These safeguards are intended for a learning project and are not a complete production security implementation.

## 📚 Key Learning Outcomes

- MCP fundamentals and client-server communication.
- Dynamic tool discovery and execution.
- LLM function calling.
- MCP and Groq integration.
- Multi-tool and multi-round orchestration.
- Asynchronous Python programming.
- CSV-to-SQLite integration.
- Dynamic database schema inspection.
- Read-only SQL execution through MCP.

## 🔮 Future Improvements

- [ ] Natural-language to SQL orchestration through the AI application.
- [ ] Support for multiple uploaded CSV datasets.
- [ ] Query result interpretation.
- [ ] Charts and data visualizations.
- [ ] Conversation history and session memory.
- [ ] Streamlit user interface.
- [ ] Application deployment.
- [ ] Improved SQL validation and security.

## 👨‍💻 Author

**Atharva Pandey**

AI/ML and Generative AI Enthusiast

- GitHub: [AtharvaPandey-coder](https://github.com/AtharvaPandey-coder)

---

**Project Status:** Actively under development.

Building an MCP-powered AI Data Analytics Assistant.
