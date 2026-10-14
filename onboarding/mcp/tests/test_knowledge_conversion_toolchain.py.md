# mcp/tests/test_knowledge_conversion_toolchain.py

## Governing Overview

[tests route overview](overview.md)

## Current source contract evidence

- Say-once refusal checks message, detail and nextAction before real conversion and successful first adoption; direct naming separately asserts existence and omission of one known statement after fixture conversion, not executed general no-text proof. [15]

- The prepared-closeout source case checks its quality-phase converted comparison base. [16]

## Purpose

**MIK-R24 rules 5 and 9: converted-format tooling and the legacy boundary.** Unconverted memory remains readable as legacy-format but ordinary memory operations refuse it whether or not any line is converted. The direct file reader names converted records rather than carrying text. Existing unit-regression cases remain; composed first-conversion cases explicitly carry `pytest.mark.integration`.

## Code Commentary

### Logic

- `test_read_ar_files_names_the_converted_records_without_carrying_them` converts fixture memory, then
  calls the direct application reader with a string path. It asserts `state=named`, source existence,
  and absence of the known `Alpha adds one.` statement in the serialized answer. The earlier
  legacy/read-text/sidecar/reference-summary assertions were removed. This limited source assertion
  is neither registered-handler execution nor a universal no-text proof.
- `test_references_are_checked_and_only_mechanical_moves_are_fixed`:
  - stale references are report-only (`findingCount` 0);
  - a quoted literal moved two lines down is re-found exactly once;
  - blobs are refreshed;
  - a changed body is left stale for the curator.
- `test_memory_quality_reads_the_converted_format`: the fixture asserts `ok=false` with one
  `R22.6-carried-stale` finding at the deleted-path sidecar. `knowledge.converted` remains present,
  legacy-format checks are `not-applicable-converted`, and the retired drift check is absent.
  These are current static assertions, not a fresh execution result.
- `test_an_unconverted_leaf_is_refused_with_the_conversion_step_on_any_line`: refusal before the official line converts names `agents-remember knowledge-convert`; afterwards it also names the crossing sync and `worktree_sync`. A converted worktree is not locked.
- `test_memory_init_creates_new_memory_in_the_text_format_only`: a new root gets the marker with exactly
  `LAYOUT_MARKER_TEXT` (`created`); a root holding a legacy card is `unconverted-existing-memory` and gets
  no marker.
- **L37: the census, card authoring and converted-candidate checks.** The retained case inventory
  is listed below; the current module has 19 top-level test definitions, including its two integration-marked first-conversion cases; this is not an executed case total:
  - `test_the_census_compares_a_converting_leaf_with_its_converted_base`: a converted card's source comes from
    the converted format, the conversion itself is no task edit, and a sidecar counts only beyond its anchors'
    mechanical fields (MIK-R30 rule 3);
  - `test_the_census_is_captured_and_rechecked_against_the_comparison_base`: both captures of the census scope
    compare against the contract's comparison base;
  - `test_a_converted_cards_kind_and_source_come_from_its_place_and_its_sidecar`;
  - `test_citation_rows_author_a_converted_cards_sidecar_with_resolved_anchors`: a new card's sidecar, and a
    reference re-authored by its number;
  - `test_one_converted_card_is_fixed_by_its_document_alone_and_unconverted_is_refused`;
  - `test_the_converted_check_compares_an_unconverted_head_through_its_converted_base` (R3-1): a carried
    reference to a file the candidate deleted or moved refuses off merge as `R22.6-carried-stale`,
    never as a new anchor. The no-base leg also refuses newly introduced migration debt alongside
    `R22.6-anchor-path`; the converted-base leg and closeout quality both assert `ok=false`,
    matching carried-anchor refusals and no carried-stale report-only findings;
  - `test_authoring_numbers_after_existing_references_dry_runs_and_validates` (R3-2);
  - `test_the_fixer_checks_every_card_first_and_refuses_by_name` (R3-3);
  - `test_a_leftover_evidence_line_is_refused_and_only_the_named_card_loses_references` (R3-3);
  - `test_one_documents_fix_reports_its_own_stale_references_and_the_status_counts`: a named fix
    reports only its selected references. Its payload-builder leg supplies a prepared whole result
    through a patched `citation_fix_tool` and asserts the delivered counts, the first 10 `stale`
    entries, and exclusion of `authoring` and `rewrittenSidecars`. It does not read a log or assert
    whole-result custody; the separate logging implementation is described below;
  - `test_two_tables_with_no_blank_line_between_them_are_refused_by_name`: a card is refused, naming the line,
    when a second table starts inside one and either holds citations; nothing is written; a card whose
    tables hold no citations is left alone; a body row of single dashes is a placeholder.

  - `test_the_prepared_closeout_hands_its_quality_phase_the_converted_base` checks the
    prepared-closeout quality-phase converted comparison base.

  The existing `memory_init` case also asserts the L24 nit: the failed-Git early return carries `layoutMarker`.
  `test_memory_quality_reads_the_converted_format` also asserts the final catalog's drift item on a converted
  run: `fail`/1 for this converted fixture, `fail`/2 for the substituted failing check, and
  `fail`/0 when neither spelling ran. Content-only stale-reference advisory cases above remain separate.

