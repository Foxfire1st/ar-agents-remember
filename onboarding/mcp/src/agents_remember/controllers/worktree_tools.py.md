# mcp/src/agents_remember/controllers/worktree_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/worktree_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ebe9ef2aa882b5ed6df6dcb2491452efc0cf5c30` |
| lastVerifiedCommitDate | 2026-06-10T07:59:14+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`worktree_tools.py` is the controller surface for worktree start, attach,
status, closeout preview/apply, direct closeout preview/apply, integration,
and cleanup tools.

## Code Commentary

The module resolves allowed repositories and coordination-contained paths from
`McpRuntimeConfig`, builds typed `git_worktree_manager.WorktreeArgs`, and
delegates lifecycle work to `worktrees.git_worktree_manager`. Repo resolution
and path confinement use the shared `_guards` helpers (`require_repo`,
`require_within_coordination`) so the security boundary lives in one place.
Worktree start can include provider setup by writing MCP-derived lifecycle
settings and handing a package-local provider setup config to the worktree
manager.

## Invariants And Boundaries

- Repo IDs must resolve through MCP settings; disallowed IDs and paths escaping
  `coordination_root` raise `AuthorityError` (via the `_guards` helpers).
- Contract paths and memory/source paths must stay under the configured
  coordination root unless a specific tool owns a setup target.
- Worktree operations call package services directly; CLI entrypoints remain
  print adapters.
- `worktree_start_tool`/`worktree_integrate_tool`/`worktree_cleanup_tool` default
  `dry_run=False` (act-by-default); the `*_closeout_apply` controllers keep
  `dry_run=False` paired with their `*_preview` tools. `dry_run=true` previews.

## Repo-Internal References
`worktree_start_tool` marks the temp lifecycle settings file with
`unlink_settings_after_setup=True` and skips its own `finally` unlink when
`_settings_owned_by_background(result)` sees a providers state of `starting` —
the background setup thread reads the file and owns the unlink (GitHub #53).
The new `retry_provider_setup` flag is forwarded to the worktree layer, and the
provider timeout is `config.timeout_caps["providerSetupSeconds"]` (default
`DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) instead of the docker-control 120 —
the documented setup cap now actually governs the worktree flow.


| Finding | Source Path |
| --- | --- |
| Worktree service behavior is owned by the worktree manager and modules. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Worktree response models define the public tool envelopes and context summary. | [worktree.py](agents-remember-md/mcp/src/agents_remember/models/worktree.py) |
| Shared repo/path authority guards (`require_repo`, `require_within_coordination`). | [_guards.py](agents-remember-md/mcp/src/agents_remember/controllers/_guards.py) |

## Update History

- 2026-06-10T07:30+02:00 — worktree_start async support (GitHub #53): the provider setup config now carries `unlink_settings_after_setup=True` and the controller skips its `finally` unlink when the result's providers state is `starting` (`_settings_owned_by_background`) — the background thread reads the temp settings file and owns the unlink. New `retry_provider_setup` flag forwarded to the worktree layer. The provider timeout switched from the hardcoded `DEFAULT_DOCKER_CONTROL_SECONDS` (120) to `config.timeout_caps['providerSetupSeconds']` (default `DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) — the documented setup cap now actually governs the worktree flow (GitHub #58 evidence showed the 120s bound on seed exports).
- 2026-06-01T20:45+02:00 — Added `worktree_abandon_tool` to the controller surface and threaded the `teardown_providers` flag through `worktree_cleanup_tool` (behavior detail lives in `provider_tools.py.md`, `abandon.py.md`, `cleanup.py.md`).
- 2026-05-31T12:30+02:00 — Repo/path guards moved to shared `_guards` (require_repo/require_within_coordination) raising AuthorityError, and namespaces are now typed `git_worktree_manager.WorktreeArgs` instead of `argparse.Namespace` (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Re-verified against `825a172` after the 0.9.x provider/worktree run; the controller surface (start, attach, status, closeout preview/apply, direct closeout preview/apply, integrate, cleanup), its coordination-containment rules, and the act-by-default `dry_run` behavior still match the source. References (`git_worktree_manager.py`, `models/worktree.py`) verified present.
- 2026-05-28T19:52+02:00: Created when worktree MCP controllers moved into their own domain module.
