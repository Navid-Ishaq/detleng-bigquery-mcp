# Frequently Asked Questions (FAQ)

> Answers to the most common questions about the DeTLeng BigQuery MCP Server.

---

# What is the DeTLeng BigQuery MCP Server?

The DeTLeng BigQuery MCP Server is an AI-powered Business Intelligence platform that connects Artificial Intelligence with trusted analytical data stored in Google BigQuery.

Instead of asking users to write SQL queries or navigate dashboards, it allows business users to ask questions in natural language and receive trusted business insights.

---

# What does MCP stand for?

MCP stands for **Model Context Protocol**.

It is an open standard that enables AI models to securely communicate with external systems such as databases, APIs, business applications, and analytical platforms.

Think of MCP as the bridge between Artificial Intelligence and real business systems.

---

# Why use MCP instead of direct SQL?

Business users should never need to write SQL.

Instead of writing queries, they simply ask questions.

Example:

Instead of

```sql
SELECT SUM(price)
FROM fact_sales;
```

A business user asks:

> "What is our total revenue?"

The MCP Server retrieves the answer from the Analytics Layer and AI explains the result in business language.

---

# Why did DeTLeng build its own MCP Server?

Most MCP implementations focus on database connectivity.

The DeTLeng approach focuses on Business Intelligence.

Instead of exposing databases, the platform exposes reusable Business Intelligence tools.

This makes the platform:

- Easier to use
- Easier to maintain
- More secure
- More business-focused

---

# Does the AI generate SQL?

Sometimes.

The preferred approach is to use Business Intelligence tools.

If a suitable tool is unavailable, future versions may generate SQL within approved analytical datasets.

The goal is always to return trusted business answers rather than unrestricted database access.

---

# Does the AI access raw datasets?

No.

The AI is designed to work with trusted analytical data.

The recommended architecture separates data into:

```
Raw Layer

↓

Staging Layer

↓

Analytics Layer

↓

Business Intelligence Assistant
```

The AI interacts only with the Analytics Layer.

---

# Can this work with my own BigQuery project?

Yes.

The platform is designed to work with any Google BigQuery project.

Simply configure:

- Google Cloud Project
- Dataset
- Service Account
- OpenAI API Key

The overall architecture remains the same.

---

# Can this work with Power BI or Looker Studio?

Yes.

Dashboards and the AI Assistant complement each other.

Dashboards provide visual analysis.

The AI Assistant provides conversational Business Intelligence.

Both use the same Analytics Layer.

---

# Which AI models are supported?

The architecture is designed to work with modern Large Language Models including:

- OpenAI
- Claude
- Gemini

Any AI platform supporting MCP can be integrated.

---

# Do I need to know SQL?

No.

Business users do not need SQL knowledge.

However, understanding SQL and Data Engineering remains valuable for developers building or extending the platform.

---

# Can I use this for client projects?

Yes.

The architecture is intentionally reusable.

Only the business data changes.

The platform architecture remains the same.

---

# Is this only for e-commerce?

No.

The current implementation demonstrates the platform using an e-commerce dataset.

The same architecture can be adapted for:

- Retail
- Finance
- Healthcare
- Manufacturing
- Logistics
- Human Resources
- Education
- Government

The business domain changes.

The engineering principles remain the same.

---

# Does this replace dashboards?

No.

Dashboards remain an important part of Business Intelligence.

The AI Assistant provides another way to interact with trusted business data.

Both approaches complement each other.

---

# Why is Data Engineering important if AI exists?

Artificial Intelligence can explain data.

It cannot replace reliable data preparation.

Trusted Business Intelligence depends on:

- Clean data
- Reliable ETL pipelines
- Data Modeling
- Analytics Engineering
- Business Rules

Data Engineering provides the foundation that AI depends on.

---

# Is this repository production-ready?

The project is being developed publicly as part of the CS-003 case study.

The architecture follows production-oriented principles, while implementation continues to evolve through documented milestones.

---

# Can I follow the implementation process?

Absolutely.

This repository is intentionally built in public.

Every milestone, architectural decision, and implementation step is documented to encourage learning and transparency.

---

# Why is everything documented?

Because documentation is an engineering asset.

Every completed implementation should leave behind:

- Working Software
- Technical Documentation
- Business Knowledge
- Reusable Components

The objective is not only to build software but also to build reusable knowledge.

---

# How can I learn more?

Explore the documentation in the **docs/** folder.

Follow the implementation journey.

Experiment with the code.

Build your own Business Intelligence Assistant.

And most importantly...

Enjoy the learning process.

---

# Still Have Questions?

If your question is not answered here, feel free to explore the project documentation or contact the DeTLeng team.

We believe that sharing knowledge is one of the best ways to advance Data Engineering, Business Intelligence, and Artificial Intelligence.

---

## DeTLeng Philosophy

> **Data Engineering builds the foundation.**

> **Business Intelligence creates understanding.**

> **Artificial Intelligence improves accessibility.**

> **Together, they create Business Value.**

---

**Happy Learning!**

**Happy Building!**

**Welcome to the DeTLeng Engineering Journey.**
