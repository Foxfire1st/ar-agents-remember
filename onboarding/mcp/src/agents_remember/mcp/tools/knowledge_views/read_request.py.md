# mcp/src/agents_remember/mcp/tools/knowledge_views/read_request.py

## Governing Overview

[MCP Tool Payload Adapters](../overview.md)

## Purpose

Defines the immutable `ReadToolRequest` parameter carrier for `knowledge_read` plus the shared refusal-payload helper and working-tree/commit code-source observer used by `knowledge_views/record_views.py`.

## Code Commentary

`ReadToolRequest` bundles every flat FastMCP argument of `knowledge_read` into one frozen dataclass, including `memory_root`, `view`, `record_id`, `source_path`, `master_id` (used by `consolidation_proposal`), `repository_root`, `code_tree_id`, and server-supplied constant `repository_id = INDEX_REPOSITORY_ID`. `_refused_read` produces the canonical refusal envelope (`ok: True`, `state: "refused"`, `view`, `repositoryId`, `refusalCode`, `refusalDetail`). `_ObservedSource` holds a resolved `(repository_root, code_tree_id, code_state)` together with any scratch `WorktreeCapture` whose lifecycle must span the read and be released via `close()`. `_observe_source(request, workspace_root)` implements three resolution rules: `codeTreeId == "working-tree"` captures `repository_root` (or `workspace_root`, raising `_NoCodeTreeError` if neither exists); an explicit `(repository_root, code_tree_id)` pair reads that commit directly; and a root alone (or `workspace_root` fallback) calls `hold_observed_code_tree`—returning empty `_ObservedSource(None, None, None)` if `workspace_root` is not a checkout, but raising `_NoCodeTreeError` when an explicit `repository_root` resolves no tree.

## Relationships

`ReadToolRequest` is imported and re-exported by `mcp/src/agents_remember/mcp/tools/knowledge.py` and consumed across `record_views.py` and tests (including `test_knowledge_consolidation_proposal.py`). `_observe_source`, `_ObservedSource`, `_NoCodeTreeError`, and `_refused_read` are used by sibling `record_views.py`; `mcp/src/agents_remember/mcp/tools/knowledge.py` currently retains its own multi-repository `_observe_source` and `_refused_read` helpers via `application.knowledge_code_pairing`. Delegates capture primitives to `application.worktree_code_state` and constant `INDEX_REPOSITORY_ID` to `memory.knowledge_index`.

## Evidence

- `ReadToolRequest` captures all flat `knowledge_read` wire arguments—including `master_id`, `record_id`, `source_path`, and server-owned `repository_id = INDEX_REPOSITORY_ID`—as one frozen dataclass. [1]
- `_refused_read` constructs the typed refusal envelope (`ok: True`, `state: "refused"`, `refusalCode`, `refusalDetail`) shared across single-record view adapters. [2]
- `_ObservedSource` owns the scratch `WorktreeCapture` for the duration of a read and releases it on `close()`. [3]
- `_observe_source` resolves `"working-tree"`, explicit commit trees, and clean-or-dirty checkout defaults, raising `_NoCodeTreeError` for an explicit unresolvable root while tolerating a non-repo workspace default. [4]
