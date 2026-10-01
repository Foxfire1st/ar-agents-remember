# git-workflow.md

## Governing Overview

[mcp overview](../../../../../../../../overview.md)

## Purpose

This example is the git-workflow starter for a memory layer whose code repository lands changes
through a gated branch (e.g. a PR-gated `main`).

## Code Commentary

### Logic

The file tells users to copy the example to memory-layer `system/git-workflow.md` and fill in the
`<placeholders>` for their repo. It states the spine (spear branch + whether it is gated; `feat/`|
`fix/` work branches; whether work is worktree-backed), an issue/PR policy table, a generic landing
flow (issue → branch → worktree → leaf closeout gate → push→PR→checks→merge→cleanup
→ `c-11-memory-carryover-from-branch` skill carryover run against the merged spear, which maps the ledger to the actual spear HEAD
including a PR merge commit even when nothing else needs carrying), a "prefer merge commit over
squash" rule for branches that bundle distinct changes, and the altitude-owned quality cadence:
deterministic local checks, targeted acceptance once at leaf closeout, no leaf-integration rerun,
full acceptance once at master integration, and deterministic pull-request validation without an
ordinary-push duplicate. The file also carries an optional release/changelog convention (tag
scheme, version-bump locations, release commit subject, PR-gated end-to-end flow).

### Conventions

Repo-specific landing and release guidance belongs here, not in coordinator tools; the coordinator
only routes "read `git-workflow.md` when present." PR-gating and the spear branch differ per repo, so
the example uses `<placeholders>` rather than hardcoded values.

### Invariants And Boundaries

The example is a starter, not a normative rule: a repo adopts it by copying and filling it in. It
points at `tools.md` for the quality wrapper itself rather than duplicating it. If a version is
asserted dynamically in tests, the example notes it must stay dynamic (not a bump location).

### Todos

None.

### Docs References

No external documentation is needed.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The memory-repo git-workflow example says it belongs in memory-layer `system/git-workflow.md`, captures the gated-branch landing flow + gates + merge convention + release flow, and uses placeholders for per-repo specifics. [1]
- The examples README documents that the memory layer owns this landing-flow file. [2]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.

## R39 Generic Landing Example

The default workflow separates deterministic hooks and PR checks from integrated acceptance:
leaf closeout accepts once, leaf integration reuses the commit, master integration accepts full
once, and pre-push never spends acceptance. Repositories point at their own adapter and make risk
thresholds part of the default accepted invocation.
