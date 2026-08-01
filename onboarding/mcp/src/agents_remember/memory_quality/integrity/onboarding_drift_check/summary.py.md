# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T01:00+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`summary.py` runs a bounded onboarding drift summary for context packets,
`drift_check`, and the closeout memory quality gate.

## Code Commentary

### Logic

The helper discovers sidecar onboarding, inline onboarding, and entity catalog
rows through `drift.py`, writes the normal Markdown report under coordination
temp, and returns counts plus a bounded actionable sample. `not_checked()`
provides the stable context-packet response when callers do not request drift.

Since 260731-EFA-L4 all three builders return the shared
`models.DriftSummaryPacket` TypedDict rather than a bare `dict[str, Any]`:
`not_checked()` (L20-L21) → `{"status": "notChecked"}`, `run_drift_summary(...)`
(L24-L72) → `{"status": "error", "error": ...}` when the onboarding root does not
exist (L30-L34) and otherwise the `summarize_rows` result, and `summarize_rows(...)`
(L75-L90) → the `checked` packet carrying `count`/`actionableCount`/`reportPath`/
`actionableSample`. This module is therefore the **producer of every `DriftStatus`
member**, and the two wire models (`models/drift.py::DriftSummary` for the context
packet, `models/memory.py::DriftCheckResponse` for the tool) validate against the
same declaration instead of each restating the enum. The `error` status this file
has always produced is the one the context-packet model used to be missing — so
the packet crashed on precisely the call meant to explain a missing onboarding
root. No return value here changed; the shape was named, not altered.

Slice 3b adds `_write_drift_snapshot(code_repository_root, context, rows)`: at the
end of `run_drift_summary` it persists what the run already computed as a durable
`ar-drift-snapshot/v1` JSON (counts by classification + `actionableCount` + the
per-sidecar rows + `checkedAt` + the current branch) under
`observer.paths.drift_snapshot_dir(coordination_root)`. The observer reducer reads
that snapshot cheaply with a staleness age instead of re-running the
git-per-sidecar classification on a poll cadence (the b1 decision). The write is
**best-effort** (`try/except OSError`), so the dashboard snapshot can never fail
the drift run that produced it. Task 29 extends the snapshot payload with `sourceRoot`, `memoryRoot`,
and optional `reportPath`, giving actionable-drift attention rows enough provenance to identify the
affected repo/memory/report instead of showing a sparse stale alarm.

Task 32 routes the snapshot filename through
`observer.drift_snapshots.drift_snapshot_path(...)` instead of rebuilding the
`<repo>__<branch>.json` path locally. The drift producer, observer pruning, and
cleanup now share one filename contract.

### Invariants And Boundaries

- Summary generation delegates classification to `drift.py`.
- Actionable classifications are limited to drifted, missing verification,
  missing, orphaned, and unsupported rows; the `ACTIONABLE_CLASSIFICATIONS` set
  is now imported from the shared `models.py`, not defined locally here.
- **This module is the drift-status producer; `models.py` is its declaration.**
  Every packet returned here must be a `DriftSummaryPacket`, and a new status
  belongs on `models.DriftStatus` — never as a bare string returned only from
  here, because the two wire models validate against that alias and would refuse
  the packet at the boundary.
- **Status decides which keys ride.** `checked` carries
  `count`/`actionableCount`/`reportPath`/`actionableSample`; `error` carries
  `error`; `notChecked` carries nothing. They are `NotRequired` on the TypedDict,
  so consumers narrow on `status` and read with `.get`.
- The report path stays temporary; drift reports are not durable memory content.
- The slice-3b drift snapshot is a best-effort write under `logs/observer/drift/`;
  a write failure is swallowed so it never fails the drift run, and its schema/dir
  come from `observer.paths` so producer and reader share one on-disk contract.
- The concrete snapshot filename comes from `observer.drift_snapshots`, so producer
  writes, projection pruning, and cleanup deletion cannot drift apart.
