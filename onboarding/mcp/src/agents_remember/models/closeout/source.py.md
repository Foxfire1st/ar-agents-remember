# mcp/src/agents_remember/models/closeout/source.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Define neutral typed inputs and evidence for closeout-door source publication.

## Code Commentary

### Logic

The module models candidate admission facts, scheduling grade input/output, evidence facts, and route-review facts with strict validation and bounded text.

### Invariants And Boundaries

- False admission facts require explanatory reasons.
- Scheduling priority is typed and separate from lifecycle state.
- Source evidence is input to door/projection derivation, never queue-owned history.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain-documentation source applies to this repository-internal route.

### Repo-Internal References

- Candidate and scheduling inputs validate readiness and priority explicitly. [1]
- Evidence and route-review facts are strict bounded source models. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
