# mcp/src/agents_remember/models/knowledge_files/census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The migration census as files: the four `ar-census-*/v1` schemas (MIK-R20 rule 1).** A census lives in
`knowledge/census/<census-id>/`: `baseline.json` (the pinned code and memory commits and the code scope),
`inventory.json` (one row per in-scope source file and per onboarding artifact, each with its governing
onboarding route), `claims/<route-slug>.json` (the legacy claims agents extracted in that route, with
their assessments and migration disposition) and `routes/<route-slug>.json` (that route's status
history). The module also holds `route_slug`, `mint_claim_id` and `governing_status`, the "latest entry
across every census" rule, at the `models` rank so every layer (including MIK-R10's coverage lookup) can
apply it. `documents.py` registers `CENSUS_MODELS` in `SCHEMA_MODELS`.

## Code Commentary

### Logic

- **Baseline and inventory.** `CensusBaseline{census, code{commit}, memory{commit}, scope}` names exact
  Git object IDs; an empty `scope` means the whole code tree. `CensusInventory{census, sources[], artifacts[]}`
  holds `InventoryRow{path, route?}` rows that must be sorted and unique, and every artifact must lie
  under `onboarding/`; `routes` is every route that governs at least one row.
- **Claims (rule 2).** `CensusClaim{id, text, location{artifact, lines?}, kind, applicability, assessments[], disposition, records?}`.
  `id` is `CLM-` plus six Crockford characters (`mint_claim_id`). Each `Assessment` has a `verdict`,
  at least one MIK-R21 `Reference` as evidence, a `Provenance{leaf|wave, session, at}` and an optional
  note. The latest assessment's verdict governs: `cell` is `T`/`F`/`U` for
  `no_concern_found`/`concern_found`/`unresolved`, and `P` with no assessment; `in_cohort` is
  `applicability == "assessable"`.
- **Dispositions.** All eight values of the packet. `_require_disposition_records`: the four admitting
  dispositions must link to records of their kind (`admitted_as_other_record` takes any kind except
  INV, FAM and DEC); only `demoted` may also link; the rest link to nothing. `discarded_false` requires
  the latest verdict to be `concern_found`.
- **Route status (rule 3).** `StatusEntry{status, reason, tree, provenance}` over the five statuses;
  `CensusRoute.statuses` has at least one entry, in time order.
- **Route slugs.** `route_slug`: `/` becomes `+`, every other character outside `[A-Za-z0-9._-]` (and a
  leading `.`) is percent-encoded, and the root route `.` is `@root`. The encoding is injective.
- **Governing status.** `governing_status(route, histories)` returns the entry with the latest
  `provenance.at` across every census; a tie goes to the larger census ID, then to the later list
  position. A route with no entry is `pending` (`DEFAULT_ROUTE_STATUS`).

### Conventions

- Timestamps are ISO 8601 and must carry a UTC offset (`_require_timestamp`, `time_of`).
- The claim-kind and applicability vocabularies are the retired database census's
  (`models/knowledge/census.py`), kept closed so comparisons stay stable.
- Claim IDs are not in `ids.py`; they are unique within a census, not repository-wide.

### Invariants And Boundaries

- The models check shape only. Append-only (rules 3 and 6), pinning and the stable claim fields are
  enforced by the validator's census rules against the comparison bases
  (`memory_quality/knowledge_census/checks.py`).
- `N = T + F + U + P` holds by construction: every in-cohort claim is exactly one cell.
- The legacy database census (`models/knowledge/census.py` and the `memory/migration/` census modules)
  is untouched and stays until MIK-R26 (leaf L26) retires it, by architect ruling.

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

The schemas, the claim and status rules, and the governing-status rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| The four schema names, the file names and the root slug. | `CENSUS_BASELINE_SCHEMA`; `ROOT_ROUTE_SLUG` | mcp/src/agents_remember/models/knowledge_files/census.py:69-79 |
| The eight dispositions and the five route statuses. | `Disposition`; `ROUTE_STATUSES` | mcp/src/agents_remember/models/knowledge_files/census.py:101-129 |
| The readable, injective route slug; `.` is `@root`. | `route_slug` | mcp/src/agents_remember/models/knowledge_files/census.py:182-196 |
| The pinned baseline and the mechanical, sorted inventory. | `CensusBaseline`; `CensusInventory` | mcp/src/agents_remember/models/knowledge_files/census.py:216-233; mcp/src/agents_remember/models/knowledge_files/census.py:249-280 |
| Provenance names exactly one of leaf or wave. | `Provenance` | mcp/src/agents_remember/models/knowledge_files/census.py:288-300 |
| Admitting dispositions link to records of their kind; only `demoted` may also link. | `_require_disposition_records` | mcp/src/agents_remember/models/knowledge_files/census.py:330-344 |
| A claim: the latest assessment governs its cell; `discarded_false` needs `concern_found`. | `CensusClaim` | mcp/src/agents_remember/models/knowledge_files/census.py:347-381 |
| A route's status history is non-empty and in time order. | `CensusRoute` | mcp/src/agents_remember/models/knowledge_files/census.py:412-425 |
| The schema-to-model map registered in `SCHEMA_MODELS`. | `CENSUS_MODELS`; `CensusDocument` | mcp/src/agents_remember/models/knowledge_files/census.py:428-434 |
| The latest status entry across every census governs; none is `pending`. | `governing_status` | mcp/src/agents_remember/models/knowledge_files/census.py:447-464 |
| The models refuse inconsistent claims and statuses. | `test_claim_and_status_models_refuse_inconsistent_records` | mcp/tests/test_knowledge_census_files.py:118-156 |
| Slugs are readable and injective. | `test_route_slugs_are_readable_and_injective` | mcp/tests/test_knowledge_census_files.py:109-115 |
| The governing status spans censuses, with the tie-break. | `test_the_governing_status_is_the_latest_entry_across_every_census` | mcp/tests/test_knowledge_census_report.py:127-167 |

## Cross-Repo References

No meaningful cross-repo references found: the models describe files of the memory repository and name code commits only by ID.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
