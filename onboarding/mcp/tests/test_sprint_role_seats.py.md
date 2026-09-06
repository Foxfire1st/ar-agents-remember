# mcp/tests/test_sprint_role_seats.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_sprint_role_seats.py`             |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`        |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks structural seat lookup stays within the exact sprint/repository and role altitude. Duplicate current occupants refuse, altitude mismatch refuses before occupant lookup, and reviewer parentage is exact at each review seam. These tests do not authorize agents to choose or impersonate another role.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same role on different sprints never crosses repository scope | `test_same_role_on_different_sprints_never_crosses_repository_scope` | mcp/tests/test_sprint_role_seats.py:141-160 |
| Duplicate current occupants fail closed | `test_duplicate_current_occupants_fail_closed` | mcp/tests/test_sprint_role_seats.py:162-167 |
| Role altitude mismatch fails before any occupant lookup | `test_role_altitude_mismatch_fails_before_any_occupant_lookup` | mcp/tests/test_sprint_role_seats.py:169-171 |
| Reviewer parent is exact for each review seam | `test_reviewer_parent_is_exact_for_each_review_seam` | mcp/tests/test_sprint_role_seats.py:173-190 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: expanded sprint-seat and
  child-authorization forcing to the four reviewer contexts and pinned the fail-closed higher-level
  unstamped boundary. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_sprint_role_seats.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: created the one-to-one onboarding card for concurrent-
  sprint binding, refusal, write-once, custody, and rebind regressions. Verification metadata will
  be stamped by closeout after the source commit exists.
