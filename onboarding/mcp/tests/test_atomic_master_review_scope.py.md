# mcp/tests/test_atomic_master_review_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_master_review_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T22:11+02:00 |
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`|
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Checks the pure route-review scope resolver: atomic child deferral, master ownership, currentness,
evidence and dependency freshness, ordered membership, and exclusion of status-only bookkeeping.

## Code Commentary

### Logic

The tests construct canonical contract and candidate inputs, then exercise scope ownership errors,
master-review requirements, currentness changes, stale evidence, membership changes, and status-only
updates. The shared fixture asserts that a parent contract exists before loading the series contract,
so a parented leaf cannot silently become a standalone case. They keep the resolver's typed refusal
surface explicit so integration callers can act on the exact stale edge.

### Conventions

These tests cover pure scope composition and refusal classification. They do not run the full
integration quality gate or make any protected-ref publication.

### Invariants And Boundaries

- Atomic child review is deferred and never accepted as a local gate.
- The atomic fixture must retain a parent contract before the series contract is loaded.
- Master scope membership/order and evidence/dependency digests are currentness inputs.
- Status-only bookkeeping cannot manufacture a current review.

### Todos

Final combined master integration execution remains parent-owned.

## Docs References

No relevant external documentation was configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation source was configured for this test module. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture parent-contract invariant. | `setUp` | mcp/tests/test_atomic_master_review_scope.py:26-38 |
| Deferred atomic child and ownership behavior. | `test_atomic_child_review_is_deferred_and_leaf_integration_has_no_master_gate`; `test_missing_canonical_master_is_an_ownership_error`; `test_parented_leaf_without_parent_contract_is_not_treated_as_standalone` | mcp/tests/test_atomic_master_review_scope.py:40-64 |
| Master review requirement/currentness and stale evidence behavior. | `test_master_integration_requires_published_master_review`; `test_published_master_review_is_current_until_evidence_changes` | mcp/tests/test_atomic_master_review_scope.py:66-112 |
| Membership and status-only invariants. | `test_child_membership_change_stales_published_master_review`; `test_master_status_bookkeeping_does_not_stale_published_review`; `test_organizational_leaf_keeps_the_existing_leaf_review_boundary` | mcp/tests/test_atomic_master_review_scope.py:114-156 |
| Canonical resolver under test. | `resolve_atomic_master_scope`; `require_current_master_route_review` | mcp/src/agents_remember/worktrees/route_review_scope.py:80-260 |

## Cross-Repo References

No meaningful cross-repo implementation reference is required for this preparation test card. The
coordination requirement is tracked in the task report.

## Update History

- 2026-09-09T22:11:57+02:00 — CCR-L42 worker return: documented the `parent_contract_path` fixture assertion and refreshed the current scope-test ranges. Verification metadata remains blank and closeout-owned; no acceptance is asserted.

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `a5a45d15c079e2194b0f34e8b6183435d7c8628c8a17266c6efd94a9d8daa2bf`, `6739` bytes, `156` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T17:31:25+02:00 — CCR-L24 final-v2 source binding: rebased active R25/R26 citation ranges against the frozen cumulative source; verification remains closeout-owned.

- 2026-09-08T16:42+02:00 — CCR-R26 source-grounded preparation: created the card for pure scope
  ownership and currentness checks from the frozen source. Commit-owned verification metadata remains
  blank.
