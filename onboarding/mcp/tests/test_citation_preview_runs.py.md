# mcp/tests/test_citation_preview_runs.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Exercises background citation previews through the shared run machinery and the public payload boundary.

## Code Commentary

The cases compare the real synchronous preview with the completed background whole result and compact answer, including a refused document, and compare memory bytes before and after. Other cases hold live work to test common capacity, identity separation and responsive polling; mutate returned data to test detachment; and exercise scope changes and worker failures. Start and poll malformed arguments, including attempted background writes, are refused.

### Invariants And Boundaries

These source assertions are not a fresh run result. The background mode is only a preview. An unsuccessful repair result and a failed worker are distinct outcomes even when a delivered answer uses a failure status.

## Evidence


- Synchronous and completed background previews agree without changing memory. [1]



- Shared capacity, identity, ownership and failure boundaries are exercised. [2]


