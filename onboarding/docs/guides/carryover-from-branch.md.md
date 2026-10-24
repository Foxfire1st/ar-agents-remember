# docs/guides/carryover-from-branch.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

Guide to selectively carrying richer converted onboarding after its code lands, through an open external-memory recovery leaf rather than a Git merge or direct official-checkout write.

## Code Commentary

Plan is read-only and writes no report. The recovery leaf starts from the landed pair with clean code at the selected official tip; both memory markers must have the same conversion version. Review the returned candidates before approval-gated apply. Replacement and review inclusion do not override target edits or differing held records.

File cards, route overviews, memory-only documents and the entity catalog are Markdown/JSON units. Their selection keys are respectively the source path, normalized route (`.` for root), memory-only path/route and literal `entity-catalog`. Differing overviews/catalogs need whole-unit review. Exact-landed evidence requires every source commit touching the path to be an official ancestor; matching patches or final bytes are the other proven tiers. Same-path overlap needs review and not-landed code is rejected. Every anchor is observed at official code; moved current anchors are re-recorded, while failed or stale observations need review. Memory-only auto-carry requires anchors all current and both target members unchanged since a resolvable memory merge base.

Missing records and their transitive links may accompany the units; different held records are not overwritten. Source history rows are reading aids, never imported answers. Apply regenerates indexes and validates the exact worktree against the leaf memory base and official code using `writer_reports`, restoring pre-apply bytes including existing edits on refusal. It commits nothing, has no `memory_commit_message` argument and refreshes no ledger cache. Retry skips equal writes, preserves differing uncommitted targets and validates the whole tree. `would-carryover` is the plan; `carried-into-worktree` is validated uncommitted content; `nothing-to-carryover` still validates. The curator authors its own rows; ordinary closeout makes the attributed gate-judged memory commit and integrates it. `carryover-pending` still holds cleanup/finalization until that publication.

The guide closes with `c-10-adopt-memory-baseline` and Adopt Existing Memory for the baseline, then links the kept `c-05-create-or-update-onboarding-files/workflows/memory-quality-control.md` procedure for `memory_quality_check`, `curator_coherence` and their tool-returned result/report paths.

## Evidence

### Repo-Internal References


- The source describes the current instructions summarized above. [1]


- Current source account and its stated boundaries. [2]
