# mcp/src/agents_remember/worktrees/modules/record_landing.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/modules/record_landing.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

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

The PR landing path forwards only the supplied landed code and memory-content commits into the shared `LandedIntegration` writer. It requests no ledger commit and cannot turn cache refresh into evidence that a remote landing occurred.

`record_landing_result(args)` cit:([`record_landing_result`], mcp/src/agents_remember/worktrees/modules/record_landing.py:58-142)
refuses unless the call is approved or a dry run
cit:(["recording a landing requires explicit developer approval"], mcp/src/agents_remember/worktrees/modules/record_landing.py:60-60),
loads the contract, and then short-circuits to `already-recorded` when the cell already records a
landed integration — `completed` or `checkpointed`
cit:(["already-recorded"], mcp/src/agents_remember/worktrees/modules/record_landing.py:76-76) —
so a repeat is idempotent rather than a second write.

It then requires the landed commit cit:(["requires landed_code_commit"], mcp/src/agents_remember/worktrees/modules/record_landing.py:93-93)
and resolves the branches that commit may legitimately have landed on. Both shapes occur: a master
integrates into its recorded source branch (the super branch), while a task whose branch was merged
straight to the protected default bypasses super entirely — which is what happened to
`ar/260831_lifecycle-owned-completion-relay`. `_landing_targets` cit:([`_landing_targets`], mcp/src/agents_remember/worktrees/modules/record_landing.py:32-46)
therefore returns the recorded `code_source_branch` plus `main` when it exists locally, keeping only
targets that are actually present.

The anti-fabrication check is an ancestry test against those targets
cit:(["not reachable from any landing target"], mcp/src/agents_remember/worktrees/modules/record_landing.py:105-105):
a commit that landed nowhere cannot set the cell. A `dry_run` reports `would-record` and writes
nothing cit:(["would-record"], mcp/src/agents_remember/worktrees/modules/record_landing.py:115-115).
The real path records `strategy=PR_STRATEGY` cit:([`PR_STRATEGY`], mcp/src/agents_remember/worktrees/modules/record_landing.py:29-29)
through the shared writer, so the cell says which route landed the work. Since 260831-LOCR-L30 the
call bundles its landed facts into the shared `LandedIntegration` record (the same record the local
routes build) and appends no `checkpoint` flag, so this route still records a final landing
cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66).

The result payload is built by `_identity_payload` cit:([`_identity_payload`], mcp/src/agents_remember/worktrees/modules/record_landing.py:49-55)
rather than by `status_payload`. That is deliberate: this operation has no worktree or provider state
to report, and avoiding the status payload keeps the operation callable and unit-testable without
bound worktree services.

### Conventions

The route label is a module constant, not a string literal at the call site, so the cell's value is
greppable and single-sourced.

Refusals raise `RuntimeError` with the corrective action in the message (pull the protected branch
locally, then record the commit it landed) instead of a bare failure.

### Boundaries Of The Recorded State (260831-LOCR-L30)

The `already-recorded` short-circuit covers **both** landing states:
`contract.integration_status in {"completed", "checkpointed"}`
cit:(["contract.integration_status in {\"completed\", \"checkpointed\"}"], mcp/src/agents_remember/worktrees/modules/record_landing.py:70-70),
and the summary branches on which one it found
cit:(["This contract already records a checkpointed integration"], mcp/src/agents_remember/worktrees/modules/record_landing.py:80-80).

The `checkpointed` half is not cosmetic. The full-record path below writes `completed` plus
`cleanup="pending"`, and that pending cleanup is exactly what `worktree_cleanup` requires before it
retires a branch; letting the pull-request route take it would have revoked the checkpoint's
guarantee that a series which landed while still open never becomes reclaimable. Completion stays
with `worktree_integrate`, which reaches it only once the series is genuinely terminal, so this route
still adds no `checkpoint` flag and offers no way to record a non-final landing — it simply declines
to overwrite one that is already recorded.

