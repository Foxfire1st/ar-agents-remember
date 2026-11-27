# mcp/src/agents_remember/cli/developer_message_files.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Keeps target-scoped complete developer messages, hashed picks and bounded sent-log history.

## Code Commentary

### Logic

Routes taskful messages to `<repository>/<task_id>/` and taskless targets to unified `taskless/<agent_id>/`, while reading back taskful folders, unified `taskless/*/*_<id>*.md`, and legacy `*/taskless/*/*_<id>*.md` files; uses guarded blob reuse and message-filing compensation for newly created unpublished files; appends bounded logs, reconciles a held row from its own receipt/request terminal end and updates its message path/hash truthfully.

### Invariants And Boundaries

Compaction evicts logs, never durable message/pick files. Published or previously reused blobs survive failure. Missing terminal evidence leaves held.

## Evidence

- Keeps target-scoped complete developer messages (taskful and unified taskless), legacy taskless read-back, hashed picks and bounded sent-log history. [1]

- Keeps target-scoped complete developer messages, hashed picks and bounded sent-log history. [2]
- Keeps target-scoped complete developer messages, hashed picks and bounded sent-log history. [3]
