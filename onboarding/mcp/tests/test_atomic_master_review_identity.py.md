# mcp/tests/test_atomic_master_review_identity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_master_review_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:10+02:00 |
| lastVerifiedCommitHash | `b281bcd68261866be306cc80a48241921b6dd0d2`|
| lastVerifiedCommitDate | 2026-09-16T14:24:58+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Checks the identity and compatibility properties of the CCR-R26 atomic-master route-review models
and aggregate scope. It is preparation evidence for the combined integration review, not a leaf
acceptance gate or final certification suite.

## Code Commentary

### Logic

The module preserves the baseline leaf route-review digest/currentness behavior, exercises aggregate
master identity and ordered membership, and checks that standalone/organizational review behavior is
not accidentally collapsed into the atomic-master boundary. The tests also cover the explicit
membership and normative-intent inputs used by the aggregate.

### Conventions

Assertions are source-level behavioral checks; no test result here grants review authority or changes
the route policy.

### Invariants And Boundaries

- Atomic children do not acquire independent route-review publication.
- Aggregate identity is sensitive to canonical membership/order and child intent inputs.
- Existing non-atomic route behavior remains independently represented.

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
| Baseline leaf digest/currentness compatibility. | `test_baseline_leaf_route_review_keeps_digest_and_currentness` | mcp/tests/test_atomic_master_review_identity.py:146-166 |
| Operational bookkeeping does not change aggregate identity. | "def test_atomic_master_aggregate_ignores_operational_bookkeeping(" | mcp/tests/test_atomic_master_review_identity.py:263-301 |
| Normative and membership changes alter aggregate identity. | "def test_atomic_master_aggregate_changes_for_normative_or_membership_changes(" | mcp/tests/test_atomic_master_review_identity.py:304-351 |
| Models under test. | `RouteReviewScope`; `RouteReviewChildIntent` | mcp/src/agents_remember/tasks/route_review.py:53-131 |

## Cross-Repo References

No meaningful cross-repo implementation reference is required for this preparation test card. The
coordination requirement is tracked in the task report.

## Update History

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `dffcb0278cd9714e42a9c4e162273ea9c425f4131fc606dc7bf21a191179b16e`, `16062` bytes, `458` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T20:12:08+02:00 — CCR-L24 v4 citation repair: re-read the two newly added identity tests against their exact current function definitions and retained the behavioral wording; successor-source verification remains uncommitted and no code/shared overview was changed.
- 2026-09-08T18:14:20+02:00 — CCR-L24 bounded memory-quality repair: re-read the two newly retained identity checks and corrected their current function ranges; no verification pin was fabricated.
- 2026-09-08T17:31:25+02:00 — CCR-L24 final-v2 source binding: rebased active R25/R26 citation ranges against the frozen cumulative source; verification remains closeout-owned.

- 2026-09-08T16:42+02:00 — CCR-R26 source-grounded preparation: created the card for identity and
  compatibility checks from the frozen source. Commit-owned verification metadata remains blank.
