# Security Architecture

> Trust is the foundation of every Business Intelligence platform.

---

**DeTLeng**

*Transform Complexity into Clarity.*

*Transform Data into Decisions.*

*Transform Knowledge into Business Value.*

---

# Overview

Artificial Intelligence becomes valuable only when it operates on trusted, governed, and secure business data.

The DeTLeng BigQuery MCP Server has been designed with security as a core architectural principle.

The AI assistant is **never granted unrestricted database access**.

Instead, every layer follows the principle of least privilege, ensuring that AI can answer business questions without exposing sensitive business assets.

---

# Security Philosophy

The DeTLeng approach follows a simple principle:

> AI should have access to business intelligence, not business databases.

This distinction is critical.

Traditional AI systems often receive broad database permissions, allowing them to generate arbitrary SQL queries against production systems.

The DeTLeng architecture deliberately avoids this design.

Instead, AI interacts only with trusted analytical datasets through controlled Business Intelligence tools.

---

# Security Layers

```
User
   │
   ▼
AI Assistant
   │
   ▼
Business Intelligence Tools
   │
   ▼
MCP Server
   │
   ▼
Analytics Dataset
   │
   ▼
BigQuery
```

Each layer has its own responsibility and security boundary.

---

# Layer 1 — User Authentication

Only authorized users should be allowed to access the AI Assistant.

Possible authentication methods include:

- Website login
- Google Authentication
- Microsoft Entra ID
- Enterprise SSO
- OAuth

The MCP Server assumes that user authentication has already been completed.

---

# Layer 2 — OpenAI

The OpenAI API is responsible only for language understanding.

It does not store or manage business permissions.

Responsibilities include:

- Understanding natural language
- Selecting appropriate Business Tools
- Summarizing analytical results
- Generating human-readable responses

OpenAI never connects directly to BigQuery.

---

# Layer 3 — MCP Server

The MCP Server acts as a controlled gateway between AI and business data.

Responsibilities include:

- Expose approved Business Intelligence tools
- Validate incoming requests
- Prevent unauthorized operations
- Execute predefined business logic
- Return structured business results

The MCP Server never exposes database credentials to users.

---

# Layer 4 — BigQuery Authentication

The MCP Server connects to BigQuery using a dedicated Google Cloud Service Account.

Example:

```
Service Account

↓

BigQuery Data Viewer

↓

Analytics Dataset Only
```

The Service Account should have read-only access.

Recommended IAM Roles:

- BigQuery Data Viewer
- BigQuery Job User

No administrative permissions should be granted.

---

# Dataset Isolation

The DeTLeng data platform separates information into multiple layers.

```
Raw Layer

↓

Staging Layer

↓

Analytics Layer
```

Only the Analytics Layer is accessible through MCP.

The Raw and Staging layers remain completely isolated.

---

# Why Analytics Layer Only?

Raw data frequently contains:

- Missing values
- Duplicate records
- Invalid formats
- Temporary fields
- Internal identifiers
- Incomplete transactions

These datasets are intended for Data Engineering, not business users.

AI should never make business decisions using incomplete or unvalidated data.

---

# Principle of Least Privilege

Every component receives only the permissions it actually requires.

Examples:

OpenAI

✓ Understand questions

✗ Read databases

✗ Modify data

✗ Delete data

---

MCP Server

✓ Execute approved Business Tools

✓ Read Analytics Layer

✗ Modify datasets

✗ Delete tables

✗ Access Raw Layer

---

BigQuery

✓ Execute read-only analytical queries

✗ Update records

✗ Delete records

✗ Create datasets

---

# Read-Only Analytics

The MCP Server is designed exclusively for analytical workloads.

Supported operations include:

- SELECT
- Aggregations
- KPIs
- Business metrics
- Trend analysis
- Summary statistics

The following operations are intentionally blocked:

- INSERT
- UPDATE
- DELETE
- DROP
- ALTER
- CREATE

This prevents accidental or malicious modification of production data.

---

# Business Tool Isolation

The AI Assistant does not generate unrestricted SQL.

Instead, it calls predefined Business Intelligence tools.

Example

```
User

↓

"What is total revenue?"

↓

get_total_revenue()

↓

BigQuery

↓

Business Result
```

The AI never receives unrestricted database access.

---

# Data Governance

Business Intelligence is only as reliable as its underlying data.

The DeTLeng platform promotes strong governance through:

- ETL validation
- Data quality checks
- Standardized dimensions
- Standardized fact tables
- Business rule validation
- Trusted analytical models

Only governed datasets are exposed to AI.

---

# Logging and Monitoring

Every business request can be logged.

Examples include:

- Timestamp
- User
- Business Tool
- Execution time
- Query duration
- Success or failure

These logs support:

- Auditing
- Troubleshooting
- Performance optimization
- Compliance

---

# Secrets Management

Sensitive credentials should never be stored inside source code.

Recommended approaches include:

- Google Secret Manager
- Environment Variables
- GitHub Secrets
- Cloud Run Secrets
- Cloud Functions Secrets

Service Account JSON files should never be committed to Git repositories.

---

# API Security

The AI Assistant communicates with the MCP Server through secure APIs.

Recommended protections include:

- HTTPS
- Authentication Tokens
- API Keys
- OAuth
- Rate Limiting
- Request Validation

---

# Future Enterprise Security

Future versions of the DeTLeng MCP platform may include:

- Row-Level Security
- Column-Level Security
- Role-Based Access Control (RBAC)
- User-Level Permissions
- Multi-Tenant Architecture
- Audit Dashboards
- Query Approval Policies
- Data Loss Prevention (DLP)

These features will support enterprise-scale deployments.

---

# Security Principles

The DeTLeng BigQuery MCP Server follows these core principles:

✓ Least Privilege

✓ Read-Only Analytics

✓ Dataset Isolation

✓ Business Tool Abstraction

✓ Secure Authentication

✓ Governed Business Intelligence

✓ Enterprise Logging

✓ Secret Management

✓ AI Without Database Exposure

---

# DeTLeng Security Framework

```
Business User
        │
        ▼
Authentication
        │
        ▼
OpenAI
        │
        ▼
MCP Server
        │
        ▼
Business Intelligence Tools
        │
        ▼
Analytics Dataset
        │
        ▼
BigQuery
```

Every layer protects the next.

No component receives unrestricted access.

---

# Final Thought

Security is not an additional feature.

It is a design principle.

The DeTLeng BigQuery MCP Server is built on the belief that Artificial Intelligence should accelerate business decisions without compromising governance, privacy, or trust.

By combining secure Data Engineering practices with controlled AI access, organizations can confidently transform trusted analytics into intelligent business insights.
