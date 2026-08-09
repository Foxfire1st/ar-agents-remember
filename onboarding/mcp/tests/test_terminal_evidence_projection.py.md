# mcp/tests/test_terminal_evidence_projection.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                  |
| path                   | `mcp/tests/test_terminal_evidence_projection.py`                 |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-08-09T01:21+02:00                                            |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`                                    |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview      | `overview.md`                                                    |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

The forcing regression suite for the 260713-TES-L2 projection lift: per-vendor terminal
evidence mapping, pi native paging, catalog seat-truth persistence, interrupt-origin
attribution, and the no-loss cursor contract. Written red before implementation (S1).

## Code Commentary

### Logic

`LatestTerminalEvidenceTests` cit:([`LatestTerminalEvidenceTests`], mcp/tests/test_terminal_evidence_projection.py:180-283) pins codex completed/interrupted frames, pi aborted
frames, newest-outcome-wins across frames, empty-page no-evidence, unknown harness/projector
no-evidence, and unmappable-native skip. `ReadEntryTerminalEvidenceTests` cit:([`ReadEntryTerminalEvidenceTests`], mcp/tests/test_terminal_evidence_projection.py:285-471) covers
non-harness/endpointless rows, codex evidence-page reads, and the pi tail walk: beyond-one-page
lift (251 entries, terminal at `entry-240`), forward tracking from a persisted cursor, empty
page no-advance, and the 8-page bound.

`CatalogSeatTruthTests` cit:([`CatalogSeatTruthTests`], mcp/tests/test_terminal_evidence_projection.py:474-618) pins the vocabulary: completed settles then claims
`turn-ended` (never "done"), interrupted is `turn-ended` immediately and never `completed`,
developer-stamp origin attribution (including the other-turn case), killed stays `exited`,
hung stays `stale` and holds the boundary, transient read failure retries the same window
(F2), and the boundary vocabulary. `OriginResolutionTests` cit:([`OriginResolutionTests`], mcp/tests/test_terminal_evidence_projection.py:620-642) pins
`interrupted_origin` directly. `SeatTurnTruthTests` cit:([`SeatTurnTruthTests`], mcp/tests/test_terminal_evidence_projection.py:644-746) covers the write helpers:
missing-row no-op, same-state no-op write, idempotent signal/interrupt stamps, and cursor
advance/idempotence. `SnapshotParityTests` (L748+) verifies the new `terminal` parameter keeps
the snapshot signature backward compatible.

### Conventions

Fake host/reader seams keep the suite sleepless and deterministic; the suite drives
`observe_terminal_liveness`/`record_*` helpers through the same seams production uses.

### Invariants And Boundaries

- Done ≠ interrupted at seat granularity; killed stays exited; hung stays stale.
- Cursors advance only on a successful read; a failed read is retried from the same window.
- The pi lift walks to the tail beyond the first 200 entries, bounded at 8 pages.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines these projections; the relay contract and tests are the authority. | `CatalogSeatTruthTests` | mcp/tests/test_terminal_evidence_projection.py:474-618 |

## Repo-Internal References

The suite exercises `serving/terminal_evidence.py`, `serving/terminal_liveness.py`,
`serving/seat_turn_truth.py`, and `serving/terminal_catalog.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lift module under test. | `read_entry_terminal_evidence`; `_read_pi_terminal_evidence` | mcp/src/agents_remember/serving/terminal_evidence.py:148-164; mcp/src/agents_remember/serving/terminal_evidence.py:166-194 |
| The liveness ordering (read terminal evidence before persisting the advanced snapshot). | `_observe_alive` | mcp/src/agents_remember/serving/terminal_liveness.py:343-426 |
| The catalog row fields and boundary predicate the suite pins. | `seat_at_turn_boundary`; "class TerminalCatalogEntry:" | mcp/src/agents_remember/serving/terminal_catalog.py:95-103; mcp/src/agents_remember/serving/terminal_catalog.py:106-220 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## Update History

- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new forcing
  suite (projection lift, pi paging, origin, seat truth, cursor no-loss). Verification
  metadata left blank: the source is uncommitted; closeout stamps the 260713-TES-L2 commit.
