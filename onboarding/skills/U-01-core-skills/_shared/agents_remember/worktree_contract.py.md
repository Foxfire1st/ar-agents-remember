# worktree_contract.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T01:01                           |
| lastVerifiedCommitHash | `b6a5c21f9309642125a468e63c8aad1a3f3beb88` |
| lastVerifiedCommitDate | 2026-05-10T01:01                           |

## Purpose

`worktree_contract.py` is the shared parser and writer for C-09 task contracts.

## Code Commentary

### Logic

The module defines `WorktreeContract`, deterministic task wrapper and worktree folder helpers, legacy task-root fallback helpers, a limited front-matter parser for the subset the workflow writes, and a writer that emits `contract.md` with task, coordination, code, memory, review, closeout, integration, and cleanup state.

### Conventions

Task wrapper folders use `ar-management/tasks/<repo-name>/<task-name>/` and contain `task.md` plus any later `contract.md`. Legacy `*-ar` task folders remain discoverable for existing contracts. Worktree groups still use `ar-management/worktrees/<repo-name>/<worktree-name>-ar/` because they are operational Git state. Contracts are operational state, not policy. Closeout commits and integration commits are separate fields because replay integration can land different commit SHAs than the reviewed closeout snapshot.

### Invariants And Boundaries

Shared-memory contracts must include memory repo, memory worktree, and ledger paths. Disabled-memory contracts must not invent fake memory paths. Integration state must remain parse-compatible with older contracts that only had closeout cleanup. Current task roots should not append `-ar`; that suffix belongs to worktree groups and legacy task-root lookup only.

### Todos

No current implementation todo is recorded for this helper.

### Docs References

No external documentation is needed; this is repository-local standard-library logic.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `WorktreeContract` records task identity, workflow, coordination, code, shared memory, review, closeout, integration, and cleanup state. | L23-L58 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| Current task-root helpers create wrapper folders without `-ar`, legacy helpers still list `*-ar` task folders, and worktree group helpers keep the operational `-ar` suffix. | L61-L96 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| Default contracts derive repo-scoped task roots, worktree groups, code worktrees, memory worktrees, and ledger paths from the coordination root. | L99-L145 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The writer emits front matter and human-readable review, closeout, integration, and cleanup state, including approved-for-commit and landed commit fields. | L138-L225 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The loader reconstructs the contract fields from parsed front matter sections and keeps old closeout cleanup placement compatible. | L328-L365 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The worktree design spec defines task contracts as local runtime state under the coordinator. | L692-L783 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-10T00:47: Updated after task wrappers stopped using the `-ar` suffix and legacy task-root lookup was added.
- 2026-05-10T00:36: Refreshed verification metadata after integration contract fields landed on main.
- 2026-05-09T23:55: Updated after contracts gained integration status, landed commit fields, and integration-scoped cleanup.
- 2026-05-09T21:59: Created onboarding for the new worktree contract helper.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-file citation with current helper evidence.
