# mcp/src/agents_remember/application/review_change_kinds.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Server-side change-kind facts from one recorded comparison. `with_change_kinds` enriches only the
family/member occurrences returned in its supplied context. The additional `implementation_facts`
entry point instead enumerates invariant identities found in realization/proof entries on either
readable index for the leaf-wide code-fact view. Returned-members-only is therefore a boundary of
family enrichment, not a promise about every public function in this module.

## Code Commentary

### Logic

`with_change_kinds` returns its input unchanged when no comparison or no entries were supplied. Otherwise
it opens one lane, computes each returned family and replaces only the context entries. Lane/index
failures at this boundary produce explicit unknown family/member facts with a bounded reason.
No absent-tree call becomes an alternate dataset-review mode.

The shared `RecordChanges` owner decides intent, guarantee and membership. The local family adapter
maps added/removed/changed guarantees to its `intent` badge; unknown/unchanged keep their meaning.
Member identity and authored position, implementation facts, evidence shaping and local path caches
remain here. Family totals are deduplicated live-member unions; unread own family/member records
make the total unknown rather than an invented complete count.

Implementation is established by added/retired/nonmechanically reanchored entries or by the lane's
actual hunk/file links. Proof entries mark test involvement; they do not confer semantic approval.
An unresolved entry range on a changed side adds unknown even beside an established implementation
fact. Unknown reasons and membership reasons remain distinct and bounded.

The optional shared `WorklistClassification` changes how computation is obtained, not who defines
reviewer attribution. `_file` projects a supplied computed path through `lane.from_worklist`, falling
back to `lane.classify` only when that path is absent, and memoizes the result or failure locally.
`_base_class` reuses the supplied classifier only when its indexed base entry equals the current one;
otherwise it constructs the existing single-entry classifier. The lane still withholds ranges not
recorded at that side's exact blob.

`implementation_facts` sorts the deduplicated indexed invariant identities, calls the same local
implementation owner and emits projected identity keys, state, proof/range flags and bounded evidence
and unknown reasons. It does not itself read a family roster, select a subject or certify whole-side
availability; its `review_code_changes` caller owns aggregate availability preflight.

### Conventions

`Fact`, `Known`, `RecordChanges` and `problems` are imported from the shared recorded-meaning module.
The two entry points have different populations. Shared classification is request-owned input,
not a persistent cache or serialized result, and no new independent hunk arithmetic is introduced.

### Invariants And Boundaries

Recorded facts, unavailable/unknown states, gate classifications and semantic verdicts remain separate.
A missing index is not evidence of unchanged knowledge. Stored legacy test/mutation/census statements
in the historical quotation below are their original evidence only, not freshly executed acceptance.

### Todos

No new execution or installed-delivery claim is made by this source-bound examination.

## Historical source-epoch account — superseded where different

The quotation preserves original explanatory detail, prior candidates and producer/test observations.
Its outdated population, no-snapshot, state/count and computation-placement claims are **not** active
contracts; the current source account and renewed evidence govern. No historical grade is renewed.

