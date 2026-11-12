# mcp/src/agents_remember/serving/explainer_watcher.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The moved watcher: whether a leaf has moved past the comparison its explainer is bound to, how many review blocks changed, and the one line the page and the stream show — answered without waking the explainer.

## Code Commentary

- `measure_notice` answers moved, clean or unreadable, and every unreadable input answers no notice: a watcher that cannot tell neither claims the leaf moved nor claims it did not.
- The capture is the comparison owner's own draft — it derives the candidate tree and drafts the four trees in memory, pinning no ref and writing no comparison record, because recording belongs to Update.
- The block count is the review lane's own: one per changed text hunk plus one per non-text change, the identities the fingerprints use, so no second diff engine exists here.
- A planning leaf's binding is measured against the master line's tips and captures nothing; the line that still holds the bound commit is followed rather than a guess between the contract's two names.
- `MoveNoticeChannel` is in-process and bounded: one latest notice per leaf, a queue of eight per subscriber with the oldest dropped, publishing deduplicated so a reconnecting page is not told twice, and a cleared notice that reads `current`.
- The channel sends no message, holds nothing and writes nothing, and `leaf_seats` lists each watched leaf's explainer generation and its leaf-role seats from receipts and role records, listing a master's own folder rather than walking the task tree.

For an actively watched leaf without an explainer environment, `unexplained_turn_notice` captures through the same owner and compares a kept baseline or the latest recorded comparison. Equal trees produce no notice; movement produces `has_explainer=false` with no Update offer. This provisional path uses at least one block when no prior comparison or reliable count exists, so that number is a notification signal rather than a measured exact hunk total. Seat discovery includes current explainer generations and receipt/role seats for active environments or explicitly watched streams. The channel keys notices and subscribers by exact repository/master/leaf, admits only a bounded latest history and removes subscriptions in the listener's `finally`.

## Evidence

- An unreadable environment or capture answers no notice at all [1]
- The capture records nothing and pins no ref [2]
- The changed-block count comes from the review lane's own hunks and non-text changes [3]
- The master line is followed at the tip of the line that still holds the bound commit [4]
- Notices are held in process, bounded per subscriber and deduplicated [5]
- Seat discovery lists watched leaves' own folders rather than walking the task tree [6]

- The no-environment turn-end path retains a baseline and offers no Update, with an explicit provisional block minimum; exact-leaf subscriptions and latest history remain bounded and close-owned. 

- The no-environment turn-end path retains a baseline and offers no Update, with an explicit provisional block minimum; exact-leaf subscriptions and latest history remain bounded and close-owned. [7]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/explainer_watcher.py::leaf_seats - the bytes it recorded now occur 5 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/explainer_watcher.py::unexplained_turn_notice - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
