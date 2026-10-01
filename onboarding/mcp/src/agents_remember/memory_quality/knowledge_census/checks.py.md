# mcp/src/agents_remember/memory_quality/knowledge_census/checks.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The rule table, the pinning, the claim and route checks and the append-only comparison.

- The nine census rules and their owners. [1]
- The fields of a recorded claim that never change. [2]
- Prefix at one base, subsequence at a merge. [3]
- Exactly the two pinned paths, and their change or deletion refused. [4]
- Claims name inventoried artifacts of their route; IDs are unique; linked records exist. [5]
- Stable claim fields and append-only assessments. [6]
- Append-only route status histories. [7]
- The entry point. [8]
- A recorded assessment is never edited; a correction appends. [9]
- Status histories are append-only; merges keep both parents. [10]
- Routes whose slug ends like a pinned file still append. [11]
- A recorded claim's identity and cohort fields are stable. [12]

### Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

No cross-repo boundary is crossed by this file.
