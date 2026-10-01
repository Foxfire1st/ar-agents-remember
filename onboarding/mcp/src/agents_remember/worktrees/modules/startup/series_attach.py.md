# mcp/src/agents_remember/worktrees/modules/startup/series_attach.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal attach seam.

- No external domain source is required for this repository-owned command result builder. [1]

### Repo-Internal References

- The one exported helper: the series branch of attach, with its two named refusals and the lineage refusal it splices in. [2]
- The caller this module was extracted from, which still owns the rest of the attach route and now delegates its series branch here. [3]
- The terminal-cleanup vocabulary that decides the first refusal. [4]
- The branch liveness probe and the command-result type every return uses. [5]
- The atomic-series status projection spliced into every payload, and the source-lineage proof whose refusal is the third refusal. [6]
- The status payload the helper starts from. [7]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

- No applicable cross-repository source was found. [8]
