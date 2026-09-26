# dashboard/src/panels/review/familyReview.oneSided.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.oneSided.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
recorded by the leaf's probe (`temp/icr/probe-l24-family-body.py`) and installed as the fixture the
family workspace case stubs `fetch` with. **40,941 bytes; sha256
`383bd101a349b2d054dca8ab7fb05cf8d182612dc17cdced57bae5c358af4db1`.** It is untracked in this leaf's
working tree (`??`), so these are candidate bytes a reader re-checks against the file, not bytes any
commit holds.

It is data with a provenance chain, not an assembled fixture: the case stubs **only `fetch`** and lets
the real client, the shared decode and the real component tree read these bytes. It is **not browser
evidence** — the repository's Playwright configs are Dagger-only and the case file says so in its own
header.

The envelope is the review read (`state: "review"`, `operation: "read_knowledge_review"`,
`surface_version: "knowledge-review-surface/1"`) over the fixture enclosure (`leaf_id: "260921-icr-l1"`,
master/task_ref `review-source-endpoints-fixture`) with the per-run fixture repository uuid normalized
to `<repository_id>`.

**What this body pins apart from its six siblings: the one membership row that a single snapshot
records, whose revision content this page did not carry.** It is the only body of the seven in which
exactly one row carries the page-scoped uncarried state **and** the other snapshot does not list that
revision at all, which is why the case can address the row in the singular and why the sentence it must
produce is a fact about the **page** — never the one-sided comparison wrapper, and never "the snapshot
records no row".

## Code Commentary

### Logic

