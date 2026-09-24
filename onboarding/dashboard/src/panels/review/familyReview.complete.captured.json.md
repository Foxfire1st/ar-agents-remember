# dashboard/src/panels/review/familyReview.complete.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.complete.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
recorded by the leaf's probe (`temp/icr/probe-l24-family-body.py`) and installed as the fixture the
family workspace case stubs `fetch` with. **46,076 bytes; sha256
`82c9ca93def45bba517a295d31ca0f098c092404beb1644423d1991998f45e37`.** It is untracked in this leaf's
working tree (`??`), so these are candidate bytes a reader re-checks against the file, not bytes any
commit holds.

It is data with a provenance chain, not an assembled fixture: the consuming case stubs **only `fetch`**
and lets the real client (`intentReview`), the shared decode and the real component tree read these
bytes, so what the cases exercise is the wire contract itself. It is **not browser evidence** — the
repository's Playwright configs are Dagger-only and the case file says so in its own header.

The envelope is the read the surface always makes: `state: "review"`, `operation:
"read_knowledge_review"`, `surface_version: "knowledge-review-surface/1"`, over the fixture enclosure
(`leaf_id: "260921-icr-l1"`, master/task_ref `review-source-endpoints-fixture`) with the per-run fixture
repository uuid normalized to `<repository_id>`.

**What this body pins apart from its six siblings: a family roster carried whole.** Every one of the
four sides carried exactly the rows its owner measured (2 of 2), every one of the eight member rows is
`state: "recorded"` — its revision content is on the page — and both guarantee shapes the vocabulary
must keep apart are present at once: one family selected the **same** family revision on both snapshots,
the other selected **two distinct** revisions carrying **different** authored text. The family context
is still `partial`, because carried-whole rosters are not a completed read walk.

## Code Commentary

### Logic

**The family context block is a `partial` composition with all its parts carried.** `families_total` 2,
`families_returned` 2, `families_remaining` 0; `membership_rows_total` 8 (the rows the read measured)
and `unique_member_revision_total` 4 (the distinct member revisions among the rows it carried). Its
`detail` is the owner's own sentence, and it names each family with its per-side remainder — the
remainder of the **walk**, which is a different count from the roster it carried.

**Each side's roster page carried the whole roster of its family revision while the walk continued.**
Every side records `members_total: 2` and carries two rows, and the owner's sentence is the arithmetic
in words: `holds 2 recorded membership(s) and this page carried 2: the remainder is 7 of the read
walk's 13 item(s)`. The page block beside it is `complete: false` with `state: "first_page"` and a
published `continuation`, `page_size=6` in the scope — so the page is a position in a walk even though
the roster it lists is whole. A reader must not read `complete` as "the roster was complete": it is the
walk's flag, and the roster's own completeness is `members` against `members_total`.

**The two guarantee shapes are both present, and they are the reason the comparison vocabulary has
three "did not change" words rather than one.** Family `65a7c216-c8d0-422d-a114-6822fba97f90` records
the **same** revision `ad5f45e2-0b95-4370-8a5e-e039b23c68f9` on both sides with the text `The retry
budget is shared by integration and synchronization.` — one authored revision stands behind both
sides. Family `c23a294f-fb8a-45e4-b930-3dedbdb751bb` moves from `e38f2f7c-ef1c-4044-9c4e-f13b0b566939`
to `7d5100c2-e038-439b-987a-13758488c098` and authors different text (`The retry budget and the batch
obligation hold together under the revised member.`) — a real before/after diff. The after side of that
family also retains the before revision id, which is what "the retained revision" means on the wire.

**The member rows travel whole, and a shared revision is one revision referenced twice.** All eight
rows are `state: "recorded"`: each carries its statement, essential conditions, exclusions, lifecycle,
payload digest, provenance and sources. The same member revision is recorded under two families, which
the row states through `other_family_revision_ids` rather than copying a second revision — the case
reads that as one canonical revision referenced twice, not as two revisions.

**Seven cases drive these bytes.** They render the recorded families, their guarantees and the full
member statements; open a family and read the guarantee comparison each shape earns; keep the family
context when a member is selected and print five facts separately; keep the source explorer independent
of the selection; keep an expanded entry expanded across a layout switch; traverse the tree by keyboard
with the current selection marked; and report the filter scope without restating the comparison totals.
Nothing in those cases passes the component a value: the bodies are the whole input.

### Conventions

- Captured bytes, never hand-edited: the provenance (source script, the fixture enclosure, the one
  `<repository_id>` normalization) is stated in the consuming case file's header, and this card adds no
  second provenance.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below therefore
  cites the whole file (`:1-1`) and names the exact key path and value in the finding — that key/value
  is what a reader re-checks, because a line number cannot distinguish two facts in a one-line file.
- The body is opaque data to this client: the case types it `unknown` and narrows it at runtime, so a
  body that lost the field a case needs fails loudly instead of mounting the surface under it.
- Numbers on this card are the file's, not a summary's: byte size and digest are the file, counts are
  the owner's own published counts.

### Invariants And Boundaries

- **A captured body is evidence, not a specification.** The contract it evidences is the read response
  the route publishes and the client vocabulary that decides what may be said about it; the file is how
  the mounted case proves the route's serialization is what the component really receives.
