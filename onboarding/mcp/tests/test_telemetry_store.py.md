# mcp/tests/test_telemetry_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_telemetry_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks telemetry journal append/read, monotonic revisions, digest tampering, missing revisions and predecessor-chain failures. Replay is read-only instrumentation, same-revision different-byte append refuses, and byte capacity remains enforced. Eight retained functions replace the prior twenty-two-test claim without declaring instrumentation to be certification authority.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Append and read round trip preserves exact events | `test_append_and_read_round_trip_preserves_exact_events` | mcp/tests/test_telemetry_store.py:73-86 |
| Append enforces monotonic event revision | `test_append_enforces_monotonic_event_revision` | mcp/tests/test_telemetry_store.py:89-96 |
| Tampered journal entry is refused | `test_tampered_journal_entry_is_refused` | mcp/tests/test_telemetry_store.py:99-106 |
| Read refuses journal gap | `test_read_refuses_journal_gap` | mcp/tests/test_telemetry_store.py:109-117 |
| Read refuses broken predecessor chain | `test_read_refuses_broken_predecessor_chain` | mcp/tests/test_telemetry_store.py:120-137 |
| Replay is read only instrumentation | `test_replay_is_read_only_instrumentation` | mcp/tests/test_telemetry_store.py:140-149 |
| Append cas collision refuses different bytes at same revision | `test_append_cas_collision_refuses_different_bytes_at_same_revision` | mcp/tests/test_telemetry_store.py:152-168 |
| Append enforces byte capacity limit | `test_append_enforces_byte_capacity_limit` | mcp/tests/test_telemetry_store.py:171-185 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 durable journal
  store suite (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
