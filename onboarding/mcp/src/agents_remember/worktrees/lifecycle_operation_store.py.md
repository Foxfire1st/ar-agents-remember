# mcp/src/agents_remember/worktrees/lifecycle_operation_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/lifecycle_operation_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash |  `17987fa66a642306eb8d20fa9a4bff2b881550d2`|
| lastVerifiedCommitDate |  2026-08-15T14:36:30+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

This file owns the single durable JSON record and self-overwriting Markdown status report for one task lifecycle operation. It is the validated, lock-protected compare-and-transition boundary used by both request handlers and detached workers.

## Code Commentary

### Logic

`LifecycleOperationStore` reads strict Pydantic records, creates them exclusively, and updates them under a filesystem lock. Every update revalidates the full model, checks immutable fields and legal state transitions, then atomically writes both the machine record and human report.

### Conventions

Paths are derived from the worktree enclosure plus operation kind; timestamped operation artifacts are deliberately not created.

### Invariants And Boundaries

- Corrupt or extra fields fail closed.
- Operation input, key, fingerprint, task identity, and irreversible/approval claims cannot move backward or be replaced.
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
| Record and report locations are deterministic per enclosure and operation kind. | `operation_record_path`; `operation_report_path` | mcp/src/agents_remember/worktrees/lifecycle_operation_store.py:53-54; mcp/src/agents_remember/worktrees/lifecycle_operation_store.py:57-58 |
| Store mutation is locked, revalidated, transition-checked, and atomically published. | `LifecycleOperationStore` | mcp/src/agents_remember/worktrees/lifecycle_operation_store.py:45-162 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The store persists only one task enclosure's internal operation state. | `LifecycleOperationStore` | mcp/src/agents_remember/worktrees/lifecycle_operation_store.py:37-162 |

## L23 Lifecycle Model Package Review

Durable operation records and vocabularies now come from `models.lifecycles.operation`. Store
ownership, validation, atomic persistence, and compare-and-swap behavior are unchanged.

## 260815-DAG-L3 Explicit Detached Writer

The lifecycle-operation store now declares both MCP and the detached lifecycle-operation process
as writers and checks that declaration at its actual write choke point. The worker no longer
depends on undeclared-process tolerance to advance its own durable record.

## Update History

- 2026-08-15T09:10+02:00 — L3 content update: enforced the explicit detached lifecycle writer
  census at record publication; verification remains closeout-owned.
- 2026-08-14T06:36+02:00 — L23 final candidate review: validated store transitions persist exact
  candidate and recovery evidence monotonically, including restart-safe post-claim reconciliation.
  Verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: recorded the lifecycle-operation model import move and
  confirmed the durable-store contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23's validated durable lifecycle operation store; verification provenance remains closeout-owned.
