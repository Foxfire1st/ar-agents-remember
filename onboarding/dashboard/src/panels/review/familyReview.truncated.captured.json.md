# dashboard/src/panels/review/familyReview.truncated.captured.json

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every row was re-derived against the MIK-L31 re-capture, and every anchor in a row occurs on the line the row
cites. Because each captured body is one minified line, the cited range is the whole file and the finding names the
exact key path and value a reader can re-check.

- **The envelope: the one review read the surface makes, its surface version, and its state.** [1]
- **The enclosure the bytes were recorded over, and the single normalization.** [2]
- **The family context: two families, the owner's eight measured rows, and three distinct carried revisions.** [3]
- **The page-scoped fact in the owner's own words: two rows measured, one carried, on a first page that publishes the cursor that reaches the rest.** [4]
- **The walk arithmetic behind the sentence: one item returned per side, with ten, eight, twelve and eleven remaining.** [5]
- **The two families by label and identity, and the selection added on the after side.** [6]
- **The receipt row for this file in the MIK-L31 re-capture, with its digest, scenario and requests.** [7]
- The one constant that binds this body to its cases, and the runtime narrowing that keeps a body with a missing field from mounting the surface. [8]
- **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** [9]
- The real-body roster case: part of the measured rows carried, never zero. [10]
- The SYNTHETIC derivation of this body that keeps the "carried no member row" branch covered (ruling Q3). [11]
- The bounded capture keeps the exact continuation, the owner-measured counts (the loaded count read from this body) and the reader state; a returned foreign walk is rejected. [12]
- Empty-roster wording and carried counts remain owned by the same page-aware tree helpers. [13]
- Partial member context retains owner counts and continuation; completing a page is not the same as carrying the whole selection. [14]

### Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

No meaningful cross-repo references found.
