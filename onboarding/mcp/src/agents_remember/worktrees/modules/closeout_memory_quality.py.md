# mcp/src/agents_remember/worktrees/modules/closeout_memory_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/closeout_memory_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T12:26+02:00 |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd` |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

Owns the external-memory quality phase adapter used by worktree closeout. The module was extracted
from `closeout.py` so the coordinator remains below the repository's 1,200-line structural rail;
the extraction preserves the same fail-closed checks and the same before/after phase result.

## Code Commentary

### Logic

`run_memory_quality_phase` asks the injected `MemoryQualityPort` for a drift context rooted at the
active code checkout, runs exactly the supplied check group against the resolved onboarding root,
and raises a bounded, actionable failure when `ok` is false. An optional
`unstamped_code_commit` lets the pre-refresh citation phase compare a dirty leaf against its real
base without fabricating closeout provenance. The formatter includes at most the first five
findings in the exception while the full quality result remains owned by the quality service.

`combine_memory_quality` joins the pre-refresh and post-refresh results into the one closeout gate
reported to callers. It merges check maps and findings, sums ordinary and report-only counts,
bounds the combined report-only sample to 50 rows, and records the service-declared check groups in
`closeoutPhases`. The pre-refresh result may be empty for memory modes or check configurations that
do not require that phase; the post-refresh result is required.

### Invariants And Boundaries

- This module owns memory-quality execution and result composition, not commit, ledger, approval,
  source-lineage, or metadata-refresh ordering. Those irreversible boundaries remain in
  `closeout.py`.
- A failed quality result raises; it is never converted into a warning or fallback path.
- Check membership comes from `MemoryQualityPort.check_groups()`. Do not duplicate the configured
  citation/style split here.
- The pre-refresh unstamped commit is comparison context only. Real verification hashes remain
  closeout-owned after the code commit exists.
- Bounded exception evidence must not replace or truncate the full service result returned after a
  successful closeout.

## Docs References

No external Domain Documentation source is configured for this repository-local closeout adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One phase builds the service-owned drift context, runs the exact check group, and refuses on a non-clean result with bounded evidence. | `run_memory_quality_phase`; `_failure_message` | mcp/src/agents_remember/worktrees/modules/closeout_memory_quality.py:17-53 |
| The combined result preserves both phase check maps, findings, counts, bounded report-only evidence, and declared phase membership. | `combine_memory_quality` | mcp/src/agents_remember/worktrees/modules/closeout_memory_quality.py:56-80 |
| Closeout calls the extracted adapter before the expensive code gate and again after metadata refresh, then returns the combined gate result. | `_memory_quality_before_refresh`; `_external_closeout_commits` | mcp/src/agents_remember/worktrees/modules/closeout.py:657-751; mcp/src/agents_remember/worktrees/modules/closeout.py:838-847 |
| The injected service bundle owns the `MemoryQualityPort` implementation and check-group vocabulary. | `MemoryQualityPort`; `WorktreeServices` | mcp/src/agents_remember/worktrees/services.py:68-95; mcp/src/agents_remember/worktrees/services.py:140-152 |

## Cross-Repo References

No cross-repository interface is owned by this internal closeout helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-13T12:26+02:00 — L23 closeout-gate repair: created from the behavior-preserving
  extraction of external-memory phase execution, bounded failure formatting, and two-phase result
  composition out of `closeout.py`. The 1,200-line structural rail remains enforced; verification
  provenance remains closeout-owned.