> ## Purpose
>
> **The change-kind facts of a tree comparison's family context, computed on the server for the members a roster page
> returned (MIK-R33, adopting ICR-R32@v1 rule 1).** `with_change_kinds(context, trees)` is the one entry point:
> `knowledge_review.compose_review` passes the composed family context through it, and each family entry comes back
> carrying `change_kinds` (`models/knowledge/review_change_kinds.ReviewFamilyChanges`): the fact of the family's own
> guarantee, the deduplicated member total, and one `ReviewMemberChange` per returned member occurrence. A dataset review
> (`trees` is `None`) gets its context back exactly as composed, so nothing here runs before a converted leaf's tree
> comparison (inert until MIK-R37). The browser orders, counts and traverses by these facts and never recomputes one.
>
> `review_change_kinds` computes the MIK-R33 change-kind facts of a tree comparison's family context for the members a roster page returned: intent, implementation and membership per member occurrence, travelling on each family context entry for the browser to order and traverse by. In W03 the recorded-meaning facts (guarantee, intent, membership) are delegated to the shared `RecordChanges`, so the detail badges and the navigation outline use one definition.
> ## Code Commentary
>
> ### Logic
>
> - **One lane per read.** `with_change_kinds` opens MIK-L32's `open_tree_lane(trees)` once and builds `_ChangeKinds`
>   over it: both memory sides are read through the lane's derived indexes, and every hunk intersection comes from
>   `TreeLane.classify(change)`, memoized per changed path (`_file`). There is no second hunk classifier and no range
>   arithmetic here (ruling 2026-09-30T15:11:20). If the trees cannot be read or compared (`LaneReadError`,
>   `apsw.Error`), every family and every returned member is `unknown`, with the bounded error as the reason (`_unread`).
> - **Returned members only.** `_returned` takes each member occurrence once by the roster's `member_id` (the same on
>   both sides for one invariant under one family), so a revised member's two revision rows share one fact set and a
>   member no page returned is never described (ICR-R32 rule 5).
> - **`intent` (`_intent` → shared `RecordChanges.intent`).** The shared index-only owner compares
>   live/retired presence, revision and byte-for-byte `statement`, `applicability`, `conditions` and
>   `exclusions`. A same-revision wording difference sets `text_differs` and establishes intent;
>   presence/wording helpers are not local `_presence`, `_WORDING` or `_wording` declarations here.
> - **`implementation` (a) (`_entry_changes`).** An entry of the member added, retired or re-anchored between the sides.
>   A changed anchor is a re-anchor unless it is the writer's mechanical carry (`classify.carried_mechanically` with the
>   worklist `Classifier`'s class of the K_B entry, `_base_class`): of MIK-R08 definition 7's exemptions only that one is
>   kept, because `touched`, `moved_or_absent` and `stale_at_base` exist for the worklist's own covering items (review R1
>   F1, ruling 17:47:43). A repair of an entry already stale at the base reads "re-anchored (stale at base)" (ruling
>   18:57:45). An undecidable class (a `CodeReadError`, an unparseable entry) leaves the fact `unknown`.
> - **`implementation` (b) (`_hunks`, `_hunk_linked`).** Only changed paths where the member records an entry are
>   classified, so a linked file in the inventory establishes nothing by itself. A hunk the lane links to an entry of
>   the member establishes the fact; a proof entry counts and marks `test`. **Definition 8 (`_file_covered`):** on a
>   changed non-text file a `file` entry of the member establishes it through the worklist's own `non_text_linked`
>   (ruling 16:22:22 item 6b); a resolved non-file entry there stays `unknown` unless the fact is established
>   (`_unintersectable`).
> - **The unconditional unknown (`_unresolved`, review R1 F4).** An entry of the member on a side where the changed file
>   changes lines (or whose content changed as non-text) that supplies no range there, or whose side's knowledge is
>   unavailable, sets `range_unresolved`, so the `unknown` mark is added even beside an established `implementation`.
>   `_withheld` words the lane's per-entry reason for a reviewer (the recorded and side blobs for
>   `recorded_blob_mismatch`; plain words plus the code for `path_absent`, `unresolved`, `unsupported_locator`,
>   `unreadable`).
> - **`membership` (`_membership`).** Whether this family's record lists the invariant on each side; unknown when a
>   side's family record cannot be read.
> - **Reasons (shared `Fact.reasons`, local `_member`).** Each unknown fact names why; unresolved
>   reasons for entries that established nothing come first. The local member assembly keeps
>   change-kind and membership reasons apart and names bounded evidence only for established facts.
> - **Family level.** `_guarantee`: `intent` when the `guarantee` text differs or the family is live on one side only,
>   `unchanged` when the same, `unknown` when a side cannot be read. `_members_total`: the deduplicated union of live
>   members on either side, `None` only when the family's own record file or a listed member's own file fails to parse
>   (`_own_problem`, review R1 note). `_position`: the invariant's index in the family record's authored `members` (after
>   side, else before), the tree's authored order (ruling 16:22:22 item 7).
>
> ### Conventions
>
> - `_ChangeKinds` retains the lane, local implementation caches and a shared `RecordChanges`
>   reader. `Fact` and `Known` are imported from `review_record_changes.py`, not local dataclasses.
>   `with_change_kinds` remains the public entry. Shared recorded-meaning reasons and local
>   implementation/evidence reasons remain bounded; `ReviewMemberChange.of` derives primary/marks.
> - The current module is 538 lines, under the 1,200-line limit.
>
> ### Invariants And Boundaries
>
> - **Candidate invariant (not ingested; no speculative ingestion): change-kind facts are computed on the server, for
>   returned members only, from recorded comparison facts; the hunk intersection comes only from MIK-L32's
>   classification, and the client never recomputes it.** Realized by `with_change_kinds` (one `open_tree_lane` per
>   read), `_returned`, `_hunk_linked` over `TreeLane.classify`, and the entry validator in `review_family_context.py`
>   that requires facts for exactly the returned members. Proved by `test_review_change_kinds.py`
>   (`test_a_partial_page_describes_only_the_members_it_returned`,
>   `test_the_facts_are_derived_and_describe_exactly_the_returned_members`), the worker's real-data reconciliation (every
>   hunk-established fact is a link in `classify_changed_path` for its path, 2 of 2), and mutations "the validator no
>   longer checks the returned members" and "a proof link establishes nothing", both caught.
> - **Candidate invariant (not ingested): unreadable or partial knowledge produces `unknown` with a stated reason, never
>   `unchanged` or a complete-looking total.** Realized by `_unread`, `_record`'s parse-problem answer, `_entries`'
>   unparsed-sidecar answer, `_unresolved`, `_unintersectable`, `_members_total` returning `None`, and the model's
>   `_unknowns_say_why`. Proved by `test_an_unreadable_sidecar_leaves_implementation_unknown_never_unchanged`,
>   `test_an_unreadable_family_record_leaves_guarantee_and_membership_unknown`,
>   `test_trees_that_cannot_be_read_make_every_fact_unknown`,
>   `test_an_unread_sidecar_of_a_changed_file_marks_unknown_beside_an_established_fact` and
>   `test_the_total_is_unknown_only_when_the_familys_own_records_fail`, with the mutations "an unparsed sidecar is
>   ignored", "an unread family record reads unchanged" and "a withheld range leaves nothing unknown", all caught.
> - **Candidate invariant (not ingested): changed intent text is never `unchanged`, even at the same revision.**
>   Realized by `_intent` delegating to `RecordChanges.intent` and its shared `wording` comparison with `text_differs`. Proved by
>   `test_every_member_occurrence_carries_its_kind_from_the_recorded_comparison` (INV-PPPPPP reworded in
>   `applicability` reads `intent` with `text_differs`, INV-EEEEEE beside it reads `unchanged`), and the mutation "a
>   same-revision text change reads unchanged", caught.
> - Nothing here is a verdict, a risk score or an assessment (ICR-R32 Exclusions).
>
> ### Todos
>
> - **Pre-curation unknowns are the lane's literal rule** (ruling 16:22:22 item 4): until an uncurated leaf's entries in
>   changed files are re-recorded at the candidate blob, they supply no range there and mark `unknown`. On the worker's
>   real scratch, FAM-R6R095RW read 7 unknown before curation and 0 after (three `+unknown` marks remained for entries
>   recorded at an older before-side blob, MIK-L32's Q2, carried to L37).
> - Review R2-4 (accepted as a note): the presence facts (`intent`, `guarantee`, `membership`) still use `_record`'s broad
>   rule, so a missing record reads `unknown` when any record of that kind fails to parse on that side; only the total
>   was narrowed. This is honest and never `unchanged`.
> - Review R3-2 (accepted): when the whole comparison or an invariant identity cannot be read, `unknown_reasons` and
>   `membership_reasons` carry the same detail, which the tree draws as two lines for two unknown facts.
>
> `_ChangeKinds` holds `meaning: RecordChanges` beside the lane. `_guarantee` maps shared `added`/`removed`/`changed` results to the detail badge word `intent`, while `unknown` and `unchanged` remain unchanged; the outline may retain added/removed/changed, so the two vocabularies are not identical. `_intent` and `_membership` return the shared facts directly. Member identity/authored position, implementation facts over realization/proof entries and lane hunks, evidence shaping and unread-side fallback stay local. The public entry and refusal behavior remain unchanged.

## Evidence

### Docs References

No configured domain-documentation source was available; these implementation claims use the direct
repository sources below, not a source registry or a copied code comment as independent authority.

### Repo-Internal References

- The module describes family occurrence facts and the new leaf-wide implementation-fact view, both from recorded comparison inputs. [1]
- The unconditional unknown for an unresolved range, the lane's reason in a reviewer's words, and a non-file entry at a non-text change. [10]
- Base-entry class reuse requires an equal indexed base entry; absent/mismatched shared classification falls back to the local one-entry classifier. [11]
- Records and entries read through each side's index; an unparsed record or sidecar answers why instead. [12]
- Change inventory and per-path results are memoized locally; supplied computed paths project through from_worklist, otherwise the lane classifies. [13]
- The composed subject review passes its family context through the family-enrichment entry point; this is not the module sole caller after leaf-wide facts were added. [14]
- Fact, Known, RecordChanges and problems are imported from the shared recorded-meaning owner. [15]
- The comparison reader carries optional shared classification beside its recorded-meaning reader. [16]
- The family badge maps the shared guarantee onto badge words [17]
- Member intent and membership are the shared facts directly [18]
- The shared intent, presence and wording functions decide revision, retired-presence and same-revision authored-text changes. [19]
- Family enrichment returns the context untouched without trees/entries; opened-lane failures mark returned family/member facts unknown, not a dataset-review mode. [2]
- The shared intent, presence and wording functions decide revision, retired-presence and same-revision authored-text changes. [20]
- The shared intent, presence and wording functions decide revision, retired-presence and same-revision authored-text changes. [21]
- Shared Fact retains established/unknown/not_established states and prioritizes unresolved reasons from non-establishing entries. [3]
- The family's own row and its total over the family's own records (review R1 note). [4]
- One member occurrence: three facts, bounded evidence, and the change kind's reasons apart from the membership's. [5]
- Local intent delegates to the shared recorded-meaning implementation. [6]
- Membership on each side of this family's record. [7]
- Implementation (a): added, retired or re-anchored; only the mechanical carry is exempt (review R1 F1); stale-at-base repairs worded apart. [8]
- Implementation (b) through the lane's links only, and definition 8 on a changed non-text file. [9]
- Leaf-wide implementation facts enumerate sorted invariant identities from realization/proof entries on either readable index, reuse the family implementation owner and bound evidence/reason excerpts. [22]

### Cross-Repo References

No new cross-repository boundary is introduced by these helpers.
