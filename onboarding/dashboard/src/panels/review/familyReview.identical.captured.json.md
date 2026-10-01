# dashboard/src/panels/review/familyReview.identical.captured.json

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every row was re-derived against this candidate, and every anchor in a row occurs on the line the row
cites. Because each captured body is one minified line, the cited range is the whole file and the
finding names the exact key path and value a reader can re-check.

- **The envelope: the one review read the surface makes, its surface version, and its state.** [1]
- **The enclosure the bytes were recorded over, and the single normalization: the per-run fixture repository uuid is written as a placeholder.** [2]
- **The family context and the row count that differs from the `complete` body: seven measured rows and four distinct member revisions.** [3]
- **The unchanged shape: the same family revision on both snapshots, carrying the same guarantee text.** [4]
- **The identical-text shape: two distinct family revisions whose guarantee text is the same string while their payload digests differ.** [5]
- **Three sides supplied their two member updates on a first page of a continuing walk, and the identical-text family's one-row after roster was read whole.** [6]
- The one constant that binds this body to its case, and the runtime narrowing that keeps a body with a missing field from mounting the surface. [7]
- **Each member source's structured locator and state: `whole_file` and `unresolved` file locators, and a recorded 3-7 line range on the exact blob that is `unresolved` with no range.** [8]
- **The provenance of this body: made over HTTP by ICR-L44's producer in its own run at source tree `a8039b8e`, which the receipt records at its top level, carrying each member source's structured locator, resolved ranges and locator state.** [9]
- **The receipt row for this body: its digest, scenario, request and normalization, under the receipt's command, source tree and selection rule.** [10]
- **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** [11]
- The fixture case distinguishes separate guarantee revisions with identical text ("Wording unchanged", both revisions named, the text once) from the same unchanged revision. [12]
- **The comparison union these bytes are read through, and the decision order that keeps the three "did not change" shapes apart: identity first, text second.** [13]
- The guarantee block distinguishes the same revision, distinct revisions with identical text and a known one-sided guarantee. [14]

### Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

No meaningful cross-repo references found.
