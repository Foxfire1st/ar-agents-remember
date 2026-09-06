# Lifecycle Generation Construction And Resume

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle/generation/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T14:48:58+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Parent overview](../overview.md)

## What This Area Is

The constructors and retained-generation transition used by lifecycle coordination. It separates creating an in-memory queued candidate from requeuing accepted intent, while the existing store and coordinator retain durable publication and worker authority.

## Hot Path Summary

Use `creation.py` to build queued records or snapshot integration refs. Use `resume.py` when retrying the exact retained generation: termination proof and mutation history determine what can be reset.

## Local Invariants And Traps

- A constructor result is not a persisted or selected generation. Store/CAS, initial certification selection, claims and detached launch remain outside this package.
- Resume increments the attempt, preserves immutable accepted input and generation, and archives exited worker evidence.
- Only reconciled-unchanged mutation legs return to pre-mutation; proven output remains retained.
- Retained closeout claims resume at recovering-after-claim; direct landing resumes running at direct-preflight.
- Atomic series cannot recover source drift by opening a leaf replay-conflict worktree.

## File-Level Onboarding Map

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only namespace |
| `creation.py` | [creation.py.md](creation.py.md) | Queued candidate and integration authority construction |
| `resume.py` | [resume.py.md](resume.py.md) | Pure retained-generation resume transition |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Queued construction and exact integration snapshots retain separate responsibilities. | `queued_operation_record`; `snapshot_integration_authority` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71; mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:74-143 |
| Resume fences termination and preserves the accepted generation and mutation histories. | `requeued_same_generation` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py:14-63 |

## Docs And Cross-Repo References

The configured Domain Documentation registry has no entries. These source-owned models and transitions introduce no cross-repository protocol.

## Update History

- 2026-09-06T14:48:58+00:00 — Created this nearest route from source at `c69d5171187fa1957025e393270db9f5a864ab14`. Preserved domain/store authority outside the wire/transition package; source review is not gate or acceptance evidence.
