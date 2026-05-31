# mcp/src/agents_remember/worktrees/git_worktree_manager.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/git_worktree_manager.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`git_worktree_manager.py` is the package-local C-09 worktree lifecycle facade
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
`argparse.Namespace` previously flowed from MCP controllers and the CLI into
the worktree domain functions.

The MCP path still calls result-returning service functions such as
`start_result()`, `closeout_result()`, `integrate_result()`, and
`cleanup_result()`. CLI command functions remain print adapters over those
payloads, so MCP controllers do not need to run `main(argv)` and parse stdout.

Worktree lifecycle payloads expose typed MCP next hints through
`nextOperation`, `nextTool`, `nextArgs`, and optional `nextRequiredArgs` instead
of CLI-shaped `next_command` strings. Provider setup for worktree start is fed
through an internal `WorktreeProviderSetupConfig` created by the MCP controller,
so callers no longer pass provider coordination roots, settings paths, or
runtime roots into the worktree start surface.

Closeout context reparsing, changed-path discovery, onboarding metadata/entity
refresh, integration replay, and cleanup now live in the extracted modules
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP worktree start writes temporary lifecycle settings and passes them to this module. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Provider setup performs isolated CGC seed and runtime preparation. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |
| Worktree status packets project lifecycle payloads into context packets. | [status.py](agents-remember-md/mcp/src/agents_remember/worktrees/status.py) |
| Worktree contract serialization lives in the package worktree contract module. | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Extracted worktree lifecycle implementation modules live under this route. | [overview.md](agents-remember-md/mcp/src/agents_remember/worktrees/modules/overview.md) |
| Long-path-safe filesystem wrappers live in the kernel filesystem helper. | [filesystem.py](agents-remember-md/mcp/src/agents_remember/kernel/filesystem.py) |
| Worktree support tests cover memory-worktree settings and long-path closeout planning regressions. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-31T12:50+02:00 — Source now imports and re-exports the typed `WorktreeArgs` dataclass DTO from `worktrees/modules/args.py` (replacing the loosely typed `argparse.Namespace` into domain functions); added it to `__all__` and noted it in the Logic section (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Updated after the worktree manager became a facade over focused lifecycle implementation modules.
- 2026-05-24T18:51+02:00: Updated after closeout planning began using memory-worktree settings and long-path-safe filesystem probes.
- 2026-05-24T05:03+02:00: Updated after worktree lifecycle payloads replaced CLI `next_command` guidance with typed MCP next hints and provider setup moved behind an internal MCP-derived config object.
- 2026-05-24T00:35+02:00: Updated after MCP worktree controllers switched from `main(argv)` capture to result-returning service functions.
- 2026-05-23T23:46+02:00: Updated after worktree provider setup stopped rebuilding provider setup CLI `argv` and switched to `ProviderSetupRequest`.
- 2026-05-23T13:46+02:00: Documented the MCP-owned provider setup path and removal of coordinator-local script execution.
