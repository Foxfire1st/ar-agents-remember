# git-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T03:30+02:00                     |
| lastVerifiedCommitHash | `a69b72e101d09423601916c03d4f59ecdee7dda6` |
| lastVerifiedCommitDate | 2026-06-11T11:08:18+02:00|

## Purpose

This example is the git-workflow starter for a memory layer whose code repository lands changes
through a gated branch (e.g. a PR-gated `main`).

## Code Commentary

### Logic

The file tells users to copy the example to memory-layer `system/git-workflow.md` and fill in the
`<placeholders>` for their repo. It states the spine (spear branch + whether it is gated; `feat/`|
`fix/` work branches; whether work is worktree-backed), an issue/PR policy table, a generic landing
flow (issue → branch → worktree → commit gate → push gate → agent owns push→PR→checks→merge→cleanup
→ `c-11-memory-carryover-from-branch` skill carryover run against the merged spear, which maps the ledger to the actual spear HEAD
including a PR merge commit even when nothing else needs carrying), a "prefer merge commit over
squash" rule for branches that bundle distinct changes, the optional CI + local pre-push quality
gate, and an optional release/changelog convention (tag scheme, version-bump locations, release
commit subject, PR-gated end-to-end flow).

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The memory-repo git-workflow example says it belongs in memory-layer `system/git-workflow.md`, captures the gated-branch landing flow + gates + merge convention + release flow, and uses placeholders for per-repo specifics. | L1-L120 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md) |
| The examples README documents that the memory layer owns this landing-flow file. | n/a | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-11T06:47+02:00: No content impact: the example's commit-gate line now says "the `c-12-closeout` skill worktree closeout preview first" instead of "/ direct-closeout preview first" (issue #62 worktree-only closeout); the starter structure this sidecar describes is unchanged.
- 2026-06-02T04:00+02:00: Updated after the example's landing flow clarified that `c-11-memory-carryover-from-branch` skill carryover (run against the merged spear) maps the ledger to the actual spear HEAD, including a PR merge commit even when nothing else needs carrying. `l-01-session-job-lifecycle` skill series, Sub-task C, mcp 1.1.0.
- 2026-06-02T03:30+02:00: Created the onboarding for the new memory-repo `git-workflow.md` example (PR-gated landing flow starter), shipped in MCP 1.0.2.
