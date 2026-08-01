# mcp/tests/test_landing_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_landing_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T09:56+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
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

- 2026-08-01T09:56+02:00 — 260731-EFA-L4 curator: No content impact: the diff is a single
  character-level fixture edit — `_contract`'s `workflow_kind="light"` becoming `"light-task"`,
  because `WorkflowKind` is now `Literal["chat-task", "light-task"]`
  (`worktrees/worktree_contract.py` L50) and `"light"` is no longer a member. The per-index
  contract identities are otherwise identical, and the workflow kind is not read by anything under
  test: the card claims contract identity across repositories and worktrees, bounded concurrency,
  slow/failed probes, stale carry-forward and age transitions, startup missing state,
  copy-on-write publication, retention, cancellation, Projector-owned shutdown, the
  publication-does-not-await-observation timing regression, and the CHATS-L5I freezing / stale-file
  rejection / reopen-without-resurrection cases — every one of which I re-read in the current
  558-line file and all of which still hold. The one reference row resolves:
  `observer/landing_state.py` exists.

- 2026-07-31T16:50+02:00 — No content impact: the only change is the `_contract` fixture helper,
  which now calls `default_contract` with the `ContractTask` / `LeafIdentity` / `RepoBranchPlan`
  parameter objects introduced for PLR0913 instead of ten loose keyword arguments. The same
  per-index contract identities are still produced, and no observer test case, probe scenario, or
  assertion in this suite changed, so the coverage record above still holds.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-12T17:30+02:00 — 260712-TRH-L7: created focused coverage for bounded background landing observation and safe cancellation.
