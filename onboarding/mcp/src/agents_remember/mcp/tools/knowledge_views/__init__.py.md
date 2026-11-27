# mcp/src/agents_remember/mcp/tools/knowledge_views/__init__.py

## Governing Overview

[MCP Tool Payload Adapters](../overview.md)

## Purpose

Package marker for `agents_remember.mcp.tools.knowledge_views`, which houses the extracted `knowledge_read` request value object and single-record/table view adapter helpers.

## Code Commentary

Contains only the one-line module docstring describing the subpackage boundary (`read_request.py` for the request and code-source observation, `record_views.py` for single-record, mark-list, writer-table, and consolidation-proposal views); it re-exports no symbols.

## Relationships

Subpackage of `mcp/src/agents_remember/mcp/tools/`, paired with sibling modules `read_request.py` and `record_views.py` and consumed by `mcp/src/agents_remember/mcp/tools/knowledge.py`. Distinct from `agents_remember.application.knowledge_views`, which owns query-view execution over an index snapshot.

## Evidence

- The package marker scopes `knowledge_views` to the `knowledge_read` adapter's request object and single-record views. [1]
