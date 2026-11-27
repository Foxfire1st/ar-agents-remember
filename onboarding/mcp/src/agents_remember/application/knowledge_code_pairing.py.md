# mcp/src/agents_remember/application/knowledge_code_pairing.py

## Governing Overview

[application](overview.md)

## Purpose

Automatic code-tree pairing and working-tree observation module for `knowledge_read`. Resolves which code checkout a memory read observes using explicit precedence without guessing by bare directory-name coincidence, and holds temporary dirty working-tree captures via `ObservedCodeSource` with explicit cleanup.

## Code Commentary

- `resolve_paired_code_root` enforces four-tier precedence: (1) explicit `request.repository_root`, (2) leaf worktree (`_leaf_code_worktree`), (3) configured repository (`_configured_code_root`), and (4) `PairingContext.workspace_root` fallback.
- `_leaf_code_worktree` resolves `contract_path` via `_code_worktree_from_contract`, then `<memory_parent>/.lifecycle/enclosure-manifest.json` (`_code_worktree_from_manifest` checking that `contract.memory_worktree` matches `resolved_memory`), then an enclosure sibling `<parent>/<slug>` for `memory-<slug>` directories containing `.git`.
- `_configured_code_root` matches `repo_id`, exact resolved `scope.memory_root`, or shared `git rev-parse --git-common-dir` (5-second timeout), enabling automatic pairing on Projects-scoped mounts where `workspace_root` is not a Git repository.
- `observe_code_source` handles `code_tree_id == WORKING_TREE_SELECTOR` (raising `NoCodeTreeError` if unpaired; otherwise capturing the worktree), explicit commit/tree IDs (`CODE_STATE_COMMIT`), and unpinned reads (`_observe_unpinned_root` via `hold_observed_code_tree`, raising `NoCodeTreeError` only when `explicit_root` was caller-supplied).
- `code_tree_of` builds a `CodeTree` that preserves `capture.object_directory` so anchors remain verifiable against dirty working-tree captures.

## Relationships

- Called by `mcp/src/agents_remember/mcp/tools/knowledge.py` and `mcp/src/agents_remember/mcp/tools/knowledge_queries.py`; tested in `mcp/tests/test_kno_r07_briefs_and_pairing.py`.
- Depends on `application/knowledge_currentness.py::CodeTree`, `application/worktree_code_state.py`, `kernel/git_command.py::git_environment`, `kernel/primitives/runtime_config.py::RepositoryScope`, and lazy `worktrees.worktree_contract.load_contract`.

## Evidence

- `resolve_paired_code_root` enforces four-tier pairing precedence: explicit root, leaf worktree, configured repository, and `workspace_root` fallback. [1]
- `observe_code_source` captures dirty working trees and raises `NoCodeTreeError` only on explicit unreadable roots or unpaired `working-tree` requests. [2]
- `code_tree_of` forwards `capture.object_directory` onto the returned `CodeTree`. [3]
- `_leaf_code_worktree` resolves `contractPath`, enclosure manifest, and `memory-<slug>` sibling worktree. [4]
- `_configured_code_root` pairs by `repo_id`, exact `memory_root`, or shared `--git-common-dir`. [5]
