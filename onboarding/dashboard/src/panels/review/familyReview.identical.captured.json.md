# dashboard/src/panels/review/familyReview.identical.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.identical.captured.json` |
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
family workspace case stubs `fetch` with. **45,393 bytes; sha256
`b018b63cd2df28e6a2a3dc16d639bf8f4bcdbc4541e2e1639e6e23bb92bd7062`.** It is untracked in this leaf's
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

**What this body pins apart from its six siblings: two DISTINCT family revisions whose authored
guarantee text is identical — `identical_text`, never "unchanged" — beside the one shape that really is
one revision on both snapshots.** Both shapes are in this one body. One family records the **same**
revision on both sides with a single payload digest, which is the only shape allowed to say the
guarantee is unchanged. The other moves from revision `6a875af6-6ff7-4bb1-b390-5b7f95fc9e58` to
revision `ff248d1c-d45c-4fd1-a8e1-f3d9f92fc6a9`, two different `payload_digest` values, and the *same*
`joint_guarantee` sentence — something was authored between them, and the text is what did not move.

## Code Commentary

### Logic

**The family context is `partial` with two families and the owner's measured counts.** Two returned of
two total, none remaining; `membership_rows_total` 7 and `unique_member_revision_total` 3 — fewer than
the `complete` body's 8 and 4, because this enclosure's second family records one member on the after
side rather than two. There is **no payload-level `page` block** in this body: it is a first read whose
per-side roster pages carry the cursors.

**The unchanged shape is decided by identity, and the body carries its evidence.** Family
`2e1099d4-f808-4880-8c2a-40a2dc90df37` records revision
`78ead1e4-77d5-4b06-9be9-7bc5d15ce307` on both snapshots with the one payload digest
`2be6d00757a83f7a3a5c4b4ce862251912802144c32b59e5c479746046ba66e` (the same digest on both sides) and
the text `The retry budget is shared by integration and synchronization.` Identity and digest agree, so
one authored revision stands behind both sides: this is the shape the client must render as
`unchanged_revision`.

**The identical-text shape is decided by identity first and text second, and this body is its only
carrier here.** Family `3b8d4338-7b3e-4edf-97d8-7fc81f396c9a` records revision `6a875af6-...` before and
revision `ff248d1c-...` after: two different revision identities, two different payload digests
(`4d9fae1f2f40779ae85f777348c6ff315c3ffd71c57007e0cd35cddabe57dbef` and
`d744d03288ae29080aa0dd909b201e507bf5f0ea569d7235ddcbe284ee78a107`), and one identical
`joint_guarantee` string. The vocabulary decides this in that order on purpose — same revision means one
authored revision, distinct revisions with equal text means `identical_text`, and only differing text is
`changed` — so a surface cannot reach "unchanged" by comparing text.

**Both rosters on this body were carried whole.** The before side of family 1 carried 2 of 2 and the
after side 2 of 2; the before side of family 2 carried 2 of 2 and its after side carried
`holds 1 recorded membership(s) and this page carried 1`. No row here is a page-scoped notice, so the
guarantee comparison is the only thing this body is about.

**One case drives these bytes, and it reads which family is which from the rendered blocks rather than
from row order.** It opens the second family and asserts the identical-text block names **different
family revisions** and says `A revision was authored between them; the text is what did not move.`, with
the unchanged block absent and the phrase `so the guarantee is unchanged` absent from it; it then opens
the first family and asserts the unchanged block says the two snapshots selected the **same** family
revision, with the identical-text block absent. That pairing is the whole point: the same two sentences
must not be interchangeable.

### Conventions

- Captured bytes, never hand-edited: the provenance lives in the consuming case file's header, and this
  card adds no second provenance.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding, because a line number
  cannot distinguish two facts in a one-line file.
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
- **A captured body is evidence, not a specification.** The contract it evidences is the read response
  the route publishes and the comparison union that decides which sentence a surface may use.
- **No page block is not a missing page.** This body is a first read: the per-side roster pages carry
  their own cursors, and the absence of a payload-level page is the shape of that read.
- **No conclusion is carried anywhere in the body.** The evidence state is `none_recorded`, the
  assessment state is `unassessed`, and the submission block is `unavailable`.
- **Not browser evidence.** These are the bytes a real route published, rendered by the real client in a
  mounted test tree; they are not a live page fed by a running publication.

### Todos

