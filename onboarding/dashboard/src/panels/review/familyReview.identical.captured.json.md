# dashboard/src/panels/review/familyReview.identical.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.identical.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:23:08+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9` |
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
re-captured over HTTP by the producer, command and source tree the adjacent receipt
`familyReview.capture-provenance.json` names, and installed as the fixture the family workspace case
stubs `fetch` with. **44,684 bytes; sha256
`fa7a257f08801afb7143e181bf5d0877bb517bd63e203360a18a692efdace660`** (the digest the receipt records). The
producer rebuilt the scenario with fresh identities until the body carried the earlier capture's structural
signature, so every UUID and digest in it is new while the shapes the case reads are the same.

It is data with a provenance chain, not an assembled fixture: the case stubs **only `fetch`** and lets
the real client, the shared decode and the real component tree read these bytes. It is **not browser
evidence** — the repository's Playwright configs are Dagger-only and the case file says so in its own
header.

The envelope is the review read (`state: "review"`, `operation: "read_knowledge_review"`,
`surface_version: "knowledge-review-surface/1"`) over the fixture enclosure (`leaf_id: "260921-icr-l1"`,
master/task_ref `review-source-endpoints-fixture`) with the per-run fixture repository uuid normalized
to `<repository_id>`.

**What this body pins apart from its siblings: two DISTINCT family revisions whose authored guarantee
text is identical — `identical_text`, never "unchanged" — beside the one shape that really is one
revision on both snapshots.** Both shapes are in this one body. `retry-budget-family` records the
**same** revision on both sides with a single payload digest, which is the only shape allowed to say the
guarantee is unchanged. `retry-and-anchor-family` moves between two different revisions with two
different `payload_digest` values and the *same* `joint_guarantee` sentence — something was authored
between them, and the text is what did not move. It is also one of the two family bodies that carry the
member-source fields `locator`, `resolved_ranges` and `locator_state`.

## Code Commentary

### Logic

**The family context is `partial` with two families and the owner's measured counts.** Two returned of
two total, none remaining; `membership_rows_total` 7 and `unique_member_revision_total` 4 — one row fewer
than the `complete` body's 8, because this enclosure's second family records one member on the after side
rather than two. There is **no payload-level `page` block** in this body: it is a first read whose
per-side roster pages carry the cursors.

**The unchanged shape is decided by identity, and the body carries its evidence.** `retry-budget-family`
records one family revision on both snapshots with one payload digest (the same digest on both sides)
and the text `The retry budget is shared by integration and synchronization.` Identity and digest agree,
so one authored revision stands behind both sides: this is the shape the client must render as
`unchanged_revision`.

**The identical-text shape is decided by identity first and text second, and this body is its only
carrier here.** `retry-and-anchor-family` records one revision before and another after: two different
revision identities, two different payload digests, and one identical `joint_guarantee` string, `The
retry budget and the anchor identity rule hold together.` The vocabulary decides this in that order on
purpose — same revision means one authored revision, distinct revisions with equal text means
`identical_text`, and only differing text is `changed` — so a surface cannot reach "unchanged" by
comparing text.

**Three rosters were carried page-first and one whole.** Three sides state `holds 2 recorded
membership(s) and this page supplies 2 member context update(s)` with a published continuation, and the
after side of `retry-and-anchor-family` states `was read whole: 1 recorded membership(s), all carried
here` with `complete: true`. No row here is a page-scoped notice, so the guarantee comparison is the only
thing the case reads from this body.

**Each member source carries its structured locator and state, and the four sources cover three facts.**
`candidate-batch-atomicity`'s `file` locator is `whole_file` on the before side (exact recorded blob) and
`unresolved` on the after side, where the tree holds different bytes (`recorded_blob_mismatch`). One
`shared-retry-budget` source records a `line_range` of lines 3-7 on a blob that holds fewer lines: its
resolution stays `exact_recorded_blob` while its `locator_state` is `unresolved` and it carries no range —
the route's own example of a recorded range the exact blob does not reach. The other
`shared-retry-budget` source is a `whole_file`. `resolved_ranges` is `[]` on every source here.

