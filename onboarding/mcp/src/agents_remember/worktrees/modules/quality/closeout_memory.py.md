# mcp/src/agents_remember/worktrees/modules/quality/closeout_memory.py

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

### Conventions

The injected service declares phase membership; the adapter only passes those check groups and
combines returned evidence. Its caller runs the code-quality gate before memory preflight.

### Invariants And Boundaries

- This module owns memory-quality execution and result composition, not commit, ledger, approval,
  source-lineage, or metadata-refresh ordering. Those irreversible boundaries remain in
  the closeout coordinator and external-memory commit owner.
- A failed quality result raises; it is never converted into a warning or fallback path.
- Check membership comes from `MemoryQualityPort.check_groups()`. Do not duplicate the configured
  citation/style split here.
- The pre-refresh unstamped commit is comparison context only. Real verification hashes remain
  closeout-owned after the code commit exists.
- Bounded exception evidence must not replace or truncate the full service result returned after a
  successful closeout.

### Todos

The coordinator helper's docstring still says memory preflight precedes the expensive code gate;
the executable `_closeout_quality_preflight` caller enforces the opposite order. Source correction
belongs to implementation work; this card follows the caller's actual order.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository-local closeout adapter.

No relevant external documentation is configured.

### Repo-Internal References

- One phase builds the service-owned drift context, runs the exact check group, and refuses on a non-clean result with bounded evidence. [1]
- The combined result preserves both phase check maps, findings, counts, bounded report-only evidence, and declared phase membership. [2]
- The module owns both memory-quality phases as standalone callers: `run_memory_quality_phase` runs one declared check group and refuses with bounded evidence, and the closeout transaction no longer invokes a code gate or a memory preflight. [3]
- The external-memory commit owner runs the refresh and the memory/ledger commits; it no longer combines a memory-quality gate result. [4]
- The memory-quality port declares drift context, check groups and quality execution. [5]
- The injected service bundle keeps memory quality and certification continuation as distinct ports. [6]

### Cross-Repo References

No cross-repository interface is owned by this internal closeout helper.

No applicable cross-repository source was found.
