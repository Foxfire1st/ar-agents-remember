# mcp/tests/test_knowledge_reader.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The Knowledge reader route's Python suite: path validation, file and code reads, the bounded
directory view and paged subtree, entries and states, route and family resolution, the without-proof
list and the census, and the code reader's bounds.

## Code Commentary

### Logic

- The suite drives the reader through its registered route against temporary repositories; the cases
  keep `present`/`absent`/`unavailable` apart, prove the 2 MiB code bound is never read, the bounded
  directory summary, states and route chains.
- MIK-R79 adds the `hasKnowledge` field to the explorer listing case's expected composed row, so the
  test now pins the new presence mark alongside the existing name, kind, `inCode`, `onboarding` and
  entry-count fields.

### Conventions

- pytest; temporary repositories and trees, one shared `world` fixture.

### Invariants And Boundaries

The suite binds the reader route's answer semantics; it does not test the dashboard or the coverage
negative matrix (which lives in its own module).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packets `MIK-R29@v1` and `MIK-R79@v1`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The explorer listing case that now expects the presence mark. [14]
- The listing entry point the route uses. [15]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
