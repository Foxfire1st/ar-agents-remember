# mcp/tests/test_atomic_series_landing_l3.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_landing_l3.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash |  `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate |  2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Atomic landing exclusion at the declared-parent boundary.

## Code Commentary

### Logic

A leaf with its exact declared atomic parent may land at the same target. Removing that parent relationship leaves a live unrelated same-target contract and requires AtomicLandingBlocked with live-nonterminal state.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The fixture uses contract/ref authority; absence of a relationship cannot be treated as permission to share the target.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact declared parent same target permits leaf landing. | `test_exact_declared_parent_same_target_permits_leaf_landing` | mcp/tests/test_atomic_series_landing_l3.py:25-26 |
| Live nonterminal unrelated same target contract blocks landing. | `test_live_nonterminal_unrelated_same_target_contract_blocks_landing` | mcp/tests/test_atomic_series_landing_l3.py:28-36 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
