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

`__all__` (`:62-72`) publishes the version and selection-rule literals, the record and its verdict
vocabulary, the channel-match and knowledge-state literals, the observation model, and the three rule
functions. `REVIEW_SYNC_REBINDING_VERSION` (`:76-78`) is a literal of this vocabulary's own rather than a
package version read at run time, so two rebindings produced by different layouts are distinguishable from
the records themselves; `REVIEW_SYNC_SELECTION_RULE` (`:80-82`) spells which generation a rebinding judges
so a reader of the record does not have to import the owner that produced it. `SyncChannelMatch` (`:88`),
`ReviewSyncRebindingVerdict` (`:97`) and `SyncKnowledgeState` (`:104`) are the three literals the rules
answer in, each carrying in its own comment why its members are the ones they are. Every pattern
(`GIT_OBJECT_PATTERN`, `SHA256_PATTERN`, `UUID_PATTERN`) and every bound (`PROSE_MAX_LENGTH`,
`PATH_MAX_LENGTH`, `LABEL_MAX_LENGTH`) comes from the shared base module.
### Invariants And Boundaries

- Currency requires a measured match on both code and memory trees.
- The complete source comparison and digest prevent rebinding to another reviewed pair.
- Missing capture remains unmeasured rather than an empty tree or guessed current selection.
- successor_action names the ordinary successor tree comparison; this value writes none.
- **`unmeasured` is never coverage.** It appears only where a comparison could not be made, and `current`
  requires a measured match on every channel the generation retained.
### Todos

None recorded.
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
- The published surface: the two literals, the three vocabularies, the observation model and the three rules. [23]
- The record's own version literal, so records from different layouts are distinguishable. [24]
- Which generation a rebinding judges, spelled here so a reader need not import the selecting owner. [25]
- **The channel-match vocabulary, including why `selected-not-retained` is a fact about the review rather than a third mismatch.** [26]
- **The three-value verdict, and the reason `unmeasured` is neither coverage nor a measured difference.** [27]
- The two states a knowledge channel can hold instead of a readable dataset. [28]
- **The code channel: a pure comparison of two identities one owner produced.** [29]
- **The knowledge channel: `unmeasured` whenever one side is not a dataset at all, and never an agreement.** [30]
- **What the declared location held, with an identity carried exactly when a dataset was read.** [31]
- **The self-consistency validator, including the refusal of an `unmeasured` channel beside a readable dataset.** [32]
- The one predicate a consumer branches on instead of re-deriving the verdict rule. [33]
- The durable publication and read-back the record travels through. [34]
- **The case that forges this record's verdict and shows the validator refusing it.** [35]
