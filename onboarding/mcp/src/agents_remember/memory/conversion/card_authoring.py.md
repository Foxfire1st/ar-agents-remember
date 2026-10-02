# mcp/src/agents_remember/memory/conversion/card_authoring.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Authoring a converted card's references: citation rows in, resolved sidecar references out (L37).**
A converted card's evidence is `- <finding> [n]` lines whose `[n]` names a reference in the card's sidecar, each
target an anchor (blob, content hash and locator). A curator never writes that JSON by hand. They write the evidence
as a citation table (`| Finding | Anchor | Source |`), and the fixer (`citation_fix`, or `memory-citations --fix`,
on a converted tree) calls `author_card_references` to turn it into references.

## Code Commentary

### Logic

- `author_card_references(memory_root, code_root, *, only=None, dry_run=False)` refuses an unconverted memory root.
  It authors every card in memory first (`_author_card`), collects the refused ones by name, and only then writes
  the cards that passed: the Markdown, and the sidecar in canonical formatting. The report holds `authoredReferences`,
  `reauthoredReferences`, `removedReferences`, `authoredCards`, `createdSidecars`, `unresolvedTargets` and `refused`.
- `_load`: a card is taken up when it holds a citation table, or when it is the one named with `only`. A card
  without a sidecar gets one from `_new_sidecar`: `ar-onboarding-file/v1` with `path` the card's source and
  `realizes: []`, or for an `overview.md` `ar-onboarding-route/v1` with `path` the route (`.` for the root).
- `_author_card` removes each citation table's header and separator lines and authors every row (`_author_row`):
  - a placeholder row (anchor and source both empty or a no-citation marker) keeps its finding as prose;
  - otherwise the row becomes `- <finding> [n]`, and `references[n]` is `citations.row_reference(...)` resolved
    against the **code working tree** (captured once per run in `_Code`) by the conversion's own rules: a symbol
    the extractor binds once, a `path:start-end` range, a whole file, a URL; anything else is `unresolved` and
    reported;
  - `n` is the next free number after the sidecar's highest (`_Card.number_for`), unless the finding ends in an
    existing `[n]`: then reference `n` is re-authored in place (its targets resolved again, its note replaced).
- With `only`, `_remove_unused` drops the references the card's Markdown no longer cites. A tree-wide run never
  removes a reference.

### Conventions

- `_cards` lists every `.md` under `onboarding/` outside dot-directories, or the one card `only` names (refused when
  it names no card).
- The authored finding's markers are escaped (`escape_markers`) so a literal `[n]` in the finding is not read as a
  reference.

### Invariants And Boundaries

- **Refusals are by name, and nothing of a refused card is written**:
  - a sidecar that is not valid JSON or does not parse as a sidecar, before (`_existing_sidecar`) or after the
    authoring;
  - a row that re-authors `[n]` while another evidence line still cites `[n]` (`_leftover`), which would silently
    re-point that line;
  - two tables with no blank line between them, when either holds citations (`_merged_tables`, called in `_load`).
    The table reader ends a table only at a blank line, so the second table's header and delimiter rows would be
    authored as findings, or a citation table below another table would be skipped. A delimiter row inside a table
    is the sign (`_is_delimiter`: every cell three dashes or more, with optional alignment colons; a body cell of
    one dash is a placeholder, not a delimiter). The reason names the line and says to put a blank line above the
    second header. A card whose tables hold no citations is never refused.
- **Every card is checked before anything is written**, so a run never stops with some cards written and others
  not.
- Cards without a citation table are never touched, except the named card's unused references.
- The module authors `references` only. `realizes` and `proves` entries are the writer's (`knowledge-ingest`).
- Known limits: a removed highest number is reused by a later run; two rows that re-author the same `[n]` in one
  run are not refused; and a second table whose delimiter cells have fewer than three dashes is not refused by name.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the L37 decisions of 2026-10-01T10:06:02, 11:12:11 and 14:05:36 in `37_cutover-to-text-storage.json`, with `MIK-R21@v1` rule 1; the curator's procedure is the c-05 skill's `converted-card-workflow.md`; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: the grammar, re-authoring by number, sidecar creation, and the refusals, two touching tables among them. [1]

- The entry: author in memory first, then write the cards that passed. [2]
- One card: its tables removed, its rows authored, a leftover line refused, unused references removed for the named card. [3]
- One row: a placeholder stays prose; otherwise a numbered line and a resolved reference. [4]
- A re-authoring is refused while another evidence line still cites its number. [5]
- The sidecar a card without one gets. [6]
- The fixer calls this module on a converted tree, scoped to one document when one is named. [7]

- Two tables with no blank line between them are refused when either holds citations. [8]
- A delimiter row: every cell three dashes or more. [9]
- Merged tables are refused by name and nothing is written; a single-dash row is a placeholder. [10]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one code working tree and writes one memory tree.

No cross-repo boundary is crossed by this file.
