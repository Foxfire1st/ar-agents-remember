# mcp/tests/test_knowledge_decisions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_decisions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:13:03+02:00 |
| lastVerifiedCommitHash | `3eb034a6ab0493a51da5dcd6d013aa6f27f39496`|
| lastVerifiedCommitDate | 2026-09-30T03:31:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R13@v2 cases (9 collected): decision records with rejected alternatives.** The content rules run in the
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
  - one alternative, none chosen, and two chosen are each refused by `R13.1-alternatives`, with the messages;
  - a rejected and a deferred alternative without `reconsider_when` are refused by `R13.1-reconsider-when`; a blank
    value is refused by the shape rule instead;
  - a stored `superseded` (status and an alternative's) is refused by `R13.2-superseded-derived`, naming both
    fields, alongside `R22.1-shape`;
  - `reconsider_on` at the chosen alternative and out of range are refused by `R13.3-reconsider-on`;
  - a decision whose only link is `reconsider_on` is reported by `R13.3-governs` and the tree is still `ok`;
  - `superseded_by`/`derived_status` derive `superseded` for the old D12, `reconsider_links` carries the subjects
    `reconsider:DEC-D18TXT#1` and `#2`, and `governs_links` returns D12's two governs links;
  - the resolver: resolved (with `task_root` and `key`), version mismatch, missing packet, a `..` repository
    (outside `tasks/`), and no root; the validator gives the same result whether the endpoint resolves or not;
  - **review F6:** a decision whose `legacyId` derives its own ID, marked `legacy-unassessed`, is refused by
    `R27.2-new-record`: a decision is never an export.

### Conventions

- The case names state the rule they prove; findings are compared as exact lists, so a new R13 finding fails a case.

### Invariants And Boundaries

- These cases are the proofs of the five candidate invariants recorded on `models/knowledge_files/decisions.py`,
  `rules_decisions.py`, `requirement_endpoint.py` and `rules_admission.py`. The F6 case was checked to fail with the
  `_exported` guard removed (worker fix round).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R13@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`13_decision-records-with-rejected-alternatives.json`), MIK-R21 rules 4 and 6 for the record and requirement-reference
shapes, and the coordination-root note Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`,
section 4.5); they live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The fixtures and each case.

| Finding | Anchor | Source |
| --- | --- | --- |
| The packet's D12 and D18 as decision documents, and the assumption they reopen on. | `_d12`; `_d18`; `_assumption` | mcp/tests/test_knowledge_decisions.py:52-84; mcp/tests/test_knowledge_decisions.py:87-126; mcp/tests/test_knowledge_decisions.py:129-139 |
| A converted tree with the given decisions, validated. | `_tree`; `_validate` | mcp/tests/test_knowledge_decisions.py:142-151; mcp/tests/test_knowledge_decisions.py:154-155 |
| Both examples pass every rule. | `test_the_packets_d12_and_d18_decisions_pass_every_rule` | mcp/tests/test_knowledge_decisions.py:172-177 |
| Alternative counts and the one chosen. | `test_alternative_counts_and_the_one_chosen_are_refused_by_rule` | mcp/tests/test_knowledge_decisions.py:180-197 |
| A rejected or deferred alternative without `reconsider_when`. | `test_a_rejected_or_deferred_alternative_without_reconsider_when_is_refused` | mcp/tests/test_knowledge_decisions.py:200-213 |
| A stored superseded, named by field. | `test_a_stored_superseded_status_is_refused_naming_the_field` | mcp/tests/test_knowledge_decisions.py:216-224 |
| `reconsider_on` must name an existing rejected or deferred alternative. | `test_reconsider_on_names_an_existing_rejected_or_deferred_alternative` | mcp/tests/test_knowledge_decisions.py:227-239 |
| A decision that governs nothing is reported, not refused. | `test_a_decision_that_governs_nothing_is_reported_not_refused` | mcp/tests/test_knowledge_decisions.py:242-248 |
| Superseded is derived; reconsider links carry their subject. | `test_superseded_is_derived_and_reconsider_links_carry_their_subject` | mcp/tests/test_knowledge_decisions.py:251-266 |
| Requirement endpoints resolve through the owner and never refuse. | `test_requirement_endpoints_resolve_through_the_owner_and_never_refuse` | mcp/tests/test_knowledge_decisions.py:280-311 |
| A decision is never an export (review F6). | `test_a_decision_is_never_an_export_so_a_legacy_id_exempts_it_from_nothing` | mcp/tests/test_knowledge_decisions.py:314-325 |
| The lane row. | "mcp/tests/test_knowledge_decisions.py" | mcp/tests/test-evidence-lanes.toml:121-121 |

## Cross-Repo References

No cross-repo boundary is crossed: every case builds its trees and task directory in memory or under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): created this card for the new test file MIK-R13 adds (9 cases, including the review F6 case). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