#### Invariants And Boundaries

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

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `record_landing_result` validates the recorded code landing and forwards the actual code/memory facts. | `record_landing_result` | mcp/src/agents_remember/worktrees/modules/record_landing.py:58-142 |

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared writer this route calls, and the cell it publishes. (`record_landed_integration`) | `record_landed_integration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66 |
| The local route that already recorded its own landing. (`_integrated_result`) | `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:574-607 |
| The `already-recorded` guard covers both landing states, so a checkpointed series is never upgraded into a reclaimable integration. (`contract.integration_status in {"completed", "checkpointed"}`) | n/a | [mcp/src/agents_remember/worktrees/modules/record_landing.py](mcp/src/agents_remember/worktrees/modules/record_landing.py) |
| The summary the checkpointed half returns, naming the still-open series and the route that completes it. (`This contract already records a checkpointed integration`) | n/a | [mcp/src/agents_remember/worktrees/modules/record_landing.py](mcp/src/agents_remember/worktrees/modules/record_landing.py) |
| Cleanup refuses until the cell this route sets reads completed. (`integration_status`) | `integration_status` | mcp/src/agents_remember/worktrees/modules/cleanup.py:677-677 |
| The dashboard PR probe whose `None`/`missing` polarity must not be read as "never landed". (`_pr_for`) | n/a | [mcp/src/agents_remember/worktrees/modules/landing.py](mcp/src/agents_remember/worktrees/modules/landing.py) |
| The MCP tool and payload that expose this operation. (`worktree_record_landing`) | `worktree_record_landing` | mcp/src/agents_remember/mcp/registration/closeout.py:201-224 |
| The application-layer entry point that confines the contract and builds the arguments. (`worktree_record_landing_tool`) | `worktree_record_landing_tool` | mcp/src/agents_remember/application/worktree_tools.py:498-531 |
| The PR landing-tail recording step in operator doctrine. (`worktree_record_landing`) | `worktree_record_landing` | system/git-workflow.md:50-50 |

## Cross-Repo References

The operation shells out to nothing. Its only external participant is the pull-request itself, which
is recorded rather than queried at decision time, so no live external boundary is cited here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=d37edafd5a2f8b43edc8d679e8b0e7a610101ba467b8373fa6400067dde477bb. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 6 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — No content impact: mechanical citation re-derivation after the
  260913-LCA-L8 change set added one import line to `worktrees/modules/cleanup.py`, shifting the
  `integration_status` refusal read from line 664 to 665. The anchor was re-read at
  `cleanup.py:665-665`, where `if contract.integration_status != "completed":` still sits; the cited
  construct and its meaning are unchanged.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:598-633. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T04:10+02:00 — 260831-LOCR-L30 follow-up: the `already-recorded` guard widened from
  `== "completed"` to `in {"completed", "checkpointed"}`, with a `checkpointed` summary variant.
  Recorded why: the full-record path writes `completed` + `cleanup="pending"`, the exact state
  `worktree_cleanup` requires, so taking it would have made an open checkpointed series reclaimable;
  completion stays on `worktree_integrate`. Replaced the former "keys on `completed` alone"
  boundary note. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T01:26:36+00:00: Generated citation repair: "requires landed_code_commit" repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:93-93. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:26:36+00:00: Generated citation repair: "not reachable from any landing target" repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:105-105. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:26:36+00:00: Generated citation repair: "would-record" repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: "requires landed_code_commit" repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:81-81. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: this route's call to the shared writer now
  bundles its landed facts into `LandedIntegration`; recorded that the route appends no `checkpoint`
  flag and still publishes a final claim, that its `already-recorded` guard is keyed on `completed`
  alone (so a `checkpointed` contract is not short-circuited), and re-derived every reference range
  shifted by the leaf. Verification metadata remains closeout-owned; no acceptance claim.
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
