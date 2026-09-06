# mcp/src/agents_remember/worktrees/modules/quality/execution/retained_reports.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/execution/retained_reports.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:15:01+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Builds and copies the bounded report population required by selected predecessor gates into the caller’s fresh candidate sandbox.

## Code Commentary

### Logic

`retained_report_inventory` first validates the selected execution. It considers frozen publication declarations whose producer gates precede the selected first gate, then visits only evidence and artifact members of the retained results. Every report path must be canonical and relative, declared for that result’s producer gate, within the declared file bound and equal to the original publication’s SHA-256/size inventory.

Repeated paths converge only when digest and size agree; conflicting producers refuse. The inventory is sorted, limited to 4,096 distinct paths and bounded by the sum of applicable frozen publication byte declarations. Large retained coverage files use their actual profile-declared allowance rather than a separate guessed transport cap.

`snapshot_retained_reports` returns directly for a first-gate execution. Otherwise it resolves every selected original path through the confined immutable-publication reader before creating a fresh destination. Each source read is bounded to its declared size plus one byte and its actual size/hash is checked before exclusive file creation. The caller’s existing sandbox lifecycle owns cleanup of any partial transport.

### Conventions

Use the supplied original publication for every source path. No current-pointer lookup, generation scan or unrelated report enters the copied population. Destination freshness and sandbox cleanup remain the caller’s responsibility.

### Invariants And Boundaries

- The selected result members and frozen producer declarations jointly define transport membership.
- Inventory metadata is insufficient without physical source reopening and bounded read verification.
- Matching repeated paths are deduplicated; conflicting bytes never overwrite an earlier member.
- This owner copies evidence; it does not accept gates, select a lifecycle generation or allocate Dagger authority.

### Todos

None recorded for this file's bounded responsibility.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Each member retains its original publication and exact declared file identity. | `RetainedReportFile` | mcp/src/agents_remember/worktrees/modules/quality/execution/retained_reports.py:22-34 |
| Inventory derives membership and byte bounds from frozen producer declarations. | `retained_report_inventory` | mcp/src/agents_remember/worktrees/modules/quality/execution/retained_reports.py:37-77 |
| All source paths are resolved before fresh exclusive transport writes. | `snapshot_retained_reports` | mcp/src/agents_remember/worktrees/modules/quality/execution/retained_reports.py:80-109 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |

## Update History

- 2026-09-06T15:15:01+00:00 — Created from the complete source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented the selected-original, terminal or transport responsibility and its actual neighboring owners. Source verification is not execution or acceptance evidence.
