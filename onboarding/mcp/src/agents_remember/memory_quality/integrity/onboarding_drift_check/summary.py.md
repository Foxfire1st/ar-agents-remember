# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-28T07:32+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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
- The report path stays temporary; drift reports are not durable memory content.
- The slice-3b drift snapshot is a best-effort write under `logs/observer/drift/`;
  a write failure is swallowed so it never fails the drift run, and its schema/dir
  come from `observer.paths` so producer and reader share one on-disk contract.
- The concrete snapshot filename comes from `observer.drift_snapshots`, so producer
  writes, projection pruning, and cleanup deletion cannot drift apart.
- Snapshot provenance (`sourceRoot`, `memoryRoot`, `reportPath`, `checkedAt`) is copied from the drift
  run context/report, not inferred by the dashboard observer.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Context packets and skill-facing drift tools call this summary helper. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py); [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| The memory quality runner wraps actionable rows from this summary as integrity findings. | [check.py](agents-remember/mcp/src/agents_remember/memory_quality/check.py) |
| `ACTIONABLE_CLASSIFICATIONS` is sourced from the shared models module. | [models.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py) |
| The drift-snapshot dir + schema the b1 write targets (shared with the reader). | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The shared drift-snapshot filename helper now used by the producer. | [observer/drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| The observer reader that consumes the persisted snapshot. | [observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| `_write_drift_snapshot` persists source/memory/report provenance beside counts and rows. | L107-L148 | [summary.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |

## Update History

- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: drift snapshots now persist `sourceRoot`,
  `memoryRoot`, and optional `reportPath`, giving actionable-drift attention rows useful provenance and
  a `checkedAt` occurrence anchor. Verification metadata pinned until closeout stamps the task-29 code
  commit.
- 2026-06-27T23:09+02:00 — Task 32 memory-mirror pruning: `_write_drift_snapshot` now uses the shared `observer.drift_snapshots.drift_snapshot_path` helper so producer, pruner, cleanup, and tests use the same file naming contract. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T20:48+02:00 — Slice 3b (browser-dashboard): `run_drift_summary` now also persists a durable `ar-drift-snapshot/v1` JSON snapshot via `_write_drift_snapshot` (best-effort) for the observer reducer to read with a staleness age — drift is classified once, on demand, never re-run on a poll cadence. Verification metadata is pinned until closeout stamps the 3b code commit.
- 2026-05-31T12:50+02:00 — Dropped the local `ACTIONABLE_CLASSIFICATIONS` set literal and now import it from the shared `models.py`; behavior-preserving. Noted the new source in Invariants And Boundaries and added the `models.py` reference (1.0.0 review remediation).
- 2026-05-24T02:47+02:00: Created after drift summary moved under `memory_quality.integrity`.
