# mcp/src/agents_remember/mcp/tools/closeout_queue.py

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Provides the thin MCP payload boundary for the sprint closeout queue.

## Code Commentary

### Logic

`closeout_queue_payload` delegates the strict request to the application boundary and merges the
result into the shared tool envelope.

### Conventions

Registration, ambient authorization, scheduling mechanics, and persistence remain in their owning
layers; this module only shapes the public payload.

### Invariants And Boundaries

- No request fields are reinterpreted here.
- Every success passes through `_tool_payload` for common response metadata.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- The payload adapter is deliberately a single delegation into the application service. [1]

### Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE Projection-Only Payload

This module is the thin payload builder for the disposable closeout projection, not a durable
pre-closeout scheduler. It delegates status/rebuild to the application owner and validates the
strict response envelope; canonical door publication and claimed operation evidence remain on
their separate surfaces.
