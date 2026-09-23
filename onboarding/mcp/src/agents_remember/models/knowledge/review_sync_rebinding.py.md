# mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T17:15:00+02:00 |
| lastVerifiedCommitHash | `473ad8242bb4c22bdabed5d5253767350381eb3e` |
| lastVerifiedCommitDate | 2026-09-23T17:26:55+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The typed record binding one comparison generation to the pair a managed sync resolved (ICR-R22@v1).**
A comparison generation records what a review *read* — the candidate source tree captured from the leaf's
own worktree, and the knowledge dataset the review compared. A managed sync then moves both: the work
branch is carried onto the official line, so the leaf's `HEAD` is the merge commit rather than the head
the review captured, and the published dataset is the union the merge produced rather than the dataset the
review compared. This module owns the value that makes that transition readable, and exactly three things:

| Owned thing | Operation | What it answers |
| --- | --- | --- |
| **The record** | `ReviewSyncRebinding` (`:193-390`) | the generation the review published, the pair each side holds after the sync, the match each channel earned, and one verdict |
| **The one verdict rule** | `review_sync_verdict` (`:142-161`) | whether the reviewed comparison still describes the resolved pair, is a measured mismatch, or could not be compared at all |
| **The two channel rules** | `code_channel_match` (`:107-117`); `knowledge_channel_match` (`:120-139`) | whether each side's post-sync identity is the identity the review recorded, measured only |

**Every field is an identity an owner produced.** The reviewed identities are read from the generation's
own sealed manifest, the resolved source side from the shipped capture owner, and the resolved knowledge
side from the route that resolves the repository's declared publication location. A reader compares the
record's own values instead of trusting a sentence about them, and the one sentence the record publishes,
`statement` (`:312-340`), is derived from those values and cannot outrun them.

**The verdict can only claim coverage it measured.** `current` is the single value that says the reviewed
generation still describes the resolved pair, and it requires a *measured* match on every channel the
generation actually retained. `moved` is a measured difference on either channel. `unmeasured` is the
honest answer for a retained knowledge operand that could not be compared at all — the declared location
held nothing this code can read — and it is **not** a softer `moved`: it is never coverage, and the
validator refuses it beside a location that did hold a readable dataset.

**This record supersedes; it does not replace.** It changes no dataset, publishes no successor generation
and grants no clearance. The successor is a normal freeze whose lineage names the judged generation as its
predecessor, and `successor_action` names that call. A record that overwrote the generation it judged, or
that re-ran the comparison itself, would be the parallel review authority the packet forbids.

## Code Commentary

### Logic

**The code channel is a pure comparison of two identities one owner produced.**
`code_channel_match` (`:107-117`) compares the reviewed candidate tree with the resolved candidate tree and
answers `matches-reviewed-input` or `differs-from-reviewed-input`; it is re-derivable from the record alone,
without reopening either tree.

**The knowledge channel answers `unmeasured` whenever one side is not a dataset at all.**
`knowledge_channel_match` (`:120-139`) returns `unmeasured` when the generation did not retain a knowledge
operand or the declared location did not answer with a readable dataset, and `unmeasured` is never
`matches-reviewed-input`: nothing was compared, so reporting a difference — or an agreement — between two
things that were never both read would be inventing an observation.

**One rule decides the verdict, and the validator asks the same function.**
`review_sync_verdict` (`:142-161`) answers `moved` on a measured difference on either channel; otherwise
`unmeasured` when the generation **retained** a knowledge operand that was never compared; otherwise
`current`. A generation that retained no knowledge operand has nothing to leave unmeasured, so its source
channel alone can make it `current` — which is exactly what it recorded.

**What the declared location held is carried as the route's own answer.**
`SyncKnowledgeObservation` (`:164-190`) holds a three-state `state` (`published`, `not-recorded`,
`unusable`), the dataset identity **exactly when one was read**, and the path and detail the read route
itself produced. Its validator refuses both directions of the mismatch: an identity beside a location that
was not read, and a published location with nothing behind it.

**The record validates itself against its own fields, so a false success cannot be manufactured.**
`ReviewSyncRebinding` (`:193-390`) carries the judged generation's id, index, binding digest and manifest
digest, the reviewed baseline and candidate trees, the reviewed knowledge state and its digest, the
resolved source head and candidate tree, the resolved knowledge observation, both channel matches, the
verdict and the successor action. `_the_rebinding_agrees_with_itself` (`:242-300`) re-derives each channel
rule and the verdict from those fields and refuses a record that disagrees, including the case of a
knowledge channel recorded `unmeasured` beside a location reported as holding a readable dataset: the code
states plainly that reading such a record as consistent is how a false success is manufactured.

**The sentence has one clause per verdict, and each says only what was measured.**
`statement` (`:312-340`) composes the record's own identities with `_code_clause` (`:342-363`) and
`_knowledge_clause` (`:365-390`). `_code_clause` names the capture as **located at** the work branch head
rather than carried by it — the resolved candidate is the capture owner's add-all tree computed in an
isolated index, so it equals the head's own tree only while the worktree is clean, and the state where it
does not is exactly the state the packet requires a sync to preserve. `_knowledge_clause` never claims an
unmeasured comparison: a generation that recorded no knowledge operand says so, and a location that
answered nothing says that instead.

**Consumers branch on one predicate.** `covers_resolved_pair` (`:302-310`) exists so a reader asks the
record whether it established coverage rather than re-deriving the rule from `state`.

### Conventions

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

