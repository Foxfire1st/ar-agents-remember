# mcp/src/agents_remember/application/knowledge_reader/records.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**How the knowledge reader spells records, links, decisions and numbered references (MIK-R29 rules 2
and 3).** Every other reader module builds its rows from these four shapes:

- **a record summary**, what a link shows before it is followed: ID, kind, status, revision and a title read
  off the record's own fields (a target the tree does not hold is `missing: true`, never dropped);
- **a decision in full**, shown whole wherever it appears: in its truth view and in every view that links to
  it (the rule carried from L13, MIK-R13 rule 6);
- **a link**, one indexed relationship with both ends named;
- **a numbered reference**, a sidecar's `[n]` with every target resolved.

## Code Commentary

### Logic

- **Titles.** `summary_of` reads the title from the kind's field (`_TITLE_FIELDS`: a family's `title`, an
  invariant's `statement`, a decision's `context`, a facet's leading field) and shortens it with L05's
  `derived_title`, except for a family, whose title is kept whole.
- **Decisions, read once per view.** `Decisions` parses every decision of the tree into `DecisionRecord`
  once, and derives who supersedes whom with L13's `superseded_by`; a decision that does not validate is kept
  as a named problem.
- **A decision in full (carried from L13, 2026-09-30T01:45:56).** `decision_document` returns every
  alternative in order with its status, reason, `reconsiderWhen` and its `reconsiderOn` targets (L13's
  `reconsider_links`), the consequences, the decider, the **stored status** and the **derived status**
  (`derived_status`: `superseded` is never stored), what it supersedes and is superseded by, and what it
  governs (`governs_links`). A decision that cannot be read answers `unreadable` with the reason. Nothing is
  re-derived here: every one of these comes from `models/knowledge_files/decisions`.
- **Link ends.** `record_link_target` turns a record's link target into a record ID, a route
  (`route:` prefix), a code anchor or a requirement. `link_document` renders one indexed relationship,
  summarising the record at either end (file, route and history-row sources carry no summary).
- **References.** `reference_items` lists a sidecar's references in number order, each with every target:
  code and test anchors carry their path (defaulting to the card's own) so they open at their locator;
  record targets carry a summary so they open their truth view.
- **Linking records.** `records_linking` groups links by their source record, never a sidecar or history
  row, each record once with every link it records.
- **A link from a history row names the record the row is about (L37, MIK-R29 rule 5).** A history row has no
  page of its own. For a link whose source is a `history_row`, `link_document` reads the row through
  `KnowledgeIndex.history_row` and adds `sourceSubject`, the summary of the row's subject, when the index holds the
  row. Such a link carries no `sourceRecord`. File and route sources are unchanged.

### Conventions

- A missing target is shown as missing; nothing is silently filtered.
- Decision status appears twice on purpose: `storedStatus` as recorded, and `derivedStatus` as a reader
  shows it. The dashboard's truth-view header shows the derived one (ruling 2026-09-30T09:42:58, F9).

### Invariants And Boundaries

- **A decision's chosen and rejected alternatives and its derived superseded status are shown whole
  wherever the decision appears** (the rule carried from L13). Realized by `decision_document`, used by the
  path view's linked records, the invariant truth view's linked records and the decision truth view. Proved by
  `test_a_decision_truth_view_shows_alternatives_and_derived_supersession` (active at commit 1, `superseded`
  at commit 2) and by the invariant case asserting the linked decision row is `superseded` too; the reviewer's
  mutations removing it from the path and truth views were killed.
- Nothing here reads Git or writes; it shapes what the index already holds.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement that a decision is shown whole wherever it appears. [1]
- The title field per kind. [2]
- A record's summary, or `missing`. [3]
- Every decision of the tree read once; the superseding map. [4]
- A decision in full: alternatives, stored and derived status, supersession, governs. [5]
- The L13 helpers every decision field is read through. [6]

- A link target's kind; one indexed link with its record ends summarised. [7]

- Numbered references, every target resolved. [8]
- Linking records, each once. [9]

- The decision case: alternatives, and superseded derived at the later commit. [10]

- A history row's incoming link carries the record the row is about. [11]
- A decision's incoming link from a history row names the row's subject. [12]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
