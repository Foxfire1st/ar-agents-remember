# mcp/tests/test_terminal_notice_commit_recovery.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins survival across the native commit cut, and that a notice write never governs whether the native publication
succeeded.

## Code Commentary

A `_CutGuard` raises a `_ProcessCut` from inside post-durable-commit cleanup, before the notice is confirmed, over a real pre-guard archive and store. It subclasses the real guard and does not replace its commit point. The separate series-generation fixture patches `direct_landing_operation.confirm_notice` to raise `_ProcessCut`; neither setup is an OS death. The cases show a native failure rolling the whole publication
back, a notice failure leaving the native success standing, a pre-success archive keeping the intent pending,
and only the exact outcome receipt proving native success.

The crash matrix adds the two after-cut situations: an abandonment after the native commit publishes once, and a
series generation after collection settling `PUBLISHED` for its own generation while a wrong one is `REFUTED`.

A separate current-generation regression creates and replaces generations through the native operation store/runtime, then faults only the current journal read while its predecessor remains readable. Root-bearing and legacy intent resolution both stay undecided; the stored original occurrence remains pending without publication. Restoring readability and settling twice publishes that occurrence once. This uses a patched in-process confirmation cut and a selective read fault, not an OS process kill or a live-host witness.

The admitted no-remains fixture has no locator or enclosure worktree. Its cases check one typed receipt and one occurrence across success/retry; exact task/master/contract restoration and intent removal on contract or receipt-write failure; and a controlled postcommit-before-confirmation interruption. Recovery interleaved after receipt rename remains undecided while publication holds the lease. Missing, oversized or wrongly typed/path/lifecycle/digest/note proof stays undecided; restoring the exact receipt lets repeated settlement publish the original occurrence once. These are in-process fault/confirmation cuts, not OS death or live-host witnesses. Recovery remains subject to the disposable notice store's existing retention and eviction limits.

## Evidence boundary

Source-level pytest cases at the reviewed freeze, not a live-page witness and no measurement: MIK-R200 evidence
item 6 is unrun and carried to L36, item 7 unrun.

## Evidence


- The controlled current-journal read fault leaves both root-bearing and legacy resolution undecided, retains the stored occurrence, then publishes that original occurrence once after readable restoration. [1]
