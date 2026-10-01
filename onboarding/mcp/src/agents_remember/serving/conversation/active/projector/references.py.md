# mcp/src/agents_remember/serving/conversation/active/projector/references.py

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Mints stable public-safe coordinates for live evidence, native history, and transcript echoes.

## Code Commentary

### Logic

`ProjectionEvidenceRefs` derives a short epoch prefix and formats `ar-ev`, `ar-native`, and
`ar-echo` reference strings. It stores no payload and performs no I/O.

### Conventions

References identify evidence coordinates; they are not source cursors or authorization tokens.

### Invariants And Boundaries

- Raw harness payloads never enter a reference.
- The bridge epoch scopes all coordinates to one authority generation.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- References are attached during native evidence-frame ingestion. [1]
- References are attached during echo-frame ingestion. [2]

### Cross-Repo References

No meaningful cross-repository references found.
