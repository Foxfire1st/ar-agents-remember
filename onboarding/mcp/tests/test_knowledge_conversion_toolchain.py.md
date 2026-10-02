# mcp/tests/test_knowledge_conversion_toolchain.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R24 rules 5 and 9: the master line's toolchain reads the text format, and unconverted memory is read
as legacy-format and refused elsewhere once its official line is converted.** 16 test functions in the
`unit-regression` lane.

## Code Commentary

### Logic

- `test_read_ar_files_returns_legacy_format_or_resolved_references`:
  - an unconverted tree's file result is `legacy-format`, with no references or sidecar, and its knowledge
    section is `legacy-format`;
  - after conversion, the knowledge section read **through `read_ar_files`** is `recorded`, with index
    `complete`, and holds the exported invariant. This is the converted-tree coverage that replaced the
    displaced ICR-R19 route assertions (architect ruling). Since 260928-MIK-L01 the statement is read from
    the seed's leaf `rows` (the family-complete leaf read, MIK-R01) rather than the scope `items`;
  - the file result is `text/v2`, with the sidecar, numbered references, a filled-in own path, and an
    invariant target carrying its record summary.
- `test_references_are_checked_and_only_mechanical_moves_are_fixed`:
  - stale references are report-only (`findingCount` 0);
  - a quoted literal moved two lines down is re-found exactly once;
  - blobs are refreshed;
  - a changed body is left stale for the curator.
- `test_memory_quality_reads_the_converted_format`: the run is `ok`, `knowledge.converted` is present,
  the legacy-format checks are `not-applicable-converted`, and there is no drift check.
- `test_an_unconverted_leaf_is_refused_only_once_its_official_line_is_converted`: no refusal while the
  official line is unconverted; afterwards the refusal names the crossing sync and `worktree_sync`.
- `test_memory_init_creates_new_memory_in_the_text_format_only`: a new root gets the marker with exactly
  `LAYOUT_MARKER_TEXT` (`created`); a root holding a legacy card is `unconverted-existing-memory` and gets
  no marker.
- **L37: the census, the card authoring and the converted check on a converted candidate.** Eleven test
  functions:
  - `test_the_census_compares_a_converting_leaf_with_its_converted_base`: a converted card's source comes from
    the converted format, the conversion itself is no task edit, and a sidecar counts only beyond its anchors'
    mechanical fields (MIK-R30 rule 3);
  - `test_the_census_is_captured_and_rechecked_against_the_comparison_base`: both captures of the census scope
    compare against the contract's comparison base;
  - `test_a_converted_cards_kind_and_source_come_from_its_place_and_its_sidecar`;
  - `test_citation_rows_author_a_converted_cards_sidecar_with_resolved_anchors`: a new card's sidecar, and a
    reference re-authored by its number;
  - `test_one_converted_card_is_fixed_by_its_document_alone_and_legacy_keeps_the_snapshot`;
  - `test_the_converted_check_compares_an_unconverted_head_through_its_converted_base` (R3-1): a carried
    reference to a file the candidate deleted or moved is reported, never refused as newly written;
  - `test_authoring_numbers_after_existing_references_dry_runs_and_validates` (R3-2);
  - `test_the_fixer_checks_every_card_first_and_refuses_by_name` (R3-3);
  - `test_a_leftover_evidence_line_is_refused_and_only_the_named_card_loses_references` (R3-3);
  - `test_one_documents_fix_reports_its_own_stale_references_and_the_response_is_bounded`: a fix of one
    document lists that document's stale references, and the MCP response caps every list at 50 with its full
    count, while an unconverted tree's result passes through;
  - `test_two_tables_with_no_blank_line_between_them_are_refused_by_name`: a card is refused, naming the line,
    when a second table starts inside one and either holds citations; nothing is written; a card whose
    tables hold no citations is left alone; a body row of single dashes is a placeholder.

  The existing `memory_init` case also asserts the L24 nit: the failed-Git early return carries `layoutMarker`.
  `test_memory_quality_reads_the_converted_format` also asserts the final catalog's drift item on a converted
  run: `pass`, `fail` with the converted check's findings, and `fail` when neither spelling ran.

### Conventions

- `_convert_in_place` converts a fixture memory tree in place through the product's own conversion (`convert_memory`, then `write_changed`).

### Invariants And Boundaries

- The rule 9 refusal case pins that nothing changes before the official line converts, the ruling that
  keeps every route unchanged before MIK-R37.

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

The cases.

- The read tool on both formats, with the converted knowledge section through the tool. [1]
- The reference check and fixer. [2]

- Memory quality on a converted tree. [3]

- The rule 9 refusal. [4]
- `memory_init` in the text format. [5]
- Its lane row. [6]

- The census compares a converting leaf with its converted base. [7]
- Citation rows author a converted card's sidecar with resolved anchors. [8]
- One converted card is fixed by its document alone; legacy keeps the snapshot. [9]
- The converted check compares an unconverted HEAD through its converted base. [10]
- The fixer checks every card first and refuses by name. [11]
- A leftover evidence line is refused, and only the named card loses references. [12]

- One document's fix reports its own stale references, and the response is bounded. [13]
- Two tables with no blank line between them are refused by name. [14]

### Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

No cross-repo boundary is crossed by this file.
