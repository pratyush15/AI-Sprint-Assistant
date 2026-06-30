# 🤖 AI Sprint Assistant

A fully local, zero-cost AI-powered Jira-like project management tool. Manage tickets, analyze sprints, and get AI-generated insights — all running on your machine with no external API costs.

Built with FastAPI, Streamlit, LangGraph, LangChain, and Ollama.

---

## ✨ Features

- **Ticket Management** — Create, update, and delete Jira-style tickets
- **AI Assistant** — Per-ticket AI actions powered by a local LLM:
  - 📊 Estimate Story Points
  - 🔴 Suggest Priority
  - ✅ Generate Acceptance Criteria
  - 🧪 Generate Test Cases
  - 🗂️ Break Down Subtasks
  - ✍️ Rewrite Ticket
  - 🔍 Analyze Ticket Quality
  - 💬 Chat with Ticket (interactive Q&A)
- **Semantic Search** — Find similar historical tickets using ChromaDB embeddings
- **Sprint Dashboard** — Visualize sprint health, readiness, risk, capacity, and workload
- **PDF Reports** — Export AI-powered sprint summaries as downloadable PDFs
- **100% Local** — No OpenAI, no cloud APIs, no costs

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| AI Framework | LangChain |
| AI Workflow | LangGraph |
| LLM | Ollama (Local LLM) |
| Embeddings | Ollama Embeddings |
| Vector Database | ChromaDB |
| API Validation | Pydantic |
| Report Generation | ReportLab |
| Language | Python 3.13 |

---

## 🏗️ System Architecture

```text
                          +----------------------+
                          |      Streamlit UI    |
                          |----------------------|
                          | • Ticket Management  |
                          | • AI Assistant       |
                          | • Sprint Dashboard   |
                          | • Similar Search     |
                          +----------+-----------+
                                     |
                                     | REST API
                                     v
                          +----------------------+
                          |      FastAPI         |
                          |----------------------|
                          | Routes               |
                          | Validation           |
                          | Business Logic       |
                          +----------+-----------+
                                     |
             +-----------------------+-----------------------+
             |                                               |
             v                                               v
+----------------------------+               +----------------------------+
|      SQLite Database       |               |       LangGraph            |
|----------------------------|               |----------------------------|
| Tickets                    |               | AI Workflow Engine         |
| Sprint Data                |               | Prompt Routing             |
+----------------------------+               +-------------+--------------+
                                                           |
                                                           v
                                              +----------------------------+
                                              |      LangChain             |
                                              |----------------------------|
                                              | Prompt Templates           |
                                              | LLM Interface              |
                                              +-------------+--------------+
                                                            |
                                                            v
                                              +----------------------------+
                                              |     Ollama (Local LLM)     |
                                              |----------------------------|
                                              | Story Points               |
                                              | Priorities                 |
                                              | Acceptance Criteria        |
                                              | Test Cases                 |
                                              | Ticket Rewrite             |
                                              | Ticket Chat                |
                                              | Sprint Intelligence        |
                                              +-------------+--------------+
                                                            |
                                 +--------------------------+-------------------------+
                                 |                                                    |
                                 v                                                    v
                      +-------------------------+                    +-------------------------+
                      |      ChromaDB           |                    |     PDF Reports         |
                      |-------------------------|                    |-------------------------|
                      | Ticket Embeddings       |                    | Sprint Summary          |
                      | Semantic Search         |                    | AI Insights             |
                      +-------------------------+                    +-------------------------+
```

---

## 🤖 AI Workflow

```text
User selects a ticket
          │
          ▼
Chooses an AI Action
          │
          ▼
Streamlit sends request
          │
          ▼
FastAPI Endpoint
          │
          ▼
LangGraph Workflow
          │
          ▼
Prompt Selection
          │
          ▼
Ollama Local LLM
          │
          ▼
AI Response
          │
          ▼
Displayed in Streamlit
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-sprint-assistant.git
cd ai-sprint-assistant
```

### 2. Create a Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install from [https://ollama.com/download](https://ollama.com/download), then verify:

```bash
ollama --version
```

### 5. Download the Required Models

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 6. Configure Environment Variables

Create a `.env` file in the project root (use `.env.example` as a reference):

```env
APP_NAME=AI Sprint Assistant
DATABASE_URL=sqlite:///./tickets.db
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
OLLAMA_EMBED_MODEL=nomic-embed-text
CHROMA_DB_PATH=data/chroma
API_BASE_URL=http://localhost:8000
```

### 7. Start Ollama

```bash
ollama serve
```

### 8. Start the FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend available at `http://localhost:8000`  
Swagger docs at `http://localhost:8000/docs`

### 9. Start the Streamlit Frontend

Open a new terminal:

```bash
streamlit run Home.py
```

App opens at `http://localhost:8501`

---

## 📂 Application Workflow

1. Create Jira-style tickets
2. Manage ticket lifecycle — Create, Update, Delete
3. Use the AI Assistant to analyze any ticket
4. Generate story points, priority, acceptance criteria, test cases, subtasks, rewrites, and quality analysis
5. Chat with a ticket interactively via the AI Chat mode
6. Search for semantically similar historical tickets using ChromaDB
7. Analyze sprint health, readiness, risk, capacity, and workload
8. Export AI-powered sprint summaries as PDF reports

---

## 🧪 Verifying the Setup

After starting both servers, confirm everything works:

| Check | URL |
|---|---|
| API docs (Swagger) | `http://localhost:8000/docs` |
| Streamlit frontend | `http://localhost:8501` |

Run through these features to validate end-to-end:

- ✅ Ticket CRUD
- ✅ AI Assistant
- ✅ Similar Ticket Search
- ✅ Sprint Dashboard
- ✅ Sprint Readiness
- ✅ Sprint Risk Analysis
- ✅ Sprint Capacity Analysis
- ✅ Workload Analysis
- ✅ PDF Sprint Report

---

## 📄 License

MIT License — free to use, modify, and distribute.
