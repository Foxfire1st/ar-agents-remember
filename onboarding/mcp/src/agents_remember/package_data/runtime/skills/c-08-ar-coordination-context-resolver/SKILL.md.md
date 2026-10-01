# c-08-ar-coordination-context-resolver/SKILL.md

## Purpose

This skill defines `c-08-ar-coordination-context-resolver` skill, the authoritative facts-only resolver for memory roots, coordination roots, settings, path rules, task roots, temporary artifact roots, worktree contract fields, ledger paths, and branch-gated cross-repo allowances.

## Code Commentary

### Logic

The skill tells agents to resolve context once and pass the resulting facts downstream instead of re-deriving topology in every workflow. It documents `code_repository_name`, `code_repository_root`, `coordination_root`, `memory_root`, `task_root`, `temp_root`, optional contract/worktree fields, JSON-first settings, path rules, storage settings, and cross-repo v2 result states. Without `task_name`, `task_root` is the repo-specific task namespace under `ar-coordination/tasks/<code-repository-name>/`; with `task_name` or a contract, it is the concrete task folder. Normal installed workflows resolve the coordination root from MCP settings; package-local resolver calls use explicit input, an installed runtime root, or the source-development `../ar-coordination` default. Source-checkout `.env` and `.env.example` files are not resolver inputs. Resolution validates supported memory locations and fails with a missing-memory error instead of inventing an empty context.

### Conventions

`c-08-ar-coordination-context-resolver` skill is facts-only. It may report worktree-related context from a contract, but creation or mutation of worktrees belongs to `c-09-git-worktree-manager` skill.

### Invariants And Boundaries

Consumers should rely on `c-08-ar-coordination-context-resolver` skill for paths and topology. They should not infer onboarding roots from current working directory names. `c-08-ar-coordination-context-resolver` skill does not create onboarding content, drift reports, or worktree state.

### Todos

Add more examples after the first real worktree-backed task contract exists in the workspace.

### Docs References

No external domain documentation applies to this repository-local skill contract.

No relevant external documentation found.

## Evidence

### Repo-Internal References

`c-08-ar-coordination-context-resolver` skill is the base dependency for `c-02-memory-quality-control` skill, `c-03-repo-bootstrap` skill, `c-04-retrieval-strategy-router` skill, `c-05-create-or-update-onboarding-files` skill, and task workflows.

- The skill accepts `code_repository_name`, optional `code_repository_root`, and `task_name`; no-task-name contexts resolve the repo task namespace, while task-name contexts resolve current wrapper task folders and persisted `*-ar` contract folders. [1]
- The skill returns topology, code repository identity/root, settings paths, repo/task-specific task roots, temp/docs/system roots, worktree fields, ledger path, path rules, and cross-repo data. [2]
- Resolution rules validate explicit onboarding roots, load worktree contract coordination first, use MCP settings or explicit/installed/default package roots for coordination, require supported memory roots, and fail clearly when no memory exists. A removed `internal` request or a repo-local `ar-memory/` root is refused by name with `memory-mode-unsupported`, never falling through to the external root; `external` is the only supported topology. [3]
- Consumers include `c-02-memory-quality-control` skill, `c-03-repo-bootstrap` skill, c-04-retrieval-strategy-router, `c-05-create-or-update-onboarding-files` skill, task workflows, and `c-09-git-worktree-manager` skill; boundaries keep `c-08-ar-coordination-context-resolver` skill out of mutation work. [4]
- The package implementation exposes the same `code_repository_name` and `code_repository_root` fields through `CoordinationContext`, context construction, and MCP/JSON output. [5]

### Cross-Repo References

`c-08-ar-coordination-context-resolver` skill may read coordinator settings, but no external repository behavior is required to understand this skill's current contract.

No meaningful cross-repo references found for current skill semantics.

## Series-Contract Notes

The packaged resolver skill now teaches active task-name lookup, optional `parent_task` disambiguation, optional `leaf_id` selection, and root/leaf `series-contract.md` paths so installed runtimes do not look for `contract.md`.
