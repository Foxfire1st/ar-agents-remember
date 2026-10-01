# mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Owns the integration-journal repair transition after a final organizational quality-gate failure:
it validates the exact failed generation and repair evidence and publishes one deterministic
waiting successor from the claimed predecessor. Projection refresh records the scheduling effect
but never owns the repair lifecycle.

## Code Commentary

### Logic

`record_organizational_completion_repair` persists repair evidence for the exact failed integration generation. The record binds operation and contract/task identity, the claimed door's sprint/candidate/master refs, the code/memory-content commit pair, and exact accepted/reset contract hashes.

Preparation reloads the durable cancelled journal and accepted contract, validates the named failure and ownership, compares the two commit values with integration authority, and constructs the deterministic waiting successor. Before writing it, the owner proves unchanged integration refs and source branches. Publication converges only on the accepted or exact reset bytes; a third contract state refuses. Scheduling projections do not own this reset.

### Conventions

Use the current integration journal and canonical contract/task refs. Commit comparisons are two-tuples; the separate sprint/candidate/master task binding remains a three-part identity. Source Git refs and serialized contract hashes retain their original roles.

### Invariants And Boundaries

- The mutating repair owner accepts no caller-supplied lifecycle record.
- Cancellation persists its durable cancelled journal before invoking the repair mutator.
- Only the exact failed final-leaf integration owner and accepted code/memory pair may reopen closeout.
- Repair refuses if the actual code or memory super moved after the failed operation.
- Cache bytes, ledger rows and a third ledger commit are absent from reset authority; code-only repair rejects any memory integration authority.
- Accepted/reset contract hashes and claimed-door successor identity remain exact and recoverable.

### Todos

No additional source-local TODO is introduced by the two-output repair change.


## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These same-repository owners preserve exact journal, pair, task and ref authority. The cache contributes no repair evidence and this module does not infer it from disk state.

- Repair evidence is persisted at the exact failed-operation seam. [1]
- The durable reset identity contains the code/memory pair and exact contract hashes. [2]
- Preparation proves cancelled ownership, matching pair/task binding and exact reset state. [3]
- Operation and code/memory source authorities are revalidated. [4]
- The repair tuple contains the exact code candidate and memory-content commit. [5]
- The reset clears only the accepted closed pair/state and creates the waiting successor. [6]
- Publication requires unchanged integration refs, unmoved sources and accepted/reset contract bytes. [7]
- The actual code and memory source branches must remain at their recorded bases. [8]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.

## 260821-CLIVE-L1 Contract Hash Parity

Organizational completion reset now hashes the exact `contract_publication_text` that `write_contract` publishes. This keeps reset identity aligned with closeout finalization and prevents normalization/serialization drift between proof and the resulting file. It does not confer queue or closeout lifecycle ownership on organizational repair.

## 260821-CLIVE-L2 Current Contract

The current source seams include `OrganizationalRepairPublicationError`, `OrganizationalRepairState`, `classify_organizational_completion_repair`. Organizational completion and repair are canonical integration-journal transitions with exact candidate, ref, quality, and cancellation evidence. The queue may schedule a door candidate but does not own failure repair or reopening lifecycle state.

### Reconciled Source Evidence

- Reset publication failures retain exact expected/observed state. [9]
- Classification describes accepted, reset or conflicting contract state. [10]
- The public classifier uses the retained journal repair evidence. [11]

## 260821-CLIVE Repair Successor Publication

Repair resolves the claimed door's task refs live through `live_closeout_door` rather than a queue
binding or long integration lock; the short task-publication lock was removed from this route. Failed organizational quality creates a fresh deterministic
waiting successor from the exact claimed predecessor and repair-journal timestamp. Operation state,
commits, refs, and repair evidence must still match; a claimed generation is never mutated into a
pseudo-cancelled door.


## PDLS Reconciliation

Organizational repair now validates typed failure payloads, exact candidate/commit binding, complete reset state, and idempotent publication through bounded helpers instead of one recursive repair function.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