- **A carried-whole roster is not a completed walk.** `page.complete` describes the walk; the roster's
  completeness is `members` against `members_total`. Flattening the two is the defect the sibling
  `truncated` and `walkFinal` bodies exist to pin from the other directions.
- **A `partial` family context is not a failure.** This body carries every part it did establish and
  states the parts it did not; the state word is the owner's, and the tree must not upgrade it.
- **The two guarantee shapes must not be merged.** Same-revision and distinct-revisions-different-text
  are different facts; only the first may be called "unchanged".
- **No conclusion is carried anywhere in the body.** The evidence state is `none_recorded`, the
  assessment state is `unassessed`, and the submission block is `unavailable` — the body reports what
  other owners recorded, and this capture is no exception.
- **Not browser evidence.** These are the bytes a real route published, rendered by the real client in a
  mounted test tree; they are not a live page fed by a running publication.

### Todos

None recorded. The body records a fixture enclosure's answer, and the sibling bodies carry the
remaining roster states; no obligation is attached to this file.

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
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The enclosure the bytes were recorded over, and the single normalization: the per-run fixture repository uuid is written as a placeholder.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The family context: two families returned of two, none remaining, the owner's measured row counts, and the `partial` state whose detail names every part it could not establish.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"families_remaining\":0,\"families_returned\":2,\"families_total\":2"; "\"membership_rows_total\":8"; "\"unique_member_revision_total\":4" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **A roster carried whole on a page that is a position in a walk: the owner's own carried-vs-measured sentence, the measured total, and the still-open page block with its published continuation.** | "holds 2 recorded membership(s) and this page carried 2"; "\"members_total\":2"; "\"page\":{\"complete\":false"; "\"page_size=6" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The unchanged shape: one family revision recorded by both snapshots, with the authored text it carries.** | "ad5f45e2-0b95-4370-8a5e-e039b23c68f9"; "The retry budget is shared by integration and synchronization." | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The changed shape: two distinct family revisions whose authored texts differ, and the retained before revision the after side still names.** | "e38f2f7c-ef1c-4044-9c4e-f13b0b566939"; "7d5100c2-e038-439b-987a-13758488c098"; "The retry budget and the batch obligation hold together under the revised member." | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The two families' identities and display labels, and that both selections are recorded comparisons.** | "\"display_label\":\"retry-budget-family\""; "\"display_label\":\"retry-and-anchor-family\""; "65a7c216-c8d0-422d-a114-6822fba97f90"; "c23a294f-fb8a-45e4-b930-3dedbdb751bb"; "\"state\":\"compared\"" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **Every member row on the page carries its revision content, which is why all eight rows are readable statements rather than page-scoped notices.** | "\"state\":\"recorded\""; "\"members_total\":2" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| The one constant that binds this body to its cases, and the runtime narrowing that keeps a body with a missing field from mounting the surface. | `captured("familyReview.complete.captured.json")`; `firstFamilyId` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:43-52; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:62-89; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:57-57|
| **The provenance of every captured body: the real route's bytes recorded by the leaf's probe, with the real client and component tree reading them in the cases.** | "holds the bytes"; "probe-l24-family-body.py" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:6-12 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:23-27 |
| **The two cases that render these bytes first: the families, their guarantees and the full member statements; and the guarantee comparison shape each family earns.** | "renders the recorded families, their authored guarantees and the full member statements"; `COMPLETE`; "The complete member statements, unchanged siblings included"; "opens a family review whose guarantee comparison is the shape the two recorded revisions support"; "the only shape" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:153-191; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:193-226 |
| The four further cases these bytes drive: the five separate facts beside a selected member, the selection-independent explorer, the layout switch, the keyboard traversal, and the filter scope. | "keeps the family context when a member is selected and states the five facts separately"; "keeps the complete source explorer independent of the family selection"; "keeps an expanded entry expanded across a diff-layout switch"; "marks the current selection and traverses the tree by keyboard"; "reports the filter scope without restating the comparison's totals" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:228-256; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:258-274; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:343-370; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:372-395; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:397-426 |
| **The vocabulary the two guarantee facts are read through: the comparison union and the three "did not change" shapes kept apart, decided by identity first and text second.** | `GuaranteeComparison`; `identical_text`; `unchanged_revision`; `one_sided`; `joint_guarantee` | dashboard/src/data/reviewFamily.ts:217-222; dashboard/src/data/reviewFamily.ts:224-233; dashboard/src/data/reviewFamily.ts:249-259 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the first of the leaf's seven captured family-review bodies.** It records what the bytes are (the route's own answer over a fixture enclosure, the probe that recorded them, the one `<repository_id>` normalization), the file's exact identity a reader can re-check (46,076 bytes; sha256 `82c9ca93def45bba517a295d31ca0f098c092404beb1644423d1991998f45e37`), and the one state it pins apart from its six siblings: **a roster carried whole** — every side carried the rows its owner measured (2 of 2), all eight member rows are `state: "recorded"`, and both guarantee shapes are present at once (the same revision on both sides for one family; two distinct revisions with different authored text for the other) while the family context stays `partial` because the read walk continues. It also records the citation convention these bodies force: each file is one minified line, so every reference row cites `:1-1` and names the exact key path and value, and two candidate anchors (`"members":[]` and the `recorded_revision_ids` array literal) were **dropped rather than cited** because a bracketed literal does not verify under the literal-grep rule. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
