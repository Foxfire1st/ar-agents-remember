# mcp/tests/test_f08_registered_handler_river.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Proves the feed through the registered handler path (MIK-R114 rule 1, evidence item 1):
bound and unbound first calls through `create_server` with a real in-memory MCP session,
the caller fixed after a startup binding rewrite, and a fresh process writing through
startup.

## Code Commentary

Four cases run the actual `create_server` + registered-handler + session path instead of
a manually installed writer: bound first-call fields, unbound chat with harness, caller
fixed after binding rewrite, and fresh-process first call. The module is the reply to
the retained E1 gap, not a second copy of the river unit surface.

## Evidence

- Bound first call through the registered handler carries caller and facts. [1]
- A fresh process writes its first call through startup. [2]
