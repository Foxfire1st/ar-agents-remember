# worktree_contract.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:57                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

`worktree_contract.py` is the shared parser and writer for C-09 task contracts.

## Code Commentary

### Logic

The module defines `WorktreeContract`, deterministic task/worktree folder helpers, a limited front-matter parser for the subset the workflow writes, and a writer that emits `contract.md` with task, coordination, code, memory, review, and closeout state.

### Conventions

Worktree-backed task folders use `ar-management/tasks/<repo-name>/<task-name>-ar/`; worktree groups use `ar-management/worktrees/<repo-name>/<worktree-name>-ar/`. Contracts are operational state, not policy.

### Invariants And Boundaries

Shared-memory contracts must include memory repo, memory worktree, and ledger paths. Disabled-memory contracts must not invent fake memory paths.

### Todos

If richer workflow artifacts need a `task/` directory instead of `task.md`, extend the writer without changing the contract schema.

### Docs References

No external documentation is needed; this is repository-local standard-library logic.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `WorktreeContract` records task identity, workflow, coordination, code, shared memory, review, and closeout state. | L16-L50 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| Default contracts derive repo-scoped task roots, worktree groups, code worktrees, memory worktrees, and ledger paths from the coordination root. | L67-L126 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The writer emits front matter and human-readable review/closeout state, including approved-for-commit and ledger commit fields. | L138-L219 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The loader reconstructs the contract fields from parsed front matter sections. | L308-L339 | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) |
| The worktree design spec defines task contracts as local runtime state under the coordinator. | L692-L783 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:59: Created onboarding for the new worktree contract helper.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-file citation with current helper evidence.
