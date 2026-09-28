# dashboard/src/panels/review/familyReview.complete.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.complete.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:00+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
re-captured over HTTP by the producer, command and source tree the adjacent receipt
`familyReview.capture-provenance.json` names, and installed as the fixture the family workspace case
stubs `fetch` with. **47,035 bytes; sha256
`1a218df366efaef04fd925950895bf611839c25afdfa48ac0ff5457bd558e91f`** (the digest the receipt records). The
producer rebuilt the scenario with fresh identities until the body carried the earlier capture's structural
signature, so every UUID in it is new while the roster shapes the cases read are the same.

It is data with a provenance chain, not an assembled fixture: the consuming case stubs **only `fetch`**
and lets the real client (`intentReview`), the shared decode and the real component tree read these
bytes, so what the cases exercise is the wire contract itself. It is **not browser evidence** — the
repository's Playwright configs are Dagger-only and the case file says so in its own header.

The envelope is the read the surface always makes: `state: "review"`, `operation:
"read_knowledge_review"`, `surface_version: "knowledge-review-surface/1"`, over the fixture enclosure
(`leaf_id: "260921-icr-l1"`, master/task_ref `review-source-endpoints-fixture`) with the per-run fixture
repository uuid normalized to `<repository_id>`.

**What this body pins apart from its siblings: a family roster carried whole, with each member source's
structured locator.** Every one of the four sides carried exactly the rows its owner measured (2 of 2),
every one of the eight member rows is `state: "recorded"`, and both guarantee shapes the vocabulary must
keep apart are present at once: one family selected the **same** family revision on both snapshots, the
other selected **two distinct** revisions carrying **different** authored text. It is also one of the two
family bodies that carry the member-source fields `locator`, `resolved_ranges` and `locator_state`. The
family context is still `partial`, because carried-whole rosters are not a completed read walk.

## Code Commentary

### Logic

**The family context block is a `partial` composition with all its parts carried.** `families_total` 2,
`families_returned` 2, `families_remaining` 0; `membership_rows_total` 8 (the rows the read measured)
and `unique_member_revision_total` 4 (the distinct member revisions among the rows it carried). Its
`detail` is the owner's own sentence, and it names each family with its per-side remainder — the
remainder of the **walk**, which is a different count from the roster it carried.

**Each side's roster page carried the whole roster of its family revision while the walk continued.**
Every side records `members_total: 2` and carries two rows, and the owner's sentence is the arithmetic in
words: `holds 2 recorded membership(s) and this page supplies 2 member context update(s)`, followed by the
walk's remainder. The page block beside it is `complete: false` with `state: "first_page"` and a published
`continuation`, `page_size=6` in the scope — so the page is a position in a walk even though the roster it
lists is whole. A reader must not read `complete` as "the roster was complete": it is the walk's flag, and
the roster's own completeness is `members` against `members_total`.

**The two guarantee shapes are both present, and they are the reason the comparison vocabulary has
three "did not change" words rather than one.** Family `retry-budget-family` records the **same**
revision on both sides with the text `The retry budget is shared by integration and synchronization.` —
one authored revision stands behind both sides. Family `retry-and-anchor-family` moves from one revision
to another and authors different text (`The retry budget and the anchor identity rule hold together.`
before, `The retry budget and the batch obligation hold together under the revised member.` after) — a
real before/after diff. The after side of that family also retains the before revision id in its
`recorded_revision_ids`, which is what "the retained revision" means on the wire.

**The member rows travel whole, and a shared revision is one revision referenced twice.** All eight
rows are `state: "recorded"`: each carries its statement, essential conditions, exclusions, lifecycle,
payload digest, provenance and sources. The same member revision is recorded under two families, which
the row states through `other_family_revision_ids` rather than copying a second revision.

**Each member source carries its structured locator and locator state.** The four sources on this body
all have `file` locators, so none carries a range: the `anchor-identity-preservation` source on the exact
recorded blob is `whole_file`, and the three `shared-retry-budget` sources whose recorded path the tree no
longer holds are `unresolved` beside `resolution: "path_absent"`. `resolved_ranges` is `[]` on every
source here.

**Seven cases drive these bytes.** They render the recorded families, their guarantees and the full
member statements; open a family and read the guarantee comparison each shape earns; keep the family
context when a member is selected and print five facts separately; keep the source explorer independent
of the selection; keep an expanded entry expanded across a layout switch; traverse the tree by keyboard
with the current selection marked; and report the filter scope without restating the comparison totals.
Nothing in those cases passes the component a value: the bodies are the whole input.

### Conventions

