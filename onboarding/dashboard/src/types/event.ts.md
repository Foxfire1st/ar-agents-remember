# dashboard/src/types/event.ts

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Declares the dashboard's TypeScript shape for observer events.

## Code Commentary

### Logic

Trust has four values and Actor has three. ObserverEvent requires schema, id, ts, kind, trust and actor; data and the lifecycle, enclosure, repository, session and span identifiers are optional.

### Conventions

Wire names remain camelCase and align with the Python event envelope. Provenance distinguishes declared, observed, inferred and approved facts.

### Invariants And Boundaries

This file supplies static types only. Its schema field is a string; it performs no runtime event validation.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation is configured. This card describes repository source only.

### Repo-Internal References

These constructs establish the behavior described above.

- Closed provenance vocabularies and event field shape [1]
- Python envelope supplies the corresponding wire names and provenance values [2]

### Cross-Repo References

No cross-repository behavior is implemented in this file.
