# mcp/tests/test_reference_anchor_owner_ledger.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_reference_anchor_owner_ledger.py` extends the publication-owner coverage to the entries the review still owed (`L191-PRE-04`): `closeout.closeout_result` on a fresh apply over the converted closeout gate's own world and on its recovered-output branch, `direct_landing_tool`, and the closeout's selected memory-quality phase. A narrower check is not an anchor waiver, and a pair a rerun resumes on is judged rather than trusted.

## Code Commentary

The fault is built, not injected: `tools/policy.py` is committed on the leaf's code side, `anchor_at` hashes it into the real repository, and the card cites it at a `symbol` locator whose bytes a later commit leaves untouched while the file blob moves. Each branch runs twice over two builds of the same fixture — healthy, where the entry publishes and the fixture is shown publishable, and faulted, where only the anchor is stale. `_apply` stubs exactly the authorities the fixture lacks (enclosure admission, settings, branch authority) and leaves the preflight gate, the validator at the commit, both commits, the closing write and the contract finalization live. `_named_findings` reads one entry per finding line, so a refusal that also withheld a worklist row cannot read as an anchor-only refusal; it is compared to `[RULE]` in every refusal. The no-op case re-bases the leaf onto the code it describes and closes the history in memory, so the closeout owes no commit on either side and still refuses the tree it records; route indexes are brought current first so the closing write really is empty.

## Evidence

- A fresh closeout refuses the stale anchor with only that rule named, changes neither worktree nor the contract, and publishes after the repair [1]
- A recovered-closeout output is judged, so a stale resumed commit refuses and the repaired one is recorded [2]
- Direct landing refuses the stale pair, leaves the memory branch, and lands the repaired pair with its closed history [3]
- A selected style phase passes over the stale world while the publication still refuses [4]
- A closeout with nothing left to commit still refuses the tree it records [5]
