# mcp/src/agents_remember/memory_quality/knowledge_census/checks.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_census/checks.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The census integrity checks the validator registers (MIK-R20 rule 1, MIK-R22 rule 9).**
`check_censuses(candidate, bases=, record_ids=)` reads the candidate's censuses and, where it compares,
the comparison bases (K_B at a commit route, every parent at a merge), and returns sorted
`CensusFinding`s under nine refusing rules (`CENSUS_RULES`). The census writer runs the same function
before it writes, so the writer and every commit route refuse the same things.

## Code Commentary

### Logic

- `R20.1-census-shape` / `R20.1-census-canonical`: the reader's problems.
- `R20.1-census-pinned`: `_is_pinned_path` pins exactly `knowledge/census/<id>/baseline.json` and
  `…/inventory.json`, nothing deeper (review R1 finding 1: a suffix match had falsely pinned claims and
  status files of routes whose slug ends in `baseline` or `inventory`). A pinned file present in a base
  may never change or be deleted: a new baseline is a new census.
- `R20.2-claim-rows`: a claim's location names an inventoried onboarding artifact governed by the route
  whose file holds the claim, and a claim ID is defined once per census.
- `R20.2-claim-stable`: once in a base, a claim's `STABLE_CLAIM_FIELDS` (`id`, `text`, `location`, `kind`,
  `applicability`) never change (review R1 finding 2, architect ruling); `disposition` and `records` may be
  set, and assessments appended. A changed `id` surfaces as the recorded claim being removed.
- `R20.2-claim-records`: every record an admitted or demoted claim links to exists (`record_ids_in`
  reads record IDs from record filenames, so an unparseable record still resolves).
- `R20.3-route-known`: a claims or status file's route governs at least one inventory row.
- `R20.3-status-append-only` and `R20.6-assessment-append-only`: with one base, the base's list is a
  prefix of the candidate's; at a merge, each parent's list is a subsequence (`_preserved`). A recorded
  claim or status file is never removed.

### Conventions

- Findings carry `rule`, `path`, `field` and `message`; they are de-duplicated and sorted.
- The checks judge no meaning: whether an assessment is right is the curator's.

### Invariants And Boundaries

- A recorded claim assessment is never edited: a correction appends a new assessment (rule 6).
- The census baseline and inventory never change once committed.
- A recorded claim's text, location, kind and applicability never change, so the cohort `N` cannot shrink silently.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The rule table, the pinning, the claim and route checks and the append-only comparison.

| Finding | Anchor | Source |
| --- | --- | --- |
| The nine census rules and their owners. | `CENSUS_RULES` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:52-65 |
| The fields of a recorded claim that never change. | `STABLE_CLAIM_FIELDS` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:71-71 |
| Prefix at one base, subsequence at a merge. | `_preserved` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:103-106 |
| Exactly the two pinned paths, and their change or deletion refused. | `_is_pinned_path`; `_pinned_findings` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:115-124; mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:127-140 |
| Claims name inventoried artifacts of their route; IDs are unique; linked records exist. | `_claim_findings`; `_claim_row_findings` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:143-175; mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:178-196 |
| Stable claim fields and append-only assessments. | `_claim_append_findings` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:221-255 |
| Append-only route status histories. | `_status_append_findings` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:258-270 |
| The entry point. | `check_censuses` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:286-312 |
| A recorded assessment is never edited; a correction appends. | `test_a_recorded_assessment_is_never_edited_and_a_correction_appends` | mcp/tests/test_knowledge_census_files.py:315-338 |
| Status histories are append-only; merges keep both parents. | `test_route_statuses_are_append_only_and_merges_keep_both_parents` | mcp/tests/test_knowledge_census_files.py:341-364 |
| Routes whose slug ends like a pinned file still append. | `test_routes_whose_slug_ends_like_a_pinned_file_still_append` | mcp/tests/test_knowledge_census_files.py:476-499 |
| A recorded claim's identity and cohort fields are stable. | `test_a_recorded_claims_identity_and_cohort_fields_are_stable` | mcp/tests/test_knowledge_census_files.py:502-532 |

## Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
