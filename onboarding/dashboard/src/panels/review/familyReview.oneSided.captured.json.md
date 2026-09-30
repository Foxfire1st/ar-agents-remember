# dashboard/src/panels/review/familyReview.oneSided.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.oneSided.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:52:00+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c` |
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
**re-captured by MIK-L31 from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder) with L44's producer,
first build accepted, and installed as the fixture the family workspace case stubs `fetch` with. **45,874 bytes;
sha256 `16e24767eb5556bd238ff195b8a6714b8ff82e3b05a9f1a5dde2f0783d3ad134`**, as its row in
`familyReview.capture-provenance.json` (`mik_l31_recapture`) records. It is the `one-sided1-one-sided` request: the
`retry-and-anchor-family` before-side cursor of a page-size-1 read, continued at page size 4.

It is data with a provenance chain, not an assembled fixture: the case stubs **only `fetch`** and lets the real
client, the shared decode and the real component tree read these bytes. It is **not browser evidence**.

The envelope is the review read (`state: "review"`, `operation: "read_knowledge_review"`,
`surface_version: "knowledge-review-surface/1"`) over the fixture enclosure (`leaf_id: "260921-icr-l1"`,
master/task_ref `review-source-endpoints-fixture`) with the per-run fixture repository uuid normalized
to `<repository_id>`.

**What this body pins: the one membership row that a single snapshot records, whose revision content this page did
not carry.** Exactly one row in the whole body carries the page-scoped uncarried state, and the other snapshot does
not list that revision at all, which is why the case can address the row in the singular and why the sentence it
must produce is a fact about the **page** — never the one-sided comparison wrapper, and never "the snapshot records
no row".

## Code Commentary

### Logic

**The body is a continued page of the before side's walk.** `payload.page` is `collection: "family_members"`,
`state: "continued"`, `returned` 5, `remaining` 6, `total` 11 on `total_basis: "selection"`, with `continued_from`
(position 1) and `continuation` cursors and a scope naming `side=before`, family revision `f20547ca…` and
`page_size=4`. The family context is `partial` with two families, `membership_rows_total` 8 and
`unique_member_revision_total` 4; every side carried both of its 2 recorded rows.

**The uncarried row is the whole reason this file exists.** `retry-and-anchor-family`'s before side lists member
`9b397d0d-93ab-4c8b-949a-546685c06e31` (`anchor-identity-preservation`, revision
`dccb2d50-628c-4f00-aa46-e3ba98c46874`) with state `content_not_on_page`. The after side of that family (revision
`a98b9149…`) lists two recorded rows and does **not** list `dccb2d50…` at all. So for that member no side this page
reached carried content: the comparison is `not_on_page`, and the only truthful sentence is the page-scoped one.

**The same body carries the other one-snapshot fact, outside the family context.** `source.unresolved` holds exactly
**two** rows (references `0133d688-6f67-467a-a24a-68b587b602c3` and `2c2e8b4a-d6c9-4d69-8a0f-c397336befca`), each
with the owner's sentence "this record is held by one snapshot and was not reached by the other side's declared
selection; it is displayed as present outside the selection and never as a deletion". That is a different owner's
fact from the member row above and must not be merged with it.

**What a reader must NOT look for in this body.** Every family side is `state: "recorded"` and carries a
guarantee, so the guarantee-level `one_sided` and `unrecorded` shapes are not composed here. This body's
one-sidedness is the member row and the two unresolved attribution rows.

**One case drives these bytes, and it asserts the boundary in four directions.** It takes the single row carrying
`review-family-member-state`, clicks that row's opener, and asserts the centre shows the not-on-page statement
containing "did not carry the revision content" while the one-sided, unchanged and changed member blocks are all
**absent**. The sibling `walkFinal` body carries eleven uncarried rows and could not be driven this way, and the
sibling `continued` body's uncarried row is listed by **both** sides.

### Conventions

- Captured bytes, never hand-edited: the provenance is the receipt's `mik_l31_recapture` row.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding.
- The body is opaque data to this client: the case types it `unknown` and narrows it at runtime.
- Numbers on this card are the file's; the identities are one draw of the scenario builder.

### Invariants And Boundaries

- **A row whose content no reached side carried is a statement about the page.** It is not a deletion,
  not an absence from a snapshot, and not a one-sided comparison.
- **`content_not_on_page` is the state the whole distinction rests on.** The membership row **is**
  recorded; only its revision content fell outside the page.
- **One snapshot holding a record is its own published fact** on `source.unresolved`, and it is not evidence that
  the other snapshot deleted anything.
