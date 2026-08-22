# mcp/src/agents_remember/worktrees/integration/lifecycle_operation_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

This file owns the single durable JSON record and self-overwriting Markdown status report for one task lifecycle operation. It is the validated, lock-protected compare-and-transition boundary used by both request handlers and detached workers.

## Code Commentary

### Logic

`LifecycleOperationStore` reads strict Pydantic records, creates them exclusively, and updates them under a filesystem lock. Every update revalidates the full model, checks immutable fields and legal state transitions, then atomically writes both the machine record and human report. Model validation and fill-only recovery preempt impossible leg-set and proven-commit rewrites; the store retains the identity, state, pre-command snapshot, observation, expected-tree, and phase-bound finalization checks that remain transition concerns.

Added `_validate_quality_certification_transition`, `_validate_queue_completion_transition`, and `_validate_organizational_repair_transition`; these fields are write-once and integrate-only.

### Conventions

Paths are derived from the worktree enclosure plus operation kind; timestamped operation artifacts are deliberately not created.

### Invariants And Boundaries

- Corrupt or extra fields fail closed.
- Operation input, key, fingerprint, and task identity cannot be replaced. Approval and closeout
  mutation/finalization evidence advance only through validated monotonic transitions.
- A terminal record cannot be replaced by a competing attempt.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this store.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs the internal durable record. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Record and report locations are deterministic per enclosure and operation kind. | `operation_record_path`; `operation_report_path` | mcp/src/agents_remember/worktrees/integration/lifecycle_operation_store.py:137-142 |
| Store mutation is locked, revalidated, transition-checked, and atomically published. | `LifecycleOperationStore` | mcp/src/agents_remember/worktrees/integration/lifecycle_operation_store.py:145-300 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The store persists only one task enclosure's internal operation state. | `LifecycleOperationStore` | mcp/src/agents_remember/worktrees/integration/lifecycle_operation_store.py:145-300 |

## L23 Lifecycle Model Package Review

Durable operation records and vocabularies now come from `models.lifecycles.operation`. Store
ownership, validation, atomic persistence, and compare-and-swap behavior are unchanged.

## 260815-DAG-L3 Explicit Detached Writer

The lifecycle-operation store now declares both MCP and the detached lifecycle-operation process
as writers and checks that declaration at its actual write choke point. The worker no longer
depends on undeclared-process tolerance to advance its own durable record.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L1 Strict Journal And Evidence

The store accepts only schema `3.0`; legacy records, extra fields, fallback readers, and runtime bypasses fail closed. Closeout transitions enforce monotonic mutation evidence, exact recovery projection, and exact finalized-contract hashes. Generation retention and cancellation are derived from mutation/finalization proof rather than phase or irreversible booleans. Publication remains lock-serialized and atomic at the file-record level; that does not make the external Git commit sequence atomic.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_store.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added immutable-transition validation for quality certification, queue completion, and organizational repair evidence. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: enforced the explicit detached lifecycle writer
  census at record publication; verification remains closeout-owned.
- 2026-08-14T06:36+02:00 — L23 final candidate review: validated store transitions persist exact
  candidate and recovery evidence monotonically, including restart-safe post-claim reconciliation.
  Verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: recorded the lifecycle-operation model import move and
  confirmed the durable-store contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23's validated durable lifecycle operation store; verification provenance remains closeout-owned.
