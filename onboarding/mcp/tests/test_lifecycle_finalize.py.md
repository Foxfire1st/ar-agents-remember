# mcp/tests/test_lifecycle_finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_lifecycle_finalize.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `../overview.md`                              |

## Purpose

Focused regression tests for the `lifecycle_finalize_task` worktree operation
and response-model registration.

## Code Commentary

The fixture creates temporary Git repositories and disabled-memory worktree
contracts so the finalizer's Git ancestry proof runs against real commits. It
also creates JSON-primary task documents through `write_task_doc`, allowing the
tests to assert that finalization writes both JSON and rendered markdown through
the production task document service.

Covered behavior:

- a finalized task updates the leaf document to `Completed`, updates only the
  immediate parent subtask row to `Completed`, and leaves the parent/master task
  status unchanged
- missing closeout/integration data or a landed commit absent from the target
  branch returns `not-finalizable-yet` blockers
- cleanup failures return `cleanup-blocked` and do not mutate task documents
- dry-run returns `would-finalize` and `would-update` without mutating documents
- `PUBLIC_TOOL_RESPONSE_MODELS` registers `lifecycle_finalize_task` to
  `LifecycleFinalizeTaskResponse`

The local `_payload` helper casts `WorktreeCommandResult.payload` for test
assertions only; runtime payloads remain typed as `dict[str, object]`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Finalizer behavior under test lives here. | `finalize_result` | mcp/src/agents_remember/worktrees/modules/finalize.py:28-94 |
| Task document read/write behavior used by the fixture lives here. | `TaskDocument` | mcp/src/agents_remember/tasks/document.py:602-716 |
| Git fixture helpers come from the existing worktree support tests. | `WorktreeSupportTests` | mcp/tests/test_worktree_support.py:767-842 |
| Public response model registry is checked for the finalizer entry. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:223-227 |

## L23 Lifecycle Model Package Review

The suite imports `LifecycleFinalizeTaskResponse` from `models.lifecycles.finalize`, its new package
owner. Finalization payload, registry, task-document, and blocker assertions are unchanged.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T04:54+02:00 — 260815-DAG-L14 curator: re-read the `TaskDocument` claim — the persisted
  model gained sprint `seats` and typed `masterRef` rows; wording retained, citation regenerated to
  the current class lines, stamp advanced to code commit 2f494982.


- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: a queue-governed task-document
  reconciliation refusal now returns the exact `task-queue-blocked` result without mutating task
  facts after worktree cleanup.

- 2026-08-13T09:05+02:00 — L23 curator: recorded the finalize-response import move and confirmed the
  regression contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T00:08+02:00 — No content impact: the parameterized finalization subtest reports a
  serializable label under xdist; finalization setup, operation, and assertions are unchanged.
  Verification metadata remains pinned until closeout.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 4 repo-internal citation rows and preserved verification metadata.

- 2026-07-31T16:50+02:00 — No content impact: the fixture's `default_contract` call now passes the
  `ContractTask` / `LeafIdentity` / `RepoBranchPlan` parameter objects added for PLR0913 instead of
  ten loose keyword arguments, and `ruff format` rewrapped the `patch(...)` context manager in the
  cleanup-blocked test. The temporary Git repos, the disabled-memory contract, the `write_task_doc`
  fixture path, and every covered behavior enumerated above are unchanged.
- 2026-06-23T22:50+02:00 — Created focused lifecycle finalizer regression coverage. Verification metadata is pending until closeout stamps the source commit.
