# mcp/src/agents_remember/worktrees/modules/quality/closeout_memory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/closeout_memory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T18:42+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

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
| One phase builds the service-owned drift context, runs the exact check group, and refuses on a non-clean result with bounded evidence. | `run_memory_quality_phase`; `_failure_message` | mcp/src/agents_remember/worktrees/modules/quality/closeout_memory.py:17-53 |
| The combined result preserves both phase check maps, findings, counts, bounded report-only evidence, and declared phase membership. | `combine_memory_quality` | mcp/src/agents_remember/worktrees/modules/quality/closeout_memory.py:56-80 |
| Closeout runs the extracted pre-refresh adapter before the expensive code gate. | `_memory_quality_before_refresh` | mcp/src/agents_remember/worktrees/modules/closeout.py:641-658 |
| The sole external-phase owner runs memory refresh and returns its combined gate result. | "def external_closeout_commits("; "memory_quality = combine_memory_quality(" | mcp/src/agents_remember/worktrees/modules/closeout_external.py:61-112; mcp/src/agents_remember/worktrees/modules/closeout_external.py:132-160 |
| The injected service bundle owns the `MemoryQualityPort` implementation and check-group vocabulary. | `MemoryQualityPort`; `WorktreeServices` | mcp/src/agents_remember/worktrees/services.py:68-95; mcp/src/agents_remember/worktrees/services.py:140-152 |

## Cross-Repo References

No cross-repository interface is owned by this internal closeout helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-29T18:42+02:00 — Split the pre-code and post-refresh citation claims so each lifecycle
  boundary has unique, verifiable source provenance; the two-phase quality contract is unchanged.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.

- 2026-08-13T12:26+02:00 — L23 closeout-gate repair: created from the behavior-preserving
  extraction of external-memory phase execution, bounded failure formatting, and two-phase result
  composition out of `closeout.py`. The 1,200-line structural rail remains enforced; verification
  provenance remains closeout-owned.
