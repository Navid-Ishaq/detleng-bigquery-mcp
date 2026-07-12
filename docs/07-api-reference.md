# API Reference

> Standard Business Intelligence interfaces for the DeTLeng BigQuery MCP Server.

---

# Overview

The DeTLeng BigQuery MCP Server provides a standardized interface between Artificial Intelligence and Business Intelligence.

Rather than exposing database tables or raw SQL execution, the platform exposes business-oriented tools that return trusted analytical results.

Each Business Intelligence tool represents a reusable API capability.

This document describes the logical API structure used throughout the platform.

---

# API Philosophy

Traditional APIs expose data.

The DeTLeng API exposes business capabilities.

Instead of requesting database records, clients request business insights.

Example

Traditional

```
GET /sales
```

DeTLeng

```
get_total_revenue()
```

Traditional

```
GET /customers
```

DeTLeng

```
get_customer_count()
```

The focus shifts from retrieving data to answering business questions.

---

# API Categories

Business Intelligence APIs are organized into logical domains.

---

## Customer Intelligence

Purpose

Provides customer-related business insights.

Available Operations

```
get_customer_count()

get_new_customers()

get_repeat_customers()

get_customer_growth()

get_top_customers()

get_customer_distribution()
```

---

## Revenue Intelligence

Purpose

Provides financial and revenue analytics.

Available Operations

```
get_total_revenue()

get_monthly_revenue()

get_average_order_value()

get_revenue_by_category()

get_revenue_by_region()
```

---

## Sales Intelligence

Purpose

Provides operational sales analytics.

Available Operations

```
get_total_orders()

get_sales_summary()

get_daily_sales()

get_monthly_sales()

get_top_products()

get_sales_trend()
```

---

## Product Intelligence

Purpose

Provides product performance analysis.

Available Operations

```
get_product_performance()

get_product_rankings()

get_best_categories()

get_low_performing_products()
```

---

## Seller Intelligence

Purpose

Provides marketplace seller analytics.

Available Operations

```
get_top_sellers()

get_seller_revenue()

get_active_sellers()

get_seller_performance()
```

---

## Delivery Intelligence

Purpose

Provides logistics performance.

Available Operations

```
get_average_delivery_time()

get_late_deliveries()

get_delivery_success_rate()

get_delivery_performance()
```

---

## Payment Intelligence

Purpose

Provides payment analytics.

Available Operations

```
get_payment_summary()

get_payment_methods()

get_average_payment_value()

get_installment_distribution()
```

---

## Executive Intelligence

Purpose

Provides executive-level business summaries.

Available Operations

```
get_daily_kpis()

get_business_summary()

get_growth_summary()

get_executive_dashboard()

get_business_health()
```

---

# Standard Tool Structure

Every Business Intelligence tool follows the same structure.

```
Business Question

↓

Business Tool

↓

Analytics Query

↓

Business Result

↓

Natural Language Explanation
```

This standard keeps the platform predictable, maintainable, and reusable.

---

# Example

Business Question

```
What is today's revenue?
```

Tool

```
get_total_revenue()
```

Business Layer

```
Analytics Dataset
```

Response

```json
{
  "metric": "Total Revenue",
  "value": 1835642.45,
  "currency": "USD"
}
```

The AI Assistant converts this structured response into a business-friendly explanation.

---

# Response Principles

Every Business Intelligence API follows the same principles.

Responses should be:

- Accurate
- Consistent
- Structured
- Human-readable
- Business-focused

The API should never expose unnecessary implementation details.

---

# Error Handling

Business Intelligence APIs should return meaningful messages.

Examples

```
Dataset not available.
```

```
No records found.
```

```
Invalid business request.
```

```
Unable to execute business tool.
```

```
Authentication required.
```

The objective is to provide understandable feedback instead of technical errors whenever possible.

---

# Future Expansion

The API architecture is intentionally modular.

New Business Intelligence tools can be added without changing the existing interface.

Future domains may include:

- Human Resources
- Finance
- Healthcare
- Manufacturing
- Supply Chain
- Education
- Marketing
- Customer Support

Each domain follows the same API design principles.

---

# API Design Principles

Every Business Intelligence API should:

✓ Represent a business capability

✓ Return trusted analytical results

✓ Hide SQL complexity

✓ Follow consistent naming conventions

✓ Produce structured responses

✓ Remain reusable across industries

---

# Naming Convention

Business tools should always use clear business terminology.

Recommended

```
get_total_revenue()

get_customer_count()

get_top_products()

get_sales_summary()
```

Avoid

```
execute_sql()

run_query()

fetch_table()

select_data()
```

The API should describe the business objective, not the implementation.

---

There will be a single **DeTLeng MCP Server** that serves as the central platform.

Within this server, multiple **Business Intelligence domains** will be organized as independent functional modules.

The high-level architecture is illustrated below:

```
                    OpenAI

                       │

                       ▼

         DeTLeng BigQuery MCP Server

                       │

 ┌──────────────┬──────────────┬──────────────┐

 ▼              ▼              ▼

Revenue      Customers      Products

Tools          Tools          Tools

 ▼              ▼              ▼

Analytics Dataset (BigQuery)
```

---


# DeTLeng API Philosophy

The purpose of this API is not to expose BigQuery.

The purpose is to expose Business Intelligence.

Artificial Intelligence should communicate using business language.

Data Engineering should manage technical complexity.

Business users should receive trusted answers without needing SQL knowledge.

---

# Final Thought

A modern API should do more than return data.

It should deliver business value.

The DeTLeng BigQuery MCP Server transforms trusted analytics into reusable Business Intelligence capabilities, allowing AI assistants to answer business questions with confidence, consistency, and clarity.

---

**Business APIs.**

**Trusted Analytics.**

**Intelligent Answers.**

**Powered by DeTLeng.**
