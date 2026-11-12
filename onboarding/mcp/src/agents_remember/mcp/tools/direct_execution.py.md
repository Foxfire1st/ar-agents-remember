# mcp/src/agents_remember/mcp/tools/direct_execution.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Adapts the architect grant operation to the common typed MCP answer boundary.

## Contract

direct_execution_grant_payload passes config, canonical task reference and action to the application owner, with optional bound caller evidence, and finalizes the result through _tool_payload under direct_execution_grant. Authority and mutation remain in the application, not this adapter.

## Evidence

- Adapts the architect grant operation to the common typed MCP answer boundary [1]
