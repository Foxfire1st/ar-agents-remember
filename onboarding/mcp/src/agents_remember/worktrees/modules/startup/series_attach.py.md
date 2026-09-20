# mcp/src/agents_remember/worktrees/modules/startup/series_attach.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/worktrees/modules/startup/series_attach.py` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

The attach-side resume of a live atomic series, or the refusal that names what actually blocks
it. `series_attach_result(contract)` is the whole module.

**This module adds no behaviour.** It is `_attach_series_result`, moved verbatim out of
`start.py` under the new name and no other change, so that the file it came from stays under the
size rail; `start.py` now imports it and calls it from `attach_result`'s series branch
(`start.py:174-175`). The card exists because the module is a governed artifact, not because the
route learned anything: every state, message and payload field below is the one `start.py`
already emitted.

## Code Commentary

### Logic

A series has no workbench of its own — its work runs in child leaves — so attaching to one means
proving its integration branch is still live and addressable rather than handing back a checkout.
The helper starts from `status_payload(contract)` plus `atomic_series_status_projection(contract)`
and then refuses, in order, on the first condition that holds:

1. `contract.cleanup in TERMINAL_SERIES_CLEANUP` → exit 2, state `series-terminal`, naming the
   observed `cleanup` value and pointing at `task_reopen` or a successor task.
2. `not branch_exists(contract.code_repo_path, contract.code_work_branch)` → exit 2, state
   `series-branch-missing`, naming the missing work branch, the source branch to re-cut from and
   the recorded base commit.
3. `lineage_refusal(source_lineage_for_contract(contract)) is not None` → exit 2 with the lineage
   block payload spliced into the same payload and its summary prefixed
   `"Attach refused before this series was resumed: "`.

Otherwise it returns exit 0 with `{"state": "attached", "attached": True, **payload}`.

The refusal this replaces named `kind == "series"`, which is a property the codebase fully
supports (`atomic_series_activation` observes it and defines its terminal predicate), so it blamed
a non-cause and hid the real one. In practice the unstated cause was a branch that had been merged
and deleted, and the message sent readers after contract staleness and operation generations
instead.

### Conventions

One function, no private helpers, and every refusal is a returned `WorktreeCommandResult` rather
than a raise — the same shape the rest of `start.py`'s result builders use.

### Invariants And Boundaries

- The three refusal states are `series-terminal`, `series-branch-missing`, and the lineage block's
  own state; all are pre-write bad-state refusals, so an attach that refuses has moved nothing.
- The payload is the status payload plus the activation projection, so a refusal is as inspectable
  as a success.
- The module owns no policy of its own: terminality comes from `TERMINAL_SERIES_CLEANUP`, branch
  liveness from `branch_exists`, and lineage from `source_lineage_for_contract`.
- It is start-side glue only; the atomic-series activation module owns what a series *is*.

### Todos

None recorded. The extraction is a size-rail move; folding any new policy into this file would
undo the reason it exists.

## Docs References

No configured Domain Documentation source applies to this repository-internal attach seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned command result builder. | "def series_attach_result(" | mcp/src/agents_remember/worktrees/modules/startup/series_attach.py:20-71 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one exported helper: the series branch of attach, with its two named refusals and the lineage refusal it splices in. | "def series_attach_result(" | mcp/src/agents_remember/worktrees/modules/startup/series_attach.py:20-71 |
| The caller this module was extracted from, which still owns the rest of the attach route and now delegates its series branch here. | `attach_result` | mcp/src/agents_remember/worktrees/modules/start.py:196-236 |
| The terminal-cleanup vocabulary that decides the first refusal. | `TERMINAL_SERIES_CLEANUP` | mcp/src/agents_remember/worktrees/scheduling_mode.py:35-35 |
| The branch liveness probe and the command-result type every return uses. | "def branch_exists("; "class WorktreeCommandResult:" | mcp/src/agents_remember/worktrees/modules/git.py:94-94; mcp/src/agents_remember/worktrees/modules/models.py:14-14 |
| The atomic-series status projection spliced into every payload, and the source-lineage proof whose refusal is the third refusal. | `atomic_series_status_projection`; "def source_lineage_for_contract("; "def lineage_refusal("; "def lineage_block_payload(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:434-446; mcp/src/agents_remember/worktrees/source_lineage.py:94-109; mcp/src/agents_remember/worktrees/source_lineage.py:110-124; mcp/src/agents_remember/worktrees/source_lineage.py:139-158 |
| The status payload the helper starts from. | "def status_payload(" | mcp/src/agents_remember/worktrees/modules/guidance.py:571-571 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | `series_attach_result` | mcp/src/agents_remember/worktrees/modules/startup/series_attach.py:20-71 |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "def status_payload(" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:571-571. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "def status_payload(" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:563-563. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `attach_result` repointed to mcp/src/agents_remember/worktrees/modules/start.py:196-236. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def branch_exists("; "class WorktreeCommandResult:" repointed to mcp/src/agents_remember/worktrees/modules/git.py:94-94; mcp/src/agents_remember/worktrees/modules/models.py:14-14. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def status_payload(" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:493-493. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "def branch_exists("; "class WorktreeCommandResult:" repointed to mcp/src/agents_remember/worktrees/modules/git.py:94-94; mcp/src/agents_remember/worktrees/modules/models.py:14-14. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "def status_payload(" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:493-493. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator: created the one-to-one sidecar for this new
  module. It is `start.py`'s `_attach_series_result` moved verbatim and renamed
  `series_attach_result` to bring that file back under the size limit, so the card records the
  extraction rather than a behaviour change: the states, messages, payload composition and refusal
  order are the ones `start.py` already emitted, and the caller's series branch is the citation
  that proves it. Verification metadata remains closeout-owned; no verification stamp advanced and
  no acceptance claim is made.
