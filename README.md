# What is MCP?

**MCP** stands for **Model Context Protocol**.

It is an open standard that allows Artificial Intelligence models to communicate with external systems, applications, databases, APIs, and business tools in a structured and secure way.

Without MCP, an AI model can only respond based on its training data and the information provided in the conversation.

With MCP, AI can retrieve live information, execute approved business tools, and interact with trusted data sources in real time.

Think of MCP as the bridge between AI and the real business world.

---

# Why is MCP Needed?

Modern businesses generate data every day.

Sales.

Customers.

Orders.

Products.

Payments.

Inventory.

Dashboards help visualize this information, but they still require users to know where to click, how to filter data, and how to interpret reports.

Business users often have much simpler questions:

- What was today's revenue?
- Which products are selling the most?
- How many customers placed orders this week?
- Which region generated the highest sales?

Instead of searching through dashboards or writing SQL queries, users simply ask the question.

MCP enables AI to retrieve trusted answers directly from business systems.

---

# Common Uses of MCP

MCP can connect AI with almost any business platform.

Examples include:

- Google BigQuery
- PostgreSQL
- SQL Server
- Snowflake
- REST APIs
- Google Drive
- GitHub
- Gmail
- Slack
- Microsoft Teams
- CRM Systems
- ERP Systems
- Internal Business Applications

In other words, MCP allows AI to work with real business systems instead of relying only on general knowledge.

---

# Why Did We Build the DeTLeng BigQuery MCP Server?

Many MCP servers are designed as general-purpose connectors.

The DeTLeng approach is different.

We are not building another generic database connector.

We are building a **Business Intelligence Layer** on top of Google BigQuery.

Instead of allowing AI to directly explore databases, the DeTLeng BigQuery MCP Server exposes trusted Business Intelligence tools.

Examples include:

- Total Revenue
- Customer Insights
- Product Performance
- Delivery Analysis
- Sales KPIs
- Business Metrics

This ensures that AI interacts with business-ready analytical data rather than raw operational data.

---

# Why This Project Matters

Artificial Intelligence is becoming the natural interface for business users.

However, AI is only as reliable as the data it receives.

The DeTLeng BigQuery MCP Server combines:

- Data Engineering
- Google BigQuery
- Business Intelligence
- OpenAI
- MCP

to create an intelligent platform where businesses can interact with trusted analytics using natural language.

Instead of asking:

```sql
SELECT SUM(payment_value)
FROM fact_sales;
```

A business user simply asks:

> **"What is our total revenue?"**

The platform handles everything else.

That is the purpose of the DeTLeng BigQuery MCP Server.



# DeTLeng BigQuery MCP Server

> Transform trusted BigQuery analytics into AI-powered business intelligence.

> **This repository documents the complete journey of building an AI-powered Business Intelligence platform—from Data Engineering foundations to intelligent business insights.**

---

# Current Project Status

The **DeTLeng BigQuery MCP Server** is currently being developed as part of the **CS-003 – Building an Analytics-Ready E-Commerce Dataset with Google BigQuery** case study.

At this stage, the project is intentionally being built in public.

The complete architecture, documentation, implementation journey, and source code are openly available to encourage learning, knowledge sharing, and community collaboration.

Anyone is welcome to explore the project, understand the architecture, and follow the implementation process from Data Engineering to AI-powered Business Intelligence.

As the project evolves, it will become the foundation for future DeTLeng Business Intelligence solutions and real-world client implementations.

If this approach aligns with your business needs, we would be delighted to discuss how DeTLeng can help build an Intelligent Business Platform for your organization.

> **Learn. Explore. Build. Collaborate.**

And when you're ready...

**Place your order.**

We will take care of the rest.

---

**DeTLeng**

*Transform Complexity into Clarity.*

*Transform Data into Decisions.*

*Transform Knowledge into Business Value.*

---

## Overview

The **DeTLeng BigQuery MCP Server** is an open, reusable Model Context Protocol (MCP) server designed to securely connect AI assistants with Google BigQuery analytics datasets.

