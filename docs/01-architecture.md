# DeTLeng BigQuery MCP Server Architecture

---

# Overview

The **DeTLeng BigQuery MCP Server** is a Business Intelligence middleware that securely connects Large Language Models (LLMs) with trusted analytics data stored in Google BigQuery.

Rather than exposing raw databases or unrestricted SQL execution, the server provides a curated set of business-oriented tools that return validated analytics and executive insights.

This architecture follows the DeTLeng philosophy:

> **From Raw Data to Business Value.**

---

# Design Goals

The architecture has been designed with the following objectives.

- Secure AI access to analytics data
- Separation of responsibilities
- Business-oriented tool design
- Reusable across multiple client projects
- Cloud-native deployment
- Easy integration with AI assistants
- Enterprise-ready scalability

---

# High-Level Architecture

```
                        Business User
                              │
                              ▼
               DeTLeng Business Intelligence Assistant
                              │
                              ▼
                    OpenAI / Claude / Gemini
                              │
                              ▼
                 DeTLeng BigQuery MCP Server
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
  Business Tools        Security Layer      Query Engine
                              │
                              ▼
                  Google BigQuery Analytics
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
    Fact Tables        Dimension Tables      Business Views
                              │
                              ▼
                    Trusted Business Answers
```

---

# Core Components

The solution is composed of several independent layers.

## 1. AI Client Layer

Responsible for interacting with end users.

Examples

- OpenAI Responses API
- Claude Desktop
- Claude Code
- Gemini
- ChatGPT
- Future AI platforms

Responsibilities

- Receive business questions
- Call MCP tools
- Generate natural language responses

---

## 2. MCP Server Layer

The central orchestration layer.

Responsibilities

- Register business tools
- Validate requests
- Control permissions
- Route queries
- Return structured results

The MCP server never stores business data.

It only acts as an intelligent bridge.

---

## 3. Business Tools Layer

This layer represents the business logic of the organization.

Examples

```
get_total_revenue()

get_customer_count()

get_total_orders()

get_top_products()

get_sales_by_region()

get_delivery_performance()
```

Every tool has one responsibility.

Business tools should hide SQL complexity from AI.

---

## 4. Query Engine

Responsible for

- Building SQL
- Executing SQL
- Handling errors
- Returning structured data

Future versions may include

- Query optimization
- SQL validation
- Query caching

---

## 5. Google BigQuery Analytics Layer

This is the only database layer exposed to AI.

Example

```
cs003_olist_analytics
```

Contains

- Fact Tables
- Dimension Tables
- Business Views

Never expose

```
Raw Dataset

Staging Dataset
```

---

# Analytics Data Flow

```
Raw CSV Files
        │
        ▼
Raw Layer
        │
        ▼
Staging Layer
        │
        ▼
Analytics Layer
        │
        ▼
BigQuery MCP Server
        │
        ▼
AI Assistant
        │
        ▼
Business User
```

---

# Request Flow

Example

User asks

```
What is the total revenue?
```

System flow

```
Business User

↓

OpenAI

↓

MCP Server

↓

Business Tool

↓

BigQuery

↓

Result

↓

AI Response

↓

Business User
```

---

# Security Architecture

Security is a core architectural principle.

## Allowed

Analytics Dataset

Business Views

Fact Tables

Dimension Tables

Business Metrics

---

## Restricted

Raw Tables

Staging Tables

System Tables

Administrative Operations

DELETE

UPDATE

INSERT

DROP

CREATE

ALTER

---

# Repository Architecture

```
detleng-bigquery-mcp/

│
├── server.py
│
├── tools.py
│
├── bigquery_client.py
│
├── config.py
│
├── requirements.txt
│
├── README.md
│
├── prompts/
│      system_prompt.md
│
└── docs/
       architecture.md
```

---

# Design Principles

The architecture follows several software engineering principles.

## Separation of Concerns

Each module has a single responsibility.

---

## Business Before SQL

Expose business concepts.

Not database tables.

---

## Security First

AI should only access trusted analytical data.

---

## Reusable Components

The same server should support multiple clients.

Only configuration changes.

---

## Cloud Native

Designed for Google Cloud Platform.

---

## Extensible

New business tools can be added without modifying the overall architecture.

---

# Future Architecture

Future versions will extend the architecture.

```
Business User
        │
        ▼
Business AI Assistant
        │
        ▼
MCP Server
        │
 ┌──────┼──────────────┐
 ▼      ▼              ▼
BigQuery CRM         ERP
 │       │             │
 ▼       ▼             ▼
Business Intelligence Platform
```

Additional integrations

- Google Drive
- Gmail
- Slack
- Microsoft Teams
- GitHub
- n8n
- REST APIs
- ERP Systems
- CRM Platforms

---

# Future Roadmap

## Phase 1

- BigQuery Connection
- MCP Server
- Business Tools

---

## Phase 2

- OpenAI Integration
- Website Integration
- Business Assistant

---

## Phase 3

- Dynamic Query Generation
- Business Views
- Metadata Layer

---

## Phase 4

- Multi-client Architecture
- SaaS Deployment
- Authentication
- Role-based Security

---

## Phase 5

- AI Agents
- n8n Automation
- Real-time Analytics
- Executive Decision Support

---

# DeTLeng Vision

The DeTLeng BigQuery MCP Server is not intended to be another database connector.

Its purpose is to become a reusable Business Intelligence platform that enables organizations to securely interact with trusted analytical data using natural language.

The architecture is designed to bridge the gap between Data Engineering, Analytics Engineering, Artificial Intelligence, and Business Decision Making.

---

## DeTLeng Principle

```
Business Problem
        │
        ▼
Data Engineering
        │
        ▼
Analytics Engineering
        │
        ▼
Business Intelligence
        │
        ▼
Artificial Intelligence
        │
        ▼
Business Decision
        │
        ▼
Business Value
```



🤝 Next

docs/

01-architecture.md          ✅
02-business-tools.md
03-security.md
04-data-flow.md
05-development-roadmap.md
06-deployment-guide.md
07-api-reference.md
08-contributing.md
09-design-principles.md
10-faq.md


