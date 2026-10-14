# reporting.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Defines the structured checkpoint contract and deterministic JSON writer used by every harness run.

## Code Commentary

### Logic

A frozen `CheckpointDefinition` owns stable requirement, expectation, and evidence-owner meaning.
`CheckpointRecorder` now holds checkpoint/diagnostic containers and assembles a schema/scenario report before overlaying caller-supplied values. It does not itself append checks, classify pass/fail or raise an acceptance failure. The former `check`/`diagnostic` methods and `CheckpointFailure` belong to the removed checkpoint-driving path, not the current recorder.

### Conventions

Definitions are separate from observations so report meaning cannot drift with incidental payload
assembly. JSON output is indented, key-sorted, UTF-8, and newline-terminated.

### Invariants And Boundaries

- Historical predecessor rule: a failed checkpoint was recorded before `CheckpointFailure` escaped. Both that exception and the check method are now removed; this module no longer enforces failure-before-raise.
- Diagnostic rows never count as acceptance proof.
- Report assembly provides the schema, scenario and containers, then overlays caller values; it is serialization support, not an acceptance verdict.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured or needed for this repository-owned evidence shape.

- Stable checkpoint meaning and observed evidence are separate records. [1]

### Repo-Internal References

- The current recorder holds supplied checkpoint and diagnostic containers and assembles a report; the former check/diagnostic/CheckpointFailure path is removed, not a retained acceptance check. [2]

### Cross-Repo References

No meaningful cross-repository reference applies.

- The report contract is wholly repository-owned. [3]
