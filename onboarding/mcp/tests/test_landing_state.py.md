# mcp/tests/test_landing_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_landing_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:30+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77` |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

Focused tests for the background landing observer and its honest snapshot contract.

## Code Commentary

The suite exercises exact contract identity across repositories and worktrees, bounded concurrency, slow and failed probes, stale carry-forward and age transitions, startup missing state, copy-on-write publication, retention, cancellation, and Projector-owned shutdown. The timing regression proves projection publication does not await remote observation.

## Invariants And Boundaries

Tests cover observer behavior only; the full repository quality gate is owned by the manager.

## Docs References

No external Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Observer implementation under test. | [landing_state.py](agents-remember/mcp/src/agents_remember/observer/landing_state.py) |

## Cross-Repo References

No cross-repo references.

## Update History

- 2026-07-12T17:30+02:00 — 260712-TRH-L7: created focused coverage for bounded background landing observation and safe cancellation.
