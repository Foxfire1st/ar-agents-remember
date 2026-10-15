# mcp/tests/test_knowledge_decisions.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R13@v2 cases (historical collection: 9): decision records with rejected alternatives.** The content rules run in the
knowledge validator over a small converted tree built in the file (`_tree`: the layout marker, one assumption
record `ASM-100K0R` and the given decisions); the derived reads are checked on the models; requirement endpoints are
resolved by the requirement owner against a real task directory under `tmp_path`. The writer's round trip is in
`test_knowledge_writer.py`. The file uses no shared support module or catalog fixture, so it needed no catalog
change; it runs in the `unit-regression` lane (`test-evidence-lanes.toml`).

## Code Commentary

### Logic

- **Fixtures.** `_d12` and `_d18` are the packet's two conforming examples as `ar-decision/v1` documents: D12 (chosen
  "several local routes", rejected "one owning route", reconsider when families rarely span subtrees), D18 (chosen
  "text files in Git", rejected "canonical SQLite", deferred "both, kept in sync", with `reconsider_on` links to the
  assumption for alternatives 1 and 2). `_variant` deep-copies and overrides fields; `_found` lists the `R13` findings
  as `(ID prefix, field, rule, report_only)`.
- **Cases:**
  - both packet examples pass every rule;
  - one alternative, none chosen, and two chosen are each refused by `R13.1-alternatives`; the message
    map filters `report.refusals` to `R13.1`, isolating that owning rule when other refusals coexist;
  - a rejected and a deferred alternative without `reconsider_when` are refused by `R13.1-reconsider-when`; a blank
    value is refused by the shape rule instead;
  - a stored `superseded` (status and an alternative's) is refused by `R13.2-superseded-derived`, naming both
    fields, alongside `R22.1-shape`;
  - `reconsider_on` at the chosen alternative and out of range are refused by `R13.3-reconsider-on`;
  - `test_a_decision_that_governs_nothing_is_refused` asserts that a decision whose only link is
    `reconsider_on` refuses under `R13.3-governs`: `report.ok` is false and the finding's
    `report_only` value is false;
  - `superseded_by`/`derived_status` derive `superseded` for the old D12, `reconsider_links` carries the subjects
    `reconsider:DEC-D18TXT#1` and `#2`, and `governs_links` returns D12's two governs links;
  - the resolver: resolved (with `task_root` and `key`), version mismatch, missing packet, a `..` repository
    (outside `tasks/`), and no root; the validator gives the same result whether the endpoint resolves or not;
  - **review F6:** a decision whose `legacyId` derives its own ID, marked `legacy-unassessed`, expects
    both `R27.2-new-record` and `R27.4-legacy-unassessed` refusals on `admission`: a decision is never
    an export, and a forged legacy marker waives neither obligation.

### Conventions

- Assertion scope is case-specific. `_found(report)` filters to the requested rule prefix
  (`R13` by default); cases comparing that returned list exactly reject extra findings only
  within that prefix. The alternative-count case uses `_found(report, "R13.1")` and filters
  refusal messages to `R13.1`, so it does not reject additional other-R13 findings. The
  stored-superseded case requires membership of the two named `R13.2-superseded-derived`
  field findings and uses `any()` for `R22.1-shape`; it does not require an exact finding set. [4] [6]

### Invariants And Boundaries

- These cases are the proofs of the five candidate invariants recorded on `models/knowledge_files/decisions.py`,
  `rules_decisions.py`, `requirement_endpoint.py` and `rules_admission.py`. The F6 case was checked to fail with the
  `_exported` guard removed (worker fix round).

### Todos

None recorded.

The alternative-reordering case compares against the before tree: reconsideration links whose indices follow the exact old option text yield no `R14` finding, while a deliberately wrong index yields an `R14` finding. `_found(..., "R14")` scopes this comparison; it does not assert that every validator rule passes or run a test here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R13@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`13_decision-records-with-rejected-alternatives.json`), MIK-R21 rules 4 and 6 for the record and requirement-reference
shapes, and the coordination-root note Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`,
section 4.5); they live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The fixtures and each case.

- The packet's D12 and D18 as decision documents, and the assumption they reopen on. [1]
- A converted tree with the given decisions, validated. [2]
- Both examples pass every rule. [3]
- A rejected or deferred alternative without `reconsider_when`. [5]
- Stored superseded: membership of the status and alternatives.1.status R13.2-superseded-derived refusals, plus any R22.1-shape refusal; no exact finding-set comparison. [6]
- `reconsider_on` must name an existing rejected or deferred alternative. [7]
- Superseded is derived; reconsider links carry their subject. [9]
- Requirement endpoints resolve through the owner and never refuse. [10]
- The lane row. [12]

### Cross-Repo References

No cross-repo boundary is crossed: every case builds its trees and task directory in memory or under `tmp_path`.

No cross-repo boundary is crossed by this file.

- Alternative counts and the one chosen: refusal-message comparisons filter to R13.1 when other rules also refuse. [4]
- `test_a_decision_that_governs_nothing_is_refused` expects `report.ok == False` and `R13.3-governs` with `report_only == False`. [8]
- A decision is never an export (review F6): the forged legacy case expects both new-record and legacy-unassessed admission refusals. [11]
- Current source delta inspected statically: Fix owning-rule filtering, governs refusal and dual legacy refusals, including renamed captions; retain derived-status and endpoint boundaries. [13]

- Reordering preserves option-text identity for reconsideration links, with an independently misbound-index control; the assertions filter R14. [14]
