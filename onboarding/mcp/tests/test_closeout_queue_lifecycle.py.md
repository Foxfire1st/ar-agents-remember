# mcp/tests/test_closeout_queue_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T14:05+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns queue binding, closeout claim/certification, integration claim, reversible release, and exact
lifecycle-operation identity.

## Code Commentary

### Logic

The suite distinguishes narrow never-governed legacy absence from damaged bound topology, then
drives idempotent claims and certification over reachable internal/external candidate records. It
also checks commit mismatch blockers and bounded operation/event identity.

### Invariants And Boundaries

- A durable queue binding fails closed if graph, parent, leaf, or contract identity later drifts.
- Certified external candidates carry exact code, memory-content, and ledger commits.
- Lifecycle transitions compare one-way owner fingerprints rather than exposing raw operation keys.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Binding damage cannot become legacy absence. | `test_live_parent_resolution_distinguishes_legacy_absence_from_bound_damage` | mcp/tests/test_closeout_queue_lifecycle.py:204-225 |
| Closeout certification binds all exact commits. | `test_certify_closeout_is_idempotent_and_binds_exact_commits` | mcp/tests/test_closeout_queue_lifecycle.py:211-256 |
| Integration claims refuse uncertified or stale candidates. | `test_claim_integration_is_idempotent_and_refuses_uncertified_or_stale` | mcp/tests/test_closeout_queue_lifecycle.py:301-320 |

## Update History

- 2026-08-17T13:20+02:00 — No content impact: L5 repair: re-pointed stale mock targets and return tuples to match the L5 integration API (publish_queue_candidate_integration_result_under_authority, branch_commit, 4-tuple _prepare_integration_commits, durable-removal-intent idempotency). The documented test intent and coverage surface are unchanged.

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: added production-entry coverage for
  legacy absence, damaged bound topology, stale revalidation, unclaimed integration, exact
  completion ownership, and reversible closeout/integration release matrices.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  binding, claim, certification, and release assertions are identical.
- 2026-08-15T12:53+02:00 — Created for L3's focused lifecycle-transition coverage with only
  reachable durable candidate fixtures.
