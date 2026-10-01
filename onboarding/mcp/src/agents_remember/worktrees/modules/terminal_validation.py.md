# mcp/src/agents_remember/worktrees/modules/terminal_validation.py

## Governing Overview

[overview](overview.md)

## Purpose

Fail-closed preflight and result validation for terminal worktree operations. A terminal result
blockage always names its component and carries a non-empty reason.

## Code Commentary

`_worktree_preflight` excludes exactly the root ledger cache from external-memory dirtiness. Code worktrees keep their full status check, and all other memory paths remain blockers when dirty. This observation performs no index, worktree or ref mutation.

### Logic

Module-level surface:

- `BranchTarget` (class, lines 25-31)
- `TerminalPreflight` (class, lines 35-38)
- `require_series_children_retired` (function, lines 41-65)
- `series_reports_is_child_enclosure` (function, lines 68-71)
- `legacy_series_reports_is_child_enclosure` (function, lines 74-85)
- `terminal_preflight` (function, lines 173-212)
- `TerminalExpectation` (class, lines 216-226)
- `TerminalResult` (class, lines 230-243)
- `terminal_result_blockers` (function, lines 246-288)
- `_worktree_preflight` (function, lines 291-330)
- `_branch_targets` (function, lines 333-356)
- `_branch_preflight` (function, lines 359-374)
- `_local_absent_remote_preflight` (function, lines 377-387)
- `_branch_identity_refusal` (function, lines 390-398)
- `_branch_refs_refusal` (function, lines 401-421)
- `_branch_checkout_refusal` (function, lines 424-435)
- `_cleanup_branch_preflight` (function, lines 438-466)
- `_abandon_branch_preflight` (function, lines 469-499)
- `_branch_presence` (function, lines 502-508)
- `_checked_out_paths` (function, lines 511-523)
- `_remote_branch_preflight` (function, lines 526-550)
- `_provider_blockers` (function, lines 553-572)
- `_result_blockers` (function, lines 575-587)
- `_done_blockers` (function, lines 590-606)
- `_nested_blockers` (function, lines 609-622)
- `_blocked_reason` (function, lines 625-637)
- `_blocker` (function, lines 640-656)
- `_blocked` (function, lines 659-667)

**Series child census and the legacy reports guard (260815-DAG-L10).**
`require_series_children_retired` verifies a series contract's recorded `worktree_group` against
`worktree_group_for(series.coordination_root, series.repo_name, series.task_name)` — the master
worktree group, `worktrees/<repo>/<master>-ar`, since L10 — before censusing live children under
`task_root / "enclosures"`; a legacy series contract still recording the task enclosure root as
its group is refused here. `series_reports_is_child_enclosure` detects a child leaf literally
named `reports` whose enclosure shares the series reports directory. `legacy_series_reports_is_child_enclosure`
— the guard `cleanup.py` / `abandon.py` actually call before removing the series reports tree —
restricts that preservation to legacy-shape contracts (group still equal to the task enclosure
root), because current contracts keep series reports under the worktree group, where no child
enclosure can live.

**The blocker contract (260913-LCA-L8).** `_blocker(component, reason)` is the only construction
path for a terminal blockage, and it raises `RuntimeError` naming the component when the reason is
missing, blank or not a string. A blockage that reports no reason cannot be told apart from a
spurious one, so it is refused at the call site that detected it rather than emitted; the L6 payload
`{"provider": "providerRuntime", "reason": null}` is now impossible to produce, not merely unlikely.
`_blocked_reason(item)` answers a result item that carries no usable reason in operator language:
`invalid-result` for a malformed item, `no reason reported by the terminal result` for a well-formed
one that reports nothing, and the item's own reason otherwise. Every call site routes through both.
The change makes a reasonless blocker unrepresentable and gives a surviving non-removal a named
reason; it adds no teardown capability, and a genuinely blocked teardown still blocks with its own
reason.

`TerminalResult` bundles one terminal operation's four (or five, with `drift_snapshots`) output
collections with `preview`, and `TerminalExpectation` states per collection which field proves
reclamation, whether that collection is a preview, and which reasons are benign.
`terminal_result_blockers(result)` reads a preview through `TerminalExpectation(preview=True)`,
because a preview answers `would_remove` where a real result answers nothing until it acts, so the
dry-run path can no longer feed preflight previews into a builder that would read them as blockages.
`_result_blockers` splits into `_done_blockers` (entries the expectation says must have been
reclaimed) and `_nested_blockers` (the remote half of a branch entry). Bundling the outputs also
replaced the five-keyword `terminal_result_blockers` signature with one `TerminalResult` argument at
every call site; the change set adds no `# noqa` and no per-file ignore.

