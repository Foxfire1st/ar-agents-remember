# mcp/tests/test_legacy_nature_tolerance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_legacy_nature_tolerance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the 260815-DAG-L13-R5/R7 legacy tolerance: nature-less masters flow through the
atomic-sequential default mode — the old dead-ends are gone, while an explicit `organizational`
standalone master keeps its refusal.

## Code Commentary

### Logic

`LegacyNatureToleranceTests` proves a nature-less standalone master resolves `master` altitude with
no parent edge (no migration), its series retires through the normal terminal authority
(abandon/cleanup stay reachable), and a terminal stale series artifact under an organizational
master is ignored and reported as a `staleSeriesArtifact` fact instead of refusing the start.
Negative branches are forced too: an explicit organizational standalone still refuses, a corrupt
series artifact still refuses, a live organizational series reports no fact, lane holders skip
unreadable or vanished masters, and master authority skips graph validation under the default mode.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; the deployed coordinator is never written.
- Tolerance is exact: nature-less resolves atomic, explicit organizational standalone still
  dead-ends.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Legacy nature tolerance and stale-artifact forcing. | `LegacyNatureToleranceTests` | mcp/tests/test_legacy_nature_tolerance.py:71-383 |
| The effective-nature resolution and stale-artifact fact under test. | `effective_execution_nature`; `stale_series_artifact_fact` | mcp/src/agents_remember/worktrees/scheduling_mode.py:94-117; mcp/src/agents_remember/worktrees/scheduling_mode.py:159-193 |
| The standalone-master altitude resolution under test. | `TaskDocumentTopology` | mcp/src/agents_remember/tasks/document_refs.py:62-555 |

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created as the legacy nature-tolerance forcing suite.
  Verification remains closeout-owned.
