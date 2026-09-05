# mcp/tests/test_legacy_operation_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_legacy_operation_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Protects explicit legacy-operation inspection, migration, archive and same-generation recovery. Legacy input remains isolated from the normal typed journal reader, and migration must preserve original bytes and proof rather than silently reinterpret history.

## Code Commentary

### Logic

Cases distinguish read-only inspection from approved migration, bound public error details, and require migration dry runs to leave neither locks nor receipts. Migration replay must be exact; conflicting amendments refuse. Concurrent migration, publication interruption and archive recovery retain deterministic evidence and executable same-action guidance.

Terminal integration archive checks prove protected refs. Recovery tests retain the same generation and ensure current worker termination outranks historical recovery hints. Source/schema parser isolation is checked explicitly so removal of the bridge can eventually be measured rather than guessed.

### Conventions

Use isolated filesystem and mocked process controls to exercise historical schema cases. Historical bytes are evidence inputs, not current production schema.

### Invariants And Boundaries

- The normal reader must not silently accept legacy records.
- Inspection preserves bytes and is non-mutating even when mutation is refused.
- Migration does not bless an invalid operation key or moved live code identity.
- Fresh termination truth outranks older recovery advice; archival requires terminal evidence and stable protected refs.

### Todos

These tests exercise explicit legacy recovery. They do not prove that the new typed certification lifecycle admission/finalization APIs are called by production.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Reader isolation, non-mutating inspection and exact migration | `test_normal_reader_refuses_legacy_and_inspect_preserves_exact_bytes`; `test_migration_dry_run_is_byte_exact_and_leaves_no_lock_or_receipt`; `test_migration_replay_is_exact_and_amendment_is_refused` | mcp/tests/test_legacy_operation_bridge.py:263-452 |
| Recoverable publication and concurrent/archive evidence | `test_migration_publication_os_error_is_bounded_and_recoverable`; `test_concurrent_exact_migration_publishes_one_canonical_record`; `test_terminal_archive_preserves_bytes_and_receipt_replays_after_crash` | mcp/tests/test_legacy_operation_bridge.py:550-645 |
| Terminal authority and moved-identity refusals | `test_archive_refuses_nonterminal_or_incomplete_evidence`; `test_terminal_integrate_archive_proves_protected_refs`; `test_migration_refuses_moved_live_code_identity` | mcp/tests/test_legacy_operation_bridge.py:673-764 |
| Same-generation recovery, termination precedence and measurable parser isolation | `test_migrated_recover_resumes_same_generation`; `test_migrated_worker_termination_outranks_historical_recovery`; `test_schema_one_parser_is_isolated_and_removal_guard_is_measurable` | mcp/tests/test_legacy_operation_bridge.py:818-1124 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Rebound the legacy bridge account to the accumulated projection changes, preserving byte-exact recovery lessons and removing stale source anchors.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the legacy bridge live-worker projection update (recovery-required, not synthetic termination). Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
