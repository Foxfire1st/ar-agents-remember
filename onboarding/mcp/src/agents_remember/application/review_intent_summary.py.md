# mcp/src/agents_remember/application/review_intent_summary.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The one owner of the changed-intent summary**: the two numbers the task entry's compact
`⇄ Intent review +N −N` control shows before the reviewer is opened (`ICR-R24@v3`, leaf
`260921-ICR-L47`). The numbers describe the **authored intent** of the comparison the entry opens — not
the change set's line totals (which the entry used to show by reusing the change-set button) and not
the subject catalogue's identity totals (which enumerate subjects without comparing them).

It answers over the reviewer's own resolution, so the entry cannot count a different pair from the one
it opens: `read_review_intent_summary` resolves the canonical task context through
`resolve_review_candidate` (a closed leaf resolves to its recorded comparison, `ICR-R12`), and
`intent_summary_of` refuses the pair through the shared
[`review_pair_preflight`](review_pair_preflight.py.md) before its count reads. The catalogue and summary share that pair-admission owner; a later
storage failure is still handled as unavailable rather than a guarantee against all temporal disagreement.

**Since MIK-L32 a tree comparison's summary also carries `attribution`** (MIK-R32 rule 9): after
`intent_summary_of` answers, `read_review_intent_summary` adds `lane_summary(resolved.trees)` from
[`review_unexplained_lane.py`](review_unexplained_lane.py.md), the unexplained-changes lane's file-level count over the
same resolved trees, in the same request. The entry therefore asks for it exactly when it asks for the intent counts,
and never more eagerly. It is attached whatever the intent counts' own state (ruling 2026-09-30T12:19:20 Q6: it is
read from the trees directly and is true on its own). A dataset comparison (`resolved.trees is None`) carries none.

`unexplained_open` is now attached beside attribution through `stored_unexplained_open`. The
optional reader admits only complete stored work bound to the exact comparison and with no undecided
unexplained hunk/file verdict. It counts gate-open items, not raw file attribution, and returns None
for missing, unreadable, incomplete, mismatched or undecidable work. This auxiliary value can remain
meaningful independently of the authored-intent result; it is never added to plus/minus.

## Code Commentary

### Logic

**Count semantics (master decision on count semantics, `task.json`, entry labelled 12:00 and
clock-corrected by the 12:10:21 entry; refined by the leaf's 16:15:11 ruling on L47-R1-F3).**

- The current text-record projection supplies one revision per identity. `_heads` reuses
  `review_revision_comparison.revision_heads` as deterministic sorting of the supplied population,
  not graph-head discovery. The subject reviewer separately takes the matching projected record
  on each side; no multi-head or intermediate-revision selector is restored by this summary.
- `+` (`added`) counts invariant and family (joint-guarantee) heads **only the after side holds**; `−`
  (`removed`) counts heads **only the before side holds**. A revised statement is one of each, so it
  counts once on each side. An identity is counted once however many families hold it (memberships
  are compared by canonical invariant identity).
- **Every successor revision counts**, including a record-only successor whose text is unchanged and
  only its origin state, acceptance reference or version moved (`_STATEMENT_FIELDS` includes
  `state_at_origin` and `acceptance_ref`; `_GUARANTEE_FIELDS` is `joint_guarantee`, `state_at_origin`,
  `acceptance_ref`). The one exclusion is a successor whose compared fields are **equal** to the
  superseded head's while its attached relationships differ — an invariant's realization claims
  (`_claim_key`: path, locator, source identity, role, rationale) or a family's members. That, and an
  unchanged head whose realizations moved, is carried as the typed `realization_only` /
  `membership_only` count and never folded into `+`/`−`.
- An identity with several heads on a side, or a retained population with no head, is classified by `_no_single_head`; `_classify` increments `unresolved` only when the two head sets differ. Equal ambiguous head sets (including two empty sets) tally nothing and do not by themselves make the answer `partial`.
- A pair the preflight refuses, or a half that fails to read between preflight and read
  (`KnowledgeStorageError`/`apsw.Error`), is **`unavailable`** with the owner's refusal and no counts.

**Read shape.** `_read_side` opens one snapshot read-only and reads, through the shipped
`read_queries` owners, each identity's projected revision ids, those rows'
compared fields, the heads' realization claims and the family heads' memberships; then closes it.
`_tally` walks the union of identities and `_classify` places each one. It runs no subject comparison
and loads no subject content beyond each head's own fields.

### Conventions

Pure composition over existing read owners, returning the typed
[`ReviewIntentSummaryResult`](../models/knowledge/review_intent_summary.py.md). It is a sibling module
rather than a growth of `review_revision_comparison.py`; the original size observation was a
historical separation rationale, not a current source extent. It imports `revision_heads` rather
than copying it.

### Invariants And Boundaries

- **Unavailable authored intent is not measured zero.** Its `counts` and `refusal` are mutually
  exclusive. Separately obtained attribution/stored-open values are not authored-intent totals and
  can coexist with that refusal; model consistency alone does not authenticate source reads.
- **One projected record per normal side.** Current selection/counting use the text records'
  own revisions. The retained no-single-head tally guard remains defensive for supplied populations;
  it is not evidence that the reviewer still offers an ambiguous multi-head wire state.
- **Same resolution, same preflight as the catalogue.** No other dataset is substituted and no
  candidate is chosen here.
- **No authored-intent writer.** This module composes read owners and returns a value. That is not
  a whole-resolution promise of no I/O or no derived cache/index maintenance by other owners.
- **The lane's count is a separate fact.** `attribution` is computed from file buckets only (no hunk read; proved by
  `test_the_entry_count_reads_file_buckets_only`) and is never folded into `+`/`−`.
