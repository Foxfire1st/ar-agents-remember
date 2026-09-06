# mcp/tests/test_memory_quality.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_memory_quality.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Entity inventory/fingerprint alignment and memory fixture builders.

## Code Commentary

### Logic

The two retained tests reject a fingerprint without an inventory entity and accept exactly one fingerprint per inventory member. Alignment remains first in the before-metadata-refresh check ordering. Helpers write actual onboarding/entity fixtures and initialize clean memory repositories.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

This source does not retain the historical full runner/style/MCP payload matrix. The ordering assertion establishes check registration, not a prohibition on authorized pre-gate memory preparation.

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
| Entity catalog alignment rejects orphaned fingerprint before code rails. | `test_entity_catalog_alignment_rejects_orphaned_fingerprint_before_code_rails` | mcp/tests/test_memory_quality.py:89-107 |
| Entity catalog alignment accepts one fingerprint per inventory entry. | `test_entity_catalog_alignment_accepts_one_fingerprint_per_inventory_entry` | mcp/tests/test_memory_quality.py:109-119 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: updated quality tool calls to the explicit typed sync request while preserving the underlying quality assertions. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: added test_start_and_poll_payload_builders_wrap_the_async_envelopes, proving the memory_quality_check payload builders wrap the async start/poll envelopes (started + runId; run-not-found → rerun guidance). Verified at code commit de3a0fd9.

- 2026-08-10T12:46+02:00 — Added focused entity-catalog alignment fixtures and pinned that this
  cheap structural check is first in the pre-code closeout phase; the delta coverage arm adds
  missing-section, duplicate-row, and line-fallback cases. Verification metadata stays pinned
  until closeout stamps the repair commit.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 8 citation findings (4 rows); scoped recheck clean.

- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-06T12:28+02:00: Corrected the memory-quality payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-24T03:09+02:00: Updated after adding dedicated history-order fixer coverage while keeping `memory_quality_check` diagnostic.
- 2026-05-24T02:47+02:00: Created for memory quality checker and payload coverage.
