# mcp/src/agents_remember/models/knowledge_files/census.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The schemas, the claim and status rules, and the governing-status rule.

- The four schema names, the file names and the root slug. [1]
- The eight dispositions and the five route statuses. [2]
- The readable, injective route slug; `.` is `@root`. [3]
- The pinned baseline and the mechanical, sorted inventory. [4]
- Provenance names exactly one of leaf or wave. [5]
- Admitting dispositions link to records of their kind; only `demoted` may also link. [6]
- A claim: the latest assessment governs its cell; `discarded_false` needs `concern_found`. [7]
- A route's status history is non-empty and in time order. [8]
- The schema-to-model map registered in `SCHEMA_MODELS`. [9]
- The latest status entry across every census governs; none is `pending`. [10]
- The models refuse inconsistent claims and statuses. [11]
- Slugs are readable and injective. [12]
- The governing status spans censuses, with the tie-break. [13]

### Cross-Repo References

No meaningful cross-repo references found: the models describe files of the memory repository and name code commits only by ID.

No cross-repo boundary is crossed by this file.