- **Presentation is not owned here.** Whether an acceptance-only successor is worded differently from a
  text revision is the change-kind owner's concern: `review_change_kinds.py` compares the record
  wording for the family-context change kinds (MIK-R33, adopting ICR-R32). The earlier `ICR-R35`/leaf
  L49 assignment of that question is superseded and retained only as history.

### Todos

- Query cost is linear in identities: one `fetch_revision_ids` call per identity per side (review R2
  observation O-R2-3: L41's summary makes 115 store calls, about 21 ms in-process). One grouped
  revision-id query per side would make it constant. The observation was routed as a candidate for a
  later performance leaf (L50/L51); it is not delivered here.

## Evidence

### Docs References

No Domain Documentation source is configured for this module; the count semantics are the repository's
own ruling, cited below.

No relevant domain documentation was found.

### Repo-Internal References

- The public reader resolves the task and attaches separate attribution/stored-open facts on the tree path. [1]

- Shared preflight precedes both reads; storage failure yields unavailable and unresolved count yields partial. [2]

- Compared statement/guarantee fields include authored wording and origin status/acceptance, not display version or provenance. [3]

- The tally keeps unequal-head unresolved, one-sided revisions, relationship-only changes and counted successors distinct. [4]

- The retained predicate detects multiple supplied heads or populated-with-none; this is not a current reviewer ambiguity selector. [5]

- Membership comparisons use canonical invariant identity rather than counting a revised shared member twice. [6]

- Realization equality uses path, locator, recorded source identity, role and rationale independently of claim-record identity. [7]

- The live-tree control reads lane attribution; the historically dataset-named control actually removes conversion knowledge and asserts no attribution. [8]

- The shared helper deterministically sorts a projected revision population; it no longer discovers multi-head lineage. [9]

- The controlled fixture source asserts added/revised/removed plus-minus and separate realization/membership counts, not a fresh execution. [10]

- The single-record shared-member fixture asserts one before/after count and unchanged membership despite two family occurrences. [11]

- The record-only/status fixture asserts successor counts separately from membership-only changes. [12]

- The retained missing-knowledge control asserts refusal/no authored counts; the independent production tally keeps unequal head sets unresolved. The old divergent-head test is historical, not resurrected. [13]

- The CLI now imports the focused summary-port owner and binds its factory, whose native reader supplies dependency observations. [14]

- Optional worklist admission requires complete exact-pair-bound decidable work; the focused port observes the optional worklist path before reuse. [15]

### Cross-Repo References

All cited model, projection, test, gate and CLI owners are in this repository; no external-system boundary is established by them.
