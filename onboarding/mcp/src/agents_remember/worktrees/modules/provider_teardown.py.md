# mcp/src/agents_remember/worktrees/modules/provider_teardown.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/provider_teardown.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0`                |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`provider_teardown.py` performs full-reclaim teardown of a worktree's isolated
provider stack. The lifecycle `stop`/`shutdown-all` actions only stop watchers
and leave backend containers and networks running; this module derives every
Docker resource by name from persisted provider settings, force-removes them,
and then recursively removes the `provider-runtime/` tree (data, logs, settings,
state).

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

### Invariants And Boundaries

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `abandon.py` calls `teardown_worktree_providers` and `remove_tree` from this module. | [abandon.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/abandon.py) |
| `cleanup.py` calls `teardown_worktree_providers` when `args.teardown_providers` is set. | [cleanup.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/cleanup.py) |
| `docker_command` and `run_command` are provided by the provider lifecycle shared layer. | [docker_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/docker_runtime.py); [command_runner.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/command_runner.py) |
| Unit tests cover resource derivation, dry-run teardown, reclaim-image selection, and branch-safety helpers. | [test_worktree_abandon.py](agents-remember-md/mcp/tests/test_worktree_abandon.py) |

## Update History

- 2026-06-01T00:00+02:00 — Created onboarding for the new provider teardown module.
