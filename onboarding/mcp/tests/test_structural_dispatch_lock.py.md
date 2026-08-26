# mcp/tests/test_structural_dispatch_lock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_structural_dispatch_lock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T16:03+02:00 |
| lastVerifiedCommitHash |  `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate |  2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces the cross-process exclusion, in-process waiter reclamation, and fixed filesystem bound of
the canonical-seat dispatch serializer.

## Code Commentary

### Logic

The suite holds a real `flock` in a forked process and proves a second nonblocking acquisition
fails. It separately forces two in-process users through one slot and verifies the live lock map is
empty after both drain. Lock-path creation failure is translated to the typed structural lock family, duplicate pinned briefs
refuse instead of selecting a row, and historical seat churn runs through a reduced stripe count to
prove created lock files are zero-length and bounded by that fixed namespace.

### Conventions

Synchronization uses events and kernel locks at explicit boundaries; no timing-only race assertion
or process-local fallback stands in for the production serializer.

### Invariants And Boundaries

- Cross-process exclusion is proven with the operating system's real file lock.
- Process-local lock entries exist only while a holder or waiter is live.
- Historical seat identity cannot create an unbounded lock-file namespace.
- Stripe files are zero-length and remain reusable rather than being unlinked while live.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the production serializer and kernel-forcing test are
the relevant evidence.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A forked process holds the production lock while a second real `flock` is refused. | `test_structural_dispatch_lock_excludes_a_second_process` | mcp/tests/test_structural_dispatch_lock.py:23-48 |
| The process-local keyed lock is reclaimed only after the last waiter drains. | `test_process_lock_map_reclaims_after_the_last_waiter_drains` | mcp/tests/test_structural_dispatch_lock.py:51-85 |
| Lock-path setup failure returns the typed lock family. | `test_lock_path_failure_is_a_typed_structural_refusal` | mcp/tests/test_structural_dispatch_lock.py:90-104 |
| Duplicate pinned briefs refuse without selection. | `test_duplicate_pinned_briefs_refuse_instead_of_selecting_one` | mcp/tests/test_structural_dispatch_lock.py:107-127 |
| Historical churn stays inside the fixed stripe namespace with zero-length artifacts. | `test_historical_seat_churn_stays_inside_the_fixed_stripe_namespace` | mcp/tests/test_structural_dispatch_lock.py:130-149 |

## Cross-Repo References

No cross-repository dependency governs this test module.

## Update History

- 2026-08-26T16:03+02:00 — Post-failure repair: added deterministic lock-path setup refusal and
  duplicate pinned-brief ambiguity coverage beside the fixed 4,096-stripe proof. No certifying test
  execution is claimed.


- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: created for bounded, real-lock serializer proof.
  Verification remains closeout-owned.