Rather than exposing raw databases or allowing unrestricted SQL execution, this project provides curated Business Intelligence tools that return trusted metrics, KPIs, and analytical insights.

It is designed around the DeTLeng philosophy:

> **From Raw Data to Business Value.**

---

# Why This Project Exists

Modern AI assistants can answer questions.

Businesses need accurate answers backed by trusted data.

This project bridges that gap.

Instead of asking an AI to guess business metrics, the assistant retrieves information directly from an analytics-ready BigQuery warehouse through carefully designed business tools.

---

# DeTLeng Philosophy

We do not simply expose databases.

We expose **Business Intelligence**.

Instead of:

```
AI
    ↓
Generate SQL
    ↓
Database
```

We build:

```
AI
    ↓
Business Intelligence Tools
    ↓
BigQuery Analytics
    ↓
Trusted Business Answers
```

---

# Key Features

- Google BigQuery Integration
- Model Context Protocol (MCP)
- AI-ready Business Intelligence
- Secure Analytics Layer Access
- Reusable Business Tools
- OpenAI Compatible
- Claude Compatible
- Gemini Compatible
- Production-Oriented Architecture

---

# Core Principles

This project follows several architectural principles.

## Analytics First

AI only accesses trusted analytics datasets.

Never raw operational tables.

Never staging datasets.

---

## Security by Design

Only approved business tools are exposed.

The AI never receives unrestricted database access.

---

## Business Over SQL

The AI interacts with business concepts rather than writing arbitrary SQL whenever possible.

Examples include:

- Total Revenue
- Customer Count
- Monthly Sales
- Top Products
- Delivery Performance

---

# High-Level Architecture

```
                User
                  │
                  ▼
      DeTLeng BI Assistant
                  │
                  ▼
        OpenAI / Claude / Gemini
                  │
                  ▼
     DeTLeng BigQuery MCP Server
                  │
                  ▼
          Business Intelligence Tools
                  │
                  ▼
      Google BigQuery Analytics Layer
                  │
                  ▼
          Trusted Business Answers
```

---

# Repository Structure

```
detleng-bigquery-mcp/

│
├── server.py
├── tools.py
├── bigquery_client.py
├── config.py
├── requirements.txt
├── README.md
│
├── prompts/
│   └── system_prompt.md
│
└── docs/
    └── architecture.md
```

---

# Current Development Status

This project is currently under active development.

Initial milestones include:

- Project Architecture
- BigQuery Connection
- MCP Server
- Business Intelligence Tools
- OpenAI Integration
- Website Integration
- Production Deployment

---

# Planned Business Intelligence Tools

Initial release will include tools such as:

- get_customer_count()
- get_total_orders()
- get_total_revenue()
- get_top_products()
- get_sales_by_region()
- get_delivery_performance()

Future releases will expand to include:

- Customer Analytics
- Product Analytics
- Revenue Analytics
- Delivery Analytics
- Payment Analytics
- Executive KPIs
- Trend Analysis
- Forecast Support

---

# Technology Stack

- Python
- FastMCP
- Google BigQuery
- Google Cloud
- OpenAI Responses API
- Model Context Protocol (MCP)

---

# DeTLeng Ecosystem

This project is part of the broader DeTLeng ecosystem focused on building Intelligent Business Systems through Data Engineering, Analytics, Artificial Intelligence, and Automation.

Core specialization:

- Data Engineering
- ETL / ELT
- Analytics Engineering
- BigQuery
- Business Intelligence
- AI Assistants
- AI Agents
- MCP
- Intelligent Business Systems

---

# Vision

The long-term objective is to create a reusable Business Intelligence layer that allows organizations to interact with their trusted analytics warehouse using natural language.

The same architecture can be reused across industries including:

- Retail
- Healthcare
- Manufacturing
- Finance
- Education
- Logistics
- Human Resources

---

# License

MIT License

---

## DeTLeng

**Transform Complexity into Clarity.**

**Transform Data into Decisions.**

**Transform Knowledge into Business Value.**
