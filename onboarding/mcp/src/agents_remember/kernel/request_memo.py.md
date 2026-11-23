# mcp/src/agents_remember/kernel/request_memo.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Owns computation memos for one native tool call or detached quality computation.

## Code Commentary

A context variable identifies the scope. Consumers create each keyed owner lazily under a lock and share it with workers that inherit the context. Scope exit clears the shared map before restoring the context token. Outside a scope, each caller chooses its owner.

## Relationships

Native tool dispatch and detached quality computation each open a scope. The request-thread helper drains blocking work before its caller leaves the scope.

## Evidence

- Scope exit clears the common owner map and restores the token. [1]
- Thread-safe lazy lookup shares an owner under one scope. [2]
