# mcp/src/agents_remember/worktrees/modules/record_landing.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/modules/record_landing.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-12T00:33+02:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktrees/modules/overview.md](overview.md)

## Purpose

The **pull-request landing route**: record a landing the remote already performed.
`worktree_integrate` lands code by moving refs locally and then records what it moved; when the code
landed through a pull request, AR moved nothing, because `gh pr merge` did. Until this route existed
the contract's `integration` cell stayed `not-started` for every PR landing — and that was not
cosmetic, because the cell is what `worktree_cleanup` requires before it retires a branch and what
the series abandon guard reads before it lets a master's integration branch go. A PR-merged master
therefore looked exactly like a master whose work had never left it.

It is `worktree_record_landing`'s domain half, reached through the MCP tool of that name.

## Code Commentary

### Logic

`record_landing_result(args)` cit:([`record_landing_result`], mcp/src/agents_remember/worktrees/modules/record_landing.py:55-126)
refuses unless the call is approved or a dry run
cit:(["recording a landing requires explicit developer approval"], mcp/src/agents_remember/worktrees/modules/record_landing.py:57-57),
loads the contract, and then short-circuits to `already-recorded` when the cell already reads
completed cit:(["already-recorded"], mcp/src/agents_remember/worktrees/modules/record_landing.py:66-66) —
so a repeat is idempotent rather than a second write.

It then requires the landed commit cit:(["requires landed_code_commit"], mcp/src/agents_remember/worktrees/modules/record_landing.py:78-78)
and resolves the branches that commit may legitimately have landed on. Both shapes occur: a master
integrates into its recorded source branch (the super branch), while a task whose branch was merged
straight to the protected default bypasses super entirely — which is what happened to
`ar/260831_lifecycle-owned-completion-relay`. `_landing_targets` cit:([`_landing_targets`], mcp/src/agents_remember/worktrees/modules/record_landing.py:29-43)
therefore returns the recorded `code_source_branch` plus `main` when it exists locally, keeping only
targets that are actually present.

The anti-fabrication check is an ancestry test against those targets
cit:(["not reachable from any landing target"], mcp/src/agents_remember/worktrees/modules/record_landing.py:90-90):
a commit that landed nowhere cannot set the cell. A `dry_run` reports `would-record` and writes
nothing cit:(["would-record"], mcp/src/agents_remember/worktrees/modules/record_landing.py:100-100).
The real path records `strategy=PR_STRATEGY` cit:([`PR_STRATEGY`], mcp/src/agents_remember/worktrees/modules/record_landing.py:26-26)
through the shared writer, so the cell says which route landed the work
cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:27-48).

The result payload is built by `_identity_payload` cit:([`_identity_payload`], mcp/src/agents_remember/worktrees/modules/record_landing.py:46-52)
rather than by `status_payload`. That is deliberate: this operation has no worktree or provider state
to report, and avoiding the status payload keeps the operation callable and unit-testable without
bound worktree services.

### Conventions

The route label is a module constant, not a string literal at the call site, so the cell's value is
greppable and single-sourced.

Refusals raise `RuntimeError` with the corrective action in the message (pull the protected branch
locally, then record the commit it landed) instead of a bare failure.

### Invariants And Boundaries

- **Never probe `gh`.** Inferring the PR route after the fact would put the network in front of a
  guard that authorizes branch deletion. Recording happens where `gh` necessarily exists — the PR
  tail — and the decision stays offline.
- **`unknown` must never mean "never landed".** The dashboard projection at
  `worktrees/modules/landing.py` returns `None` when `gh` is absent, unauthed, or errored; that
  polarity is correct for a dashboard and would be dangerous as a deletion gate.
- **It must not become a second writer.** All cell writes go through `landing_record`.
- **It does not move refs, carry memory, or push.** Carryover is C-11's, separately guarded by
  cleanup.

### Todos

None. A standalone PR-tail recording step is required operator doctrine, and it is named as step 8
of the landing flow in the repo's `system/git-workflow.md`.

## Docs References

No external Domain Documentation source is configured for this memory repo; these are
repository-internal git and contract semantics, so the retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared writer this route calls, and the cell it publishes. | `record_landed_integration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:27-48 |
| The local route that already recorded its own landing. | "record_landed_integration(" | mcp/src/agents_remember/worktrees/modules/integrate.py:376-376 |
| Cleanup refuses until the cell this route sets reads completed. | `integration_status` | mcp/src/agents_remember/worktrees/modules/cleanup.py:664-664 |
| The dashboard PR probe whose `None`/`missing` polarity must not be read as "never landed". | `_pr_for` | mcp/src/agents_remember/worktrees/modules/landing.py:93-150 |
| The MCP tool and payload that expose this operation. | `worktree_record_landing` | mcp/src/agents_remember/mcp/registration/closeout.py:179-204 |
| The application-layer entry point that confines the contract and builds the arguments. | `worktree_record_landing_tool` | mcp/src/agents_remember/application/worktree_tools.py:427-461 |
| The PR landing-tail recording step in operator doctrine. | `worktree_record_landing` | system/git-workflow.md:48-56 |

## Cross-Repo References

The operation shells out to nothing. Its only external participant is the pull-request itself, which
is recorded rather than queried at decision time, so no live external boundary is cited here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-11T23:05:00+00:00: Five claims failed provenance: the bare `"state"` quote anchor matched three `state` cells, `record_landed_integration` resolved at both the import and the call site, `integration_status != "completed"` was a backticked expression rather than an anchor, and the operator-doctrine row carried a range-less memory path. Each claim now anchors text that occurs exactly once in its cited source — `"already-recorded"`, `"would-record"`, the call `record_landed_integration(` in `integrate.py`, the `integration_status` identifier at the cleanup refusal — and the doctrine row cites `system/git-workflow.md:48-56`, the step-8 "Record the landing" block that names `worktree_record_landing`. Claim intent unchanged; the anchor forms are narrower and the doctrine citation is now a real repo-relative range in this memory repo.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_record_landing` repointed to mcp/src/agents_remember/mcp/registration/closeout.py:179-204. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_record_landing_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:427-461. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "requires landed_code_commit" repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:78-78. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "not reachable from any landing target" repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:90-90. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-12T00:33+02:00 — Created by the LOCR-L29 curator pass. Documents the new pull-request
  landing route: the both-shapes landing-target resolution, the ancestry refusal that prevents the
  cell being set from a commit that landed nowhere, the deliberate offline stance (it never probes
  `gh`), and why its payload is built without `status_payload`. Verification metadata is pinned to the
  leaf base commit and remains closeout-owned.