**Every collection that needs the preview flag now carries it (260915-KS-L23, D-15).** The
`drift_snapshots` branch was the one collection that did **not** propagate `preview`, so a preview's
`would_remove` entry was read through the real call's `would_delete` key, looked like a blockage, and
`_blocker` raised `RuntimeError` on the missing reason — a cleanup *preview* failed on exactly the
contracts a real finalize completed. It now passes `preview=result.preview` like its siblings, and
`remove_drift_snapshot` is the producer that makes the flag necessary: under `dry_run` it emits
`{"removed": False, "would_remove": True}`, the `removed`/`would_remove` pair. The `branch` collection
is the deliberate exception and needs no flag: its preview producer emits `deleted: False,
would_delete: True`, which is what `_blocked`'s default `pending_key` already reads, so the branch
half of a preview was and remains correctly classified without `preview=True`.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- A terminal result blockage always names its component and a non-empty reason; a producer that
  supplies neither raises where it is detected instead of emitting an anonymous blockage.
- A preview is read as a preview: an entry carrying `would_remove` (or `would_delete`) states what the
  operation would reclaim and is never counted as a blockage.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- External-memory preflight excludes the root cache while preserving other dirtiness. [1]
- Defines the class `BranchTarget`. [2]
- Defines the class `TerminalPreflight`. [3]
- The series child census fails closed on a non-canonical worktree group; the legacy guard preserves a colliding child `reports` enclosure only for legacy-shape contracts. [4]
- Defines the function `terminal_preflight`. [5]
- `TerminalExpectation` states what one collection must show: the field that proves reclamation, whether it is a preview, and the benign reasons. [6]
- `TerminalResult` bundles one terminal operation's output collections with whether they are a preview or what happened. [7]
- Defines the function `terminal_result_blockers`. [8]
- Defines the function `_worktree_preflight`. [9]
- Builds the exact code and optional external-memory terminal branch targets owned by the validated contract. [10]
- Defines the function `_branch_preflight`. [11]
- Defines the function `_local_absent_remote_preflight`. [12]
- Defines the function `_branch_identity_refusal`. [13]
- Defines the function `_branch_refs_refusal`. [14]
- Defines the function `_branch_checkout_refusal`. [15]
- Defines the function `_cleanup_branch_preflight`. [16]
- Defines the function `_abandon_branch_preflight`. [17]
- Defines the function `_branch_presence`. [18]
- Defines the function `_checked_out_paths`. [19]
- Defines the function `_remote_branch_preflight`. [20]
- Defines the function `_provider_blockers`; every provider, container and network blockage it emits goes through `_blocker`. [21]
- Defines the function `_result_blockers`, which reads each collection through a `TerminalExpectation`. [22]
- Every entry the expectation says must have been reclaimed and was not. [23]
- The remote half of a branch entry, reported separately from the local half. [24]
- Answers a result item's reason, or why it carries none: `invalid-result` for a malformed item, operator language for a reasonless one. [25]
- The only construction path for a terminal blockage; it refuses a missing, blank or non-string reason instead of emitting an anonymous blocker. [26]
- Defines the function `_blocked`. [27]
- The focused cases that pin the reasonless result and the refusal of an unnameable reason. [28]

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260918-TSIP-L6 The Drift-Snapshot Collection Declares Its Preview

`terminal_result_blockers` (`:246-297`) builds one expectation per terminal collection, and the
drift-snapshot collection was the only one whose expectation omitted `preview=result.preview`
(`T62`/`D49`). `_done_blockers` reads the *pending* key off that flag, and this collection's
producer answers a dry run with `would_remove`
(`kernel/primitives/drift_snapshot.py::_remove_snapshot_file`) exactly as the worktree, directory
and provider collections beside it do. Without the flag the entry was neither reclaimed, nor
pending, nor reasoned, so `_blocker` (`:647-665`) raised and **every preview of a task that has a
drift snapshot crashed on its own producer's output** — the repair is the one keyword argument at
`:285-292`, and the three cases that hold it (a preview, a real reasonless result, and the
tool-level cleanup preview) are in `mcp/tests/test_terminal_blocker_reasons.py:382-480`.