### Conventions

- `_convert_in_place` converts a fixture memory tree in place through the product's own conversion (`convert_memory`, then `write_changed`).

### Invariants And Boundaries

- MIK-R46 replaces the historical conditional lock: ordinary operations refuse unconverted memory even before any official line converts. Legacy reading and conversion stay available; converted candidates and crossing sync retain their routes. The composed tests cover official-line conversion/closeout/landing and second-leaf crossing, plus conversion in place before first baseline adoption. The official-line case explicitly fast-forwards `main` to `super` as repository-check setup; it does not prove public master integration.

### Todos

None recorded.

## MIK-R46 R8: first-baseline refusal is said once

The integration-marked `test_memory_without_a_baseline_converts_in_place_then_adopts` keeps the real Git/unborn-branch setup and public conversion/adoption calls. Before conversion it asserts `state=legacy-format`, a short unconverted-root reason in `message`, and the conversion command in both `detail` and `nextAction`. It then converts in place and still asserts `ok=true`/`state=adopted`; the old long-message expectation is replaced, not the completion predicate. This case does not turn the separately open fixer R3-3 failure into whole-file green.


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






### Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

No cross-repo boundary is crossed by this file.

### Current Source-Inspection References

- Historical former both-format/inline-knowledge read account only; the current direct reader names converted records and asserts the limited omission described above. [1]
- The reference check and fixer. [2]
- The rule 9 refusal. [4]
- `memory_init` in the text format. [5]
- Its lane row. [6]
- The census compares a converting leaf with its converted base. [7]
- Citation rows author a converted card's sidecar with resolved anchors. [8]
- One converted card is fixed by its document alone; unconverted fixing refuses with the conversion step. [9]
- The fixer checks every card first and refuses by name. [11]
- A leftover evidence line is refused, and only the named card loses references. [12]
- Two tables with no blank line between them are refused by name. [14]


- Converted quality asserts ok=false for one deleted-path carried-stale refusal; catalog drift is fail/1. [3]
- The converted HEAD base distinguishes carried deleted/moved-path refusals from new anchors; no-base migration debt also refuses and closeout quality agrees. [10]
- `test_one_documents_fix_reports_its_own_stale_references_and_the_status_counts` asserts selected-document stale scope and, with a prepared producer result, delivered counts, the first 10 stale entries and exclusion of authoring/rewritten-sidecar material; it has no log-readback or custody assertion. [13]
- Current source delta inspected statically: Repair converted quality/catalog outcome, carried/new classifications and 10-entry delivery; preserve L46 and content-only advisory cases. [17]
- Separate implementation custody path: producer whole/result projection, finalized whole-result detail input, redaction, destination and size/budget/write controls; not a log-readback assertion in the conversion test. \[18] [18]
