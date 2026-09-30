# mcp/src/agents_remember/application/knowledge_reader/records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_reader/records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement that a decision is shown whole wherever it appears. | "**A decision** is always shown whole wherever it appears" | mcp/src/agents_remember/application/knowledge_reader/records.py:1-17 |
| The title field per kind. | `_TITLE_FIELDS` | mcp/src/agents_remember/application/knowledge_reader/records.py:54-65 |
| A record's summary, or `missing`. | `record_summary`; `summary_of` | mcp/src/agents_remember/application/knowledge_reader/records.py:69-75; mcp/src/agents_remember/application/knowledge_reader/records.py:78-90 |
| Every decision of the tree read once; the superseding map. | `Decisions` | mcp/src/agents_remember/application/knowledge_reader/records.py:94-116 |
| A decision in full: alternatives, stored and derived status, supersession, governs. | `decision_document` | mcp/src/agents_remember/application/knowledge_reader/records.py:119-157 |
| The L13 helpers every decision field is read through. | "from agents_remember.models.knowledge_files.decisions import (" | mcp/src/agents_remember/application/knowledge_reader/records.py:29-34 |
| A link target's kind; one indexed link with its record ends summarised. | `record_link_target`; `link_document` | mcp/src/agents_remember/application/knowledge_reader/records.py:160-170; mcp/src/agents_remember/application/knowledge_reader/records.py:173-189 |
| Numbered references, every target resolved. | `reference_items`; `_reference_target` | mcp/src/agents_remember/application/knowledge_reader/records.py:192-210; mcp/src/agents_remember/application/knowledge_reader/records.py:213-227 |
| Linking records, each once. | `records_linking` | mcp/src/agents_remember/application/knowledge_reader/records.py:230-248 |
| The decision case: alternatives, and superseded derived at the later commit. | `test_a_decision_truth_view_shows_alternatives_and_derived_supersession` | mcp/tests/test_knowledge_reader.py:898-910 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new module MIK-R29 adds, recording the rule carried from L13 at 01:45:56 (a decision's chosen and rejected alternatives and its derived superseded status are shown whole, read through `models/knowledge_files/decisions`) and ruling 09:42:58 F9 (the derived status heads the truth view). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
