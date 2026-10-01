# reporting.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Defines the structured checkpoint contract and deterministic JSON writer used by every harness run.

## Code Commentary

### Logic

A frozen `CheckpointDefinition` owns stable requirement, expectation, and evidence-owner meaning.
`CheckpointRecorder.check` appends actual candidate evidence and raises only after preserving the
failed record; diagnostics remain non-acceptance context.

### Conventions

Definitions are separate from observations so report meaning cannot drift with incidental payload
assembly. JSON output is indented, key-sorted, UTF-8, and newline-terminated.

### Invariants And Boundaries

- Every failed checkpoint is recorded before `CheckpointFailure` escapes.
- Diagnostic rows never count as acceptance proof.
- Report assembly is deterministic and carries the scenario name.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured or needed for this repository-owned evidence shape.

- Stable checkpoint meaning and observed evidence are separate records. [1]

### Repo-Internal References

- Failure is raised only after the structured checkpoint is appended. [2]

### Cross-Repo References

No meaningful cross-repository reference applies.

- The report contract is wholly repository-owned. [3]
