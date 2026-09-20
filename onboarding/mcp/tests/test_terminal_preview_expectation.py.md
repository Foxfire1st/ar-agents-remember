# mcp/tests/test_terminal_preview_expectation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_preview_expectation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T19:08+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a`|
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The lane that pins **a cleanup preview and the cleanup it previews agreeing about the same
collection.** `D-15` measured the failure: `lifecycle_finalize_task` with `dry_run=true` returned
`state: cleanup-blocked` on a `driftSnapshot` blocker that carried no reason, while the real finalize
on the same contract completed and reclaimed everything.

The cause was **one missing keyword** in one branch. Every sibling collection in
`terminal_result_blockers` (`mcp/src/agents_remember/worktrees/modules/terminal_validation.py:246-292`)
propagates `preview=result.preview` into its `TerminalExpectation`; the `driftSnapshot` branch did
not (`:280-286`). A preview's drift-snapshot entry answers `would_remove`, so read with the real
call's pending key it looked like an entry that reclaimed nothing, and `_blocker`
(`:644-660`) refused to invent the missing reason — correctly, because a blockage an operator cannot
read is not a blockage. A preview therefore failed on exactly the contracts a real finalize
completed.

## Code Commentary

### Logic

The module drives the **real validator** over the three shapes the production producer emits —
`kernel/primitives/drift_snapshot.py::_remove_snapshot_file` (`:38-...`) is what writes them — rather
than synthesizing an outcome the producer cannot produce. `_result` (`:27-41`) builds a
`TerminalResult` whose only non-empty collection is `drift_snapshots={"code": snapshot}`, with
`providers={"state": "torn-down"}` so the provider half contributes no blocker; that isolation is
what makes the assertion about the `driftSnapshot` branch specifically rather than about the
validator as a whole. The four snapshot builders are the producer's own three result shapes:

| Builder | Shape | Producer's own fields |
| --- | --- | --- |
| `_preview_snapshot` (`:44-51`) | a preview that *would* remove | `removed: False` + `would_remove: True` |
| `_removed_snapshot` (`:54-60`) | a real removal | `removed: True` |
| `_absent_snapshot` (`:63-70`) | already gone | `removed: False` + `reason: "already-absent"` |
| `_failed_snapshot` (`:73-80`) | a real failure | `removed: False` + `reason: "[Errno 13] Permission denied"` |

The three cases:

- **`test_a_preview_over_a_live_drift_snapshot_reports_no_blocker`** (`:83-91`) — the measured L14
  shape. Before the fix this call raised
  `RuntimeError: terminal result blocker driftSnapshot=code carries no reason`; the assertion is
  `terminal_result_blockers(...) == []`.
- **`test_the_preview_and_the_real_call_agree_over_the_same_collection`** (`:94-104`) — the module's
  actual subject, asserted from four directions in one case: the preview answers `would_remove`, the
  real call answers `removed`, and an entry that was already gone is benign in **both** modes. That
  is what "one keyword apart, not one judgement apart" means.
- **`test_a_real_drift_snapshot_failure_still_blocks_with_its_reason`** (`:107-116`) — the guard
  against "fixing" this by making the collection benign. The assertion is the exact blocker dict
  `[{"driftSnapshot": "code", "reason": "[Errno 13] Permission denied"}]`, so a genuine
  drift-snapshot failure must still block **and must still name the component and the reason**. This
  is the case that goes red if the expectation is relaxed instead of corrected.

### Conventions

The module imports exactly two names — `TerminalResult` and `terminal_result_blockers` — from the
validator it measures, and nothing else from the package: no fixture module, no test-support import,
so the evidence-lifecycle catalog records no transitive consumer here. The five helpers are
module-level functions with docstrings that state the role the value plays in the assertion rather
than restating its type, and every value is a plain `dict[str, object]` literal, which is what the
validator's own signature accepts.

**The lane registration is the manifest row**: this module carries **no `pytestmark`**, and its
single lane row was **appended** to the end of `unit-regression` in
`mcp/tests/test-evidence-lanes.toml:192` — item 16's half (a), because a mid-list insertion shifts
every row below it.

### Invariants And Boundaries

- **A blockage always names itself and its reason.** `_blocker` raises rather than emit a
  reason-less entry, and this module asserts the reason's exact text on the one path that must still
  block — the fix may not be achieved by weakening that rule.
- **A preview is never read as a result.** `TerminalExpectation.preview` selects the key that proves
  reclamation; the `would_remove`/`removed` pair is the whole difference.
- **The `driftSnapshot` branch must stay on the same footing as its siblings.** Every collection
  built from a `TerminalResult` propagates `preview` — the comment beside the fixed branch records
  exactly why.
- **Boundary.** This is a test module. It owns no production contract and adds no support module.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of D-15 and of the three shapes it drives. | "A cleanup *preview* and the cleanup it previews must agree about the same collection." | mcp/tests/test_terminal_preview_expectation.py:1-17 |
| **The one entry point, with the fixed `driftSnapshot` branch and its comment.** | `terminal_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:246-292 |
| The expectation type whose `preview` flag selects the reclamation key. | `TerminalExpectation` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:216-226 |
| The result type that bundles the outputs with whether they are a preview. | `TerminalResult` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:230-243 |
| **The producer of the shape this module drives: the real drift-snapshot remover.** | `_remove_snapshot_file` | mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:38-38 |
| One terminal result whose only non-empty collection is the drift snapshot. | `_result` | mcp/tests/test_terminal_preview_expectation.py:27-41 |
| The preview's own entry shape: `would_remove`, not `removed`. | `_preview_snapshot` | mcp/tests/test_terminal_preview_expectation.py:44-51 |
| The real removal and the already-absent entries. | `_removed_snapshot`; `_absent_snapshot` | mcp/tests/test_terminal_preview_expectation.py:54-60; mcp/tests/test_terminal_preview_expectation.py:63-70 |
| The genuine failure, which must still block with its reason. | `_failed_snapshot` | mcp/tests/test_terminal_preview_expectation.py:73-80 |
| **The measured L14 shape: a preview over a live drift snapshot reports no blocker.** | `test_a_preview_over_a_live_drift_snapshot_reports_no_blocker` | mcp/tests/test_terminal_preview_expectation.py:83-91 |
| **Preview and apply are the same judgement, asserted from four directions in one case.** | `test_the_preview_and_the_real_call_agree_over_the_same_collection` | mcp/tests/test_terminal_preview_expectation.py:94-104 |
| **The other half of the contract: the fix may not swallow a real failure.** | `test_a_real_drift_snapshot_failure_still_blocks_with_its_reason` | mcp/tests/test_terminal_preview_expectation.py:107-116 |
| The lane row this module was appended to. | "mcp/tests/test_terminal_preview_expectation.py" | mcp/tests/test-evidence-lanes.toml:197-197 |

## Cross-Repo References

No cross-repository behavior is implemented or measured in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_terminal_preview_expectation.py" repointed to mcp/tests/test-evidence-lanes.toml:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:08+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): created this one-to-one card for the case lane the cleanup-preview fix owes. It records the mechanism precisely — one branch of `terminal_result_blockers` omitted `preview=result.preview` while every sibling propagated it — the four producer shapes the module drives, and the case that keeps the fix honest by requiring a genuine drift-snapshot failure to still block **with its reason**. It also records that the module imports exactly two names from the validator and no test-support module, so no consumer row is owed. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate. The `reviewedWorkingCandidate` row states what was read, and closeout owns the stamp.
