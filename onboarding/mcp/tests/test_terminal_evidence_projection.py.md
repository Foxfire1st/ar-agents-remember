# mcp/tests/test_terminal_evidence_projection.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                  |
| path                   | `mcp/tests/test_terminal_evidence_projection.py`                 |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-08-09T01:21+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                    |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                    |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

The forcing regression suite for the 260713-TES-L2 projection lift: per-vendor terminal
evidence mapping, pi native paging, catalog seat-truth persistence, interrupt-origin
attribution, and the no-loss cursor contract. Written red before implementation (S1).

## Code Commentary

### Logic

`LatestTerminalEvidenceTests` cit:([`LatestTerminalEvidenceTests`], mcp/tests/test_terminal_evidence_projection.py:179-281) pins codex completed/interrupted frames, pi aborted
frames, newest-outcome-wins across frames, empty-page no-evidence, unknown harness/projector
no-evidence, and unmappable-native skip. `ReadEntryTerminalEvidenceTests` cit:([`ReadEntryTerminalEvidenceTests`], mcp/tests/test_terminal_evidence_projection.py:284-470) covers
non-harness/endpointless rows, codex evidence-page reads, and the pi tail walk: beyond-one-page
lift (251 entries, terminal at `entry-240`), forward tracking from a persisted cursor, empty
page no-advance, and the 8-page bound.

`CatalogSeatTruthTests` cit:([`CatalogSeatTruthTests`], mcp/tests/test_terminal_evidence_projection.py:473-616) pins the vocabulary: completed settles then claims
`turn-ended` (never "done"), interrupted is `turn-ended` immediately and never `completed`,
developer-stamp origin attribution (including the other-turn case), killed stays `exited`,
hung stays `stale` and holds the boundary, transient read failure retries the same window
(F2), and the boundary vocabulary. `OriginResolutionTests` cit:([`OriginResolutionTests`], mcp/tests/test_terminal_evidence_projection.py:619-640) pins
`interrupted_origin` directly. `SeatTurnTruthTests` cit:([`SeatTurnTruthTests`], mcp/tests/test_terminal_evidence_projection.py:643-744) covers the write helpers:
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
| No external/domain document defines these projections; the relay contract and tests are the authority. | `CatalogSeatTruthTests` | mcp/tests/test_terminal_evidence_projection.py:473-616 |

## Repo-Internal References

The suite exercises `serving/terminal_evidence.py`, `serving/terminal_liveness.py`,
`serving/seat_turn_truth.py`, and `serving/terminal_catalog.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lift module under test. | `read_entry_terminal_evidence`; `_read_pi_terminal_evidence` | mcp/src/agents_remember/serving/terminal_evidence.py:145-160; mcp/src/agents_remember/serving/terminal_evidence.py:163-190 |
| The liveness ordering (read terminal evidence before persisting the advanced snapshot). | `_observe_alive` | mcp/src/agents_remember/serving/terminal_liveness.py:343-426 |
| The catalog row fields and boundary predicate the suite pins. | `seat_at_turn_boundary`; "class TerminalCatalogEntry:" | mcp/src/agents_remember/models/terminal_catalog.py:58-64; mcp/src/agents_remember/models/terminal_catalog.py:68-72 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## Update History

- 2026-08-10T10:40+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new forcing
  suite (projection lift, pi paging, origin, seat truth, cursor no-loss). Verification
  metadata left blank: the source is uncommitted; closeout stamps the 260713-TES-L2 commit.


