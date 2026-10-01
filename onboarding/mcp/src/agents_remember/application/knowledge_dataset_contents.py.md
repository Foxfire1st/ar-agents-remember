# mcp/src/agents_remember/application/knowledge_dataset_contents.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**Which invariant revisions one knowledge dataset file holds, read through the shipped view API
(ICR-R29@v1).** Two operations need the same question answered the same way, because one of them
decides whether authored work may be deleted: the bootstrap run asks it of the repository's published
dataset to name what is still owed, and the staging cleanup owner asks it of a staged candidate to
decide whether that candidate is the published truth or holds authored rows nobody else has. A second
implementation of the walk would let those two answers drift, and the drift would show up as destroyed
work rather than as a test failure.

**The answer is deliberately multi-valued, and `absence_established` is the field that carries it.** A
walk that finished *measured* the set, so a revision not in it is absent. A walk that stopped — a page
cap, a refusal, a page that could not be rendered — did not measure the whole set, so absence was not
established for anything it had not reached, and the caller is told so instead of receiving a shorter
set it would read as complete. `revisions` is a measurement in both cases: a revision the walk actually
read is present whatever the walk did afterwards.

Nothing here opens a database directly, computes a digest, or decides what a record means. The rows come
from `read_knowledge_view` at the dataset's own snapshot, which is the same surface the reviewer and a
planning read use.

## Code Commentary

### Logic

**Four states, four different facts, never merged** (`:50-71`). `ContentsState` is the
`Literal["complete", "absent", "partial", "unavailable"]` and the `DatasetContents` docstring defines
each: `complete` is a walk that reached its end inside the page cap, so an absent revision is a
**measured** absence; `absent` is **no dataset file at the location at all**, which is also measured —
nothing was written there, which is not the same fact as a file that could not be read; `partial` is a
walk that stopped early or a page that refused, so absence was not established for anything it had not
reached; `unavailable` is a file that is there and could not be read as a dataset of this code, or no
namespace was established to address it.

**`absence_established` is true for exactly the two states that finished their work** (`:78-87`):
`complete` and `absent`. The docstring states the consequence of getting it wrong: a caller that read a
partial walk or an unreadable file as absent would turn a bounded read into manufactured work.

**`measured_empty` is the one case where "no revisions" is a measurement** (`:89-98`):
`absence_established and not self.revisions`. That single property is what lets the cleanup owner remove
a candidate holding no authored row without guessing.

**The walk is a bounded continuation loop over the invariant view** (`:101-180`). A missing file is
answered before any read (`absent`, with `pages=0`); a missing namespace is answered next
(`unavailable`, because a view read refuses a namespace its file does not carry, and that refusal is
reported as an unreadable dataset rather than as an empty one); `open_view_context` is then asked, and
its `KnowledgeRefusal` becomes `unavailable`. Each page is read with `limit=MAX_VIEW_ROWS`, the page's
own revisions are added, and the walk ends as `complete` when the payload carries no continuation. A
page that refuses ends the walk as `partial` **carrying the revisions already found**, and reaching
`DATASET_CONTENTS_MAX_PAGES` (`:48`) ends it as `partial` with the sentence saying the walk was stopped
and absence is not established for what it had not reached.

**A page's revisions come from the rows' own subjects** (`:198-207`). `_page_revisions` reads
`row.subject.revision_id` and a row whose subject carries no revision is **not** counted: the subject is
what the store recorded, and an empty revision is a fact about that row rather than a revision id this
read may invent.

**The page cap is generous for a real catalogue and finite for an implausible one** (`:45-48`): a page
carries at most the view's own `MAX_VIEW_ROWS`, and reaching the cap is reported as a limitation, never
as an absence.

### Conventions

The module imports the application view surface and the knowledge model types, and nothing from the
kernel or the worktree planes. It is a read: it writes nothing and holds no state beyond one walk.

### Invariants And Boundaries

- `complete` and `absent` establish absence; `partial` and `unavailable` do not.
- A location with **no dataset file** is a measured absence, distinct from a file that could not be read.
- A missing namespace is `unavailable`, never an empty dataset.
- A walk that stopped still reports the revisions it read; it does not report a shorter complete set.
- No database is opened directly and no digest is computed here; the rows are the view's rows.
- A row whose subject carries no revision id contributes nothing.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

No external documentation is required for the dataset contents walk.

### Repo-Internal References

- **The module's own statement of why one implementation serves both callers and what the drift would cost.** [1]
- The published surface: the page cap, the value and the one entry point. [2]
- **The page cap, generous for a real catalogue and finite for an implausible one.** [3]
- **The four non-merging states as a declared vocabulary.** [4]
- **The four states defined, including no-file-at-all as a measurement distinct from an unreadable file.** [5]
- **Absence established only by the two states that finished their work.** [6]
- **The one case where "no revisions" is a measurement, which is what cleanup may act on.** [7]
- **The bounded walk: absent file, missing namespace, page loop, refusal as partial, and the cap as a limitation.** [8]
- The unreadable-dataset constructor, which never reports emptiness. [9]
- The refusal code carried into the partial sentence when a page refuses. [10]
- **Where a page's revisions come from: the rows' own subjects, with an empty revision contributing nothing.** [11]
- The view surface the rows come from, which is the same one the reviewer and a planning read use. [12]
- The view request, its payload and the page bound one page carries. [13]
- **The two callers this one walk serves: the run's remaining-work readback and the cleanup guard.** [14]

### Cross-Repo References

No cross-repository behavior is implemented in this file: it reads one dataset file on the local
filesystem. The resolved settings' `crossRepo.allow` is empty, so nothing here names, reads or writes
another repository.

No meaningful cross-repo references found.
