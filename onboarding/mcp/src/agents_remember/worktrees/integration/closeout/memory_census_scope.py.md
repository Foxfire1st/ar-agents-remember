# mcp/src/agents_remember/worktrees/integration/closeout/memory_census_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/memory_census_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09 |
| lastVerifiedCommitHash | `8133b6a9de2f787cb6c4527621a70123357aff31` |
| lastVerifiedCommitDate | 2026-09-08T13:24:49+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Closeout integration overview](overview.md)

## Purpose

Captures the exact route-owned code and memory Git scope used by the structural memory census. It binds the canonical memory candidate pair, supports future-code and current-head modes, and records working, committed, and memory path changes without accepting them.

## Code Commentary

### Logic

`MemoryCensusCodeInput` validates the route mode and pair-owned code identities. `MemoryCensusScope` serializes the exact scope facts and exposes working, committed, and memory path projections. `capture_memory_census_scope` rechecks pair and memory-tree stability around the capture; `_diff` derives bounded Git path changes from exact trees.

### Invariants And Boundaries

- The route derives candidate identity from the admitted contract and does not accept a caller-selected future tree.
- Pair, contract, and memory-tree changes during capture fail closed.
- Scope capture supplies structural evidence only; it does not mint semantic repair or certification authority.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Scope capture is repository-owned and exact-tree based. | `capture_memory_census_scope` | mcp/src/agents_remember/worktrees/integration/closeout/memory_census_scope.py:107-140 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Code-input modes and pair-owned candidate fields are strict. | `MemoryCensusCodeInput` | mcp/src/agents_remember/worktrees/integration/closeout/memory_census_scope.py:25-52 |
| Scope identity exposes stable serialized and path-change observations. | `MemoryCensusScope` | mcp/src/agents_remember/worktrees/integration/closeout/memory_census_scope.py:69-104 |
| The route captures exact changes and refuses movement during the observation. | `capture_memory_census_scope`; `_diff` | mcp/src/agents_remember/worktrees/integration/closeout/memory_census_scope.py:107-140; mcp/src/agents_remember/worktrees/integration/closeout/memory_census_scope.py:249-286 |

## Cross-Repo References

None; the scope owner uses the local contract and pair authorities.

## Update History

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent governed sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `22b06a4f685103bf7cc17d65975b520b61d72c125071a52f43b73cbdea0c47b0`). No future candidate verification stamp was used.
