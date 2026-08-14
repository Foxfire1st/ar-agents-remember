# mcp/src/agents_remember/application/provider_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/provider_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`application/provider_runtime.py` (260731-EFA-L9) is the provider lifecycle runtime for worktree
start/teardown, moved out of the `worktrees` package because worktrees ranks below providers and
may not import them. It combines the former `worktrees/modules/provider_teardown.py` teardown
mechanics with the background setup launcher and status projection formerly owned by
`worktrees/modules/provider_async.py`; the composition root binds it into `WorktreeServices`.

Teardown performs full-reclaim teardown of a worktree's isolated provider stack. The lifecycle
`stop`/`shutdown-all` actions only stop watchers and leave backend containers and networks
running; this module derives every Docker resource by name from persisted provider settings,
force-removes them, and then recursively removes the `provider-runtime/` tree (data, logs,
settings, state).

## Code Commentary

### Logic

`teardown_worktree_providers(contract, dry_run)` reads the worktree provider
settings from `<group>/provider-runtime/settings/provider-settings.json`, calls
`_worktree_provider_docker_resources` to derive container and network names, and
then runs `_docker_rm_f` and `_docker_network_rm` against each resource.
Finally it calls `remove_tree` on the `provider-runtime/` path.

`_worktree_provider_docker_resources` walks each provider in
`contextProviders.providers`, collecting container names from runner
`containerName`, runner `containerNameTemplate` (expanded per `repoId` root),
backend `containerName`, and embedder backend `containerName`. Network names are
collected from runtime and backend `network.name` fields.

`remove_tree(path, dry_run, reclaim_image, reclaim_cwd)` attempts a plain
`shutil.rmtree`. When that raises `PermissionError` (provider data is
written root-owned by containers), it calls `_reclaim_ownership` which launches
a one-shot Docker container with `--entrypoint chown -R <uid>:<gid> /reclaim`
(the bind-mounted path). After ownership is reclaimed, `rmtree` is retried with
`ignore_errors=True`. `_reclaim_image` picks the first backend/embedder image
found in the settings (it must already be local because it created the data).
`_host_owner` reads `os.getuid()`/`os.getgid()`, returning `None` on non-POSIX
platforms; if either is unavailable the reclaim is reported as unsupported.

`_docker_rm_f` issues `docker rm -f <name>` with a 60 s timeout, treating
"no such container" stderr as already-absent rather than a failure.
`_docker_network_rm` follows the same pattern for `docker network rm`.

### Background Setup Launcher And Status Projection

`launch_provider_setup` (cit:([`launch_provider_setup`], mcp/src/agents_remember/application/provider_runtime.py:73-73)) creates the progress file at
`setup_progress_path(worktree_group)` (`provider-runtime/setup-progress.json`) with
`progress_identity(contract)`, starts a daemon thread, and immediately returns the `starting`
payload (`progressFile`, `pollTool: worktree_status`, and the seed-vs-reindex `expectation`
text). The thread runs the provider setup and finishes the progress with the payload's `state`.
`provider_setup_status(contract)` (cit:([`provider_setup_status`], mcp/src/agents_remember/application/provider_runtime.py:124-124)) is the status projection used by
`worktree_status`, including ready-to-use `retryArgs` on `failed`/`failed-unchecked`/`stale`;
`provider_setup_running(contract)` (cit:([`provider_setup_running`], mcp/src/agents_remember/application/provider_runtime.py:150-150)) is the live-fresh-heartbeat guard
`worktree_cleanup`/`worktree_abandon` use so teardown never races the setup thread.

### Invariants And Boundaries

- The launcher must return before any provider work happens; the contract must already be
  written when it is called; `runner`/`thread_factory` are injectable test seams; a dead server
  mid-setup leaves a stale heartbeat and `retry_provider_setup` is the recovery path — never
  block teardown on a stale heartbeat.
- The module reads persisted settings only; it does not query the live Docker
  daemon for resource discovery.
- `docker rm -f` is used unconditionally (force-removes even running containers).
- Container template names with `<repoId>` are expanded for each root entry
  before deduplication.
- Ownership reclaim is POSIX-only and silently reports unsupported when
  `os.getuid`/`os.getgid` are absent (Windows).
- `remove_tree` is exported and reused by `abandon.py` for the group-dir
  force-remove path.
- The function returns structured result dicts for every resource; teardown
  never raises on partial failures.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `docker_command` and `run_command` are provided by the provider lifecycle shared layer. | "def docker_command"; "def run_command" | mcp/src/agents_remember/providers/lifecycle/command_runner.py:15-15; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:18-18 |

## Update History
- 2026-08-04T13:00:51+02:00 — 260731-EFA-L6 S18-B11 curator: reconciled abandon/cleanup ownership and the focused test evidence, and supplied scoped fixer input for generated ranges. Verification metadata unchanged.

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 4 citation items; scoped citation check now passes.

- 2026-06-01T00:00+02:00 — Created onboarding for the new provider teardown module.
