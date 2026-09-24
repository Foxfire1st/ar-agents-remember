# mcp/src/agents_remember/application/knowledge_dataset_contents.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_dataset_contents.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T09:20+02:00 |
| lastVerifiedCommitHash | `06ed70cfcde7e3860ee5b53435727e7512e4335c` |
| lastVerifiedCommitDate | 2026-09-24T10:53:01+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No configured Domain Documentation source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the dataset contents walk. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of why one implementation serves both callers and what the drift would cost.** | "one of them decides whether authored work may be"; "would show up as destroyed work rather than as a test" | mcp/src/agents_remember/application/knowledge_dataset_contents.py:1-21 |
| The published surface: the page cap, the value and the one entry point. | `__all__` | mcp/src/agents_remember/application/knowledge_dataset_contents.py:39-43 |
| **The page cap, generous for a real catalogue and finite for an implausible one.** | `DATASET_CONTENTS_MAX_PAGES` | mcp/src/agents_remember/application/knowledge_dataset_contents.py:45-50 |
| **The four non-merging states as a declared vocabulary.** | `ContentsState` | mcp/src/agents_remember/application/knowledge_dataset_contents.py:50-52 |
| **The four states defined, including no-file-at-all as a measurement distinct from an unreadable file.** | `DatasetContents`; "which is not the same fact as" | mcp/src/agents_remember/application/knowledge_dataset_contents.py:53-76 |
| **Absence established only by the two states that finished their work.** | `absence_established`; "manufactured work" | mcp/src/agents_remember/application/knowledge_dataset_contents.py:78-87 |
| **The one case where "no revisions" is a measurement, which is what cleanup may act on.** | `measured_empty` | mcp/src/agents_remember/application/knowledge_dataset_contents.py:89-98 |
| **The bounded walk: absent file, missing namespace, page loop, refusal as partial, and the cap as a limitation.** | `dataset_revisions`; "absence was not established" | mcp/src/agents_remember/application/knowledge_dataset_contents.py:101-180 |
| The unreadable-dataset constructor, which never reports emptiness. | `_unreadable` | mcp/src/agents_remember/application/knowledge_dataset_contents.py:183-189 |
| The refusal code carried into the partial sentence when a page refuses. | `_code_of` | mcp/src/agents_remember/application/knowledge_dataset_contents.py:192-195 |
| **Where a page's revisions come from: the rows' own subjects, with an empty revision contributing nothing.** | `_page_revisions`; "revision_id" | mcp/src/agents_remember/application/knowledge_dataset_contents.py:198-209 |
| The view surface the rows come from, which is the same one the reviewer and a planning read use. | `read_knowledge_view`; `open_view_context`; `KnowledgeRefusal` | mcp/src/agents_remember/application/knowledge_views.py:86-86; mcp/src/agents_remember/application/knowledge_views.py:292-292; mcp/src/agents_remember/models/knowledge/result.py:235-235 |
| The view request, its payload and the page bound one page carries. | `ViewRequest`; `ViewPayload`; `InvariantView`; `MAX_VIEW_ROWS`; `ViewRefusal` | mcp/src/agents_remember/models/knowledge/view.py:1117-1117; mcp/src/agents_remember/models/knowledge/view.py:934-934; mcp/src/agents_remember/models/knowledge/view.py:988-988; mcp/src/agents_remember/models/knowledge/view.py:1025-1025; mcp/src/agents_remember/models/knowledge/view.py:185-185 |
| **The two callers this one walk serves: the run's remaining-work readback and the cleanup guard.** | `dataset_revisions`; `measured_empty` | mcp/src/agents_remember/application/knowledge_bootstrap.py:197-199; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:466-470 |

## Cross-Repo References

No cross-repository behavior is implemented in this file: it reads one dataset file on the local
filesystem. The resolved settings' `crossRepo.allow` is empty, so nothing here names, reads or writes
another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T10:50+02:00 — 260921-ICR-L29 curator, **micro-round-2 bytes (documentation only)** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`): **re-read against the
  corrected docstrings; the card and the source agree** — the module docstring now opens "The answer is deliberately four-valued" and its state description reads "The four states are four different facts and are never merged", which is what this card says. All ranges were re-derived for the docstring-only line shift. **No verification stamp was advanced.**

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): created this one-to-one card for the module
  `ICR-R29@v1` introduced as **the dataset contents read**. The stamp basis is the leaf's base commit,
  because the module is untracked there. The sentence a reader must not lose is `absence_established`:
  a bounded or refused walk does **not** establish that a revision is absent, and a location with no
  dataset file at all **does** — so `remaining` and `unmeasured` in the run's report stay two different
  facts. This card also records that `measured_empty` is a measurement of zero rather than an assumption
  of emptiness, which is what makes the cleanup owner's second branch safe. No verification stamp
  beyond the leaf's base is advanced: the candidate is uncommitted and the governed closeout owns the
  real commit.
