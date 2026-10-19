# mcp/src/agents_remember/cli/dashboard_review_reads.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Bind the exact inputs a recorded comparison's answers are a function of, so the reviewer's three
recorded reads — intent, entries and trees — can be served again unchanged while every one of those
inputs still holds, and computed every time when they do not. (The summary read is served by
`IntentSummaryCache`, not here.) A live comparison has no record to bind and passes straight through.

## Code Commentary

### What a kept answer is a function of

`recorded_answer_sources` resolves the leaf's own record and returns the `ReadInput` set a recorded
answer depends on; `_sources_of` names them: the record's bytes, the comparison and generation
directories its generation lives in, the worklist, and the object-store census of the trees it reads.
`_reads_from_its_record` separates a recorded comparison from a live one, which is what keeps a live
view out of the cache: it is a function of a working tree and belongs to nobody's record.

### The object dependency is checked, not counted

`_recorded_sides` names every recorded comparison's four sides — code base, code candidate, memory base
and memory candidate — deduplicated across the leaf's records, and `_trees_still_readable` proves
each of them still entirely present: one `rev-list --objects --no-object-names --missing=print` over
all of those trees fails if the traversal fails or prints any object as missing (`?`), and
`_object_bodies_readable` then makes Git consume every one of those bodies through a single
`cat-file --batch`, checking each header and length against the request so an object lost between the
traversal and the read is caught. An equal count of objects is not equal availability — one removed
tree and one added blob leave the census the same size — so a missing or unreadable tree produces the
fresh answer instead of the kept one.

### Composition, not a second implementation

`RecordedReviewAnswers.intent`, `.entries` and `.trees` key each read by the question it asks
(`_tree_key` for a tree view) and hand the sources plus a `produce` callable to
`RecordedAnswerReuse.answer`. The callable is the shipped composition the route used before this
module existed, so a kept answer and a fresh one cannot disagree about what a read means.

## Invariants And Boundaries

- A recorded answer is keyed by its record, its directories, its worklist and its objects; nothing a
  reader's open does to a working tree enters the key.
- A kept answer is byte-identical to a fresh computation of the same inputs, and is never served
  after one of those inputs changed or became unreadable.
- A live comparison is never kept here.
- This module reads the leaf's contract and Git objects; it writes no record and authorizes no path.

## Evidence

- The recorded routes' inputs are the record, its generation directories, the worklist and the object census, and a live comparison binds none of them. [1]
- A kept answer is served only while every recorded tree can still be read, so a removed tree yields the fresh answer rather than the kept inventory. [2]
- The four recorded trees one record holds are named once, for the reuse check. [3]
- Intent, entries and the tree view each pass their exact question and the shipped composition to one reuse store. [4]
