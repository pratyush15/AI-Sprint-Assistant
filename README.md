# 🤖 AI Sprint Assistant

A fully local, zero-cost, AI-powered Jira-style sprint management tool. Manage tickets, get AI-generated ticket insights through a genuine **multi-agent LangGraph pipeline**, search historical tickets semantically, and export AI-driven sprint health reports — all running on your own machine with no cloud API costs.

Built with **FastAPI**, **Streamlit**, **LangGraph**, **LangChain**, **ChromaDB**, and **Ollama**.

---

## ✨ Features

- **Ticket Management** — Create, update, and delete Jira-style tickets
- **Multi-Agent AI Assistant** — Per-ticket actions powered by a 4-agent LangGraph pipeline:
  - 📊 Estimate Story Points
  - 🔴 Suggest Priority
  - ✅ Generate Acceptance Criteria
  - 🧪 Generate Test Cases
  - 🗂️ Break Down Subtasks
  - ✍️ Rewrite Ticket
  - 🔍 Analyze Ticket Quality
  - 💬 Chat with Ticket (interactive Q&A)
- **Semantic Search** — Find similar historical tickets using ChromaDB + Ollama embeddings
- **Sprint Dashboard** — Visualize sprint health, readiness, risk, capacity, and workload
- **PDF Reports** — Export AI-generated sprint summaries as downloadable PDFs
- **100% Local** — No OpenAI, no cloud APIs, no per-token costs

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| AI Orchestration | LangGraph (multi-agent state graph) |
| AI Framework | LangChain |
| LLM | Ollama (local — `llama3.2`) |
| Embeddings | Ollama (local — `nomic-embed-text`) |
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
| Tickets                    |               | Multi-Agent AI Pipeline    |
| Sprint Data                |               | (Analyzer → Router →       |
|                            |               |  Clarifier/Executor →      |
|                            |               |  Reviewer)                 |
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

## 🤖 Multi-Agent AI Workflow

Every per-ticket AI action (story points, priority, test cases, subtasks, etc.) is routed through the **same 4-agent LangGraph pipeline** — only the task-specific prompt plugged into the executor changes.

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
FastAPI Endpoint (/ai/run)
          │
          ▼
+--------------------------------+
|  Agent 1: Context Analyzer     |
|  Reads the ticket, writes      |
|  context notes                 |
+----------------+----------------+
                 |
                 v
      Router (conditional edge)
      description too thin?
        /                    \
     yes                      no
      |                        |
      v                        v
+---------------------+   +--------------------------------+
| Agent 2: Clarifier   |   | Agent 3: Task Executor         |
| Asks clarifying      |   | Runs the requested action,     |
| questions instead     |   | enriched with Agent 1's notes |
| of guessing           |   +----------------+----------------+
+-----------+-----------+                    |
            |                                v
            |                     +--------------------------------+
            |                     | Agent 4: Reviewer              |
            |                     | Checks the draft against its   |
            |                     | own format rules, corrects it  |
            |                     +----------------+----------------+
            |                                      |
            +------------------+-------------------+
                                v
                     Displayed in Streamlit
```

**Agent roles:**

1. **Context Analyzer** — reads the raw ticket title/description and produces structured notes about it (what it's about, what's implied). Runs first, on every request.
2. **Router (conditional edge)** — a deterministic check: if the ticket description is too thin to act on (fewer than 4 words), route to the Clarifier instead of guessing. Otherwise, route to the Task Executor.
3. **Clarifier** *(branch)* — generates specific clarifying questions instead of producing a low-quality guess for an under-specified ticket.
4. **Task Executor** — runs the actual requested action (one of 8 prompt templates), using the Context Analyzer's notes as additional grounding.
5. **Reviewer** — a second LLM pass that checks the Executor's draft against that action's own formatting rules (e.g. "exactly one story point, no range," "exactly 5 test cases") and corrects it before it's returned.

This is a genuine multi-agent design: distinct agent roles, a real conditional branch, and state (`context_notes`, `draft_content`) passed between agents — not a single node picking between prompt strings.

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

Create a matching `.env` inside `dashboard/` with at least `API_BASE_URL`.

### 7. Start Ollama

```bash
ollama serve
```

### 8. Start the FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend: `http://localhost:8000` · Swagger docs: `http://localhost:8000/docs`

### 9. Start the Streamlit Frontend

Open a new terminal:

```bash
cd dashboard
streamlit run Home.py
```

App: `http://localhost:8501`

---

## 📂 Project Structure

```
ai-sprint-assistant/
├── app/
│   ├── agents/
│   │   ├── graph.py          # LangGraph multi-agent state graph + conditional routing
│   │   ├── nodes.py          # The 4 agents: analyzer, clarifier, executor, reviewer
│   │   └── prompts.py        # All prompt templates (per-ticket + sprint-level)
│   ├── api/
│   │   ├── routes.py         # Ticket CRUD
│   │   ├── ai_routes.py      # POST /ai/run — per-ticket AI actions
│   │   ├── sprint_routes.py  # Sprint summary/readiness/risk/capacity/workload/PDF
│   │   └── vector_routes.py  # POST /vector/search — semantic search
│   ├── database/             # SQLAlchemy models, session, seed data
│   ├── services/             # Business logic layer (ticket, AI, sprint, vector)
│   ├── vector_db/            # ChromaDB wrapper
│   └── main.py                # FastAPI app entrypoint
├── dashboard/
│   ├── pages/                 # Streamlit multi-page app
│   ├── components/            # Reusable UI components
│   └── api_client.py           # All backend API calls
├── data/                       # SQLite DB + Chroma vector store (generated)
└── requirements.txt
```

---

## 🔌 Key API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/tickets/` | List all tickets |
| `POST` | `/tickets/` | Create a ticket |
| `PUT` | `/tickets/{id}` | Update a ticket |
| `DELETE` | `/tickets/{id}` | Delete a ticket |
| `POST` | `/ai/run` | Run a multi-agent AI action on a ticket |
| `POST` | `/vector/search` | Semantic search for similar tickets |
| `GET` | `/ai/sprint-summary` | AI-generated sprint summary |
| `GET` | `/ai/sprint-readiness` | AI sprint readiness score |
| `GET` | `/ai/sprint-risk` | AI sprint risk analysis |
| `GET` | `/ai/sprint-capacity` | AI sprint capacity analysis |
| `GET` | `/ai/workload` | Per-assignee story point workload |
| `GET` | `/ai/sprint-report` | Download full sprint report as PDF |

---

## 🧪 Verifying the Setup

| Check | URL |
|---|---|
| API docs (Swagger) | `http://localhost:8000/docs` |
| Streamlit frontend | `http://localhost:8501` |

Run through these to validate end-to-end:

- ✅ Ticket CRUD
- ✅ Multi-Agent AI Assistant (all 8 actions)
- ✅ Similar Ticket Search
- ✅ Sprint Dashboard (metrics, charts, filters)
- ✅ Sprint Readiness / Risk / Capacity / Workload
- ✅ PDF Sprint Report export

---

## 📄 License

MIT License — free to use, modify, and distribute.
