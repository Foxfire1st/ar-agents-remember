# mcp/tests/test_causal_failure_localization.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_causal_failure_localization.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Exact-node causal blocking and reproducible runtime-failure records.

## Code Commentary

### Logic

A temporary package has one dependent test and one independent same-file test. Forcing the owner preflight failure names only the exact dependent node and keeps the artifact non-accepting. Runtime classification distinguishes socket, timeout and OS failures and records worker, seed, duration and process topology.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Suppression is exact-node rather than whole-file. Unclassified failures require classification before retry; this reduced suite does not separately prove every historical process-family case.

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
| Failed owner blocks only source proved exact nodes. | `test_failed_owner_blocks_only_source_proved_exact_nodes` | mcp/tests/test_causal_failure_localization.py:54-67 |
| Observed runtime failures retain exact retry inputs. | `test_observed_runtime_failures_retain_exact_retry_inputs` | mcp/tests/test_causal_failure_localization.py:69-99 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-28T14:18+02:00 — Reconciled causal-localization test symbols and ranges against the
  committed PDLS candidate; the documented proof behavior is unchanged.

- 2026-08-28T11:32+02:00 — Added direct imported-owner-class attribute-call forcing to the causal
  dependency proof.

- 2026-08-28T10:03:40+02:00 — Expanded the source-derived cascade to three dependent contracts and
  added forcing for every distinct runtime family plus process-topology retention.
- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for source-derived
  exact-node causality, safe independent continuation, and reproducible failure evidence.
