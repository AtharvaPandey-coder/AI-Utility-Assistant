# MCP AI Utility Assistant 🤖

An AI-powered utility and data analytics assistant built using **Python, Model Context Protocol (MCP), Groq LLM, SQLite, Pandas, and Streamlit**.

The project demonstrates how an LLM can dynamically discover, select, and execute external Python tools through an MCP client-server architecture.

Users can interact with the assistant through a Streamlit interface, perform text and mathematical operations, upload multiple CSV files, and query different datasets using natural language.

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

- Upload multiple CSV files through the Streamlit interface.
- Import CSV datasets into SQLite using Pandas.
- Automatically create database tables from CSV filenames.
- Support for different datasets rather than a fixed dataset.
- Dynamically inspect database schemas.
- Retrieve table names and column metadata.
- Expose database schema inspection through an MCP tool.
- Generate SQL queries based on natural-language questions.
- Execute read-only SQL queries through an MCP tool.
- Return query results with column names and row counts.
- Limit returned query results to 1,000 rows.

### Streamlit Interface

- Interactive chat interface.
- Multiple CSV file uploader.
- Button-based database loading.
- Display user and assistant messages.
- Basic conversation history using Streamlit session state.
- Clear conversation functionality.
- Error handling for database operations.

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

1. The user submits a natural-language request through the Streamlit interface.
2. The AI application connects to the MCP server.
3. The MCP client discovers the available tools.
4. MCP tool schemas are converted into Groq-compatible schemas.
5. Groq selects the appropriate tool and generates its arguments.
6. The AI application extracts the tool name and arguments.
7. The MCP client calls the selected server tool.
8. The MCP server executes the corresponding Python function.
9. Results are returned to the AI application.
10. Groq can request additional tools if needed.
11. The LLM generates the final response.

## 🗄️ Database Workflow

1. The user uploads one or more CSV files through Streamlit.
2. The application passes the uploaded files to the database creation function.
3. Pandas reads the CSV files and imports their contents into SQLite.
4. Database schema inspection discovers available tables and columns.
5. The `get_database_schema` MCP tool exposes the schema information.
6. The LLM uses the discovered schema to determine the appropriate SQL query.
7. The `execute_sql_query` MCP tool executes the read-only query.
8. Query results are returned to the AI application.
9. The LLM interprets the results and generates a natural-language response.

The database workflow has been tested with different datasets, including pizza sales and student enrollment data.

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
├── app.py
├── server.py
├── client.py
├── ai_app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

The `data/` directory contains sample datasets. Users can also upload their own CSV files through the Streamlit interface.

The SQLite database is generated locally and excluded from Git tracking.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| MCP | Communication between AI applications and tools |
| Groq API | LLM integration and function calling |
| AsyncIO | Asynchronous operations |
| Pandas | CSV processing |
| SQLite | Database storage |
| SQL | Database queries |
| Streamlit | Interactive user interface |
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
```

Activate it on Windows:

```bash
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

Get your API key from [Groq Console](https://console.groq.com/).

Never upload your `.env` file or expose your API key.

## ▶️ Running the Project

**Run the Streamlit application:**

```bash
streamlit run app.py
```

**Run the MCP client separately:**

```bash
python client.py
```

**Run the AI application through the terminal:**

```bash
python ai_app.py
```

**Create the SQLite database from local CSV files:**

```bash
python database/create_database.py
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
- Natural-language-to-SQL workflows.
- Read-only SQL execution through MCP.
- Building interactive AI applications using Streamlit.

## 🔮 Future Improvements

- [ ] Advanced context engineering and conversational memory.
- [ ] Automatic replacement of previous dataset tables.
- [ ] Improved CSV validation and error handling.
- [ ] More advanced SQL validation and execution safeguards.
- [ ] Charts and data visualizations.
- [ ] Application deployment.

## 👨‍💻 Author

**Atharva Pandey**

AI/ML and Generative AI Enthusiast

- GitHub: [AtharvaPandey-coder](https://github.com/AtharvaPandey-coder)

---

**Project Status:** Core functionality implemented and tested with multiple datasets. Further improvements are planned.

Building an MCP-powered AI Utility and Data Analytics Assistant.
