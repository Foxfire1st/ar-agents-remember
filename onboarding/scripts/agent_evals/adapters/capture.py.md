# scripts/agent_evals/adapters/capture.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Converts explicit Codex and Claude transcript schemas into source-bound events while retaining raw records.

## Code Commentary

### Invariants And Boundaries

Unsupported dispatches remain opaque. Retained replay uses frozen exports rather than reopening live transcripts.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
