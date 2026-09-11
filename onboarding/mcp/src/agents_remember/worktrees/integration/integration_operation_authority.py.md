# mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Re-proves that an integration landing output is the exact closeout candidate its contract recorded.

## Code Commentary

`require_authorized_integration_commits` proves the landing output equals the contract's recorded closeout commits and refuses a replay: conflict resolution must produce a new leaf closeout rather than reuse an older pair. The candidate commits are contract facts, so the proof reads the contract (`contract.code_commit`, `contract.memory_content_commit`, `contract.ledger_commit`) and never a journal record. The journaled operation admission and the stored source-tip authority this module once owned are deleted; the live source-tip refusal is now pure Git ancestry in `prepare_integration_ref_move`.

## Invariants And Boundaries

- A contract path alone is not integration authority.
- The contract's recorded closeout commit triple — code, memory content, ledger — is the immutable operation fact.
- Authorized outputs must equal the contract's recorded accepted candidate; no unrecorded replay result may land.
- Any mismatch fails closed; there is no journaled operation record left to consult or fall back to.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Operation admission is contract-bound, not journal-bound: the landing output is compared with the contract's recorded closeout commits. | `require_authorized_integration_commits` | mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py:9-31 |
| Source tips are revalidated immediately before protected movement at the prepared-move boundary, not in this module. | `prepare_integration_ref_move` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:101-164 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seam is `require_authorized_integration_commits`. Integration authority is contract-bound: the landing output is compared against the contract's recorded closeout commits and no journaled operation record is read. The moved-source refusal is pure Git ancestry in `prepare_integration_ref_move`.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `require_authorized_integration_commits` at this ownership boundary; the former `require_plane_integration_operation` and `require_current_integration_sources` seams are deleted. | `require_authorized_integration_commits` | mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py:9-31 |

## Update History
- 2026-09-11T23:05:00+00:00: Repaired three claims against the current source. The card claimed a journaled operation admission (`require_plane_integration_operation`) binding the requested key to one durable authority record and a stored source-tip revalidation (`require_current_integration_sources`); both functions are deleted, the module is now the 31-line `require_authorized_integration_commits` that compares the landing output with the contract's recorded closeout commits, and the moved-source refusal lives in the pure-Git replay requirements of `prepare_integration_ref_move`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created durable integration-operation proof onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