None recorded. The three "did not change" guarantee shapes have their carriers across this file and its
siblings, and no obligation is attached to this one.

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
| **The family context and the counts that differ from the `complete` body: seven measured rows and three distinct member revisions.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"membership_rows_total\":7"; "\"unique_member_revision_total\":3" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **The unchanged shape: the same family revision on both snapshots, carrying the same payload digest.** | "78ead1e4-77d5-4b06-9be9-7bc5d15ce307"; "\"payload_digest\":\"2be6d00757a83f7a3a5c4eb4ce862251912802144c32b59e5c479746046ba66e\""; "2e1099d4-f808-4880-8c2a-40a2dc90df37"; "\"state\":\"first_page\"" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **The identical-text shape: two distinct family revisions whose guarantee text is the same string while their payload digests differ.** | "6a875af6-6ff7-4bb1-b390-5b7f95fc9e58"; "ff248d1c-d45c-4fd1-a8e1-f3d9f92fc6a9"; "\"joint_guarantee\":\"The retry budget and the anchor identity rule hold together.\""; "\"payload_digest\":\"4d9fae1f2f40779ae85f777348c6ff315c3ffd71c57007e0cd35cddabe57dbef\""; "\"payload_digest\":\"d744d03288ae29080aa0dd909b201e507bf5f0ea569d7235ddcbe284ee78a107\""; "3b8d4338-7b3e-4edf-97d8-7fc81f396c9a" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| **Both rosters on this body were carried whole, including the one-row after roster of the identical-text family.** | "holds 1 recorded membership(s) and this page carried 1"; "holds 2 recorded membership(s) and this page carried 2" | dashboard/src/panels/review/familyReview.identical.captured.json:1-1 |
| The one constant that binds this body to its case, and the runtime narrowing that keeps a body with a missing field from mounting the surface. | `captured("familyReview.identical.captured.json")`; `firstFamilyId` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:65-68; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:74-97|
| **The provenance of every captured body: the real route's bytes recorded by the leaf's probe, with the real client and component tree reading them in the cases.** | "holds the bytes"; "probe-l24-family-body.py" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:6-12 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:23-27 |
| The fixture case distinguishes separate guarantee revisions with identical text from the same unchanged revision. | "distinguishes two distinct revisions with identical text from one unchanged revision" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:509-530 |
| **The comparison union these bytes are read through, and the decision order that keeps the three "did not change" shapes apart: identity first, text second.** | `GuaranteeComparison`; `identical_text`; `unchanged_revision`; `one_sided`; `joint_guarantee`; `memberComparison` | dashboard/src/data/reviewFamily.ts:217-222; dashboard/src/data/reviewFamily.ts:224-233; dashboard/src/data/reviewFamily.ts:41-41; dashboard/src/data/reviewFamily.ts:254-254; dashboard/src/data/reviewFamily.ts:257-257; dashboard/src/data/reviewFamily.ts:285-296 |
| The guarantee block distinguishes the same revision, distinct revisions with identical text and a known one-sided guarantee. | `GuaranteeComparisonBlock` | dashboard/src/panels/review/FamilyReviewCenter.tsx:104-169 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **citation repair only, second move:** the F1 fix round moved the guarantee-level blocks in `panels/review/FamilyReviewCenter.tsx` again, so this card's three ranges became `:132-1230`, `:156-1230` and `:156-1234`; the anchors still resolve inside them. The captured body itself is unchanged. No verification stamp was advanced.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the row naming the two renderings this body's case reads was re-anchored, and no claim wording changed.** L36's insertion moved the guarantee-level blocks those anchors live in, so the three ranges became `:132-1200`, `:156-1200` and `:156-1204`; the anchors (`review-center-guarantee-identical-text`, `review-center-guarantee-unchanged`, `identical_text`, `one_sided`) all resolve inside them. The captured body itself is unchanged and this leaf re-measured A3's member order on the new build as untouched. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the leaf's identical-text guarantee body.** It records the file's exact identity (45,393 bytes; sha256 `b018b63cd2df28e6a2a3dc16d639bf8f4bcdbc4541e2e1639e6e23bb92bd7062`) and the state it pins apart from its six siblings: **two DISTINCT family revisions whose authored guarantee text is identical**, carrying two different payload digests and the same `joint_guarantee` string, beside the one shape that really is one revision on both snapshots (same revision, same digest) — so this single body holds both the `identical_text` shape and the `unchanged_revision` shape the case must keep apart. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
