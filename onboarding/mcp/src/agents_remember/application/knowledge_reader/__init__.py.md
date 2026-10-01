# mcp/src/agents_remember/application/knowledge_reader/__init__.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The entry point of the path-based knowledge reader (MIK-R29): one read-only question per call, answered
from one memory tree.** The dashboard's Knowledge area addresses every view by the values its URL carries:
the repository, the memory tree (`published` by default, a memory commit, or `leaf:<scope>`) and the view's
own subject (a path, a record ID, a census ID, a locator, a continuation). `read_knowledge_reader` checks the
view name, opens the selection (`selection.open_selection`), dispatches to the view's function, and wraps
the answer in the reader's envelope: `view`, `state` and the `selection` block.

The reader needs no task: a leaf is only one of the ways to name a tree. It is reached only through the
composition root's `knowledge_reader` port (`cli/dashboard.py`) and the GET route in
`serving/knowledge_reader.py`.

## Code Commentary

### Logic

- **The views.** `READER_VIEWS` names nine: `selections`, `tree`, `path`, `subtree`, `record`, `records`,
  `census`, `without-proof` and `code`. Any other name answers `invalid-request` before anything is read.
- **Selections first.** `selections` needs no opened tree (`selection.selection_options`), so it is answered
  before `open_selection`. Every other view opens the selection; a `ReaderUnavailable` (`not-converted`,
  `unavailable`, `invalid-request`) is returned as its own typed answer with the requested commit spelling.
- **Dispatch.** `_answer` routes `census`, `code` (which must name a path) and `record` (which must name an
  ID; an ID the tree does not hold is `not-found`), and a table of the remaining views, each answered with
  `state: "view"`.
- **Failures.** A `ReaderRequestError` (a bad path, a malformed locator, a missing subject) becomes
  `invalid-request`, which the route serves as 400. Any member of `READ_FAILURES` becomes
  `state: "unavailable"` with the exception's type and text. Programming errors are not caught (review F11).
- **The envelope.** The answer is `{"view", "selection": selection.to_document(), **answer}`. Because the
  answer's own keys come last, an answer that carries its own `selection` block overrides the default: a
  resumed `subtree` page returns the measured selection, so its envelope names the code tree its page was
  measured at (ruling 2026-09-30T11:24:12, R3-1).
- **Lifetime.** The opened selection is a context manager; its index connection is closed when the answer
  is built.

### Conventions

- `ReaderQuery` is the serving tier's `KnowledgeReaderQuery`: the application imports the transport's query
  type, not the other way round, so the route stays transport-only.
- Every answer names what kind of answer it is in `state`; the caller never infers it from an empty body.

### Invariants And Boundaries

- **Candidate invariant (not ingested): the reader never writes a repository.** It reads the derived index
  (MIK-R23) and Git objects only; building a commit's index writes only the coordination runtime's cache
  (ruling 2026-09-30T09:42:58 Q2). Realized by the GET-only route, the reads in `selection.py`, `files.py`
  and `timeline.py`, and no write call anywhere in the package. Proved by
  `test_the_route_serves_every_view_and_the_reader_writes_nothing` (refs, status and object counts of both
  repositories unchanged after every view) and
  `test_the_published_tree_reads_uncommitted_state_writes_nothing_and_offers_a_pin` (a dirty published tree),
  and by the worker's and reviewer's real-data snapshots on the converted scratch.
- **Candidate invariant (not ingested): every reader answer names the code tree it measured and its
  source.** Realized by `ReaderSelection.to_document` (`codeTree`, `codeSource`, `codeNote`) in this
  envelope, and by the subtree page's own measured selection block (R3-1). Proved by the selection tests
  (`paired-code-commit`, `checkout-head`, the leaf note) and
  `test_a_subtree_walk_measures_every_page_at_the_code_tree_it_began_at`.
- **Unconverted memory reads are unchanged.** An unconverted tree answers `not-converted` before any index
  is built; the landed routes answer byte-identically base against worktree (the worker's and reviewer's
  unconverted comparisons). Inert on the installed runtime until MIK-R37.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of the views, read-only reads and named failures. [1]
- The nine views. [2]
- One question: selections first, the selection opened, the typed failures and the envelope. [3]
- Dispatch by view; a record the tree does not hold is `not-found`. [4]
- The `invalid-request` answer. [5]
- The measured selection block a subtree page returns in place of the default (R3-1). [6]
- The composition root's port that calls this function. [7]
- The route case: every view served, nothing written. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
