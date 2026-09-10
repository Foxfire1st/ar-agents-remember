# mcp/tests/test_memory_quality.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_memory_quality.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-09T18:57+02:00 |
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532` |
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Memory-census metadata authority, historical-row and moved-card handling, and entity-catalog alignment tests.

## Code Commentary

### Logic

The first four tests exercise the census repair boundary: a valid current sidecar mapping is accepted despite absent or stale historical metadata, a repaired current mapping is not vetoed by an old association, a removed historical sidecar remains an absent census row without a removal blocker, and a move retains both the old absent row and the new present row. The two retained tests reject a fingerprint without an inventory entity and accept exactly one fingerprint per inventory member. Alignment remains first in the before-metadata-refresh check ordering. Helpers write exact onboarding/entity fixtures and initialize clean memory repositories.

### Conventions

The retained entity assertions were present at IAS `d3610903`; the current candidate carries four census regression cases covering current metadata, historical rows, and moved old/new cards. Historical entries below record earlier test populations and do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Current census cases distinguish current candidate metadata from historical metadata: current missing or conflicting mappings remain blockers, while historical-only associations provide removal context, remain enumerable as absent rows, and do not veto a valid current mapping or require an extra removal declaration. The ordering assertion establishes check registration, not a prohibition on authorized pre-gate memory preparation.

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
| Current repaired metadata and historical removal behavior are covered by the census regression helper. | `test_census_accepts_repaired_current_onboarding_metadata` | mcp/tests/test_memory_quality.py:94-196 |
| A repaired current mapping is accepted even when the historical card named an old source. | `test_census_repaired_old_association_does_not_veto_current_mapping` | mcp/tests/test_memory_quality.py:198-221 |
| A removed historical card remains an absent row without a removal blocker. | `test_census_retains_historical_removal_row_without_mapping_validation` | mcp/tests/test_memory_quality.py:223-251 |
| A moved card retains old and new census rows with absent and present final states. | `test_census_move_retains_old_and_new_rows` | mcp/tests/test_memory_quality.py:253-280 |
| Entity catalog alignment rejects orphaned fingerprint before code rails. | `test_entity_catalog_alignment_rejects_orphaned_fingerprint_before_code_rails` | mcp/tests/test_memory_quality.py:282-300 |
| Entity catalog alignment accepts one fingerprint per inventory entry. | `test_entity_catalog_alignment_accepts_one_fingerprint_per_inventory_entry` | mcp/tests/test_memory_quality.py:302-312 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-09T23:45:19+02:00 — CCR-L42 census regression reconciliation: documented the four current-versus-historical census cases, including absent historical rows without an extra removal declaration and moved old/new row preservation, and refreshed all current test ranges. Verification metadata remains unchanged until closeout.

- 2026-09-09T18:57:35+02:00 — CCR-L42 census repair: documented the three current-versus-historical metadata regression cases and the two retained entity-catalog tests, and refreshed current source citations. Verification metadata remains unchanged until closeout.

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
