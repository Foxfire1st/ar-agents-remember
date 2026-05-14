# worktree_contract.py

| Field                  | Value                                                                  |
| ---------------------- | ---------------------------------------------------------------------- |
| repository             | agents-remember-md                                                     |
| path                   | `skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py` |
| doc_type               | `file-level-onboarding`                                                |
| lastUpdated            | 2026-05-10T01:19                                                       |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`                             |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

`worktree_contract.py` is the common parser and writer for C-09 task contracts.

## Code Commentary

### Logic

The module defines `WorktreeContract`, deterministic task wrapper and worktree folder helpers, legacy task-root fallback helpers, a limited front-matter parser for the subset the workflow writes, and a writer that emits `contract.md` with task, coordination, code, memory, review, commit approval, closeout, integration, and cleanup state.

### Conventions

Task wrapper folders use `ar-coordination/tasks/<repo-name>/<task-name>/` and contain `task.md` plus any later `contract.md`. Persisted `*-ar` task folders remain discoverable for existing contracts. Worktree groups still use `ar-coordination/worktrees/<repo-name>/<worktree-name>-ar/` because they are operational Git state. Contracts are operational state, not policy. Closeout commit approval is recorded as a human-review note, while closeout commits and integration commits remain separate fields because replay integration can land different commit SHAs than the reviewed closeout snapshot.

### Invariants And Boundaries

External-memory contracts must include memory repo, memory worktree, and ledger paths. Disabled-memory contracts must not invent fake memory paths. Integration state must remain parse-compatible with older contracts that only had closeout cleanup. Commit approval notes are optional for older contracts but should be written by new closeouts. Current task roots should not append `-ar`; that suffix belongs to worktree groups and legacy task-root lookup only.

### Todos

No current implementation todo is recorded for this helper.

### Docs References

No external documentation is needed; this is repository-local standard-library logic.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                                                                                                            | Citations | Source Path                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------- |
| `WorktreeContract` records task identity, workflow, coordination, code, external memory, review, commit approval note, closeout, integration, and cleanup state.                                     | L23-L59   | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| Current task-root helpers create wrapper folders without `-ar`, legacy helpers still list `*-ar` task folders, and worktree group helpers keep the operational `-ar` suffix.                       | L68-L97   | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| Default contracts derive repo-scoped task roots, worktree groups, code worktrees, memory worktrees, and ledger paths from the coordination root.                                                   | L100-L146 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The writer emits front matter and human-readable review, commit approval, closeout, integration, and cleanup state, including approved-for-commit, commit approval note, and landed commit fields. | L169-L268 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The loader reconstructs the contract fields from parsed front matter sections and keeps old closeout cleanup placement compatible.                                                                 | L349-L389 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The worktree design spec defines task contracts as local runtime state under the coordinator.                                                                                                      | L692-L783 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md)         |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-10T01:19: Updated after contracts began recording an explicit commit approval note during closeout.
- 2026-05-10T00:47: Updated after task wrappers stopped using the `-ar` suffix and legacy task-root lookup was added.
- 2026-05-10T00:36: Refreshed verification metadata after integration contract fields landed on main.
- 2026-05-09T23:55: Updated after contracts gained integration status, landed commit fields, and integration-scoped cleanup.
- 2026-05-09T21:59: Created onboarding for the new worktree contract helper.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-file citation with current helper evidence.
