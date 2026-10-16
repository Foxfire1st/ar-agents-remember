# mcp/src/agents_remember/serving/task_document_cache.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Keep one serving app’s prepared full task-document bodies while all body-generation inputs remain current.

## Code Commentary

The cache key is the requested coordination root and document path. A retained body is returned before another parse only after its generation validates; a stale value is dropped. Cold reads use the existing bounded body reader under generation capture and serialize its TaskSummary-shaped body once, with a digest of the actual response bytes.

Default limits are 1,024 entries and 16 MiB in total, with least-recently-used eviction. An individually oversized body is served but not retained. Missing documents return no body; unreadable or changing generations are not admitted as reusable results. The lock protects cache accounting, not a second task-document authority.

## Evidence

- Current generations bypass re-parsing; stale bodies are dropped before the existing reader runs. [1]
- The app-owned cache has positive entry/byte bounds and exact retained-byte accounting. [2]
