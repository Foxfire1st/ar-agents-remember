# claude_stream_limits.py

## Governing Overview
[serving overview](overview.md)

## Purpose
Immutable positive bounds for startup, acceptance, retained correlation history, and event queues.

## Code Commentary
`ClaudeAdapterLimits` validates external-process and bounded-resource settings; limits are never semantic
or readiness fallbacks.

## Invariants And Boundaries
Keep bounds explicit and reject non-positive values.

## Evidence

### Repo-Internal References
- Consumed by the adapter facade. [1]
