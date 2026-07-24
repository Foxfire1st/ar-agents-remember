# mcp/tests/test_landing_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_landing_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:30+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
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

## 260718-CHATS-L5I Current Delta

Landing-state tests now cover freezing fully observed completed facts, stale/corrupt frozen-file rejection, and reopening without resurrection of the prior landing result.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-12T17:30+02:00 — 260712-TRH-L7: created focused coverage for bounded background landing observation and safe cancellation.
