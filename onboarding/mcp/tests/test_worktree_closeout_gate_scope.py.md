# mcp/tests/test_worktree_closeout_gate_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_gate_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T11:48:55+02:00 |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd` |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|
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
| Production closeout stages the task worktree before invoking the strict gate. | `gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129 |

## Cross-Repo References

The temporary consumer fixture models the generic wrapper contract without depending on another
product repository.

## Update History

- 2026-08-14T11:48:55+02:00 — Created for the R42 file-size extraction. Preserved the exact
  created/deleted-file scope regression formerly housed in `test_worktree_closeout_quality_gate.py`;
  final source verification remains closeout-owned.
