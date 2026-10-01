# mcp/src/agents_remember/memory/conversion/cards.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The Markdown half of converting one onboarding card or route overview (MIK-R24 rules 1 and 3).**
`split_card` takes a legacy card apart into its metadata, its real citation rows in output order, and an
output template. `render_card` writes the converted Markdown once every real row has a reference number.

## Code Commentary

### Logic

- **Metadata.** The `| Field | Value |` table before the first `##` heading loses the seven
  `DROPPED_METADATA` fields: `path`, `repository`, `doc_type`, `governingOverview`, `lastUpdated`,
  `lastVerifiedCommitHash` and `lastVerifiedCommitDate`. Their values are still returned (`metadata`) for
  the anchor commit and the audit. Any other row (`sourceRoute`, `repo`, `generated`, …) stays in a
  smaller table, and a table left with no row is removed.
- **Update History.** Every `## Update History` section is removed, and its bytes are counted
  (`_drop_history`). Git keeps the text.
- **Citation tables.** Every `| Finding | Anchor | Source |` table outside fenced code is replaced in
  place (`_take_table`). A real row becomes a template slot for `- <finding> [n]`. A placeholder row
  (anchor and source both empty, `—` or `n/a`) produces no reference, and its finding stays as a prose line.
- **One Evidence section (`_assemble`).** Every `##` section whose heading ends in `References` or
  `Evidence` moves, in document order and one heading level lower, into one `## Evidence` section. That
  section stands where the first of them stood. A citation table in any other section (about 120 on the
  real tree) is replaced where it stands. This layout was the worker's choice where the packet is silent,
  and the architect accepted it.
- **Stray rows.** `_stray_citation_rows` lists the 1-based lines that look like citation rows (a pipe row
  with a `path:line` source) but belong to no table: typically rows appended after a blank line below a
  table. They stay unchanged, and the report lists them (219 rows in 79 cards on the real tree; review R1
  finding 4).
- **Escaping.** `render_card` substitutes each row's number through private-use sentinels (spelled
  `"\ue000{}\ue001"` in source), escapes the text with `markers.escape_markers` (the validator's own
  grammar), and only then turns the sentinels into `[n]`. So the only markers of the converted Markdown are
  the reference numbers the conversion wrote. It returns the number of marker-shaped legacy texts it
  escaped (none on the real tree).

### Conventions

- Table parsing reuses the shipped citation and document-shape parsers (`style/citations/cells`,
  `style/document_shape/tables`, `inline_scan.unfenced_lines`), so the conversion reads the same rows the
  legacy checker read.

### Invariants And Boundaries

- **All other prose is unchanged**, and no marker is placed in prose: the conversion authors no knowledge.
- A row numbered `None` (no reference) keeps its finding as prose.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The split, the render, and the rules each applies.

- The seven dropped metadata fields and the Evidence heading. [1]
- A card taken apart: metadata, rows in output order, template, stray rows. [2]
- The metadata rows are dropped; other rows stay in a smaller table. [3]
- Update History is dropped and its bytes counted. [4]
- A citation table becomes finding lines; a placeholder stays prose. [5]
- The split. [6]
- Stray citation-shaped rows are left alone and listed. [7]
- The reference sections move into one Evidence section, one level lower. [8]
- The render: sentinels, then the validator's escaping, then the numbers. [9]
- A card becomes prose, one Evidence section and numbered references. [10]
- Rendered back without history, a card reproduces its content. [11]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
