# mcp/src/agents_remember/worktrees/git_worktree_manager.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`git_worktree_manager.py` is the package-local `c-09-git-worktree-manager` skill worktree lifecycle facade
behind MCP worktree tools.

## Code Commentary

### Logic

The module now re-exports the public worktree lifecycle surface from focused
implementation modules under `worktrees/modules/`. It preserves imports such as
`agents_remember.worktrees.git_worktree_manager.start_result` while moving the
actual operation logic into smaller files for Git adapters, guidance, start,
onboarding refresh, closeout, integration, cleanup, and CLI parsing. It also
re-exports the typed `WorktreeArgs` dataclass DTO (from
`worktrees/modules/args.py`), which replaces the loosely typed
`argparse.Namespace` previously flowed from MCP application entry points and the CLI into
the worktree domain functions.

The MCP path still calls result-returning service functions such as
`start_result()`, `sync_result()` (GitHub #54 sub-task D, re-exported from
`worktrees/modules/sync.py`), `closeout_result()`, `integrate_result()`,
`checkpoint_landing_result()` (260831-LOCR-L30), `pause_result()`
(260831-LOCR-L37, from `worktrees/modules/pause.py`), and
`cleanup_result()`. Dashboard task 14 adds `FinalizeArgs` and
`finalize_result()` from `worktrees/modules/finalize.py`; callers use this
facade for terminal lifecycle finalization so cleanup plus task-document
completion stay on the same public worktree surface. The facade also re-exports the issue #83 committed-range
closeout surface — `closeout_changed_paths` (from `modules/closeout.py`),
`committed_changed_paths` and `commit_text_or_none` (from `modules/git.py`),
and `contract_memory_verified_commit` (from `modules/onboarding.py`) — so tests
and callers reach the worklist and body-gate baseline helpers through the
stable facade path. 260712-PTS-L1 adds the leaf-id heal to the same surface: the
facade re-exports `heal_contract_leaf_ids` (from `worktrees/worktree_contract.py`)
and `command_heal_leaf_ids` (from `modules/cli.py`) in `__all__`, so the explicit
one-shot legacy-id migration is reachable through the stable facade path like
the lifecycle operations. CLI command functions remain print adapters over those
payloads, so MCP application entry points do not need to run `main(argv)` and parse stdout.
The former direct-closeout re-exports (`direct_closeout_result`,
`direct_closeout_preview_payload`, `validate_direct_external_context`,
`command_direct_closeout`) were removed with the direct-closeout surface
(issue #62): closeout is worktree-only.

Worktree lifecycle payloads expose typed MCP next hints through
`nextOperation`, `nextTool`, `nextArgs`, and optional `nextRequiredArgs` instead
of CLI-shaped `next_command` strings. Provider setup for worktree start is fed
through an internal `WorktreeProviderSetupConfig` created by the MCP application entry point,
so callers no longer pass provider coordination roots, settings paths, or
runtime roots into the worktree start surface.

Closeout context reparsing, changed-path discovery, onboarding metadata/entity
refresh, integration replay, cleanup, and lifecycle finalization now live in the extracted modules
documented by the `modules/overview.md` route overview.

### Invariants And Boundaries

- Worktree provider setup must not invoke `<coordinationRoot>/scripts`.
- Provider enablement and roots come from MCP-derived provider settings, not
  coordinator `system/settings.json`.
- Worktree provider setup should pass typed provider setup options directly and
  should not round-trip through provider setup CLI parsing.
- Worktree status and closeout payloads should describe the next MCP tool/state,
  not shell commands.
- MCP worktree tools should call result-returning functions directly; CLI
  commands should remain adapters for operator use.
- Git subprocesses use `stdin=subprocess.DEVNULL` so they cannot consume MCP
  stdio.
- Contract paths and worktree roots must stay inside the resolved coordination
  workflow model.
- External-memory closeout planning must use memory-worktree settings when the
  task branch changed eligibility rules.
- Onboarding sidecar/catalog probes must tolerate long Windows paths that Git
  can report but normal `Path.exists()`/`Path.is_file()` may miss.
- The facade is the stable public surface for `worktrees/modules/`: a module extracted there is
  re-exported here and listed in `__all__`. The most recent addition is `pause_result`
  from `worktrees/modules/pause.py` (260831-LOCR-L37), so the public `worktree_pause` tool reaches
  the stop-only route through the same stable facade path as its siblings. Before it, the facade
  re-exported `checkpoint_landing_result`
  from `worktrees/modules/integrate.py` (260831-LOCR-L30), so the public
  `worktree_checkpoint_landing` tool reaches the partial-master landing route through the same
  stable facade path as `integrate_result`. Before it, the facade re-exported `record_landing_result`
  from `worktrees/modules/record_landing.py`, so the pull-request landing tool and the direct
  landing path both publish through the one shared landed-integration writer.

## Evidence

### Repo-Internal References

- MCP worktree start writes temporary lifecycle settings and passes them to this module. [1]
- Provider setup performs isolated provider seed and runtime preparation. [2]
- Worktree status packets project lifecycle payloads into context packets. [3]
- Worktree contract serialization lives in the package worktree contract module. [4]
- The facade declares its public worktree lifecycle result exports, including the pull-request landing recorder, the checkpoint landing route and the stop-only pause. [5]
- The pause's result function is imported from its own module and listed in the facade's public export surface, so the stop route is reachable through the stable facade path. [6]
- Terminal lifecycle finalization is implemented in the extracted module. [7]
- Long-path-safe filesystem wrappers live in the kernel filesystem helper. [8]

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.