- Snapshot provenance (`sourceRoot`, `memoryRoot`, `reportPath`, `checkedAt`) is copied from the drift
  run context/report, not inferred by the dashboard observer.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Context packets and skill-facing drift tools call this summary helper. | — | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py); [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| The memory quality runner wraps actionable rows from this summary as integrity findings, reading the status-conditional keys with `.get`. | `run_drift_quality_check` L71-L104 | [check.py](agents-remember/mcp/src/agents_remember/memory_quality/check.py) |
| `ACTIONABLE_CLASSIFICATIONS` and, since 260731-EFA-L4, `DriftSummaryPacket`/`DriftStatus` are sourced from the shared models module. | `DriftStatus` L14; `DriftSummaryPacket` L17-L25 | [models.py](models.py) |
| The context-packet wire model that validates this packet's `status` — the one that used to lack `error`. | `DriftSummary` L13-L23 | [models/drift.py](agents-remember/mcp/src/agents_remember/models/drift.py) |
| The tool response model that validates the same packet. | `DriftCheckResponse` L13-L23 | [models/memory.py](agents-remember/mcp/src/agents_remember/models/memory.py) |
| The drift-snapshot dir + schema the b1 write targets (shared with the reader). | — | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The shared drift-snapshot filename helper now used by the producer. | — | [observer/drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| The observer reader that consumes the persisted snapshot. | — | [observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| `_write_drift_snapshot` persists source/memory/report provenance beside counts and rows. | L108-L150 | [summary.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |

## Update History

- 2026-08-01T01:00+02:00 — 260731-EFA-L4 curator: the Logic section described what the three
  builders return but not what type they return it *as*, which is the whole of this leaf's change
  here. Verified against the diff and the current source: `not_checked` (L20-L21),
  `run_drift_summary` (L24-L72) and `summarize_rows` (L75-L90) are now all typed
  `-> DriftSummaryPacket`, imported from the package's `models.py` alongside
  `ACTIONABLE_CLASSIFICATIONS`. Recorded that this module is therefore the producer of every
  `DriftStatus` member and that both wire models now validate against that one declaration —
  including the `error` status this file has always produced at L30-L34 and which
  `models/drift.py::DriftSummary` did not accept, so the context packet crashed on the very call
  meant to report a missing onboarding root. No return value changed; the shape was named, not
  altered. Added two invariants and three reference rows. **Citation repair**: the
  `_write_drift_snapshot` row cited L107-L148, which starts one line before the `def` and stops
  two lines short of the `except OSError` degrade — corrected to L108-L150. The
  Repo-Internal References header was two columns while one row already carried a third
  `Citations` cell (so that range never rendered) — widened the header and gave every row the
  third cell.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: drift snapshots now persist `sourceRoot`,
  `memoryRoot`, and optional `reportPath`, giving actionable-drift attention rows useful provenance and
  a `checkedAt` occurrence anchor. Verification metadata pinned until closeout stamps the task-29 code
  commit.
- 2026-06-27T23:09+02:00 — Task 32 memory-mirror pruning: `_write_drift_snapshot` now uses the shared `observer.drift_snapshots.drift_snapshot_path` helper so producer, pruner, cleanup, and tests use the same file naming contract. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T20:48+02:00 — Slice 3b (browser-dashboard): `run_drift_summary` now also persists a durable `ar-drift-snapshot/v1` JSON snapshot via `_write_drift_snapshot` (best-effort) for the observer reducer to read with a staleness age — drift is classified once, on demand, never re-run on a poll cadence. Verification metadata is pinned until closeout stamps the 3b code commit.
- 2026-05-31T12:50+02:00 — Dropped the local `ACTIONABLE_CLASSIFICATIONS` set literal and now import it from the shared `models.py`; behavior-preserving. Noted the new source in Invariants And Boundaries and added the `models.py` reference (1.0.0 review remediation).
- 2026-05-24T02:47+02:00: Created after drift summary moved under `memory_quality.integrity`.
