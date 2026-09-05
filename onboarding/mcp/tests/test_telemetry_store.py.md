# mcp/tests/test_telemetry_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_telemetry_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The durability and content-addressing verification suite for the CCR-R16@v3 durable telemetry
journal store (leaf 260831-CCR-L16). Its twenty-two unit-regression tests force
`certification/telemetry/store.py` - append/read/replay round trips on temporary directories, the
monotonic revision rule, CAS collisions, digest tamper refusal, revision-chain gap and
predecessor-chain refusal, closeout/diagnostic envelope separation, read-only replay, capacity
limits, canonical-byte verification, and hostile path/address refusals.

## Code Commentary

### Logic

Tests run against a temporary store root with a small `TelemetryStorePolicy`.
`test_append_and_read_round_trip_preserves_exact_events` (`test_telemetry_store.py:101-116`) verifies
the basic round trip; `test_append_enforces_monotonic_event_revision` and
`test_tampered_journal_entry_is_refused` (`test_telemetry_store.py:117-136`) pin revision and digest
rules; `test_separate_closeout_and_diagnostic_envelopes` (`test_telemetry_store.py:137-146`) verifies
envelope separation; `test_read_refuses_journal_gap` (`test_telemetry_store.py:147-157`) and
`test_replay_is_read_only_instrumentation` (`test_telemetry_store.py:178-189`) pin chain and replay
semantics; `test_capacity_limit_is_enforced` (`test_telemetry_store.py:212-230`) verifies byte
budget enforcement; and the CAS pair (`test_append_cas_identical_bytes_returns_existing_path` and
`test_append_cas_collision_refuses_different_bytes_at_same_revision`,
`test_telemetry_store.py:247-278`) verifies the append is an exact CAS publication.

### Conventions

The suite exercises the real filesystem store on `tmp_path`; no mocks replace atomic writes, digests,
or capacity checks.

### Invariants And Boundaries

- Every append/read/replay test asserts exact store semantics, never fallback behavior.
- Tampered, non-canonical, or broken-chain entries are refused.
- The module is registered as explicit `unit-regression` evidence.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose normative requirement makes the durable
journal the reconstruction authority. Task artifact paths are not repo-relative citations, so
this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Round trips, monotonic revisions, envelope separation, and read-only replay are pinned. | `test_append_and_read_round_trip_preserves_exact_events`; `test_separate_closeout_and_diagnostic_envelopes`; `test_replay_is_read_only_instrumentation` | mcp/tests/test_telemetry_store.py:101-146; mcp/tests/test_telemetry_store.py:178-189 |
| Tampered entries, journal gaps, non-canonical bytes, and hostile addresses are refused. | `test_tampered_journal_entry_is_refused`; `test_read_refuses_journal_gap`; `test_entry_path_rejects_unsupported_envelope_kind` | mcp/tests/test_telemetry_store.py:127-157; mcp/tests/test_telemetry_store.py:295-301 |
| CAS publication and capacity limits are enforced on the real store. | `test_append_cas_identical_bytes_returns_existing_path`; `test_append_cas_collision_refuses_different_bytes_at_same_revision`; `test_capacity_limit_is_enforced` | mcp/tests/test_telemetry_store.py:247-278; mcp/tests/test_telemetry_store.py:212-230 |
| The suite exercises the production journal store and its policy models. | `DurableTelemetryStore`; `TelemetryStorePolicy`; `TelemetryJournalEntry` | mcp/src/agents_remember/certification/telemetry/store.py:81-316; mcp/src/agents_remember/certification/telemetry/store.py:41-49; mcp/src/agents_remember/certification/telemetry/store.py:50-64 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite is repository-local and exercises production certification telemetry store behavior on a temporary root. | `test_append_and_read_round_trip_preserves_exact_events` | mcp/tests/test_telemetry_store.py:101-116 |

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 durable journal
  store suite (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
