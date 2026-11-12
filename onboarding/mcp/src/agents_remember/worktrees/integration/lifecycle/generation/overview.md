# Lifecycle Generation Construction And Resume

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle/generation/` |

## Governing Overview

[Parent overview](../overview.md)

## Purpose

This package constructs in-memory queued lifecycle candidates and resumes the exact retained generation. It separates fresh record construction from retrying accepted intent; the lifecycle store and coordinator own durable publication, generation selection and worker execution.

## Hot Path Summary

Use `creation.py` to build a queued record or snapshot integration authority from the closed-out code commit and, for external memory, the memory-content commit. Use `resume.py` to advance a retained generation's attempt while preserving its accepted input and mutation evidence.

## How It Is Built

`queued_operation_record` combines the worktree contract, operation input and candidate into a queued record. It carries candidate state, tree, task intent and fingerprint, derives the operation key and report path, and records the queue timestamp. Closeout records receive initial mutation evidence; integration records receive derived lifecycle dependencies. Construction itself does not persist or select the record.

`snapshot_integration_authority` requires a completed closeout with a code commit. It resolves integration targets, reads their current branch commits and compares those commits with the closed-out output commits. External memory additionally requires its repository and memory-content commit. The snapshot records the exact source refs and commits alongside the candidate output commits; it does not select a ledger commit into the generation. A replay request with source drift creates a conflict transaction for a leaf, but refuses that transaction for an atomic series.

`requeued_same_generation` returns a modified copy of the retained record. It increments the attempt, clears completion, failure, guidance and cancellation fields, and updates termination and mutation histories. Direct landing returns to running at `direct-preflight`. Other operations return to queued status, with the closeout recovery projection determining the phase when applicable.

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only namespace |
| `creation.py` | [creation.py.md](creation.py.md) | Queued candidate and integration authority construction |
| `resume.py` | [resume.py.md](resume.py.md) | Pure retained-generation resume transition |

## Invariants And Boundaries

- Constructor results are neither persisted nor selected generations. Store/CAS, initial certification selection, claims and detached launch remain outside this package.
- Resume preserves generation identity, task intent, immutable accepted input and retained same-generation evidence. When worker termination evidence is present, it must prove exit before resume; exited evidence is appended to the termination history.
- Only mutation legs in `reconciled-unchanged` state are archived into mutation history and reset to `pre-mutation`, clearing their before, observed and expected-output-tree fields. Proven output remains retained.
- A retained closeout with private preparation and no consumed claim resumes at `recovering-private-preparation`. A retained closeout with claim or recovery ownership resumes at `recovering-after-claim`; otherwise its phase is `queued`.
- Atomic series cannot recover source drift by opening a leaf replay-conflict worktree. The refusal directs recovery to orchestrator-owned block recovery or graph reshape.
- The configured source registry has no entries. The constructors and resume transition define source-owned records and transitions, without introducing a cross-repository protocol.

## Evidence

- Queued construction and exact integration snapshots retain separate responsibilities. [1]
- Resume preserves the accepted generation and mutation histories, requires exit when termination evidence is present, and delegates closeout phase selection to the recovery projection. [2]
- Integration generation authority follows the actual publication pair: the closed-out code commit and external memory-content commit, without selecting a ledger commit. [3]
