# mcp/src/agents_remember/worktrees/modules/terminal_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/terminal_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-09-14T15:05+02:00 |
| lastVerifiedCommitHash | `96bfe755d2b605d42a9d001714cc7d8eb592a073` |
| lastVerifiedCommitDate | 2026-09-14T15:15:20+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Fail-closed preflight and result validation for terminal worktree operations. A terminal result
blockage always names its component and carries a non-empty reason.

## Code Commentary

### Logic

Module-level surface:

- `BranchTarget` (class, lines 24-30)
- `TerminalPreflight` (class, lines 34-37)
- `require_series_children_retired` (function, lines 40-64)
- `series_reports_is_child_enclosure` (function, lines 67-70)
- `legacy_series_reports_is_child_enclosure` (function, lines 73-84)
- `terminal_preflight` (function, lines 172-211)
- `TerminalExpectation` (class, lines 215-225)
- `TerminalResult` (class, lines 229-242)
- `terminal_result_blockers` (function, lines 245-287)
- `_worktree_preflight` (function, lines 290-329)
- `_branch_targets` (function, lines 332-355)
- `_branch_preflight` (function, lines 358-373)
- `_local_absent_remote_preflight` (function, lines 376-386)
- `_branch_identity_refusal` (function, lines 389-397)
- `_branch_refs_refusal` (function, lines 400-420)
- `_branch_checkout_refusal` (function, lines 423-434)
- `_cleanup_branch_preflight` (function, lines 437-465)
- `_abandon_branch_preflight` (function, lines 468-498)
- `_branch_presence` (function, lines 501-507)
- `_checked_out_paths` (function, lines 510-522)
- `_remote_branch_preflight` (function, lines 525-549)
- `_provider_blockers` (function, lines 552-571)
- `_result_blockers` (function, lines 574-586)
- `_done_blockers` (function, lines 589-605)
- `_nested_blockers` (function, lines 608-621)
- `_blocked_reason` (function, lines 624-636)
- `_blocker` (function, lines 639-655)
- `_blocked` (function, lines 658-666)

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `BranchTarget`. | `BranchTarget` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:24-30 |
| Defines the class `TerminalPreflight`. | `TerminalPreflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:34-37 |
| The series child census fails closed on a non-canonical worktree group; the legacy guard preserves a colliding child `reports` enclosure only for legacy-shape contracts. | `require_series_children_retired`; `legacy_series_reports_is_child_enclosure` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:40-64; mcp/src/agents_remember/worktrees/modules/terminal_validation.py:73-84 |
| Defines the function `terminal_preflight`. | `terminal_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:172-211 |
| `TerminalExpectation` states what one collection must show: the field that proves reclamation, whether it is a preview, and the benign reasons. | `TerminalExpectation` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:215-225 |
| `TerminalResult` bundles one terminal operation's output collections with whether they are a preview or what happened. | `TerminalResult` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:229-242 |
| Defines the function `terminal_result_blockers`. | `terminal_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:245-287 |
| Defines the function `_worktree_preflight`. | `_worktree_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:290-329 |
| Builds the exact code and optional external-memory terminal branch targets owned by the validated contract. | `_branch_targets` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:332-355 |
| Defines the function `_branch_preflight`. | `_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:358-373 |
| Defines the function `_local_absent_remote_preflight`. | `_local_absent_remote_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:376-386 |
| Defines the function `_branch_identity_refusal`. | `_branch_identity_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:389-397 |
| Defines the function `_branch_refs_refusal`. | `_branch_refs_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:400-420 |
| Defines the function `_branch_checkout_refusal`. | `_branch_checkout_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:423-434 |
| Defines the function `_cleanup_branch_preflight`. | `_cleanup_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:437-465 |
| Defines the function `_abandon_branch_preflight`. | `_abandon_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:468-498 |
| Defines the function `_branch_presence`. | `_branch_presence` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:501-507 |
| Defines the function `_checked_out_paths`. | `_checked_out_paths` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:510-522 |
| Defines the function `_remote_branch_preflight`. | `_remote_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:525-549 |
| Defines the function `_provider_blockers`; every provider, container and network blockage it emits goes through `_blocker`. | `_provider_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:552-571 |
| Defines the function `_result_blockers`, which reads each collection through a `TerminalExpectation`. | `_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:574-586 |
| Every entry the expectation says must have been reclaimed and was not. | `_done_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:589-605 |
| The remote half of a branch entry, reported separately from the local half. | `_nested_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:608-621 |
| Answers a result item's reason, or why it carries none: `invalid-result` for a malformed item, operator language for a reasonless one. | `_blocked_reason` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:624-636 |
| The only construction path for a terminal blockage; it refuses a missing, blank or non-string reason instead of emitting an anonymous blocker. | `_blocker` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:639-655 |
| Defines the function `_blocked`. | `_blocked` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:658-666 |
| The focused cases that pin the reasonless result and the refusal of an unnameable reason. | `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason`; `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` | mcp/tests/test_terminal_blocker_reasons.py:223-243; mcp/tests/test_terminal_blocker_reasons.py:246-259 |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator: documented the blocker contract this change set
  introduced. `_blocker` is now the only blockage construction path and refuses a missing, blank or
  non-string reason; `_blocked_reason` answers a reasonless or malformed result item in operator
  language; `TerminalResult` and `TerminalExpectation` bundle the outputs with preview-versus-real so
  the dry-run path reads preflight previews as previews. Recorded the new symbols, the invariant that
  a blockage always names its component and reason, and the L6 payload that motivated it. Re-derived
  every anchor against the current file — the block inserted after `terminal_preflight` moved
  `terminal_result_blockers` 214-239 → 245-287 and every later symbol by +48 lines — and added the
  rows for the new symbols plus the focused cases. The change makes a reasonless blocker
  unrepresentable and names a surviving non-removal's cause; it adds no teardown capability.
  Verification metadata remains closeout-owned.

- 2026-08-20T05:12+02:00 — L13 landed-wave refresh: the series closeout-report routing
  commit (0a746c9f) touched this source; card re-verified against the current file, verification
  stamp advanced to 0a746c9f. Body unchanged — the documented contract still holds.


- 2026-08-19T04:05+02:00 — 260815-DAG-L10 curator: `require_series_children_retired` now checks
  the recorded series `worktree_group` against `worktree_group_for(...)` (the master worktree
  group) instead of the task enclosure root, and the new `legacy_series_reports_is_child_enclosure`
  restricts child-`reports`-enclosure preservation to legacy-shape contracts. Added the three
  series-census functions to the module surface, documented the guard, and repaired all reference
  ranges (L10's +18-line shift plus older stale rows). Verification metadata stamped at the landed
  code commit `e41ea31d`.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
