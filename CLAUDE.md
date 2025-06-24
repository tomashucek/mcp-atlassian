# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Testing
- `uv run pytest` - Run all tests
- `uv run pytest tests/unit/` - Run unit tests only
- `uv run pytest tests/integration/` - Run integration tests only
- `uv run pytest -k "test_name"` - Run specific test
- `uv run pytest --cov` - Run tests with coverage

### Code Quality
- `uv run ruff check` - Lint code
- `uv run ruff format` - Format code
- `uv run mypy src/` - Type checking
- `uv run pre-commit run --all-files` - Run all pre-commit hooks

### Development Setup
- `uv sync` - Install dependencies and sync environment
- `uv run pre-commit install` - Install pre-commit hooks
- `uv run mcp-atlassian --help` - View CLI options

### Running the Server
- `uv run mcp-atlassian` - Run with stdio transport (default)
- `uv run mcp-atlassian --transport sse --port 9000` - Run with SSE transport
- `uv run mcp-atlassian --oauth-setup` - Run OAuth setup wizard
- `uv run mcp-atlassian --verbose` - Run with verbose logging

## Architecture Overview

### Core Structure
This is an MCP (Model Context Protocol) server that bridges Atlassian products (Jira and Confluence) with AI language models. The architecture follows a layered approach:

**Server Layer** (`src/mcp_atlassian/servers/`):
- `main.py` - Main FastMCP server with tool filtering and multi-user authentication
- `jira.py` / `confluence.py` - Service-specific MCP tool registration
- `context.py` - Shared application context for configuration state

**Client Layer** (`src/mcp_atlassian/jira/` & `src/mcp_atlassian/confluence/`):
- Service-specific API clients that handle authentication and API communication
- Each service has dedicated modules for different operations (issues, pages, search, etc.)

**Models Layer** (`src/mcp_atlassian/models/`):
- Pydantic models for structured data validation and serialization
- Separate model hierarchies for Jira and Confluence entities

**Preprocessing Layer** (`src/mcp_atlassian/preprocessing/`):
- Content transformation and sanitization before sending to LLMs
- Handles HTML/markup conversion and data filtering

### Key Patterns

**Multi-Service Configuration**: The server dynamically loads Jira and/or Confluence configurations based on available environment variables. Services are only enabled if properly authenticated.

**Tool Filtering**: Tools can be filtered by:
- Enabled tools list (`ENABLED_TOOLS` env var)
- Read-only mode (`READ_ONLY_MODE` env var) 
- Service availability (missing config disables related tools)

**Authentication Flexibility**: Supports multiple auth methods:
- API tokens (Cloud)
- Personal Access Tokens (Server/Data Center)
- OAuth 2.0 (Cloud only)
- Per-user authentication in HTTP transports

**Transport Options**: Supports stdio (for IDE integration), SSE, and streamable-HTTP transports for different deployment scenarios.

### Configuration Management
Environment-based configuration with precedence: CLI args > env vars > defaults. Main config classes are `JiraConfig` and `ConfluenceConfig` in respective service directories.

**Custom Headers**: Both services support custom User-Agent headers via `JIRA_USER_AGENT` and `CONFLUENCE_USER_AGENT` environment variables for firewall compatibility.

### Testing Strategy
- Unit tests for individual components with mocked dependencies
- Integration tests for API communication and authentication flows
- Fixtures provide consistent test data across test suites