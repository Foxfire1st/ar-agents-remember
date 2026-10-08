# mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The v2 managed-sync rebinding record binds the complete retained tree comparison to the exact code/memory pair a sync resolved. The value makes a transition readable; it grants no clearance and performs no recovery.

## Code Commentary

### Logic

ReviewSyncRebinding carries ReviewTreeComparisonRecord and its complete-record digest, the resolved code head/tree and optional memory head/tree, both channel matches, the measured state and successor_action. The memory head and tree are present together. Its validator requires the source comparison's leaf and digest, derives both matches from the exact retained candidate trees, and applies tree_sync_verdict.

tree_sync_verdict reports moved on a measured difference, unmeasured on an uncompared channel, and current only for an exact match on both captured trees. covers_resolved_pair is true only for current. Missing memory capture carries memory_detail and never becomes code-only tree-pair coverage.

The statement derives the reviewed and resolved trees and their measured matches. A dirty capture is the tree the existing capture owner observed; the head locates it and is not a substitute for it. The application records through record_review_sync_rebinding and reads through its retained-record route.

### Invariants And Boundaries

- Currency requires a measured match on both code and memory trees.
- The complete source comparison and digest prevent rebinding to another reviewed pair.
- Missing capture remains unmeasured rather than an empty tree or guessed current selection.
- successor_action names the ordinary successor tree comparison; this value writes none.

### Historical boundary — MIK-R26

LegacyReviewSyncRebinding decodes v1 generation/dataset evidence without rewriting it. Its original verdict remains historical fact, but covers_resolved_pair is false because it recorded no exact reviewed memory tree. It cannot certify a v2 tree pair.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstrings, fields and validators. The three
details a reader should carry: **the verdict has three values and only `current` claims coverage**;
**`unmeasured` is not a softer `moved`** but the honest answer for a channel that was never compared; and
**the record validates itself from its own fields**, so an internally inconsistent success cannot be
constructed.


- The v2 value retains the complete reviewed tree comparison and exact post-sync pair. [1]


- The tree-sync rule requires both exact matches for current. [10]


- The validator checks source leaf/digest, paired memory head/tree and both matches. [13]


- Only a current v2 pair measurement covers the resolved pair. [14]


- The generated sentence names the complete reviewed and resolved pair. [15]


- The actual source-bound producer captures owner inputs and constructs the v2 value. [18]

- The durable publication and read-back the record travels through. [19]
- **The read half that projects this record's own verdict into the review's measured-currentness vocabulary.** [20]

- Tests measure exact pair, memory-only movement, capture absence and legacy noncoverage. [22]


### Cross-Repo References

No cross-repository behavior is implemented in this file. Every identity it carries was produced inside
the contract's own repository boundary; the one absolute path it does not carry — the publication location
— is resolved by its owner at read time and is reported there.

No meaningful cross-repo references found.
