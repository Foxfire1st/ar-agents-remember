# Lifecycle Generation Construction And Resume

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle/generation/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| governingOverview | `../overview.md` |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Queued construction and exact integration snapshots retain separate responsibilities. | `queued_operation_record`; `snapshot_integration_authority` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71; mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:74-137 |
| Resume fences termination and preserves the accepted generation and mutation histories. | `requeued_same_generation` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py:14-58 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Integration generation authority follows the actual publication pair. | `snapshot_integration_authority` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:74-137 |

## Docs And Cross-Repo References

The configured Domain Documentation registry has no entries. These source-owned models and transitions introduce no cross-repository protocol.

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): clamped mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:74-138 to mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:74-137, the range the cited construct now occupies
- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Documented integration generation construction without a ledger authority cell. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-06T22:41:21+00:00: Generated citation repair: `requeued_same_generation` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py:14-58. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T14:48:58+00:00 — Created this nearest route from source at `c69d5171187fa1957025e393270db9f5a864ab14`. Preserved domain/store authority outside the wire/transition package; source review is not gate or acceptance evidence.