**The body is a continued page of the before side's walk.** `payload.page` is `collection:
"family_members"`, `state: "continued"`, `returned` 5, `remaining` 6, `total` 11 on
`total_basis: "selection"`, with `continued_from` and `continuation` cursors and a scope naming
`side=before`, family revision `af44f607-e364-443a-8cee-fe2a1d4e8e82` and `page_size=4`. The family
context is `partial` with two families, `membership_rows_total` 8 and — the lowest among the seven
bodies — `unique_member_revision_total` 2, because this page carried one row per side of each family.

**The uncarried row is the whole reason this file exists.** Family
`dc9b58d2-f5d0-4a9c-b6df-1ec44c422f94`'s before side measured 2 rows and carried both: one `recorded`
row and one row whose state is `content_not_on_page` for revision
`63a89639-aac8-4802-ba97-3324c3f6acaf` (member `f117ecca-1d81-4e46-b91c-c2c8d36675a0`). The after side
of that family records revision `74555fd7-8d39-4561-a672-f9973f74c0d4` and lists one recorded row — it
does **not** list `63a89639-...` at all. So for that member, no side this page reached carried content:
the comparison is `not_on_page`, and the only truthful sentence is the page-scoped one the member
statement prints, which is exactly what the row itself already says in its own detail.

**The same body carries the other one-snapshot fact, outside the family context.** `source.unresolved`
holds exactly **two** rows, both with the owner's sentence `this record is held by one snapshot and was
not reached by the other side's declared selection; it is displayed as present outside the selection and
never as a deletion` (references `21fcbbd7-a5a8-4903-a4d4-e96abbb6d0ce` and
`23053fbb-423f-4a36-a1eb-3972f3aa22d1`). That is the attribution vocabulary's statement about a record
held by one snapshot; it is a different owner's fact from the member row above and must not be merged
with it.

**What a reader must NOT look for in this body.** Every one of its four family sides is `state:
"recorded"` and carries a guarantee object — as do all 26 sides across the seven captured bodies — so
the **guarantee-level** `one_sided` (exactly one snapshot recorded a revision, no comparison made) and
`unrecorded` shapes are not composed here at all. The vocabulary declares those shapes and the renderer
has a block for them, but this body's one-sidedness is the member row and the two unresolved
attribution rows. A reader (or a later curator) who expects an unrecorded family side in this file will
not find one, and should not "fix" the body to supply it.

**One case drives these bytes, and it asserts the boundary in four directions.** It takes the single
row carrying `review-family-member-state`, clicks that row's opener, and asserts the centre shows the
not-on-page statement containing `did not carry the revision content` while the one-sided, unchanged and
changed member blocks are all **absent**. Singular addressing is itself part of the evidence: the
sibling `walkFinal` body carries eleven uncarried rows and could not be driven this way, and the sibling
`continued` body's uncarried row is listed by **both** sides, which is the different sentence pair the
case beside this one drives.

### Conventions

- Captured bytes, never hand-edited: the provenance lives in the consuming case file's header, and this
  card adds no second provenance. The body itself carries the capture directory in its inventory
  command (`temp/icr/l24-capture/scenario-one-sided/...`), which is where the file's name comes from.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding, because a line number
  cannot distinguish two facts in a one-line file.
- The body is opaque data to this client: the case types it `unknown` and narrows it at runtime.
- Numbers on this card are the file's: byte size and digest are the file, counts are the owner's.

### Invariants And Boundaries

- **A row whose content no reached side carried is a statement about the page.** It is not a deletion,
  not an absence from a snapshot, and not a one-sided comparison: the sentence names the page and the
  revision, and stops there.
- **`content_not_on_page` is the state the whole distinction rests on.** The membership row **is**
  recorded; only its revision content fell outside the page. A rendering that reads the state as "the
  snapshot has no row" falsifies the store.
- **One snapshot holding a record is its own published fact.** It appears on `source.unresolved` with
  the owner's sentence, and it is not evidence that the other snapshot deleted anything.
- **The guarantee-level one-sided shape is not in this body.** All seven captured bodies record a
  guarantee on every side; a reader must not read this file's name as a claim about family revisions.
- **No conclusion is carried anywhere in the body.** The evidence state is `none_recorded`, the
  assessment state is `unassessed`, and the submission block is `unavailable`.
- **Not browser evidence.** These are the bytes a real route published, rendered by the real client in a
  mounted test tree; they are not a live page fed by a running publication.

### Todos

None recorded. The one-sided member sentence and the one-snapshot attribution sentence are both
published by their owners; no obligation is attached to this file.

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
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The enclosure the bytes were recorded over, the one normalization, and the capture directory the file's own name comes from.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>"; "scenario-one-sided"; "l24-capture" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The page block: this is a continued page of the before side's walk, with its returned/remaining/total arithmetic and its scope.** | "\"collection\":\"family_members\""; "\"state\":\"continued\""; "\"returned\":5"; "\"remaining\":6"; "\"total\":11"; "\"page_size=4" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The family context, with the lowest distinct-revision count of the seven bodies because each side carried one row.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"membership_rows_total\":8"; "\"unique_member_revision_total\":2" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The one uncarried row of the whole body: its revision identity, its member identity, and the state that says the row is recorded while its content is not on the page.** | "63a89639-aac8-4802-ba97-3324c3f6acaf"; "f117ecca-1d81-4e46-b91c-c2c8d36675a0"; "\"state\":\"content_not_on_page\"" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The two families and the rosters this page measured against what it carried, including the one-row sides.** | "c47d4be4-4780-483a-a43b-3eedb7022507"; "dc9b58d2-f5d0-4a9c-b6df-1ec44c422f94"; "762083cc-a98b-4afe-9cfb-a5be1fe7bb67"; "af44f607-e364-443a-8cee-fe2a1d4e8e82"; "74555fd7-8d39-4561-a672-f9973f74c0d4"; "holds 2 recorded membership(s) and this page carried 1"; "\"members_total\":2" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| **The other one-snapshot fact: two unresolved attribution rows, each displaying a record held by one snapshot as present outside the selection rather than as a deletion.** | "this record is held by one snapshot and was not reached by the other side's declared selection; it is displayed as present outside the selection and never as a deletion"; "\"recorded_reference\":\"21fcbbd7-a5a8-4903-a4d4-e96abbb6d0ce\""; "\"recorded_reference\":\"23053fbb-423f-4a36-a1eb-3972f3aa22d1\"" | dashboard/src/panels/review/familyReview.oneSided.captured.json:1-1 |
| The one constant that binds this body to its case, and the runtime narrowing that keeps a body with a missing field from mounting the surface. | `captured("familyReview.oneSided.captured.json")`; `firstFamilyId` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:65-68; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:74-97|
| **The provenance of every captured body: the real route's bytes recorded by the leaf's probe, with the real client and component tree reading them in the cases.** | "holds the bytes"; "probe-l24-family-body.py" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:6-12 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:23-27 |
| **The case this body exists for: it addresses the single uncarried row, reads the page-scoped statement, and refuses all three comparison wrappers.** | "states a member whose content the page did not carry as that, not as a one-sided statement"; "did not carry the revision content"; `ONE_SIDED` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:532-550; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:546-546; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:58-58 |
| **The derivation that decides this row: a member comparison falls to the one-sided helper, and nothing carried means `not_on_page` while exactly one carried means `one_sided`.** | `memberComparison`; `oneSidedMember`; `not_on_page`; `one_sided` | dashboard/src/data/reviewFamily.ts:285-296; dashboard/src/data/reviewFamily.ts:298-321 |
| **The row's own page-scoped line in the tree, and the member statement block the centre mounts for it.** | "review-family-member-state"; "statement not carried on this page"; "review-center-member-not-on-page"; "did not carry the revision content" | dashboard/src/panels/review/FamilyTree.tsx:410-410; dashboard/src/panels/review/FamilyTree.tsx:411-411; dashboard/src/panels/review/FamilyReviewCenter.tsx:567-567; dashboard/src/panels/review/FamilyReviewCenter.tsx:201-201; dashboard/src/panels/review/FamilyReviewCenter.tsx:202-202 |
| Roster context does not select a primary statement pair; the subject owner supplies that pair, while an unaddressable member remains context. | `SelectedStatement`; `UnavailableMember` | dashboard/src/panels/review/SubjectReview.tsx:53-114; dashboard/src/panels/review/FamilyReviewCenter.tsx:764-787 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **citation repair only, second move:** the F1 fix round shifted the member-statement and guarantee-level blocks in `panels/review/FamilyReviewCenter.tsx` below the A4 section, so the guarantee-level fact line moved `:1177-1187` → `:1207-1217` (the two member-statement ranges `:227-233` and `:289-297` are above the insertion and did not move). No claim wording changed. No verification stamp was advanced.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the two rows this card carries into `panels/review/FamilyReviewCenter.tsx` were re-anchored, and no claim wording changed.** The member statement block's not-carried line moved `:226-232` → `:227-233`, the comparison wrapper `:288-296` → `:289-297`, and the guarantee-level fact line `:690-700` → `:1177-1187`; each new range was derived from the construct's own declaration at this tip. The captured body and this card's claims about it are unchanged. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the leaf's one-sided body, and recorded what "one-sided" actually means on these bytes.** The file's exact identity is 40,941 bytes; sha256 `383bd101a349b2d054dca8ab7fb05cf8d182612dc17cdced57bae5c358af4db1`. The state it pins apart from its six siblings is **the single membership row that only one snapshot records, whose revision content this page did not carry** (revision `63a89639-aac8-4802-ba97-3324c3f6acaf`, member `f117ecca-1d81-4e46-b91c-c2c8d36675a0`), which the case addresses in the singular and which must render as a page fact rather than as the one-sided wrapper. The card records the correction a reader needs: **every one of this body's four family sides is `state: "recorded"` with a guarantee — as are all 26 sides across the seven captured bodies — so the guarantee-level `one_sided`/`unrecorded` shapes are not composed by this body at all**; its one-snapshot facts are the member row above and the two `source.unresolved` attribution rows. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
