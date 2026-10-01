# dashboard/src/panels/review/familyReview.continued.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
**re-captured by MIK-L31 from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder) with L44's producer,
first build accepted, and installed as the fixture the family workspace cases stub `fetch` with. **49,355 bytes;
sha256 `9e13e39f3eb51f83c81f5eb878917c61c1aa6a68cf9bf895218333923c27e563`**, as its row in
`familyReview.capture-provenance.json` (`mik_l31_recapture`) records. It is the `bounded1-continued` request: the
truncated body's `retry-budget-family` after-side cursor, read at page size 6.

It is data with a provenance chain, not an assembled fixture: the cases stub **only `fetch`** and let the real
client, the shared decode and the real component tree read these bytes. It is **not browser evidence**.

The envelope is the review read (`state: "review"`, `operation: "read_knowledge_review"`,
`surface_version: "knowledge-review-surface/1"`) over the fixture enclosure (`leaf_id: "260921-icr-l1"`,
master/task_ref `review-source-endpoints-fixture`) with the per-run fixture repository uuid normalized
to `<repository_id>`.

**What this body pins: it is a page of a roster walk continued from a published cursor, and it is byte-for-byte
the answer to the cursor its sibling published.** Its `payload.page.continued_from` is the same string as
`familyReview.truncated.captured.json`'s `retry-budget-family` after-side `page.continuation` (both decode to
`position 1`). It also carries a **both-sides-listed** member row whose content fell outside the page on one side.

## Code Commentary

### Logic

The consumer sends the exact cursor published by the selected side. This continued capture answers the after-side
walk of `retry-budget-family`; when the control selected the before walk or another primary revision selection,
the client rejects that response and retains the coherent display.

**The page block is the continuation answer, with both cursors on the wire.** `collection:
"family_members"`, `state: "continued"`, `continued_from` and `continuation` carried as opaque base64 cursors,
`returned` 7, `remaining` 5, `total` 12 and `total_basis: "selection"`, with the scope naming `side=after`, family
revision `79ce3ed4…`, the policy version and `page_size=6`. The two cursors decode to `knowledge-read-cursor/v1`
payloads whose position is 1 in and 7 out.

**The per-side roster page states where the cursor came from.** `retry-budget-family`'s after page is
`state: "continued"` and carries the same `continued_from` and `continuation` as the payload-level block; the other
three side pages are ordinary `first_page`s at page size 6.

**One row on this page is a membership without its content, recorded by both sides.** Member
`cb5d5f97-d379-457f-9fa4-f41ef41beeb5` (revision `3fb46ae4-dd0a-41c1-8833-7ecf69d76101`, `candidate-batch-atomicity`)
is `state: "recorded"` on the before side and `state: "content_not_on_page"` on the after side, and the row's own
detail says the content is "stated as such, not filled in". The client renders that as a statement about the page
while still drawing the statement from the side whose content is on the page.

**The family context is `partial` and its counts are the owner's.** Two families, `membership_rows_total` 8,
`unique_member_revision_total` 4; every side carried both of its 2 recorded rows. The selected subject's revision
selection is `ambiguous`, and `source.unresolved` holds two attribution rows.

**Five cases drive these bytes:** the walk case (with `truncated`), the bounded member-context case, the
uncarried-operand case, the bounded before-only case, and the workspace-state case across two page requests.

### Conventions

- Captured bytes, never hand-edited: the provenance is the receipt's `mik_l31_recapture` row.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding, because a line number
  cannot distinguish two facts in a one-line file.
- The body is opaque data to this client: the cases type it `unknown` and narrow it at runtime.
- Cursors are carried, never parsed, by the client; decoding them is a reader's verification step.
- Numbers on this card are the file's; the identities are one draw of the scenario builder.

### Invariants And Boundaries

- **A page is not a whole.** The continued page states the rows it carried, the rows remaining and the
  cursor that reaches them; it never claims the roster or the walk is complete.
- **The cursor belongs to the server.** The value the control sends is the value the page published;
  this body is the answer to exactly that value.
- **A row listed by both sides is not a missing row.** One side's content being outside the page is a
  fact about the page, and the other side's content is still rendered.
- **No conclusion is carried anywhere in the body**, and **not browser evidence**.

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
- **The page block that makes this a continuation: the collection, the continued state, both cursors, the returned/remaining/total arithmetic and the scope.** [3]
- **The row listed by both sides whose content fell outside the page on one side.** [4]
- **The family context and its owner's counts, still `partial`.** [5]
- **The receipt row for this file in the MIK-L31 re-capture: the truncated body's after-side cursor at page size 6.** [6]
- The one constant that binds this body to its cases, and the runtime narrowing. [7]
- **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** [8]
- The client sends the selected published cursor unchanged and rejects this capture when it answers another side or primary selection. [9]
- The continuation cases preserve page-scoped missing content and owner-measured totals without inventing primary statement absence. [10]
- The captured continuation verifies that family selection, filter, layout, full-file preference and continuation controls survive two page reads. [11]
- **The vocabulary the page-scoped row is read through: `content_not_on_page` as the state the distinction rests on, and `not_on_page` versus `one_sided` as two different facts.** [12]

### Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

No meaningful cross-repo references found.
