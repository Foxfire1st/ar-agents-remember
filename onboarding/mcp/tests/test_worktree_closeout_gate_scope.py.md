# mcp/tests/test_worktree_closeout_gate_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_gate_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Prove that leaf closeout's quality gate observes exactly the content it will commit, including
newly created files and staged deletions, and that a refused gate commits nothing while retaining
the certified staged tree for a deterministic retry.

## Code Commentary

### Logic

`gate_scope_contract_fixture` creates a real repository plus linked leaf worktree with the wrapper,
pytest configuration, and a tracked package already committed. `ScopeRecordingGate` runs the real
scope derivation and Ruff's first enforcing rail over the resulting lint paths.

`CloseoutGateSeesCreatedFilesTests` proves three directions: an untracked created file containing
F401 fails before any commit; a refusal leaves HEAD/contract unchanged and the worktree staged; and
a successful closeout makes the gate's Python lint paths equal the Python paths in the committed
tree, including the created file while excluding a deleted one.

### Conventions

Git topology, index behavior, scope derivation, and Ruff are real. Only the Dagger boundary is
replaced by the scope-recording gate so the regression can inspect the exact candidate presented to
the first rail without launching a second acceptance graph.

### Invariants And Boundaries

- The quality gate's scope and the commit's content are one set, not parallel approximations.
- Created files cannot enter the commit unseen, and deleted files cannot remain in lint scope.
- A gate refusal changes neither code HEAD nor contract state; retaining the staged candidate is
  intentional retry state.
- This suite proves closeout scope composition; Dagger remains the production executor.

### Todos

None recorded.

## Docs References

The staged-candidate and Dagger-only closeout contract is recorded in `system/git-workflow.md`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture isolates a linked leaf whose base already carries every prerequisite for scope derivation. | `gate_scope_contract_fixture` | mcp/tests/test_worktree_closeout_gate_scope.py:38-96 |
| The recording gate runs production scope derivation and Ruff over the selected lint paths. | `ScopeRecordingGate` | mcp/tests/test_worktree_closeout_gate_scope.py:99-127 |
| Created-file failure, refused-gate staging, and commit-tree equality cover both sides of the exact-scope invariant. | `CloseoutGateSeesCreatedFilesTests` | mcp/tests/test_worktree_closeout_gate_scope.py:130-208 |
| Production closeout stages the task worktree before invoking the strict gate. | `gate_staged_code` | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:77-129 |

## Cross-Repo References

The temporary consumer fixture models the generic wrapper contract without depending on another
product repository.

## 260821-CLIVE-L1 Closeout Fixture Migration

Quality-gate scope cases now use canonical normalized closeout args. Their staging and created-file assertions are unchanged; validation and journal authority are satisfied before the test reaches the code-quality boundary.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-14T11:48:55+02:00 — Created for the R42 file-size extraction. Preserved the exact
  created/deleted-file scope regression formerly housed in `test_worktree_closeout_quality_gate.py`;
  final source verification remains closeout-owned.
