# Data Flow

> From a business question to a trusted business answer.

---

# Overview

The purpose of the DeTLeng BigQuery MCP Server is simple:

> Transform natural language questions into trusted business intelligence.

Traditional Business Intelligence platforms require users to understand SQL, dashboards, data models, and analytical tools.

The DeTLeng approach removes this complexity.

Business users simply ask questions in natural language.

The platform handles everything else.

---

# The Journey

Imagine a Sales Manager asks:

> **"What was our total revenue?"**

The manager does not know SQL.

The manager does not know BigQuery.

The manager does not know how the data warehouse is designed.

The manager simply wants an answer.

The DeTLeng platform takes care of the rest.

---

# Complete Data Flow

```
Business User
        │
        ▼
Case Study Website
        │
        ▼
DeTLeng Business Intelligence Assistant
        │
        ▼
OpenAI Responses API
        │
        ▼
DeTLeng BigQuery MCP Server
        │
        ▼
Business Intelligence Tool
        │
        ▼
Google BigQuery
        │
        ▼
Analytics Dataset
        │
        ▼
Trusted Business Result
        │
        ▼
Natural Language Explanation
        │
        ▼
Business User
```

Every component has a single responsibility.

Together, they create an intelligent Business Intelligence platform.

---

# Step 1 — Business Question

Everything begins with a business question.

Examples include:

- What is our total revenue?
- Which products sell the most?
- Who are our top customers?
- Which state generates the highest sales?
- How many orders were delivered late?
- What is the average delivery time?

No SQL.

No dashboards.

No technical knowledge required.

---

# Step 2 — AI Understands the Intent

The OpenAI Responses API analyses the user's request.

Its responsibility is to understand:

- User intent
- Business context
- Required KPI
- Required Business Tool

The AI does not calculate business metrics.

It identifies which tool should be used.

---

# Step 3 — MCP Selects the Right Tool

Instead of allowing AI to freely generate SQL, the MCP Server exposes trusted Business Intelligence tools.

Examples:

```
get_total_revenue()

get_top_products()

get_customer_count()

get_average_delivery_time()

get_monthly_sales()
```

Each tool has a single responsibility.

This keeps the platform predictable, reliable, and easy to maintain.

---

# Step 4 — Querying BigQuery

The selected Business Tool communicates with Google BigQuery.

The query is executed only against the Analytics Layer.

```
cs003_olist_analytics
```

The Raw and Staging datasets are never queried by the AI Assistant.

Only trusted analytical data is used.

---

# Step 5 — Business Result

BigQuery returns structured business data.

Examples:

```
Revenue

Orders

Customers

Products

Payments

Delivery

Reviews
```

At this stage, the result is still raw numerical data.

---

# Step 6 — AI Explains the Result

The OpenAI Responses API transforms structured analytical data into a business-friendly explanation.

Instead of displaying raw numbers, the assistant provides meaningful insights.

Example:

```
Total Revenue

£13.6 Million

Generated from 99,441 completed orders.

Average Order Value

£136.82
```

The focus is not simply answering questions.

The goal is helping businesses make better decisions.

---

# Why This Architecture?

Without MCP

```
Business User

↓

AI

↓

Guess

↓

Possible Hallucination
```

With MCP

```
Business User

↓

AI

↓

Business Tool

↓

BigQuery

↓

Trusted Analytics

↓

Reliable Business Answer
```

The AI becomes an intelligent interface—not the source of truth.

The Analytics Layer remains the trusted source of business data.

---

# Current Implementation

Current Website

```
casestudy.detleng.com
```

Current AI

- OpenAI Responses API

Current Data Warehouse

- Google BigQuery

Current Dataset

```
cs003_olist_analytics
```

Current Data Model

- Fact Tables
- Dimension Tables

Current Purpose

- AI-powered Business Intelligence Demonstration

---

# Future Data Flow

As the platform evolves, the data flow will become fully automated.

```
Business Files

        │

        ▼

Google Cloud Storage

        │

        ▼

ETL Pipeline

        │

        ▼

BigQuery

        │

        ▼

Analytics Layer

        │

        ▼

MCP Server

        │

        ▼

Business Intelligence Assistant

        │

        ▼

Business Decision
```

New business data will automatically refresh the Analytics Layer.

The AI Assistant will always answer using the latest trusted information.

No manual intervention will be required.

---

# The DeTLeng Philosophy

Data has no value until it becomes information.

Information has no value until it supports a decision.

Artificial Intelligence has no value until it works with trusted data.

That is why DeTLeng combines Data Engineering, Business Intelligence, and Artificial Intelligence into a single implementation framework.

The result is not simply another chatbot.

It is an Intelligent Business Platform.

---

# Final Thought

The DeTLeng BigQuery MCP Server is not designed to replace Business Intelligence professionals.

It is designed to make Business Intelligence accessible to everyone.

Business users ask questions.

The platform finds trusted answers.

Data Engineers build the foundation.

Artificial Intelligence delivers the experience.

Together, they transform data into business value.

---

> **Current Status**
>
> This project is actively being developed as part of the **CS-003 Analytics-Ready E-Commerce Case Study**.
>
> The implementation is intentionally open to encourage learning, collaboration, and transparency.
>
> Today, it demonstrates AI-powered Business Intelligence using a public analytics dataset.
>
> Tomorrow, the same architecture will power real-world business solutions for organizations worldwide.
>
> **Learn. Explore. Build. Collaborate.**
>
> **And when you're ready...**
>
> **Let's build your Intelligent Business Platform together.**
>
> **— Team DeTLeng**
