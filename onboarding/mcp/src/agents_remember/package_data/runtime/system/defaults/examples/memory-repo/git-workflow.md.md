# git-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-24T14:31Z                           |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca` |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
| governingOverview      | `../../../../../../../../overview.md`       |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The memory-repo git-workflow example says it belongs in memory-layer `system/git-workflow.md`, captures the gated-branch landing flow + gates + merge convention + release flow, and uses placeholders for per-repo specifics. | `# Git Workflow Example`; `## The landing flow`; `## PR merge: prefer a merge commit over squash`; `## Commit and push quality gates`; `## Release And Changelog Convention` | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md:1-97 |
| The examples README documents that the memory layer owns this landing-flow file. | `## Memory Repo` | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md:19-36 |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## R39 Generic Landing Example

The default workflow separates deterministic hooks and PR checks from integrated acceptance:
leaf closeout accepts once, leaf integration reuses the commit, master integration accepts full
once, and pre-push never spends acceptance. Repositories point at their own adapter and make risk
thresholds part of the default accepted invocation.

## Update History

- 2026-08-14T11:25+02:00 — R39 curator: recorded generic exact-once landing cadence and adapter
  ownership. Verification remains closeout-owned.

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: repaired 2 table rows and 7 prose citations (9 citation items); scoped citation check now passes.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 whole-file citation that ran past the
  end of the example (the file is 97 lines). Corrected after reading the example end to end — the
  copy-to-`system/git-workflow.md` instruction cit:(["Copy or rename this file"], mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md:3-3),
  Spine cit:([`## Spine`], mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md:11-21),
  issue/PR table cit:([`## When you need an issue + PR`], mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md:22-30),
  landing flow and gates cit:([`## The landing flow`; `### Gates, in one line`], mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md:31-56),
  merge-commit convention cit:([`## PR merge: prefer a merge commit over squash`], mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md:57-67),
  quality gates cit:([`## Commit and push quality gates`], mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md:68-85),
  and release convention cit:([`## Release And Changelog Convention`], mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md:86-97) are all still present.

- 2026-07-24T14:31Z — 260718-CHATS-L5I CRAP/commit-gate curation: replaced the
  former optional CI/pre-push framing with one mandatory default repository
  wrapper at pre-commit, closeout-before-mutation, pre-push, and CI. CRAP at or
  above the configured threshold (30 by default) fails without a separate strict
  flag. Verification metadata remains pinned until the code commit.

- 2026-06-11T06:47+02:00: No content impact: the example's commit-gate line now says "the `c-12-closeout` skill worktree closeout preview first" instead of "/ direct-closeout preview first" (issue #62 worktree-only closeout); the starter structure this sidecar describes is unchanged.
- 2026-06-02T04:00+02:00: Updated after the example's landing flow clarified that `c-11-memory-carryover-from-branch` skill carryover (run against the merged spear) maps the ledger to the actual spear HEAD, including a PR merge commit even when nothing else needs carrying. `l-01-session-job-lifecycle` skill series, Sub-task C, mcp 1.1.0.
- 2026-06-02T03:30+02:00: Created the onboarding for the new memory-repo `git-workflow.md` example (PR-gated landing flow starter), shipped in MCP 1.0.2.