**One case drives these bytes, and it reads which family is which from the rendered blocks rather than
from row order.** It opens the identical-text family and asserts, since MIK-R31 rule 3 (the ICR 13:40
decision, rendered by MIK-L31), that the block says "Wording unchanged · revision <before8> → <after8>", shows the
guarantee **once**, and names both revision IDs under "Revision records", with the unchanged block absent and never
"so the guarantee is unchanged" (before MIK-L31 the block showed both texts side by side as "two recorded
revisions"); it then opens the other family and asserts the unchanged block says the two
snapshots selected the **same** family revision, with the identical-text block absent. That pairing is
the whole point: the same two sentences must not be interchangeable.

### Conventions

- Captured bytes, never hand-edited: the provenance is the receipt `familyReview.capture-provenance.json`,
  pointed at by the consuming case file's header; this card adds no second provenance.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding, because a line number
  cannot distinguish two facts in a one-line file. Rows name labels and sentences rather than the
  per-build UUIDs and digests, which change on every re-capture.
- The body is opaque data to this client: the case types it `unknown` and narrows it at runtime.
- Digest equality is a fact about the recorded revision, not a rendering decision: the client compares
  identities first and text second, and the digests are what a reader checks to see the two revisions
  really are two.

### Invariants And Boundaries

- **"Unchanged" may only be said of one authored revision behind both sides.** This body is the pair
  that proves the rule: the same text on two distinct revisions is `identical_text`, and calling it
  unchanged would hide the revision the store records.
- **"Changed" is text, not identity.** Two distinct revisions carrying the same text are not a changed
  guarantee; the two shapes are decided in that order by the vocabulary, not by the renderer.
- **An exact blob is not a resolved region.** The line-range source here is `exact_recorded_blob` and
  `unresolved` at once; the region is read from `resolved_ranges`, never from the resolution.
- **A captured body is evidence, not a specification.** The contract it evidences is the read response
  the route publishes and the comparison union that decides which sentence a surface may use.
- **No page block is not a missing page.** This body is a first read: the per-side roster pages carry
  their own cursors, and the absence of a payload-level page is the shape of that read.
- **Not browser evidence.** These are the bytes a real route published, rendered by the real client in a
  mounted test tree; they are not a live page fed by a running publication.

### Todos

None recorded for this file.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every row was re-derived against this candidate, and every anchor in a row occurs on the line the row
cites. Because each captured body is one minified line, the cited range is the whole file and the
finding names the exact key path and value a reader can re-check.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **The enclosure the bytes were recorded over, and the single normalization: the per-run fixture repository uuid is written as a placeholder.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **The family context and the row count that differs from the `complete` body: seven measured rows and four distinct member revisions.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"membership_rows_total\":7"; "\"unique_member_revision_total\":4" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **The unchanged shape: the same family revision on both snapshots, carrying the same guarantee text.** | "\"display_label\":\"retry-budget-family\""; "The retry budget is shared by integration and synchronization."; "\"state\":\"first_page\"" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **The identical-text shape: two distinct family revisions whose guarantee text is the same string while their payload digests differ.** | "\"display_label\":\"retry-and-anchor-family\""; "\"joint_guarantee\":\"The retry budget and the anchor identity rule hold together.\""; "\"payload_digest\"" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **Three sides supplied their two member updates on a first page of a continuing walk, and the identical-text family's one-row after roster was read whole.** | "was read whole: 1 recorded membership(s), all carried here"; "holds 2 recorded membership(s) and this page supplies 2 member context update(s)" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| The one constant that binds this body to its case, and the runtime narrowing that keeps a body with a missing field from mounting the surface. | `captured("familyReview.identical.captured.json")`; `firstFamilyId` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:74-77; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:78-81; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:87-110|
| **Each member source's structured locator and state: `whole_file` and `unresolved` file locators, and a recorded 3-7 line range on the exact blob that is `unresolved` with no range.** | "\"locator\":{\"end_line\":7,\"kind\":\"line_range\",\"start_line\":3}"; "\"locator_state\":\"whole_file\""; "\"locator_state\":\"unresolved\""; "\"resolution\":\"recorded_blob_mismatch\""; "\"resolved_ranges\":[]" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **The provenance of this body: made over HTTP by ICR-L44's producer in its own run at source tree `a8039b8e`, which the receipt records at its top level, carrying each member source's structured locator, resolved ranges and locator state.** | "familyReview.capture-provenance.json"; "its own run, at source tree a8039b8e" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:9-11 |
| **The receipt row for this body: its digest, scenario, request and normalization, under the receipt's command, source tree and selection rule.** | "familyReview.identical.captured.json"; "captured_source_tree" | dashboard/src/panels/review/familyReview.capture-provenance.json:1-35 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:32-36 |
| The fixture case distinguishes separate guarantee revisions with identical text ("Wording unchanged", both revisions named, the text once) from the same unchanged revision. | "it(\"distinguishes two distinct revisions with identical text" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:550-579 |
| **The comparison union these bytes are read through, and the decision order that keeps the three "did not change" shapes apart: identity first, text second.** | `GuaranteeComparison`; `identical_text`; `unchanged_revision`; `one_sided`; `joint_guarantee`; `memberComparison` | dashboard/src/data/reviewFamily.ts:243-248; dashboard/src/data/reviewFamily.ts:250-259; dashboard/src/data/reviewFamily.ts:41-41; dashboard/src/data/reviewFamily.ts:280-280; dashboard/src/data/reviewFamily.ts:283-283; dashboard/src/data/reviewFamily.ts:311-322 |
| The guarantee block distinguishes the same revision, distinct revisions with identical text and a known one-sided guarantee. | `GuaranteeComparisonBlock` | dashboard/src/panels/review/FamilyReviewCenter.tsx:127-209 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): No content impact: the guarantee-block row into `FamilyReviewCenter.tsx`, which this leaf changed, was normalised by the installed fixer (`114-188` → `127-209`). The block still distinguishes the same revision, distinct revisions with identical text and a known one-sided guarantee; on a tree comparison it now word-diffs a changed text first (MIK-L35), which this body's identical text never reaches. Claim wording unchanged. No stamp advanced.
- 2026-09-30T10:52:00+02:00 — 260928-MIK-L31 curator (follow-up after the L31 worker's comment-only edits, staged; the change set is now 46 files over `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`): citation re-anchored; the fixture bytes are unchanged. The worker's comment-only rewrite of the `ReviewWorkspace.family.test.tsx` header (MIK-L31 follow-up) no longer says "re-captured over HTTP"; the provenance row is reworded to the header's new text (this body is from ICR-L44's own run at `a8039b8e`, the receipt's top level) and re-measured (`8-13` → `9-11`). The rows below the header were re-pointed by the exact −1 line shift.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update; the fixture bytes are unchanged. The case that reads this body now asserts MIK-R31 rule 3's rendering of identical guarantee text on two revisions ("Wording unchanged · revision a → b", the text once, both IDs in details). **Reopened claim reworded and re-anchored** on an `it(` quote; this pass's generated bullet for it was removed.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the body was re-captured over HTTP from the real review route (44,684 bytes; sha256 `fa7a257f…c660`, recorded in `familyReview.capture-provenance.json`). Corrected the counts (`unique_member_revision_total` is 4) and the roster description (three first-page sides and one after roster read whole), replaced per-build UUIDs and digests with labels and sentences, described the four sources' locator states — including a recorded 3-7 line range on a 3-line exact blob that is `unresolved` with no range — and pointed provenance at the receipt. The identical-text and unchanged shapes it pins are unchanged. No verification stamp was advanced.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **citation repair only, second move:** the F1 fix round moved the guarantee-level blocks in `panels/review/FamilyReviewCenter.tsx` again, so this card's three ranges became `:132-1230`, `:156-1230` and `:156-1234`; the anchors still resolve inside them. The captured body itself is unchanged. No verification stamp was advanced.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the row naming the two renderings this body's case reads was re-anchored, and no claim wording changed.** L36's insertion moved the guarantee-level blocks those anchors live in, so the three ranges became `:132-1200`, `:156-1200` and `:156-1204`; the anchors (`review-center-guarantee-identical-text`, `review-center-guarantee-unchanged`, `identical_text`, `one_sided`) all resolve inside them. The captured body itself is unchanged and this leaf re-measured A3's member order on the new build as untouched. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the leaf's identical-text guarantee body.** It records the file's exact identity (45,393 bytes; sha256 `b018b63cd2df28e6a2a3dc16d639bf8f4bcdbc4541e2e1639e6e23bb92bd7062`) and the state it pins apart from its six siblings: **two DISTINCT family revisions whose authored guarantee text is identical**, carrying two different payload digests and the same `joint_guarantee` string, beside the one shape that really is one revision on both snapshots (same revision, same digest) — so this single body holds both the `identical_text` shape and the `unchanged_revision` shape the case must keep apart. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
