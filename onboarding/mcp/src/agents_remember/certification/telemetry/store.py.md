# mcp/src/agents_remember/certification/telemetry/store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/telemetry/store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

The append / content-addressed owner for durable CCR-R16@v3 telemetry journal entries.
Closeout-generation and diagnostic-run envelopes live in separate store roots. Each append is a
CAS publication: the entry at an exact (envelope, execution, revision) address must byte-match
the previously stored entry, every read revalidates the revision chain and each entry digest, and
replay is strictly read-only instrumentation that can never alter authority.

## Code Commentary

### Logic

`TelemetryStorePolicy` (`store.py:41-49`) carries the operation-scoped capacity (max events per
execution, max bytes) and the existing owner that reclaims the store. `TelemetryJournalEntry`
(`store.py:50-64`) binds one event to its own digest and the digest of its exact predecessor
(empty for revision one), and validates that its `eventDigest` matches the event content.
`TelemetryReplay` (`store.py:67-79`) is instrumentation-only and cannot alter authority.
`DurableTelemetryStore` (`store.py:81-316`) is the root- and policy-bound owner:
`append` (`store.py:88-127`) computes the expected next revision from the existing chain,
refuses a mismatched revision, CAS-publishes the canonical bytes under the
`telemetry-event-cas-collision` rule, enforces the byte budget
(`_require_capacity` at `store.py:225-251`), writes atomically, and verifies the read-back bytes;
`read` (`store.py:129-143`) revalidates the complete revision chain and every entry digest
(`_read_entries` at `store.py:183-224`); and `replay` (`store.py:145-156`) returns the read-only
`TelemetryReplay`. Envelope roots (`_envelope_root` at `store.py:158-159`) split
closeout-generation from diagnostic-run journals, and `_entry_path` (`store.py:161-182`) rejects
unsupported kinds and non-positive revisions.

### Conventions

The store is append-only and content-addressed; entries are canonical JSON bytes derived from the
frozen models (`_canonical_bytes` at `store.py:263-269`), and reads are the only authority for the
chain.

### Invariants And Boundaries

- Each append is a CAS publication: identical bytes at an existing revision return the existing
  path; different bytes at the same revision are refused as a collision.
- Every read revalidates the revision chain (no gaps, no broken predecessor digests) and every
  entry digest; tampered or non-canonical entries are refused.
- Closeout-generation and diagnostic-run envelopes never share a store root.
- Replay is read-only instrumentation and can never alter authority.
- Capacity is bounded by the operation-scoped policy (max events and max bytes per execution).

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose normative requirement makes the durable
journal the reconstruction authority for cost, order, and recovery. Task artifact paths are not
repo-relative citations, so this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One journal entry binds an event to its digest and its exact predecessor digest. | `TelemetryJournalEntry` | mcp/src/agents_remember/certification/telemetry/store.py:50-64 |
| Append CAS-publishes the next revision and verifies the read-back bytes. | `DurableTelemetryStore.append` | mcp/src/agents_remember/certification/telemetry/store.py:88-127 |
| Reads revalidate the revision chain and every digest; replay stays read-only. | `DurableTelemetryStore.read`; `DurableTelemetryStore.replay`; `TelemetryReplay` | mcp/src/agents_remember/certification/telemetry/store.py:129-156; mcp/src/agents_remember/certification/telemetry/store.py:67-79 |
| Envelope roots and entry paths keep closeout and diagnostic journals apart and reject bad addresses. | `_envelope_root`; `_entry_path` | mcp/src/agents_remember/certification/telemetry/store.py:158-182 |
| Capacity and collision rules are policy- and byte-bounded, never inferred. | `_require_capacity`; `_canonical_bytes` | mcp/src/agents_remember/certification/telemetry/store.py:225-251; mcp/src/agents_remember/certification/telemetry/store.py:263-269 |
| The event and envelope vocabulary comes from the models layer. | `TelemetryEvent`; `TelemetryExecutionKind` | mcp/src/agents_remember/certification/telemetry/models.py:673-851; mcp/src/agents_remember/certification/telemetry/models.py:39-39 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 durable telemetry
  journal store (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
