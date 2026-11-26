# mcp/tests/test_terminal_preview_expectation.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The lane pins **a cleanup preview and the cleanup it previews agreeing about the same collection.**

`terminal_result_blockers` is at `mcp/src/agents_remember/worktrees/modules/terminal_validation.py:260-312`. Its drift-snapshot branch at `:294-311` passes `preview=result.preview` at line 309. `_blocker` (`:715-731`) refuses a missing reason.

## Code Commentary

### Logic

The module drives the **real validator** over four result shapes of the production producer —
`kernel/primitives/drift_snapshot.py::_remove_snapshot_file` (`:38-55`) returns those fields — rather
than synthesizing an outcome the producer cannot produce. `_result` (`:27-41`) builds a
`TerminalResult` whose only non-empty collection is `drift_snapshots={"code": snapshot}`, with
`providers={"state": "torn-down"}` so the provider half contributes no blocker; that isolation is
what makes the assertion about the `driftSnapshot` branch specifically rather than about the
validator as a whole. The four snapshot builders model those result shapes:

| Builder | Shape | Producer's own fields |
| --- | --- | --- |
| `_preview_snapshot` (`:44-51`) | a preview that *would* remove | `removed: False` + `would_remove: True` |
| `_removed_snapshot` (`:54-60`) | a real removal | `removed: True` |
| `_absent_snapshot` (`:63-70`) | already gone | `removed: False` + `reason: "already-absent"` |
| `_failed_snapshot` (`:73-80`) | a real failure | `removed: False` + `reason: "[Errno 13] Permission denied"` |

The three cases:

- **`test_a_preview_over_a_live_drift_snapshot_reports_no_blocker`** (`:83-91`) asserts
  `terminal_result_blockers(...) == []` for a preview-shaped drift snapshot.
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

The module imports exactly two names — `TerminalResult` and `terminal_result_blockers` — from the validator, with no test-support import. This direct import shape does not establish absence of evidence-catalog dependencies: the catalog declares this module as a consumer of the global user-settings guard and Node lockfile artifacts. Its five helpers construct typed terminal results or plain snapshot dictionaries for the assertions.

This module carries **no `pytestmark`**.


### Invariants And Boundaries

- **A blockage always names itself and its reason.** `_blocker` raises rather than emit a
  reason-less entry, and this module asserts the reason's exact text on the one path that must still
  block — the fix may not be achieved by weakening that rule.
- **Preview entries report pending removal.** The drift-snapshot expectation uses `removed` as its done key.
  The validator uses `would_remove` as the pending key in preview mode and `would_delete` otherwise.
- **The `driftSnapshot` expectation receives the preview flag.** The worktree, directory and
  drift-snapshot expectations receive `result.preview`; the branch expectation and provider helper
  do not receive that flag. The comment beside the fixed drift-snapshot branch records why the former missing preview keyword misread `would_remove` as a real-result reclamation failure, along with the earlier fix’s merge provenance.
- **Boundary.** This is a test module. It owns no production contract and adds no support module.

### Todos

None recorded.

## Retained Full-Card Audit Context

These distinct accounts are retained from memory base `81cfe4a8`. Dates, source coordinates, counts, outcomes and ownership describe their recorded epochs; this pass adds no execution, mutation result or acceptance. Historical reference labels are custody text and do not select live anchors.

### D-15 preview/finalize discrepancy

> The lane that pins **a cleanup preview and the cleanup it previews agreeing about the same
> collection.** `D-15` measured the failure: `lifecycle_finalize_task` with `dry_run=true` returned
> `state: cleanup-blocked` on a `driftSnapshot` blocker that carried no reason, while the real finalize
> on the same contract completed and reclaimed everything.

The D-15 result is the earlier recorded incident, not a new finalize run. Current source still supplies the preview/cleanup agreement checks.

### Missing-keyword cause and reason boundary

> The historical cause was **one missing keyword** in the drift-snapshot branch. The current
> `terminal_result_blockers` is at
> `mcp/src/agents_remember/worktrees/modules/terminal_validation.py:260-312`; its drift-snapshot
> branch is at `:294-311` and now propagates `preview=result.preview` at line 309, as the sibling
> collections do. The retained defect account describes the earlier omission: a preview's
> `would_remove` entry was read with the real call's pending key and appeared to reclaim nothing.
> `_blocker` (currently `:715-731`) refuses a missing reason. The recorded failure therefore concerned
> previews of contracts that a real finalize completed; it is historical regression context, not a
> claim that the current branch still omits the keyword or a new execution result.

The keyword omission and its consequence are explicitly historical; the current branch passes preview=result.preview. The old sibling-universal wording elsewhere is not current behavior: branch expectations and provider helper do not receive that flag.

### Measured L14 regression shape

> - **`test_a_preview_over_a_live_drift_snapshot_reports_no_blocker`** (`:83-91`) — the measured L14
>   shape. Before the fix this call raised
>   `RuntimeError: terminal result blocker driftSnapshot=code carries no reason`; the assertion is
>   `terminal_result_blockers(...) == []`.

The earlier failure text and L14 attribution remain historical. The current [] assertion, four-direction agreement and genuine-failure guard are unchanged; no test was rerun.

### Earlier append-only lane account

> The earlier leaf’s recorded append-at-end account describes its historical catalog, not the current row position.
> The earlier append-only registration was recorded at historical `mcp/tests/test-evidence-lanes.toml:192`; that source-epoch coordinate is not current navigation.

The old 599 locator and the original 192 registration account describe earlier source epochs.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References




- The expectation carries the done key and preview flag. The blocker scan uses the flag to select the pending key. [3]

- The result type that bundles the outputs with whether they are a preview. [4]
- The production remover returns the fields modeled by the four snapshot fixtures. [5]
- One terminal result whose only non-empty collection is the drift snapshot. [6]
- The preview fixture has removed set to false and would_remove set to true. [7]
- The real removal and the already-absent entries. [8]
- The genuine failure, which must still block with its reason. [9]

### Cross-Repo References

No cross-repository behavior is implemented or measured in this file.

No meaningful cross-repo references found.

### Repo-Internal References (continued)




- The test passes the preview-shaped snapshot fixture with preview mode enabled and asserts no blockers. [10]

- The case checks preview, real removal and an already-absent entry over the same drift-snapshot collection. [11]

- A real drift-snapshot failure remains blocking and retains its reason. [12]

- The result fixture isolates the drift snapshot and defines the preview, removed, already-absent and failed inputs. [1]

### Repo-Internal References (renewed)

- The drift-snapshot branch uses a preview-aware expectation; its adjacent comment records the earlier missing-keyword cause and merge provenance. [2]

- The `unit-regression` lane selects `mcp/tests/test_terminal_preview_expectation.py` (`mcp/tests/test-evidence-lanes.toml:625`). [13]
