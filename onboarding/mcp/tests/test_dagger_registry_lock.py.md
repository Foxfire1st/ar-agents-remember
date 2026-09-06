# mcp/tests/test_dagger_registry_lock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dagger_registry_lock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Host Dagger registry locking composed with checkout coordinator isolation.

## Code Commentary

### Logic

An undeclared linked-checkout caller admits and releases an exact host owner while live coordination writes still refuse before parent creation. Nested exception paths retain exclusion until the outer release; independent threads and processes verify the physical lock remains held and is later released.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Host registry permission does not grant coordinator permission or declare a process identity. Tests use temporary authority roots and an inspector double, not a new Dagger engine.

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
| Host admission keeps undeclared checkout coordinator writes refused. | `test_host_admission_keeps_undeclared_checkout_coordinator_writes_refused` | mcp/tests/test_dagger_registry_lock.py:89-114 |
| Registry nested exception retains then releases thread and process exclusion. | `test_registry_nested_exception_retains_then_releases_thread_and_process_exclusion` | mcp/tests/test_dagger_registry_lock.py:147-164 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:28+02:00 — Created the four-case registry composition regression card against the prepared L30 code; distinguished real process/thread exclusion from the engine-inspection double.