- Captured bytes, never hand-edited: the provenance is the receipt `familyReview.capture-provenance.json`
  (command, route, source tree, selection rule, signature, attempts, capture-record digest and the one
  `<repository_id>` normalization), pointed at by the consuming case file's header; this card adds no
  second provenance.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below therefore
  cites the whole file (`:1-1`) and names the exact key path and value in the finding — that key/value
  is what a reader re-checks, because a line number cannot distinguish two facts in a one-line file. Rows
  name labels and sentences rather than the per-build UUIDs, which change on every re-capture.
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
- **No conclusion is carried anywhere in the body.** The body reports what other owners recorded.
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
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The enclosure the bytes were recorded over, and the single normalization: the per-run fixture repository uuid is written as a placeholder.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The family context: two families returned of two, none remaining, the owner's measured row counts, and the `partial` state whose detail names every part it could not establish.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"families_remaining\":0,\"families_returned\":2,\"families_total\":2"; "\"membership_rows_total\":8"; "\"unique_member_revision_total\":4" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **A roster carried whole on a page that is a position in a walk: the owner's own carried-vs-measured sentence, the measured total, and the still-open page block with its published continuation.** | "holds 2 recorded membership(s) and this page supplies 2 member context update(s)"; "\"members_total\":2"; "\"page\":{\"complete\":false"; "\"page_size=6" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The unchanged shape: one family revision recorded by both snapshots, with the authored text it carries.** | "\"display_label\":\"retry-budget-family\""; "The retry budget is shared by integration and synchronization." | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The changed shape: two distinct family revisions whose authored texts differ, and the retained before revision the after side still names.** | "The retry budget and the anchor identity rule hold together."; "The retry budget and the batch obligation hold together under the revised member."; "\"recorded_revision_ids\"" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **The two families' display labels, and that both selections are recorded comparisons.** | "\"display_label\":\"retry-budget-family\""; "\"display_label\":\"retry-and-anchor-family\""; "\"state\":\"compared\"" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **Each member source's structured locator and state: file locators only, `whole_file` on the exact blob, `unresolved` where the path is absent, and no resolved range anywhere.** | "\"locator\":{\"kind\":\"file\"}"; "\"locator_state\":\"whole_file\""; "\"locator_state\":\"unresolved\""; "\"resolution\":\"path_absent\""; "\"resolved_ranges\":[]" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| **Every member row on the page carries its revision content, which is why all eight rows are readable statements rather than page-scoped notices.** | "\"state\":\"recorded\""; "\"members_total\":2" | dashboard/src/panels/review/familyReview.complete.captured.json:1-1 |
| The one constant that binds this body to its cases, and the runtime narrowing that keeps a body with a missing field from mounting the surface. | `captured("familyReview.complete.captured.json")`; `firstFamilyId` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:63-72; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:82-109; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:77-77 |
| **The provenance of this body: re-captured over HTTP by the producer, command and source tree the receipt names, carrying each member source's structured locator, resolved ranges and locator state.** | "familyReview.capture-provenance.json"; "re-captured over HTTP" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:8-13 |
| **The receipt row for this body: its digest, scenario, request and normalization, under the receipt's command, source tree and selection rule.** | "familyReview.complete.captured.json"; "captured_source_tree" | dashboard/src/panels/review/familyReview.capture-provenance.json:1-25 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:33-37 |
| **The two cases that render these bytes first: the families, their guarantees and the full member statements; and the guarantee comparison shape each family earns.** | "renders the recorded families, their authored guarantees and the full member statements"; `COMPLETE`; "The complete member statements, unchanged siblings included"; "opens a family review whose guarantee comparison is the shape the two recorded revisions support"; "the only shape" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:163-201; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:203-236 |
| The four further cases these bytes drive: the five separate facts beside a selected member, the selection-independent explorer, the layout switch, the keyboard traversal, and the filter scope. | "keeps the family context when a member is selected and states the five facts separately"; "keeps the complete source explorer independent of the family selection"; "keeps an expanded entry expanded across a diff-layout switch"; "marks the current selection and traverses the tree by keyboard"; "reports the filter scope without restating the comparison's totals" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:238-266; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:268-284; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:353-380; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:382-405; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:407-436 |
| **The vocabulary the two guarantee facts are read through: the comparison union and the three "did not change" shapes kept apart, decided by identity first and text second.** | `GuaranteeComparison`; `identical_text`; `unchanged_revision`; `one_sided`; `joint_guarantee` | dashboard/src/data/reviewFamily.ts:243-248; dashboard/src/data/reviewFamily.ts:250-259; dashboard/src/data/reviewFamily.ts:275-285 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`dashboard/src/panels/review/ReviewWorkspace.family.test.tsx`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the body was re-captured over HTTP from the real review route (47,035 bytes; sha256 `1a218df3…e91f`, recorded in `familyReview.capture-provenance.json`) so its member sources carry `locator`, `resolved_ranges` and `locator_state`. Every identity in it is new, so the card now names labels and sentences instead of per-build UUIDs, states the roster sentence as the route now words it (`this page supplies 2 member context update(s)`), describes the four sources' locator states, and points its provenance at the receipt instead of the retired probe. The shapes it pins are unchanged. No verification stamp was advanced.

- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the first of the leaf's seven captured family-review bodies.** It records what the bytes are (the route's own answer over a fixture enclosure, the probe that recorded them, the one `<repository_id>` normalization), the file's exact identity a reader can re-check (46,076 bytes; sha256 `82c9ca93def45bba517a295d31ca0f098c092404beb1644423d1991998f45e37`), and the one state it pins apart from its six siblings: **a roster carried whole** — every side carried the rows its owner measured (2 of 2), all eight member rows are `state: "recorded"`, and both guarantee shapes are present at once (the same revision on both sides for one family; two distinct revisions with different authored text for the other) while the family context stays `partial` because the read walk continues. It also records the citation convention these bodies force: each file is one minified line, so every reference row cites `:1-1` and names the exact key path and value, and two candidate anchors (`"members":[]` and the `recorded_revision_ids` array literal) were **dropped rather than cited** because a bracketed literal does not verify under the literal-grep rule. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
