# mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Owns the integration-journal repair transition after a final organizational quality-gate failure:
it validates the exact failed generation and repair evidence, retires the scheduling candidate,
and reopens only that leaf's closeout. Queue projection records the scheduling consequence but does
not own the repair lifecycle.

## Code Commentary

### Logic

`record_organizational_completion_repair` persists the exact reset generation at the gate-failure seam together with the terminal failure. `organizational_completion_repair_evidence` binds operation identity, contract/task identity, sprint/candidate/master documents, exact code/memory/ledger commits, and the SHA-256 of the only permitted reset contract. `prepare_organizational_completion_repair` reloads the canonical cancelled `integrate` WAL and requires `cancelled`, `cancelRequested`, and `finishedAt` before validating the failure result, repair evidence, operation identity, integration authority, queue binding, and commit tuple; then it retires the candidate and publishes the reset contract.

### Invariants And Boundaries

- The mutating repair owner accepts no caller-supplied lifecycle record.
- Cancellation persists the cancelled WAL before invoking the repair mutator.
- Only the exact failed final-leaf integration owner may reopen the closeout.
- Repair refuses if the code or memory super moved after the failed gate.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reset generation is persisted at the exact gate-failure seam. | `record_organizational_completion_repair` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:136-157 |
| Durable exact reset identity is built before first publication. | `organizational_completion_repair_evidence` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:160-189 |
| Failed candidate is retired and only its leaf closeout reopened. | `prepare_organizational_completion_repair` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:192-261 |
| Operation identity and code/memory integration authority are re-validated. | `_require_operation_identity` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:340-413 |
| Reset contract clears the closed leaf back to not-started. | `_quality_repair_contract` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:477-530 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L1 Contract Hash Parity

Organizational completion reset now hashes the exact `contract_publication_text` that `write_contract` publishes. This keeps reset identity aligned with closeout finalization and prevents normalization/serialization drift between proof and the resulting file. It does not confer queue or closeout lifecycle ownership on organizational repair.

## 260821-CLIVE-L2 Current Contract

The current source seams include `OrganizationalRepairPublicationError`, `OrganizationalRepairState`, `classify_organizational_completion_repair`. Organizational completion and repair are canonical integration-journal transitions with exact candidate, ref, quality, and cancellation evidence. The queue may schedule a door candidate but does not own failure repair or reopening lifecycle state.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `OrganizationalRepairPublicationError`, `OrganizationalRepairState`, `classify_organizational_completion_repair` at this ownership boundary. | L47-L73; L77-L95; L98-L107 | `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion repair WAL and crash recovery.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