- **`unmeasured` is never coverage.** It appears only where a comparison could not be made, and `current`
  requires a measured match on every channel the generation retained.
- **A resolved identity travels only on the channel that moved** — a channel that still matches, was never
  compared, or could not be read has no resolved value to report, and inventing one is the fabricated
  identity this vocabulary exists to refuse.
- **The reviewed digest is named exactly when the generation retained one**, and the validator ties that
  both ways.
- **The record carries, never recomputes, the generation's identities.** Ids, indices, seals and digests
  are copied from the sealed manifest; a digest derived here would be a second identity.
- **Boundary: the record records a supersession and performs none.** The remedy is a successor generation
  frozen by the freeze owner with this generation as its `parent`; an earlier receipt's or record's bytes
  are never rewritten here.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the module's own docstrings, fields and validators. The three
details a reader should carry: **the verdict has three values and only `current` claims coverage**;
**`unmeasured` is not a softer `moved`** but the honest answer for a channel that was never compared; and
**the record validates itself from its own fields**, so an internally inconsistent success cannot be
constructed.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the transition it makes readable, the owner-produced fields, and why the verdict can only claim measured coverage.** | `ReviewSyncRebinding` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:1-43; mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:193-390 |
| The published surface: the two literals, the three vocabularies, the observation model and the three rules. | `__all__` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:62-72 |
| The record's own version literal, so records from different layouts are distinguishable. | `REVIEW_SYNC_REBINDING_VERSION` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:74-78 |
| Which generation a rebinding judges, spelled here so a reader need not import the selecting owner. | `REVIEW_SYNC_SELECTION_RULE` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:80-82 |
| **The channel-match vocabulary, including why `selected-not-retained` is a fact about the review rather than a third mismatch.** | `SyncChannelMatch` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:84-88 |
| **The three-value verdict, and the reason `unmeasured` is neither coverage nor a measured difference.** | `ReviewSyncRebindingVerdict` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:90-97 |
| The two states a knowledge channel can hold instead of a readable dataset. | `SyncKnowledgeState` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:99-104 |
| **The code channel: a pure comparison of two identities one owner produced.** | `code_channel_match` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:107-117 |
| **The knowledge channel: `unmeasured` whenever one side is not a dataset at all, and never an agreement.** | `knowledge_channel_match` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:120-139 |
| **The one verdict rule, shared by the writer and the record's own validator.** | `review_sync_verdict` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:142-161 |
| **What the declared location held, with an identity carried exactly when a dataset was read.** | `SyncKnowledgeObservation` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:164-190 |
| **The record itself: every owner-produced identity, both channel matches, the verdict and the successor action.** | `ReviewSyncRebinding` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:193-240 |
| **The self-consistency validator, including the refusal of an `unmeasured` channel beside a readable dataset.** | `_the_rebinding_agrees_with_itself` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:242-300 |
| The one predicate a consumer branches on instead of re-deriving the verdict rule. | `covers_resolved_pair` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:302-310 |
| **The sentence: one clause per verdict, each saying only what the record measured.** | `statement` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:312-340 |
| **The source clause that names the head as where the capture was taken, not as what carries it.** | `_code_clause` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:342-363 |
| **The knowledge clause, which never claims a comparison nobody made.** | `_knowledge_clause` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:365-390 |
| **The writer that assembles this record from the owners' values and asks this module's rule for the state.** | `_assemble` | mcp/src/agents_remember/application/review_sync_rebinding.py:641-678 |
| The durable publication and read-back the record travels through. | `publish_durable_evidence`; `read_back_evidence` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:137-166; mcp/src/agents_remember/memory/knowledge/durable_evidence.py:169-203 |
| **The read half that projects this record's own verdict into the review's measured-currentness vocabulary.** | `_project` | mcp/src/agents_remember/application/review_sync_movement.py:165-213 |
| The successor route this record's remedy names and never performs. | `freeze_review_comparison` | mcp/src/agents_remember/application/review_comparison_freeze.py:232-276 |
| **The case that forges this record's verdict and shows the validator refusing it.** | `test_a_forged_rebinding_verdict_is_refused_by_the_record_itself` | mcp/tests/test_review_sync_rebinding.py:514-634 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every identity it carries was produced inside
the contract's own repository boundary; the one absolute path it does not carry — the publication location
— is resolved by its owner at read time and is reported there.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee`): created this one-to-one card for the module this leaf introduced as **ICR-R22@v1's record vocabulary** — the value that binds one comparison generation to the exactly resolved source/knowledge pair a managed sync produced. It records what a consumer has to act on: the verdict has **three** values and only `current` claims coverage, so it requires a measured match on every channel the generation actually retained; `unmeasured` is the honest answer for a retained knowledge operand that could not be compared and is **never** a softer `moved`; every field is an identity an owner produced (the sealed manifest, the shipped capture owner, the publication route) rather than a derivation of this module's; and the record validates itself from its own fields, so an inconsistent success cannot be manufactured — reading one as consistent is, in the code's own words, how a false success is made. Two boundaries are carried as boundaries and not as defects: the one sentence is derived from the fields and cannot outrun them, in particular the source clause names the work branch head as **where the capture was taken** rather than as what carries the add-all tree, which Git denies in exactly the WIP-restored state the packet requires a sync to preserve; and the record records a supersession and performs none, leaving the successor to the freeze owner. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `e605822eb3bf83bf63a45963c5f51d5fc28859ee`, this leaf's recorded base — because every construct cited here exists only in this leaf's uncommitted working tree; what was actually read is that working tree, and the governed closeout owns the real stamp once the code commit exists.
