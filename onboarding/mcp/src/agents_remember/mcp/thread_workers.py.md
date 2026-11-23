# mcp/src/agents_remember/mcp/thread_workers.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Runs blocking native tool work in a thread while preserving its request context.

## Code Commentary

The helper shields the worker task. If the caller exits through an exception, the helper waits for the worker to finish despite repeated cancellation, observes any worker exception and propagates the caller's original exception. The caller retains its scope and any write lock while the worker drains.

## Relationships

Native dispatch uses this helper for blocking calls. The registered role start and role start set operations use it directly.

## Evidence

- The shielded worker drains before the caller propagates its exception. [1]