- **No conclusion is carried anywhere in the body**, and **not browser evidence**.

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
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The enclosure the bytes were recorded over, the one normalization, and the scratch directory the capture ran in.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>"; "l31-one-sided" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The page block: a continued page of the before side's walk, with its returned/remaining/total arithmetic and its scope.** | "\"collection\":\"family_members\""; "\"returned\":5"; "\"remaining\":6"; "\"total\":11"; "\"page_size=4" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The family context and its counts.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"membership_rows_total\":8"; "\"unique_member_revision_total\":4" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The one uncarried row of the whole body: its revision and member identities, and the state that says the row is recorded while its content is not on the page.** | "dccb2d50-628c-4f00-aa46-e3ba98c46874"; "9b397d0d-93ab-4c8b-949a-546685c06e31"; "\"state\":\"content_not_on_page\"" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The other one-snapshot fact: two unresolved attribution rows, each a record held by one snapshot displayed as present outside the selection.** | "\"recorded_reference\":\"0133d688-6f67-467a-a24a-68b587b602c3\""; "\"recorded_reference\":\"2c2e8b4a-d6c9-4d69-8a0f-c397336befca\"" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The receipt row for this file in the MIK-L31 re-capture.** | "familyReview.oneSided.captured.json" | dashboard/src/panels/review/familyReview.capture-provenance.json:78-78 |
| The one constant that binds this body to its case, and the runtime narrowing. | "const ONE_SIDED"; "function firstFamilyId" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:71-71; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:87-110 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:32-36 |
| **The case this body exists for: it addresses the single uncarried row, reads the page-scoped statement, and refuses all three comparison wrappers.** | "states a member whose content the page did not carry as that, not as a one-sided statement" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:581-599 |
| **The derivation that decides this row: a member comparison falls to the one-sided helper, and nothing carried means `not_on_page` while exactly one carried means `one_sided`.** | `memberComparison`; `oneSidedMember`; `not_on_page`; `one_sided` | dashboard/src/data/reviewFamily.ts:311-322; dashboard/src/data/reviewFamily.ts:324-347 |
| **The row's own page-scoped line in the tree, and the member statement block the centre mounts for it.** | "review-family-member-state"; "statement not carried on this page"; "review-center-member-not-on-page"; "did not carry the revision content" | dashboard/src/panels/review/FamilyTree.tsx:410-411; dashboard/src/panels/review/FamilyReviewCenter.tsx:231-232 |
| Roster context does not select a primary statement pair; the subject owner supplies that pair, while an unaddressable member remains context. | "export function SelectedStatement({"; "function UnavailableMember({" | dashboard/src/panels/review/SubjectReview.tsx:217-280; dashboard/src/panels/review/FamilyReviewCenter.tsx:838-861 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |


## Update History
- 2026-09-30T10:52:00+02:00 — 260928-MIK-L31 curator (follow-up after the L31 worker's comment-only edits, staged; the change set is now 46 files over `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`): **resolved Todo:** the header of `ReviewWorkspace.family.test.tsx` was refreshed by the worker (comments only) and now names this body's MIK-L31 re-capture (`mik_l31_recapture`); the Todo is removed. The rows into that test were re-pointed by the exact −1 line shift the shorter header causes.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update for the MIK-L31 re-capture (MIK-R31 rule 6, the L44-R1-F5 remainder). The card now describes the new bytes (45,874 bytes, sha256 `16e24767…`): the before-side continued page at page size 4, the one uncarried row `9b397d0d…`/`dccb2d50…`, `unique_member_revision_total` 4, and the two unresolved attribution rows `0133d688…` and `2c2e8b4a…`. **Claims re-anchored:** every row naming the old identities, counts, capture directory and the old provenance (`63b47629`, `not_recaptured`) is replaced by a row on the new bytes and the receipt's `mik_l31_recapture` row; the cross-file rows into `FamilyReviewCenter.tsx` and `SubjectReview.tsx`, already stale, are re-measured (`231-232`, `838-861`, `217-280`, on line-exact quotes); this pass's generated bullet for the receipt row was removed.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): provenance correction; the fixture bytes are unchanged and still hold their `63b47629` capture. The case header that cited the retired probe script now names that capture and the receipt's `not_recaptured` section, so the provenance row and the Purpose sentence were corrected to say this body was not re-captured and why, and the ranges into the lengthened header and `reviewFamily.ts` were re-measured.

- 2026-09-27T01:27:31+00:00 — Reconciled the source-linked test references after the cursor case rename and line movement. Current loaded-context and mismatched-walk behavior is stated explicitly; capture bytes, recorded provenance and generated history are preserved. No verification hash/date was changed.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **citation repair only, second move:** the F1 fix round shifted the member-statement and guarantee-level blocks in `panels/review/FamilyReviewCenter.tsx` below the A4 section, so the guarantee-level fact line moved `:1177-1187` → `:1207-1217` (the two member-statement ranges `:227-233` and `:289-297` are above the insertion and did not move). No claim wording changed. No verification stamp was advanced.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the two rows this card carries into `panels/review/FamilyReviewCenter.tsx` were re-anchored, and no claim wording changed.** The member statement block's not-carried line moved `:226-232` → `:227-233`, the comparison wrapper `:288-296` → `:289-297`, and the guarantee-level fact line `:690-700` → `:1177-1187`; each new range was derived from the construct's own declaration at this tip. The captured body and this card's claims about it are unchanged. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the leaf's one-sided body, and recorded what "one-sided" actually means on these bytes.** The file's exact identity is 40,941 bytes; sha256 `383bd101a349b2d054dca8ab7fb05cf8d182612dc17cdced57bae5c358af4db1`. The state it pins apart from its six siblings is **the single membership row that only one snapshot records, whose revision content this page did not carry** (revision `63a89639-aac8-4802-ba97-3324c3f6acaf`, member `f117ecca-1d81-4e46-b91c-c2c8d36675a0`), which the case addresses in the singular and which must render as a page fact rather than as the one-sided wrapper. The card records the correction a reader needs: **every one of this body's four family sides is `state: "recorded"` with a guarantee — as are all 26 sides across the seven captured bodies — so the guarantee-level `one_sided`/`unrecorded` shapes are not composed by this body at all**; its one-snapshot facts are the member row above and the two `source.unresolved` attribution rows. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
