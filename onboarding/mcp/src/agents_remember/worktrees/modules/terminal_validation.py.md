# mcp/src/agents_remember/worktrees/modules/terminal_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/terminal_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-09-14T17:20+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| External-memory preflight excludes the root cache while preserving other dirtiness. | `_worktree_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:291-330 |
| Defines the class `BranchTarget`. | `BranchTarget` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:25-31 |
| Defines the class `TerminalPreflight`. | `TerminalPreflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:35-38 |
| The series child census fails closed on a non-canonical worktree group; the legacy guard preserves a colliding child `reports` enclosure only for legacy-shape contracts. | `require_series_children_retired`; `legacy_series_reports_is_child_enclosure` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:41-65; mcp/src/agents_remember/worktrees/modules/terminal_validation.py:74-85 |
| Defines the function `terminal_preflight`. | `terminal_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:173-212 |
| `TerminalExpectation` states what one collection must show: the field that proves reclamation, whether it is a preview, and the benign reasons. | `TerminalExpectation` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:216-226 |
| `TerminalResult` bundles one terminal operation's output collections with whether they are a preview or what happened. | `TerminalResult` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:230-243 |
| Defines the function `terminal_result_blockers`. | `terminal_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:246-288 |
| Defines the function `_worktree_preflight`. | `_worktree_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:291-330 |
| Builds the exact code and optional external-memory terminal branch targets owned by the validated contract. | `_branch_targets` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:333-356 |
| Defines the function `_branch_preflight`. | `_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:359-374 |
| Defines the function `_local_absent_remote_preflight`. | `_local_absent_remote_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:377-387 |
| Defines the function `_branch_identity_refusal`. | `_branch_identity_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:390-398 |
| Defines the function `_branch_refs_refusal`. | `_branch_refs_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:401-421 |
| Defines the function `_branch_checkout_refusal`. | `_branch_checkout_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:424-435 |
| Defines the function `_cleanup_branch_preflight`. | `_cleanup_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:438-466 |
| Defines the function `_abandon_branch_preflight`. | `_abandon_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:469-499 |
| Defines the function `_branch_presence`. | `_branch_presence` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:502-508 |
| Defines the function `_checked_out_paths`. | `_checked_out_paths` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:511-523 |
| Defines the function `_remote_branch_preflight`. | `_remote_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:526-550 |
| Defines the function `_provider_blockers`; every provider, container and network blockage it emits goes through `_blocker`. | `_provider_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:553-572 |
| Defines the function `_result_blockers`, which reads each collection through a `TerminalExpectation`. | `_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:575-587 |
| Every entry the expectation says must have been reclaimed and was not. | `_done_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:590-606 |
| The remote half of a branch entry, reported separately from the local half. | `_nested_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:609-622 |
| Answers a result item's reason, or why it carries none: `invalid-result` for a malformed item, operator language for a reasonless one. | `_blocked_reason` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:625-637 |
| The only construction path for a terminal blockage; it refuses a missing, blank or non-string reason instead of emitting an anonymous blocker. | `_blocker` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:640-656 |
| Defines the function `_blocked`. | `_blocked` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:659-667 |
| The focused cases that pin the reasonless result and the refusal of an unnameable reason. | `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason`; `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` | mcp/tests/test_terminal_blocker_reasons.py:232-252; mcp/tests/test_terminal_blocker_reasons.py:255-268 |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-09-18T19:20+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **corrected an over-general claim in this card.** The Logic said the dry-run path can no longer read a preview as a blockage, but the `drift_snapshots` branch of `terminal_result_blockers` was building `TerminalExpectation(done_key="removed")` **without** `preview=result.preview` while every other collection propagated it — so a preview's `would_remove` entry was read with the real call's `would_delete` key and `_blocker` raised `RuntimeError: terminal result blocker driftSnapshot=code carries no reason`. The branch now passes the flag, and the card states the fix, names `remove_drift_snapshot` as the `removed`/`would_remove` producer that makes it necessary, and records the one deliberate exception: the `branch` collection needs no flag because its preview producer emits `deleted: False, would_delete: True`, which `_blocked`'s default `pending_key` already reads. No other claim was falsified. Existing citation ranges were left for the citation pass; noted drift: `terminal_result_blockers` now spans `246-292` (card cites `246-288`) and every symbol below it shifted by four lines (`_worktree_preflight` 291-330 → 295-334, `_provider_blockers` 553-572 → 557-576, `_blocker` 640-656 → 644-660, `_blocked` 659-667 → 663-671), while the module-source list above still carries the pre-change numbers.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock
- 2026-09-17T03:31:11+02:00 — 2026-09-15 — LCA L9 terminal delivery: `_worktree_preflight` excludes exactly the root ledger cache from external-memory dirtiness. Code worktrees keep their full status check, and all other memory paths remain blockers when dirty. This observation performs no index, worktree or ref mutation.
- 2026-09-15T06:37:50+02:00 — LCA L9 terminal delivery: `_worktree_preflight` excludes exactly the root ledger cache from external-memory dirtiness. Code worktrees keep their full status check, and all other memory paths remain blockers when dirty. This observation performs no index, worktree or ref mutation.


- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): `_remote_branch_preflight` now hands the runner one
  `GitRunnerOptions(timeout=GIT_REMOTE_TIMEOUT_SECONDS)` object for
  `git ls-remote --heads origin <branch>` instead of a `timeout=` keyword. No content impact: this card
  stated no `run_git` call form, the module's import line changed in place without adding a line, and
  no cited range was derived from an `input_text=`, `work_dir=` or `timeout=` mention — every symbol
  range above still names its current symbol, so no citation anchor changed. Verification metadata
  remains closeout-owned.

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
