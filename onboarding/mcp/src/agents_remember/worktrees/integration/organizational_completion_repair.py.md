# mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e` |
| lastVerifiedCommitDate | 2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Owns the integration-journal repair transition after a final organizational quality-gate failure:
it validates the exact failed generation and repair evidence and publishes one deterministic
waiting successor from the claimed predecessor. Projection refresh records the scheduling effect
but never owns the repair lifecycle.

## Code Commentary

### Logic

`record_organizational_completion_repair` persists exact repair evidence at the gate-failure seam.
The evidence binds operation identity, contract/task refs, claimed door, sprint/candidate/master,
exact commits, and deterministic successor bytes. Preparation re-reads canonical journal and task
authority under the short task-publication lock, proves the failure and worker/commit state, then
publishes the exact waiting successor and projection effects.

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

## 260821-CLIVE Repair Successor Publication

Repair uses the short task-publication lock and the claimed door's task refs rather than a queue
binding or long integration lock. Failed organizational quality creates a fresh deterministic
waiting successor from the exact claimed predecessor and repair-journal timestamp. Operation state,
commits, refs, and repair evidence must still match; a claimed generation is never mutated into a
pseudo-cancelled door.


## PDLS Reconciliation

Organizational repair now validates typed failure payloads, exact candidate/commit binding, complete reset state, and idempotent publication through bounded helpers instead of one recursive repair function.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded exact repair-backed waiting-successor publication under task CAS. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion repair WAL and crash recovery.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
