# mcp/src/agents_remember/memory_quality/memory_census_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/memory_census_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T10:26:37+02:00 |
| lastVerifiedCommitHash | `2fa5e81f4da44a0a87f1a700c5363a9d563e7f9d` |
| lastVerifiedCommitDate | 2026-09-11T09:51:31+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Memory quality overview](overview.md)

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
| Scope capture is repository-owned and exact-tree based. | `capture_memory_census_scope` | mcp/src/agents_remember/memory_quality/memory_census_scope.py:107-140 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Code-input modes and pair-owned candidate fields are strict. | `MemoryCensusCodeInput` | mcp/src/agents_remember/memory_quality/memory_census_scope.py:25-52 |
| Scope identity exposes stable serialized and path-change observations. | `MemoryCensusScope` | mcp/src/agents_remember/memory_quality/memory_census_scope.py:69-104 |
| The route captures exact changes and refuses movement during the observation. | `capture_memory_census_scope`; `_diff` | mcp/src/agents_remember/memory_quality/memory_census_scope.py:107-140; mcp/src/agents_remember/memory_quality/memory_census_scope.py:249-286 |

## Cross-Repo References

None; the scope owner uses the local contract and pair authorities.

## Update History

- 2026-09-11T10:26:37+02:00 — Moved the mirrored sidecar from `mcp/src/agents_remember/worktrees/integration/closeout/memory_census_scope.py` to `mcp/src/agents_remember/memory_quality/memory_census_scope.py`. Relocated with the de-entanglement cut (commit `be517eec`, "relocate memory_census_scope into memory_quality"). Only the import block was reordered by the move; every cited anchor range was re-verified against the new path and is unchanged. Governing overview link repointed to the memory quality overview. Verification metadata refreshed to code commit `2fa5e81f4da44a0a87f1a700c5363a9d563e7f9d`.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent governed sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `22b06a4f685103bf7cc17d65975b520b61d72c125071a52f43b73cbdea0c47b0`). No future candidate verification stamp was used.
