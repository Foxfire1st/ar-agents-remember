# mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Provides proof, classification, and contract/door reset helpers for retained organizational integration journal records. Those helpers bind the failed generation and exact repair evidence to a deterministic waiting successor. Current ordinary integration runs in one synchronous call. Public control of a retained integration record returns the synchronous replacement before reconciliation.

## Code Commentary

### Logic

The evidence writer `record_organizational_completion_repair` binds the failed record to its operation and task identities, the claimed door's sprint/candidate/master refs, the code and memory-content commits, and the accepted and reset contract hashes. The current production integration route does not invoke this writer.

`OrganizationalRepairPublicationError`, `OrganizationalRepairState`, and `classify_organizational_completion_repair` inspect and report the retained reset evidence, classifying a contract and live door as `not-applicable`, `accepted`, `reset`, `reset-door-pending` (reset contract bytes on disk while the live closeout door is still `claimed`), or `developer-decision`.

Given an exact cancelled integration journal and accepted contract, `prepare_organizational_completion_repair` checks the named failure and ownership, compares the two commit values with integration authority, builds the reopened contract through `_quality_repair_contract` (clearing closed/integrated fields without writing a `closeout_door` attribute on `WorktreeContract`), and publishes the reset contract and deterministic waiting successor closeout door through `_publish_reset` and `_write_repair_door`. It checks unchanged integration refs and unmoved source branches before publication, prepares the successor waiting door before writing the reset contract, verifies the published reset bytes, and then publishes and verifies the successor door in the closeout door journal. If door publication is interrupted after the reset contract write, it raises a retryable `OrganizationalRepairPublicationError` (`organizational-completion-door-publication-interrupted`, `next_action="cancel"`) and classifies as `reset-door-pending`; retrying resumes through `_complete_pending_repair_door` until the waiting successor door is live. The current public handler refuses the integration kind before it can reach cancellation.

### Conventions

The helper reads the exact integration journal and canonical contract and task refs. Commit comparisons are two-tuples, while the separate sprint/candidate/master task binding is a three-part identity. `_contract_sha256` hashes the exact `contract_publication_text` that `write_contract` publishes, and Git refs plus serialized contract hashes govern drift detection and idempotent reset classification.

### Invariants And Boundaries

- The mutating repair owner accepts no caller-supplied lifecycle record.
- `prepare_organizational_completion_repair` requires an already-persisted durable cancelled integration journal (`status == "cancelled"`, `cancelRequested`, non-empty `finishedAt`).
- Only the exact failed final-leaf integration owner and accepted code/memory pair may reopen closeout.
- Repair refuses if the actual code or memory super moved after the failed operation.
- Cache bytes, ledger rows and a third ledger commit are absent from reset authority; code-only repair rejects any memory integration authority.
- Accepted/reset contract hashes and claimed-door successor identity remain exact and recoverable, including retry recovery of an interrupted successor door publication through `reset-door-pending`.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These same-repository owners preserve exact journal, pair, task and ref authority. The cache contributes no repair evidence and this module does not infer it from disk state.

- The legacy evidence writer binds repair evidence at the exact failed-operation seam. [1]
- Operation and code/memory source authorities are revalidated. [4]
- The repair tuple contains the exact code candidate and memory-content commit. [5]
- The actual code and memory source branches must remain at their recorded bases. [8]
- Reset publication failures retain exact expected/observed state. [9]
- The public classifier uses the retained journal repair evidence. [11]

- The durable reset identity records the code/memory pair and SHA-256 hashes of `contract_publication_text`. [2]
- Preparation proves cancelled ownership, matching pair/task binding, and exact reset state, or completes a pending waiting-door publication. [3]
- `_quality_repair_contract` clears only the accepted closed pair/state without setting `closeout_door` on `WorktreeContract`, while `_successor_repair_door` derives the waiting successor published to the door journal. [6]
- Publication requires unchanged integration refs and unmoved sources, writes exact reset contract bytes, and publishes the waiting successor door with typed interruption/conflict errors. [7]
- Classification describes `not-applicable`, `accepted`, `reset`, `reset-door-pending`, or `developer-decision` contract and door state. [10]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.
