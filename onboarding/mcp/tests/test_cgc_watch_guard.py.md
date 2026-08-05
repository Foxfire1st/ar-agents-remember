# mcp/tests/test_cgc_watch_guard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_cgc_watch_guard.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-09T23:55+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Tests the CGC watcher entrypoint guard Docker asset
(`package_data/runtime/providers/docker/codegraphcontext/watch_guard.py`):
the wait-for-genuine-PONG loop, the read-only File-count probe, the
poisoned-graph clearing threshold, and the always-exec-cgc contract.

## Code Commentary

### Logic

The guard imports `redis` at module level, which is only installed inside the
runner image, so the test injects a stub `redis` module into `sys.modules`
before loading the asset by file path with `importlib`. Tests then drive
`wait_for_ready` (PONG, loading-then-ready, deadline give-up),
`indexed_file_count` (count parsing, empty-key → None, other response errors
re-raised, unparseable replies → None), `clear_poisoned_graph` (delete at
count 0, keep at/above threshold, skip absent graphs), and `main` (graph
check then `os.execvp("cgc", ...)`; exec happens even when the backend never
becomes ready or no graph name is set).

### Invariants And Boundaries

- Loading the asset by file path also gives the package_data copy real
  coverage, which is what keeps the guard's CRAP scores under the CI
  threshold; removing these tests reintroduces a `--fail-on-crap-threshold`
  failure.
- The stub redis module must mirror the exception hierarchy the guard
  catches (`RedisError`, `BusyLoadingError`, `ResponseError`).
- Every `main` test must assert `execvp` is called — the guard's contract is
  that no failure path blocks the watcher.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests resolve the packaged watch guard through `GUARD_PATH`. | `GUARD_PATH` | mcp/tests/test_cgc_watch_guard.py:17-27 |
| The packaged watch guard defines its executable `main`. | `main` | mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py:88-106 |
| The provider Dockerfile copies the guard to `/usr/local/bin/cgc-watch-guard.py`. | "cgc-watch-guard.py" | providers/docker/codegraphcontext/Dockerfile:16-16 |
| The watcher Compose template sets the guard as the watcher entrypoint. | `entrypoint` | providers/compose/codegraphcontext.watcher.yaml.tmpl:25-25 |

## Update History

- 2026-08-04T13:42:02+02:00 — 260731-EFA-L6 S18-B08 curator: split test-path resolution, packaged entrypoint, Dockerfile copy, and Compose entrypoint so each whole claim has one owner.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_cgc_watch_guard.py`
  since the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3
  line(s) with no token change whatsoever. Checked by parsing both revisions and comparing the
  abstract syntax trees (identical) and the comment tokens (identical), so no symbol, signature,
  default, decorator, control-flow branch, docstring, or assertion this card describes has moved,and every claim this card makes about its own source still holds.

- 2026-06-09T23:55+02:00: Created with the guard's unit tests after the CRAP report flagged `wait_for_ready` at the 30.0 threshold (0% coverage on a CC-5 function).
