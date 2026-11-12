# mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Constructs queued lifecycle records and captures exact integration branch authority for the lifecycle coordinator.

## Code Commentary

### Logic

External-memory integration snapshots use `memory_content_commit` as the task output and compare its ancestry with the actual memory target tip. Both the integration authority and any replay-conflict transaction carry that content commit directly; neither needs a ledger pairing or ledger commit.

`queued_operation_record` carries the supplied candidate state/tree, task intent and fingerprint into the operation identity, report locator and queued state. Closeout records receive initial mutation evidence; integrate records bind their declared dependencies. `snapshot_integration_authority` requires a completed closeout code commit, reads the actual target branch tips and ancestry, and captures both sides for external memory. Replay drift creates a conflict transaction for leaves; atomic series refuse opening a leaf conflict worktree.

### Conventions

The queued constructor and integration snapshot were extracted from the coordinator without changing their core behavior. The snapshot reads repository authority; the constructor returns an in-memory record.

#### Invariants And Boundaries

- Returning a queued record does not persist it or select certification: the lifecycle/store composition owns atomic initial selection, predecessor archival, door publication and launch.
- External-memory integration requires the memory repository and exact accepted content commit.
- Exact source refs and candidate commits remain distinct; observed drift cannot be replaced with guessed branch state.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `queued_operation_record` retains accepted candidate/task identity and initializes kind-specific evidence. [1]
- `snapshot_integration_authority` captures actual code/memory target tips and accepted content outputs. [2]

- Queued records retain candidate/task identity and initialize kind-specific evidence. (`queued_operation_record`) [3]
- Integration authority is captured from completed output and current target refs, with explicit replay boundaries. (`snapshot_integration_authority`) [4]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No additional cross-repository evidence applies.
