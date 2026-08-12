# mcp/src/agents_remember/worktrees/lifecycle_operation_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/lifecycle_operation_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate |  2026-08-12T17:53:40+02:00|
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
| Record and report locations are deterministic per enclosure and operation kind. | `operation_record_path`; `operation_report_path` | mcp/src/agents_remember/worktrees/lifecycle_operation_store.py:37-43 |
| Store mutation is locked, revalidated, transition-checked, and atomically published. | `LifecycleOperationStore` | mcp/src/agents_remember/worktrees/lifecycle_operation_store.py:45-162 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The store persists only one task enclosure's internal operation state. | `LifecycleOperationStore` | mcp/src/agents_remember/worktrees/lifecycle_operation_store.py:37-162 |

## Update History

- 2026-08-12T15:19+02:00 — Created for L23's validated durable lifecycle operation store; verification provenance remains closeout-owned.
