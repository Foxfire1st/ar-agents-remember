# mcp/tests/test_knowledge_validator.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R22 rules 1–9, MIK-R27 admission and MIK-R80 overview order at unit level, over converted fixture trees.** Each test changes one thing in the fixture tree and checks the owning rule's rendered file, field and rule (`_only`). The admission section exercises the rules MIK-R27 adds to the registry; the overview section exercises purpose-first, no leaf/date sections and terminal citation placement. Registered in the `unit-regression` lane. This card describes definitions and assertions, not a claim that a particular test run passed.

## Code Commentary

### Logic

The admission registry pin includes refusing `R27.4-record-kept`; named sync/conversion reporting on old admission does not waive base-held record retention. Ordinary unsupported existing criteria now refuse off merge.

- **Baseline:** the fixture explicitly supplies its own converted comparison base and asserts a
  pass with only carried incomplete `LEGACY_COUNT` reporting. Registry pins distinguish MIK-R22
  `merge_reports` (`R22.6-carried-stale`) from `migration_debt` (missing Markdown and unresolved
  targets), and assert no registered plain report-only rules. Debt-positive cases supply a base
  that already holds the actual finding; these are not no-base passes.
- **Rule 1:** a bad field, a non-canonical file (naming the formatter), a file outside the layout, and a misplaced sidecar.
- **Rule 2:** the filename prefix, duplicate IDs after a merge (`merge conflict:` naming both files), the packet's conforming parallel-mint example, and duplicate entry IDs across sidecars.
- **Rules 4 and 5:** an invariant that lists its realizations; a missing family member.
- **Rule 6, relocated definitions:** the six anchor-path cases now live in `test_validator_link_targets.py`, not this module. That owner checks an added anchor at a missing path, a carried anchor at a deleted path (refused off merge under `R22.6-carried-stale`; with an empty code tree the family's carried routes also refuse under `R04.1-carried-route-absent`; the boundary sync merge reports), the packet's boundary merge example, re-anchored and moved entries, locator and content rules, and an unconverted base with the standalone conversion.
- **Rule 7:** a closed history file is frozen (edited, deleted, closed in one merge parent); an open one may change; history is shape-only (the packet's rename boundary example).
- **The retired subject kept in the tree (MIK-R09, L09 review R2-1, ruling 2026-09-30T17:59:48).** The three rule-7 cases use a history file whose subject `INV-RET1R3` stands for "a subject that has since been retired". Since L09, MIK-R09's `R09-history-rows` rule checks every history file's subjects at every route (`unknown_subjects`), so a subject absent from the tree would now refuse. MIK-R22 rule 3 says records are never deleted (retiring sets `status: retired` and keeps the file), so the fixtures now model it faithfully: `RETIRED` adds `INV-RET1R3` with `status: retired` (and an unchecked admission) to each tree, including the left merge parent. The assertions are unchanged, and the packet's boundary example (a renamed `before` path in a closed file) still passes.
- **Rules 8 and 9:** applicability by the marker; a later refusing rule runs everywhere and
  `test_a_later_packets_rule_runs_everywhere_and_plain_report_only_is_refused` asserts that
  plainly report-only registration raises `ValueError` and never enters the registry.
- **Markers:** the grammar table and the invalid-number message.
- **MIK-R27, the admission rule** (leaf 260928-MIK-L27), with helpers that change one record's admission, drop the proof sidecar's `proves`, leave `INV-7K3F9Q`'s realizations in `integrate.py` only, or add an exported invariant (`_with_export`: its ID is `derived_record_id("invariant", EXPORTED_LEGACY_ID)`, or a forged ID when `identifier` is given):
  - the packet's admitted example supplies a genuine base lacking the target ID, asserts new-record
    admission passes, and keeps a reference-only negative with that same base; the admitted prose
    cases also omit the target in their bases so existing-record dispatch cannot produce a vacuous pass;
  - **reference-only justifications are refused**, naming the record, `admission.justification` and the criterion: 20 refused forms (the packet's "introduced by L43", bare IDs, D-IDs and hashes by ruling 22:11:24 Q2, and the provenance phrasings of ruling 23:04:57 F1 such as "Per ruling D14", "Added in commit a4eba7b7", "L43/L44", "Implements R27.2", "ICR L45", "Added on 2026-09-28 in L43"), and 9 admitted ones, including real prose with reference-shaped words ("Deadbeef cafe faced a decade", "Uses D3 to render the chart", "L1 cache and L2 cache"); a new family and a new decision are refused the same way;
  - no criterion is refused by the shape rule `R22.1-shape` (field `admission…criteria`), and `legacy-unassessed` on a new record by `R27.2-new-record`;
  - an unsupported `guarded_by_test` (no proof) and an unsupported `spans_locations` (one file, named) are refused on a new record;
  - **an existing record whose test was deleted refuses off merge**; the current renamed case
    checks the live single-base refusal and the sync-merge report with its named repair reason;
  - unsupported exported live records refuse off merge; retired records remain exempt; a record
    held by either merge parent is existing and its unsupported criterion reports at sync;
  - **a forged legacy ID does not make a record exported** (ruling 23:04:57 F2): the genuine export is not new but its unsupported criterion still refuses under the existing rule, and the same record under `INV-F0RG3D` is refused as new, for the claim and for `legacy-unassessed`;
  - based legacy debt names live records by kind and drops assessed/retired ones. Counterexamples
    assert assessed-to-unassessed, retired-to-live-unassessed and assessed-routeless-to-unassigned
    states refuse as new findings; a genuinely different second base holding the debt allows
    carried incomplete reporting. ID presence alone does not establish carried debt;
  - all four admission rules register: new-record and record-kept refuse; existing-record carries
    `merge_reports` and `writer_reports`, legacy-count carries `migration_debt`. Neither flag is
    a permanent reporting exemption from publication/landing.

### Overview order

The five negative/combined overview cases now supply genuine fixture comparison bases as well as `leaf_publication=True` to `_validate`, retaining the offending-heading/line and exact R80-rule assertions; its default remains unchanged for the other rule families. The overview cases retain positive controls for the conforming fixture, a non-root route without a governing section, and fenced heading examples. Despite its name, `test_root_overview_needs_no_governing_section` calls `_route_overview`, which rewrites `ROUTE_CARD = onboarding/mcp/src/agents_remember/worktrees/overview.md`; its assertion is an empty R80 finding list for that nested fixture, not a repository-root boundary control. [16] Negatives require the actual offending heading or line for buried/paraphrased purpose, leaf/date sections and scattered markers. The combined fixture checks all three R80 rule IDs and calls `require_valid_commit(..., leaf_publication=True)`, requiring a named refusal. A standalone conversion retains its legacy prose without R80 findings; ordinary registration requires all three rules to be refusing and not writer-reported. The separate order module extends the ATX and trailing-region counterexamples.

### Conventions

- The rule-9 test refuses registration of `TEST.report`, registers `TEST.refuse`, checks duplicate
  registration and named refusal, then cleans both possible IDs from `registry._REGISTRY` in `finally`.

### Invariants And Boundaries

- Packet examples remain unit-level assertions across this module and the separated `test_validator_link_targets.py`; their moved definitions are not still defined here.

### Todos

None recorded.

The moved carried-gone/reanchored controls additionally expect the separate `R22.6-link-target-path` refusal; four of the six relocated function ASTs are unchanged. The boundary-merge function itself is unchanged and its evidence below now binds the actual new file. The split does not delete its assertion or claim those definitions still reside here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

Representative cases; the full list is in the module.

- Merge duplicates are conflicts naming both files; parallel mints merge cleanly. [2]

- The hand-added marker is refused. [3]


- A dot-named card and its sidecar are validated. [4]

- The retired record the history fixtures keep in every tree (records are never deleted, MIK-R22 rule 3; L09 R2-1). [6]
- A closed history file is frozen. [7]

- MIK-R27: reference-only justifications are refused, real prose is admitted. [8]


- MIK-R27: a forged legacy ID does not make a record exported. [11]


### Cross-Repo References

No meaningful cross-repo references found: the cases run over in-memory trees.

No cross-repo boundary is crossed by this file.


- A based fixture passes with carried incomplete legacy debt; merge_reports/migration_debt sets and absence of plain report-only rules are pinned. [1]


- MIK-R27: test_an_existing_record_whose_test_was_deleted_refuses_off_merge distinguishes leaf refusal from sync reporting. [9]


- MIK-R27: test_exported_retired_and_merged_records_refuse_off_merge retains retired exemption and sync reporting, not an export waiver. [10]


- MIK-R27: actual base-held legacy debt, new-finding counterexamples and merge_reports/migration_debt/writer flags. [12]


- test_a_later_packets_rule_runs_everywhere_and_plain_report_only_is_refused rejects plain report-only registration and exercises a later refusing rule. [13]


- Five negative/combined R80 assertions use genuine comparison bases and explicit leaf publication, retaining exact offending-heading/rule checks and the shared default. [14]


- Current source delta inspected statically: Repair baseline/admission/reporting and registry/R80 witnesses; preserve genuine new-admission bases, finding-based debt and retirement. [15]

- The root-named positive control actually edits the nested worktrees overview via _route_overview/ROUTE_CARD and asserts no R80 findings there; it is not a repository-root control. [16]

- The boundary merge keeps the same three-stale-report assertion in its relocated definition. [5]
