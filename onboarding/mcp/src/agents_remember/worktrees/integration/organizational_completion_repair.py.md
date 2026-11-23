# mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Retains proof and reset helpers for organizational integration records written by the former journal route. Those helpers bind the failed generation and exact repair evidence to a deterministic waiting successor. Current ordinary integration runs in one synchronous call. Public control of a retained integration record returns the synchronous replacement before reconciliation.

## Code Commentary

### Logic

The legacy evidence writer `record_organizational_completion_repair` binds the failed record to its operation and task identities, the claimed door's sprint/candidate/master refs, the code and memory-content commits, and the accepted and reset contract hashes. The current production integration route does not invoke this writer.

Given an exact cancelled integration journal and accepted contract, the retained preparation helper checks the named failure and ownership, compares the two commit values with integration authority, and constructs the deterministic waiting successor. It checks unchanged integration refs and source branches before publication, which converges only on accepted or exact reset bytes. The current public handler refuses the integration kind before it can reach cancellation.

### Conventions

The retained helper reads the exact integration journal and canonical contract and task refs. Commit comparisons are two-tuples, while the separate sprint/candidate/master task binding is a three-part identity. Git refs and serialized contract hashes retain their original roles.

### Invariants And Boundaries

- The mutating repair owner accepts no caller-supplied lifecycle record.
- The older cancellation route persisted its cancelled journal before invoking the repair mutator.
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

- The legacy evidence writer binds repair evidence at the exact failed-operation seam. [1]
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

## 260821-CLIVE-L2 Retained Contract

The original integration-journal transition bound the exact candidate, refs, quality verdict and cancellation evidence. `OrganizationalRepairPublicationError`, `OrganizationalRepairState` and `classify_organizational_completion_repair` still read and report the retained reset evidence. This compatibility preserves journal history after synchronous integration replaced that public control path.

### Reconciled Source Evidence

- Reset publication failures retain exact expected/observed state. [9]
- Classification describes accepted, reset or conflicting contract state. [10]
- The public classifier uses the retained journal repair evidence. [11]

## 260821-CLIVE Repair Successor Publication

The older repair transition resolved the claimed door's task refs through `live_closeout_door`.
A failed organizational quality check created a deterministic waiting successor from the exact
claimed predecessor and repair-journal timestamp. Operation state, commits, refs and repair
evidence had to match. The original transition kept the claimed door intact.


## PDLS Reconciliation

Organizational repair now validates typed failure payloads, exact candidate/commit binding, complete reset state, and idempotent publication through bounded helpers instead of one recursive repair function.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
