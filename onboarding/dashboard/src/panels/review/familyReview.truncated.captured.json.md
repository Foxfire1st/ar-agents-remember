# dashboard/src/panels/review/familyReview.truncated.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.truncated.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076` |
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
**re-captured by MIK-L31 from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder) with L44's producer,
first build accepted, and installed as the fixture the family workspace cases stub `fetch` with. **36,793 bytes;
sha256 `ac5cae6f39d6f650b3979f0b8a6afb8106204b3ad1fad2bedea81eae087db8fa`**, as its row in
`familyReview.capture-provenance.json` (`mik_l31_recapture`) records. It is the `bounded1-truncated` request of the
`build_family_scenario` build (page size 1).

It is data with a provenance chain, not an assembled fixture: the cases stub **only `fetch`** and let the real
client, the shared decode and the real component tree read these bytes. It is **not browser evidence**.

The envelope is the review read (`state: "review"`, `operation: "read_knowledge_review"`,
`surface_version: "knowledge-review-surface/1"`) over the fixture enclosure (`leaf_id: "260921-icr-l1"`,
master/task_ref `review-source-endpoints-fixture`) with the per-run fixture repository uuid normalized
to `<repository_id>`.

**What this body pins now: a bounded roster whose first page carried part of the rows the read measured.** Since
ICR-L38 a first page always carries the member its first items represent, so every side measured **2** recorded
membership rows and carried **1** (the owner's sentence: "holds 2 recorded membership(s) and this page supplies 1
member context update(s)"); `unique_member_revision_total` is **3** while `membership_rows_total` stays **8**. The
page-scoped "carried none" state the earlier capture pinned is no longer produced by the route; the case that
renders it runs over a labelled SYNTHETIC derivation of this body (ruling 2026-09-30T05:36:19 Q3). This body is
also the cursor partner of the sibling `continued` body.

## Code Commentary

### Logic

**Every roster page on this body is the first position of a walk.** Each side's page block is
`complete: false`, `state: "first_page"`, `page_size=1`, and publishes a `continuation`: one item returned
per side, with `retry-and-anchor-family` at 10 of 11 remaining (before) and 8 of 9 (after), and
`retry-budget-family` at 12 of 13 (before) and 11 of 12 (after).

**There is no payload-level `page` block**, as before: this is the first read of the selection and the per-side
roster pages carry their own cursors.

**The two families.** `retry-and-anchor-family` (`0cafa823…`) moves from revision `e9aebe42…` to `ea0b95c8…`;
`retry-budget-family` (`13b94682…`) records `79ce3ed4…` on both sides. The selected subject's revision selection is
`added` (after side only), and `source.unresolved` holds one attribution row for a record held by one snapshot.

**The cursor is the server's.** The `continuation` of `retry-budget-family`'s after-side roster page is,
byte for byte, the sibling `continued` body's `payload.page.continued_from` (both decode to position 1). The walk
cases read that cursor out of the rendered control and assert it is sent unchanged.

**The cases these bytes drive.** The real-body roster case (all four rosters print "records 2 membership row(s);
loaded context contains 1 of them", no empty-roster sentence, never "measured zero"); the SYNTHETIC case (this body
with every roster's member rows removed, so the "carried no member row" branch stays covered); the bounded
member-context case, whose loaded count is read from this body and asserted below 4; the walk case and the
workspace-state case (with `continued`).

### Conventions

- Captured bytes, never hand-edited: the provenance is the receipt's `mik_l31_recapture` row, and the capture
  record it binds.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding, because a line number
  cannot distinguish two facts in a one-line file.
- The body is opaque data to this client: the cases type it `unknown` and narrow it at runtime.
- Numbers on this card are the file's: byte size and digest are the file, counts are the owner's. The
  identities are one draw of the scenario builder; a re-capture draws new ones.

### Invariants And Boundaries

- **A page that carried part of N measured rows is stated as that part.** The owner's own two measures are printed,
  and "the read measured zero" is never said; only a measured-empty roster may say it.
- **The cursor belongs to the server.** The continuation this page publishes is the continuation the walk
  continues; the client forwards it unchanged.
- **An absent payload-level page is a shape, not a loss.**
- **No conclusion is carried anywhere in the body.** No evidence record, no assessment, and the submission block
  is `unavailable`.
- **Not browser evidence.**

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every row was re-derived against the MIK-L31 re-capture, and every anchor in a row occurs on the line the row
cites. Because each captured body is one minified line, the cited range is the whole file and the finding names the
exact key path and value a reader can re-check.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The enclosure the bytes were recorded over, and the single normalization.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The family context: two families, the owner's eight measured rows, and three distinct carried revisions.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"membership_rows_total\":8"; "\"unique_member_revision_total\":3" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The page-scoped fact in the owner's own words: two rows measured, one carried, on a first page that publishes the cursor that reaches the rest.** | "holds 2 recorded membership(s) and this page supplies 1 member context update(s)"; "\"members_total\":2"; "\"state\":\"first_page\""; "\"page_size=1" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The walk arithmetic behind the sentence: one item returned per side, with ten, eight, twelve and eleven remaining.** | "\"primary_items_remaining\":10"; "\"primary_items_remaining\":8"; "\"primary_items_remaining\":12"; "\"primary_items_remaining\":11" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The two families by label and identity, and the selection added on the after side.** | "retry-and-anchor-family"; "retry-budget-family"; "0cafa823-a47f-4250-a451-c1f883136049"; "13b94682-b7c0-4182-b626-71459a7fcd38"; "\"state\":\"added\"" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The receipt row for this file in the MIK-L31 re-capture, with its digest, scenario and requests.** | "familyReview.truncated.captured.json" | dashboard/src/panels/review/familyReview.capture-provenance.json:56-56 |
| The one constant that binds this body to its cases, and the runtime narrowing that keeps a body with a missing field from mounting the surface. | "const TRUNCATED"; "function firstFamilyId" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:68-68; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:87-110 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:32-36 |
| The real-body roster case: part of the measured rows carried, never zero. | "states a bounded roster page as the part of the measured rows it carried, never as zero" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:451-469 |
| The SYNTHETIC derivation of this body that keeps the "carried no member row" branch covered (ruling Q3). | "SYNTHETIC FIXTURE, not a route body"; "structuredClone(TRUNCATED as ReviewResult)" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:471-491 |
| The bounded capture keeps the exact continuation, the owner-measured counts (the loaded count read from this body) and the reader state; a returned foreign walk is rejected. | "sends the family's published cursor and refuses a response from another walk"; "it(\"heads a bounded member context partial"; "keeps the reader's workspace state across two page requests through the centre's own control" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:299-342; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:504-548; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:695-748 |
| Empty-roster wording and carried counts remain owned by the same page-aware tree helpers. | `emptyRosterSentence`; `carriedOf` | dashboard/src/panels/review/FamilyTree.tsx:251-253; dashboard/src/panels/review/FamilyTree.tsx:255-269 |
| Partial member context retains owner counts and continuation; completing a page is not the same as carrying the whole selection. | `FamilyMemberContext`; `completionNote` | dashboard/src/panels/review/FamilyReviewCenter.tsx:583-644; dashboard/src/panels/review/FamilyTree.tsx:244-249 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |


## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`FamilyReviewCenter.tsx`, `FamilyTree.tsx`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept); 1 row(s) the fixer declined re-pointed by the exact base-to-staged line shift (each byte-identical to memory HEAD, its anchors checked in the base and shifted ranges). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:21:53+00:00: Generated citation repair: `FamilyMemberContext`; `completionNote` repointed to dashboard/src/panels/review/FamilyReviewCenter.tsx:583-644; dashboard/src/panels/review/FamilyTree.tsx:244-249. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): No content impact: MIK-R34 inserted one import line each in `FamilyTree.tsx` and `FamilyReviewCenter.tsx`, so the fixer normalised the two consumer rows by one line. Claims unchanged. No stamp advanced.
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): No content impact: two rows into `FamilyTree.tsx` and `FamilyReviewCenter.tsx`, which this leaf changed, were normalised by the installed fixer; the empty-roster row kept a range (`FamilyTree.tsx:218-220`) that no longer holds either of its anchors, so it was dropped, and the row now cites `carriedOf` at `231-233` and `emptyRosterSentence` at `235-249`. Claim wording unchanged. No stamp advanced.
- 2026-09-30T10:52:00+02:00 — 260928-MIK-L31 curator (follow-up after the L31 worker's comment-only edits, staged; the change set is now 46 files over `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`): **resolved Todo:** the header of `ReviewWorkspace.family.test.tsx` was refreshed by the worker (comments only) and now names this body's MIK-L31 re-capture (`mik_l31_recapture`); the Todo is removed. The rows into that test were re-pointed by the exact −1 line shift the shorter header causes.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update for the MIK-L31 re-capture (MIK-R31 rule 6, the L44-R1-F5 remainder; ruling 05:36:19 Q3 for the synthetic case). The card now describes the new bytes (36,793 bytes, sha256 `ac5cae6f…`): every side measured 2 rows and carried 1, `unique_member_revision_total` 3, the new family identities and walk counts, and the cases that read it (the real-body roster case, the SYNTHETIC case, the body-derived counts of review F7/R2-7). **Claims re-anchored:** every row naming the old bytes (the carried-0 sentence, `unique_member_revision_total` 0, the old family and revision identities, the walk counts) and the old provenance rows (`63b47629`, `not_recaptured`) are replaced by rows on the new bytes and the receipt's `mik_l31_recapture` row; the three case rows whose titles changed are re-anchored (the committed 2026-09-26 bullet for the empty-roster case is left intact; that case now reads `emptyRoster`); this pass's three generated bullets for the replaced rows were removed.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): provenance correction; the fixture bytes are unchanged and still hold their `63b47629` capture. The case header that cited the retired probe script now names that capture and the receipt's `not_recaptured` section, so the provenance row and the Purpose sentence were corrected to say this body was not re-captured and why, and the ranges into the lengthened header and `reviewFamily.ts` were re-measured.

- 2026-09-27T01:27:31+00:00 — Reconciled the source-linked test references after the cursor case rename and line movement. Current loaded-context and mismatched-walk behavior is stated explicitly; capture bytes, recorded provenance and generated history are preserved. No verification hash/date was changed.
- 2026-09-26T21:12:36+00:00: Generated citation repair: "prints one empty-roster sentence in both columns, not two that happen to agree" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:583-607. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **citation repair only, re-checked at the post-fix tip:** `missingRowNote` sits above the A4 section, so this card's range `:256-263` is unchanged by the F1 fix round; it is re-confirmed here rather than left implicit. No verification stamp was advanced.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the row naming the centre's bounded-missing-row sentence was re-anchored, and no claim wording changed.** `missingRowNote` moved `:255-262` → `:256-263` with L36's one-line import addition; the anchor still resolves inside the new range and the sentence's two branches are unaltered. **This body also feeds the case this leaf added** (`ReviewWorkspace.family.test.tsx`: the A4 collection case mounts `WALK_FINAL`, not this body), so nothing about this capture's own case changed. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the leaf's bounded-roster body.** It records the file's exact identity (31,590 bytes; sha256 `91b6a1d6b4a2885389b80355a1dbf7aade71d00693556960d8a9d7bbe0efa9d6`) and the state it pins apart from its six siblings: **every side measured two recorded membership rows and carried none**, so `unique_member_revision_total` is 0 while `membership_rows_total` is 8 and only the page-scoped sentence is true — with the cursor this body publishes being the very cursor the sibling `continued` body continues (byte-equal, both decoding to `position 1`). It also records the two anchors this card **dropped rather than cited** (the empty `members` array and the `recorded_revision_ids` array literal) because a bracketed literal does not verify under the literal-grep rule. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
