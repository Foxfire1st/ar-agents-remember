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
[`review_pair_preflight`](review_pair_preflight.py.md) before reading anything, so the catalogue and
the summary cannot disagree about whether a pair is readable.

**Since MIK-L32 a tree comparison's summary also carries `attribution`** (MIK-R32 rule 9): after
`intent_summary_of` answers, `read_review_intent_summary` adds `lane_summary(resolved.trees)` from
[`review_unexplained_lane.py`](review_unexplained_lane.py.md), the unexplained-changes lane's file-level count over the
same resolved trees, in the same request. The entry therefore asks for it exactly when it asks for the intent counts,
and never more eagerly. It is attached whatever the intent counts' own state (ruling 2026-09-30T12:19:20 Q6: it is
read from the trees directly and is true on its own). A dataset comparison (`resolved.trees is None`) carries none.

## Code Commentary

### Logic

**Count semantics (master decision on count semantics, `task.json`, entry labelled 12:00 and
clock-corrected by the 12:10:21 entry; refined by the leaf's 16:15:11 ruling on L47-R1-F3).**

- Each side's current statement of an identity is its **head revision** under
  `review_revision_comparison.revision_heads` — the rule the reviewer uses to choose which before/after
  revisions it renders (`ICR-R07`). This module reuses it; it does not define a second head rule.
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
- An identity with several heads on a side, or a retained population with no head, is **unresolved**
  (`_no_single_head`); the answer is then `partial`, never a guessed winner.
- A pair the preflight refuses, or a half that fails to read between preflight and read
  (`KnowledgeStorageError`/`apsw.Error`), is **`unavailable`** with the owner's refusal and no counts.

**Read shape.** `_read_side` opens one snapshot read-only and reads, through the shipped
`read_queries` owners, the predecessor edges, each identity's retained revision ids, the head rows'
compared fields, the heads' realization claims and the family heads' memberships; then closes it.
`_tally` walks the union of identities and `_classify` places each one. It runs no subject comparison
and loads no subject content beyond each head's own fields.

### Conventions

Pure composition over existing read owners, returning the typed
[`ReviewIntentSummaryResult`](../models/knowledge/review_intent_summary.py.md). It is a sibling module
rather than a growth of `review_revision_comparison.py` (worker observation O1: that file is 552
lines); it imports `revision_heads` from there instead of copying it.

### Invariants And Boundaries

- **Unavailable is never zero.** No count is produced for an unread comparison; the model's validator
  makes `counts` and `refusal` mutually exclusive.
- **One head rule.** The summary's head is the revision comparison's head; changing one without the
  other would let the entry count a revision the reviewer renders as superseded.
- **Same resolution, same preflight as the catalogue.** No other dataset is substituted and no
  candidate is chosen here.
- **Read-only.** It writes, retains and freezes nothing.
- **The lane's count is a separate fact.** `attribution` is computed from file buckets only (no hunk read; proved by
  `test_the_entry_count_reads_file_buckets_only`) and is never folded into `+`/`−`.
- **Presentation is not owned here.** Whether an acceptance-only successor is worded differently from a
  text revision is `ICR-R35`/leaf L49's concern (leaf ruling 16:15:11 on F3; master decision 13:40 on
  "wording unchanged").

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

The summary composes the reviewer's resolution, the shared pair preflight and the revision comparison's
head rule; the fixture tests pin every count class.

- The public read: the reviewer's own resolution, a refused resolution returned as `unavailable`; a tree comparison's lane count attached (MIK-L32). [1]
- One resolved pair: the shared preflight first, then both sides read, a mid-read storage failure refused as unreadable, `partial` exactly when something is unresolved. [2]
- The compared fields, including the record status that makes a record-only successor count. [3]
- The classification: unresolved, after-only, before-only, relationship-only, or a counted successor. [4]
- Several heads, or a population with none, is not one head. [5]
- Family members compared by canonical invariant identity, so a member whose invariant moved is the same membership. [6]
- What one realization claim asserts, independent of the claim record's own identity. [7]
- The lane count read on a live tree leaf; none on a dataset leaf. [8]
- The head rule reused from the revision comparison owner. [9]
- The fixture that pins added/revised/removed as +/− and realization-only/membership-only as typed counts. [10]
- A revised member shared by two families counts once on each side. [11]
- A status-only or version-only successor counts once on each side (L47-R1-F3). [12]
- Divergent heads make the answer `partial`; absent knowledge is `unavailable` with no counts. [13]
- The composition root wires this read as the fourth review port. [14]

### Cross-Repo References

No cross-repository behavior is implemented here; the read stays inside one repository namespace's two
snapshots.

No meaningful cross-repo references found.
