# FastMCP Commands Reference

---

# DeTLeng BigQuery MCP Server

Professional command reference for developing, testing, inspecting and validating
FastMCP servers.

This document records the commands discovered during the development of the
DeTLeng BigQuery MCP Server.

---

# Display FastMCP Help

```bash
fastmcp --help
```

Description

Displays all available FastMCP commands.

Useful for discovering newly added CLI features after upgrading FastMCP.

---

# Display Version

```bash
fastmcp version
```

Description

Displays the installed FastMCP version.

Useful for debugging version compatibility issues.

---

# List Registered MCP Tools

```bash
fastmcp list server.py
```

Description

Loads the MCP server and lists every registered tool.

Example Output

```
Tools (6)

server_status()

customer_count()

total_orders()

total_revenue()

top_products()

delivery_performance()
```

Purpose

- Verify tool registration
- Confirm decorators are working
- Validate server loading
- Quick health check

This is the fastest command for validating an MCP server.

---

# List Resources

```bash
fastmcp list server.py --resources
```

Description

Lists every registered MCP Resource.

Useful when building knowledge bases or exposing documents through MCP.

---

# List Prompts

```bash
fastmcp list server.py --prompts
```

Description

Lists every registered MCP Prompt.

Useful for Prompt Engineering workflows.

---

# Display Input Schemas

```bash
fastmcp list server.py --input-schema
```

Description

Displays the JSON schema for every registered tool input.

Useful when integrating AI clients.

---

# Display Output Schemas

```bash
fastmcp list server.py --output-schema
```

Description

Displays the JSON schema for tool outputs.

Useful for validating structured responses.

---

# Export Tool List as JSON

```bash
fastmcp list server.py --json
```

Description

Exports all registered tools as JSON.

Useful for automation and documentation.

---

# Inspect MCP Server

```bash
fastmcp inspect server.py
```

Description

Inspects the complete MCP server.

Displays server metadata and registration details.

Useful before publishing an MCP server.

---

# Export Inspection Report

```bash
fastmcp inspect server.py --format fastmcp
```

Description

Exports the FastMCP server specification.

Useful for documentation and debugging.

---

# Export MCP Protocol Specification

```bash
fastmcp inspect server.py --format mcp
```

Description

Exports the server using the official MCP protocol format.

Useful when integrating external MCP clients.

---

# Save Inspection Report

```bash
fastmcp inspect server.py --format mcp --output report.json
```

Description

Generates a JSON inspection report.

Useful for CI/CD pipelines and documentation.

---

# Run MCP Server

```bash
python server.py
```

Description

Starts the MCP server using the project's Python entry point.

Used during development.

---

# Run Through FastMCP

```bash
fastmcp run server.py
```

Description

Runs the MCP server directly using the FastMCP CLI.

Useful when testing outside the Python entry point.

---

# Call an MCP Tool

```bash
fastmcp call server.py customer_count
```

Description

Calls an individual MCP tool directly from the command line.

Useful for rapid testing without an AI client.

---

# Call Tool With Parameters

```bash
fastmcp call server.py top_products --limit 5
```

Description

Executes an MCP tool that accepts parameters.

Useful for validating business logic.

---

# Discover MCP Servers

```bash
fastmcp discover
```

Description

Searches for FastMCP project configurations on the local machine.

Useful when managing multiple MCP servers.

---

# Generate CLI

```bash
fastmcp generate-cli server.py
```

Description

Generates a standalone command-line interface for the MCP server.

Useful for distributing internal tools.

---

# Install MCP Server

```bash
fastmcp install
```

Description

Installs the MCP server for supported MCP clients.

Useful for Claude Desktop and other compatible environments.

---

# Development Commands

Show development options

```bash
fastmcp dev --help
```

Description

Displays development commands available in FastMCP.

Useful while building and debugging MCP servers.

---

# Common Validation Workflow

Step 1

```bash
python test_bigquery.py
```

Verify BigQuery connectivity.

---

Step 2

```bash
python test_tools.py
```

Validate Business Intelligence tools.

---

Step 3

```bash
fastmcp list server.py
```

Verify MCP tool registration.

---

Step 4

```bash
fastmcp inspect server.py
```

Inspect the complete MCP server.

---

Step 5

```bash
python server.py
```

Run the production MCP server.

---

# Recommended Development Workflow

BigQuery

↓

Business Tools

↓

Test Tools

↓

Register MCP Tools

↓

Inspect Server

↓

Run Server

↓

Connect AI Client

↓

Production

---

End of Document
