"""Logging utilities for MCP Atlassian.

This module provides enhanced logging capabilities for MCP Atlassian,
including level-dependent stream handling to route logs to the appropriate
output stream based on their level.
"""

import logging
import sys
from typing import TextIO


def setup_logging(
    level: int = logging.WARNING, stream: TextIO = sys.stderr
) -> logging.Logger:
    """
    Configure MCP-Atlassian logging with level-based stream routing.

    Args:
        level: The minimum logging level to display (default: WARNING)
        stream: The stream to write logs to (default: sys.stderr)

    Returns:
        The configured logger instance
    """
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Remove existing handlers to prevent duplication
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Add the level-dependent handler
    handler = logging.StreamHandler(stream)
    formatter = logging.Formatter("%(levelname)s - %(name)s - %(message)s")
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    # Configure specific loggers
    loggers = ["mcp-atlassian", "mcp.server", "mcp.server.lowlevel.server", "mcp-jira"]

    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

    # Return the application logger
    return logging.getLogger("mcp-atlassian")


def mask_sensitive(value: str | None, keep_chars: int = 4) -> str:
    """Masks sensitive strings for logging.

    Args:
        value: The string to mask
        keep_chars: Number of characters to keep visible at start and end

    Returns:
        Masked string with most characters replaced by asterisks
    """
    if not value:
        return "Not Provided"
    if len(value) <= keep_chars * 2:
        return "*" * len(value)
    start = value[:keep_chars]
    end = value[-keep_chars:]
    middle = "*" * (len(value) - keep_chars * 2)
    return f"{start}{middle}{end}"


def get_masked_session_headers(headers: dict[str, str]) -> dict[str, str]:
    """Get session headers with sensitive values masked for safe logging.

    Args:
        headers: Dictionary of HTTP headers

    Returns:
        Dictionary with sensitive headers masked
    """
    sensitive_headers = {"Authorization", "Cookie", "Set-Cookie", "Proxy-Authorization"}
    masked_headers = {}

    for key, value in headers.items():
        if key in sensitive_headers:
            if key == "Authorization":
                # Preserve auth type but mask the credentials
                if value.startswith("Basic "):
                    masked_headers[key] = f"Basic {mask_sensitive(value[6:])}"
                elif value.startswith("Bearer "):
                    masked_headers[key] = f"Bearer {mask_sensitive(value[7:])}"
                else:
                    masked_headers[key] = mask_sensitive(value)
            else:
                masked_headers[key] = mask_sensitive(value)
        else:
            masked_headers[key] = str(value)

    return masked_headers


def log_config_param(
    logger: logging.Logger,
    service: str,
    param: str,
    value: str | None,
    sensitive: bool = False,
) -> None:
    """Logs a configuration parameter, masking if sensitive.

    Args:
        logger: The logger to use
        service: The service name (Jira or Confluence)
        param: The parameter name
        value: The parameter value
        sensitive: Whether the value should be masked
    """
    display_value = mask_sensitive(value) if sensitive else (value or "Not Provided")
    logger.info(f"{service} {param}: {display_value}")
