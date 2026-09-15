# mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
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


## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

These same-repository owners preserve exact journal, pair, task and ref authority. The cache contributes no repair evidence and this module does not infer it from disk state.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Repair evidence is persisted at the exact failed-operation seam. | L150-L171 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| The durable reset identity contains the code/memory pair and exact contract hashes. | L174-L206 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| Preparation proves cancelled ownership, matching pair/task binding and exact reset state. | L209-L250 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| Operation and code/memory source authorities are revalidated. | L440-L452 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| The repair tuple contains the exact code candidate and memory-content commit. | L595-L614 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| The reset clears only the accepted closed pair/state and creates the waiting successor. | L617-L643 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| Publication requires unchanged integration refs, unmoved sources and accepted/reset contract bytes. | L348-L363 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| The actual code and memory source branches must remain at their recorded bases. | L694-L699 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## 260821-CLIVE-L1 Contract Hash Parity

Organizational completion reset now hashes the exact `contract_publication_text` that `write_contract` publishes. This keeps reset identity aligned with closeout finalization and prevents normalization/serialization drift between proof and the resulting file. It does not confer queue or closeout lifecycle ownership on organizational repair.

## 260821-CLIVE-L2 Current Contract

The current source seams include `OrganizationalRepairPublicationError`, `OrganizationalRepairState`, `classify_organizational_completion_repair`. Organizational completion and repair are canonical integration-journal transitions with exact candidate, ref, quality, and cancellation evidence. The queue may schedule a door candidate but does not own failure repair or reopening lifecycle state.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Reset publication failures retain exact expected/observed state. | L49-L75 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| Classification describes accepted, reset or conflicting contract state. | L92-L111 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |
| The public classifier uses the retained journal repair evidence. | L114-L123 | [mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py](mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py) |

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

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Reconciled two-commit repair identity, unchanged task/source/ref checks and deterministic reset publication; moved current reference sections before the preserved historical entries. Source SHA-256 `1d203a8eb3543c23ccea6f31fef3238bfc1022057a28823b2746c1fb2b467171`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the lock removal and the
  live door disposition are the frozen changes and the earlier entry records them. Re-checked the
  cited ranges (`record_…` `:150`, the evidence builder `:174`, `prepare_…` `:210`,
  `_require_operation_identity` `:442`, `_quality_repair_contract` `:621`): they hold. No wording
  changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` changed since
  the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit — the short task-publication lock was removed and the door
  disposition is now resolved live. Corrected the Logic sentence, the repair section and the
  2026-08-24 history wording to match. Verification metadata remains closeout-owned.
- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded exact repair-backed waiting-successor publication under the then-current task CAS. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion repair WAL and crash recovery.