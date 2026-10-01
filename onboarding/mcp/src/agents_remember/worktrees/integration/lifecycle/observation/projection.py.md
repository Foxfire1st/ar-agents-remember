# mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py

## Governing Overview

[worktree integration overview](../../overview.md)

## Purpose

Owns read-only lifecycle-journal observation across closeout, integration, and direct landing. It
turns exact retained records and contract/location failures into total public projections without
acquiring mutation, queue, or lifecycle-evidence authority.

## Code Commentary

### Logic

`observe_operation`, `latest_operation_projection`, and `current_operation_projections` locate and
read the stable enclosure-root journals, project every actionable sibling, and surface typed read
or location decisions. `unreadable_contract_operation_projections` retains exact-path journal
visibility when the task contract is unreadable while deliberately exposing no unsafe controls.
The final read pass reconciles observable worker exit and proven closeout mutations into a derived
projection; it does not rewrite the journal.

### Conventions

Aggregate readers remain total across damaged pre-locator state. Task-addressed tools retain the
precise repair refusal, while broad status projection returns no unsafe guess. Imports that would
create a projection cycle stay local to the read helper.

### Invariants And Boundaries

- Observation never writes journals, task documents, doors, queues, Git refs, or contracts.
- Mutable task status cannot hide an actionable journal sibling.
- An unreadable contract preserves exact retained evidence but yields zero legal controls unless
  authority can be re-established.
- Queue rows are schedulability projection only and never become lifecycle evidence here.
- Mutation and recovery facts are derived from exact journal/Git evidence, not inferred from prose.

### Todos

None recorded.

## Evidence

### Docs References

No configured external Domain Documentation source governs this repository-internal projection.

### Repo-Internal References

The source defines the total observation and degraded-projection contract.

- Single/latest/all readers project retained journals and keep task status from hiding siblings. [1]
- Location contradictions and unreadable contracts become bounded developer-decision projections with no controls. [2]
- Worker exit and closeout mutation recovery are reconciled into read-only derived records. [3]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.


## 260831-CCR-L15 Observed Operation Projection

`observed_operation_projection` projects one exact durable journal read through the
shared status pipeline: `_project_observed_record` performs only read-only
reconciliation, then `operation_projection` renders the envelope. CCR-R18/R15: a
status-change wait snapshot must be the same coherent envelope a task status read returns for the
exact record whose durable meaningful revision the waiter compared, so the returned cursor and
envelope never splice facts from different journal revisions.

- The read-only wait snapshot projection entry point. [4]
The application wait controller named here was deleted with the door/operation plane (commit `41b0812e`); this projection now has no public wait caller.
