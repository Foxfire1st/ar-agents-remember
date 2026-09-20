# mcp/src/agents_remember/application/provider_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/provider_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-14T15:05+02:00                     |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c`                |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

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

**Every non-removal result carries a reason (260913-LCA-L8).** `remove_tree` answers
`{"path": ..., "removed": False, "reason": ...}` whenever it reclaimed nothing: `already-absent` for
a path that is not there, `permission denied: <error>` when the ownership reclaim cannot run (no
reclaim image in the settings, no readable host owner on this platform, or a failed reclaim
container), and `still present after docker ownership reclaim` for the one branch that retries the
removal after a successful ownership reclaim and the tree survives it. That last branch was the only
producer in the repository able to answer `removed: False` with no reason at all, and the terminal
blocker builder in `worktrees/modules/terminal_validation.py` builds a blockage from exactly this
field — so a reasonless answer there became a blockage no operator could act on. This change names
the branch's cause rather than adding a new teardown capability: a `remove_tree` that still cannot
remove the tree reports the same non-removal, now with its reason.

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

The background setup job owns its temporary settings cleanup. Successful setup writes the
provider state through its supplied callback; failed payloads do not publish a success state file.
A supported setup exception records a failed progress result, and the finally block removes the
job’s temporary settings on either outcome. The foreground returns starting/status guidance while
the daemon thread owns completion.

cit:([`launch_provider_setup`], mcp/src/agents_remember/application/provider_runtime.py:73-121)

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
- Every `remove_tree` result that reclaimed nothing names its reason, so the `providerRuntime` field
  of a teardown payload can never reach the terminal blocker builder reasonless.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `docker_command` and `run_command` are provided by the provider lifecycle shared layer (re-paired to their real owners; the previous row had the two anchors swapped). | "def run_command"; "def docker_command" | mcp/src/agents_remember/providers/lifecycle/command_runner.py:15-15; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:18-18 |
| The one removal path: a not-present path, a dry run, a plain `rmtree`, and the permission-denied reclaim retry whose surviving tree now carries its own reason. | `remove_tree` | mcp/src/agents_remember/application/provider_runtime.py:289-326 |
| The port the worktree layer reaches this module through; its `teardown` and `remove_tree` members are what a worktree operation can call. | `ProviderLifecyclePort` | mcp/src/agents_remember/worktrees/services.py:54-96 |
| The focused cases that pin the reason on every non-removal result and the surviving-tree cause. | `test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing`; `test_a_reclaimed_but_surviving_provider_runtime_reports_why_it_survived` | mcp/tests/test_terminal_blocker_reasons.py:306-329; mcp/tests/test_terminal_blocker_reasons.py:314-352 |

## Update History
- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator: documented that `remove_tree` names a reason on
  every result that reclaimed nothing — `already-absent`, `permission denied: <error>`, and the new
  `still present after docker ownership reclaim` on the post-reclaim retry branch, which was the only
  path in the repository that could answer `removed: False` silently and so the only producer that
  could hand the terminal blocker builder a reasonless `providerRuntime` item. Recorded it as a named
  cause on an existing non-removal rather than a new teardown capability. Re-derived the anchors this
  card keeps: `remove_tree` resolves at `289-326` after the +3 comment lines, `launch_provider_setup`
  `73-121`, `provider_setup_status` `124-147` and `provider_setup_running` `150-155` are unchanged.
  Added the `remove_tree`, `ProviderLifecyclePort` and focused-case rows, and corrected the
  `docker_command`/`run_command` row, whose two anchors were paired with the wrong files. Verification
  metadata remains closeout-owned.

- 2026-08-04T13:00:51+02:00 — 260731-EFA-L6 S18-B11 curator: reconciled abandon/cleanup ownership and the focused test evidence, and supplied scoped fixer input for generated ranges. Verification metadata unchanged.

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 4 citation items; scoped citation check now passes.

- 2026-06-01T00:00+02:00 — Created onboarding for the new provider teardown module.
