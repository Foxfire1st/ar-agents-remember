# mcp/src/agents_remember/worktrees/git_worktree_manager.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/git_worktree_manager.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview      | `../../../overview.md`                     |

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
`worktrees/modules/sync.py`), `closeout_result()`, `integrate_result()`, and
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP worktree start writes temporary lifecycle settings and passes them to this module. | `worktree_start_tool` | mcp/src/agents_remember/application/worktree_tools.py:77-156 |
| Provider setup performs isolated provider seed and runtime preparation. | `ProviderSetupRequest`; `prepare_enabled_providers`; `write_isolated_provider_settings` | mcp/src/agents_remember/providers/provider_setup.py:57-120; mcp/src/agents_remember/providers/provider_setup.py:219-233; mcp/src/agents_remember/providers/provider_setup.py:591-629 |
| Worktree status packets project lifecycle payloads into context packets. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:61-143 |
| Worktree contract serialization lives in the package worktree contract module. | `contract_to_text` | mcp/src/agents_remember/worktrees/worktree_contract.py:689-740 |
| The facade declares its public worktree lifecycle result exports. | `__all__` | mcp/src/agents_remember/worktrees/git_worktree_manager.py:96-167 |
| Terminal lifecycle finalization is implemented in the extracted module. | `finalize_result` | mcp/src/agents_remember/worktrees/modules/finalize.py:55-141 |
| Long-path-safe filesystem wrappers live in the kernel filesystem helper. | `extended_path`; `exists`; `is_file` | mcp/src/agents_remember/kernel/filesystem.py:16-25; mcp/src/agents_remember/kernel/filesystem.py:28-29; mcp/src/agents_remember/kernel/filesystem.py:32-33 |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `worktree_status_packet` repointed to mcp/src/agents_remember/application/worktree_status.py:61-143. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:39+02:00 — 260731-EFA-L6 S18-B13 curator: bound lifecycle, provider, status, contract, facade, filesystem, and test claims to exact anchors.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1: re-exported `heal_contract_leaf_ids` (from
  `worktree_contract.py`) and `command_heal_leaf_ids` (from `modules/cli.py`) and added both to
  `__all__`, putting the explicit one-shot legacy leaf-id heal on the stable facade surface.
  Verification metadata pinned until closeout stamps the 260712-PTS-L1 commit.
- 2026-06-23T22:50+02:00 — Re-exported `FinalizeArgs` and `finalize_result` for the new `lifecycle_finalize_task` terminal operation. Verification metadata pinned until closeout stamps the source commit.

- 2026-06-12T19:06+02:00 — Issue #83: re-exported the committed-range closeout surface (`closeout_changed_paths`, `committed_changed_paths`, `commit_text_or_none`, `contract_memory_verified_commit`) and added them to `__all__`.
- 2026-06-11T06:47+02:00 — Dropped the direct-closeout re-exports (`direct_closeout_result`, `direct_closeout_preview_payload`, `validate_direct_external_context`, `command_direct_closeout`) from the facade imports and `__all__` (issue #62 worktree-only closeout).
- 2026-06-10T09:56+02:00 — Re-exported `sync_result` from the new `worktrees/modules/sync.py` (GitHub #54 sub-task D).
- 2026-06-01T20:45+02:00 — Re-exported `abandon_result`, `teardown_worktree_providers`, and `delete_branch_force` for the new worktree abandon/teardown path.
- 2026-05-31T12:50+02:00 — Source now imports and re-exports the typed `WorktreeArgs` dataclass DTO from `worktrees/modules/args.py` (replacing the loosely typed `argparse.Namespace` into domain functions); added it to `__all__` and noted it in the Logic section (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Updated after the worktree manager became a facade over focused lifecycle implementation modules.
- 2026-05-24T18:51+02:00: Updated after closeout planning began using memory-worktree settings and long-path-safe filesystem probes.
- 2026-05-24T05:03+02:00: Updated after worktree lifecycle payloads replaced CLI `next_command` guidance with typed MCP next hints and provider setup moved behind an internal MCP-derived config object.
- 2026-05-24T00:35+02:00: Updated after MCP worktree controllers switched from `main(argv)` capture to result-returning service functions.
- 2026-05-23T23:46+02:00: Updated after worktree provider setup stopped rebuilding provider setup CLI `argv` and switched to `ProviderSetupRequest`.
- 2026-05-23T13:46+02:00: Documented the MCP-owned provider setup path and removal of coordinator-local script execution.
