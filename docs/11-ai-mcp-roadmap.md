# DeTLeng BI Tutor + BigQuery MCP Integration Roadmap (Phase 1)

## Current Architecture ✅

```
chat-widget.js
        │
        ▼
aapkaustaad-ai-backend
        │
        ▼
OpenAI
        │
        ▼
Answer
```

---

# Target Architecture

```
chat-widget.js
        │
        ▼
aapkaustaad-ai-backend
        │
        ├────────► OpenAI
        │
        │
        └────────► detleng-bigquery-mcp
                        │
                        ▼
                  Google BigQuery
                        │
                        ▼
                 Business Results
                        │
                        ▼
                     OpenAI
                        │
                        ▼
                  Final Response
                        │
                        ▼
                     Widget
```

---

# Phase 1 — Deploy MCP Server

### Step 1

✅ GitHub Repository Ready

```
detleng-bigquery-mcp
```

Status

```
Completed
```

---

### Step 2

Deploy New Render Service

Repository

```
detleng-bigquery-mcp
```

Build

```
pip install -r requirements.txt
```

Start

```
python server.py
```

Status

```
In Progress
```

---

### Step 3

Configure Environment Variables

Render

↓

Environment

Add required variables

Example

```
PROJECT_ID

DATASET_ID

OPENAI_API_KEY (if required)

etc.
```

Status

```
Pending
```

---

### Step 4

Connect Google Cloud

Purpose

```
Allow Render service
↓

to access BigQuery
```

Need

```
Service Account

OR

Application Default Credentials
```

Status

```
Pending
```

---

### Step 5

Test MCP Server

Example

```
customer_count()

total_orders()

total_revenue()

top_products()
```

Expected

```
JSON response
```

Status

```
Pending
```

---

# Phase 2 — Connect AI Backend

Current

```
Widget

↓

aapkaustaad-ai-backend

↓

OpenAI
```

Update

```
Widget

↓

aapkaustaad-ai-backend

↓

OpenAI

↓

Call MCP when needed
```

Status

```
Pending
```

---

# Phase 3 — Intelligent Tool Calling

User asks

```
How many customers?
```

↓

Backend

↓

OpenAI decides

↓

Use MCP Tool

↓

customer_count()

↓

BigQuery

↓

Result

↓

OpenAI explains

↓

Widget

---

User asks

```
Explain ETL
```

↓

No MCP call

↓

Normal AI response

---

# Final Goal

One chatbot

↓

Understands the question

↓

If business knowledge

→ Answer directly

If business data required

→ Query BigQuery through MCP

↓

Return one intelligent response

---

# Current Progress

| Task                        | Status         |
| --------------------------- | -------------- |
| Chat Widget                 | ✅ Complete     |
| AI Backend                  | ✅ Running      |
| BigQuery MCP Repository     | ✅ Ready        |
| Render Deployment           | 🟡 In Progress |
| Google Cloud Authentication | ⏳ Pending      |
| Backend → MCP Integration   | ⏳ Pending      |
| End-to-End Testing          | ⏳ Pending      |

---

