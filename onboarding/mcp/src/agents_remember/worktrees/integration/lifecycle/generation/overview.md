# Lifecycle Generation Construction And Resume

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle/generation/` |

## Governing Overview

[Parent overview](../overview.md)

## What This Area Is

The constructors and retained-generation transition used by lifecycle coordination. It separates creating an in-memory queued candidate from requeuing accepted intent, while the existing store and coordinator retain durable publication and worker authority.

## Hot Path Summary

`creation.py` snapshots integration authority from code and memory-content output refs only. Generation identity, task intent and retained same-generation evidence remain mandatory; no ledger commit is selected into a new generation.

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

## Evidence

### Repo-Internal References

- Queued construction and exact integration snapshots retain separate responsibilities. [1]
- Resume fences termination and preserves the accepted generation and mutation histories. [2]

Current working-candidate evidence for this route:

- Integration generation authority follows the actual publication pair. [3]

### Docs And Cross-Repo References

The configured Domain Documentation registry has no entries. These source-owned models and transitions introduce no cross-repository protocol.
