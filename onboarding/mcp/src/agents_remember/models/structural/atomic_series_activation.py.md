# mcp/src/agents_remember/models/structural/atomic_series_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/structural/atomic_series_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[structural models overview](overview.md)

## Purpose

This file defines the closed durable vocabulary for selecting one live atomic master per normalized
protected source pair. It keeps source identity, current selection, observation state, and malformed
snapshot archive evidence strict and separate from task documents, queue members, and operation
journals.

## Code Commentary

### Logic

`AtomicSeriesSourceRef` identifies one repository plus canonical source branch;
`AtomicSeriesSourcePair` combines code with optional external memory. `AtomicSeriesActivationRecord`
stores the pair fingerprint, selected master and canonical contract path, one of
`vacant|reconciling|active`, a monotonic revision, and selection time. The observed vocabulary adds
`unreadable` without making it a writable selection state. `AtomicSeriesActivationArchiveEvidence`
binds an archive classification (`raw-bytes|opaque-entry|absence`), optional snapshot path, digest,
size, original activation path/error, replacement master, and repair time. That vocabulary lets a
repair prove whether it copied malformed regular bytes, moved an opaque nonregular entry without
following it, or observed absence.

### Conventions

Every model is frozen and rejects extra fields. Repository/branch/path text is nonblank and bounded;
fingerprints use lowercase SHA-256. `TaskDocumentRef` is the master identity, while runtime ids and
queue positions never enter the record.

### Invariants And Boundaries

- A source pair has at most one replace-in-place activation record.
- `unreadable` is read evidence, never a state callers may publish.
- A durable vacant record retains the last selected master for audit and exact cancellation replay.
- These models contain no commit, claim, certification, integration, or lifecycle state.
- Opaque-entry evidence describes quarantine; it never claims the entry was read as trusted bytes.

### Todos

Exact model claims and citations are reconciled to the frozen source. Verification metadata remains
intentionally empty while this source is uncommitted.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The activation store derives and validates this source-pair and record vocabulary. | `atomic_series_source_pair`; `_require_record_identity` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:105-127; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:385-395 |
| Focused tests prove source-pair isolation, replacement selection, vacancy, and archive evidence. | `AtomicSeriesActivationTests` | mcp/tests/test_atomic_series_activation.py:110-362 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of source-pair, selection, and archive
  vocabulary; verification awaits the real code commit.

- 2026-08-26T06:05+02:00 — Moved this card with the model into `models/structural/`; canonical
  vocabulary and history are preserved, and the structural route now governs it. Final ranges
  remain post-Dagger-owned.

- 2026-08-26T05:40+02:00 — Reconciled archive evidence with the final regular/opaque/absence
  vocabulary and nonregular-entry quarantine. Final ranges remain post-Dagger-owned.

- 2026-08-26T02:55+02:00 — Drafted strict one-to-one onboarding for the moving IAS candidate;
  final citation ranges and verification provenance remain post-Dagger work.
