# mcp/src/agents_remember/application/knowledge_write_answer.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Shapes the writer report into the mounted knowledge_write reply.

## Code Commentary

`write_answer` shapes the full validated `KnowledgeWriteResponse` payload: state, owner, memory root, code tree, counts from complete record/entry/history lists, bounded problem/violation/note/written/removed lists with separate truncation indicators and total counts (`violationCount`, `writtenCount`, `removedCount`), and full report location (`reportPath`/`reportError`).

`compact_write_answer` builds the bounded inline tool answer passed to `_tool_payload(..., answer=...)`: it strips `ENVELOPE_STRIPPED_FIELDS` and `None` values, caps `problems`, `violations`, `notes`, `written`, and `removed` at `COMPACT_WRITE_LIST_MAX = 5` entries inline while setting the exact total counts and truncation flags whenever shortened, and preserves `reportPath`, `refusalCode`, `refusalDetail`, and `counts`.

## Evidence

- `write_answer` retains the writer's outcome, counts, truncation flags, and full report location in the validated payload. [1]
- `compact_write_answer` caps `problems`, `violations`, `notes`, `written`, and `removed` at `COMPACT_WRITE_LIST_MAX` (5) inline with total counts and truncation flags while stripping envelope fields. [2]
