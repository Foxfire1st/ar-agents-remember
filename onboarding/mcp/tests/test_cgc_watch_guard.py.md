# mcp/tests/test_cgc_watch_guard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_cgc_watch_guard.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-09T23:55+02:00                     |
| lastVerifiedCommitHash | `04f736d5fdaf23002b0e4172b7475a1108da0d9e`|
| lastVerifiedCommitDate | 2026-06-09T22:16:49+02:00|
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

| Finding | Source Path |
| --- | --- |
| The asset under test, baked into the runner image as `/usr/local/bin/cgc-watch-guard.py`. | [watch_guard.py](agents-remember-md/mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py) |
| The watcher Compose template sets the guard as the watcher entrypoint. | [codegraphcontext.watcher.yaml.tmpl](agents-remember-md/providers/compose/codegraphcontext.watcher.yaml.tmpl) |

## Update History

- 2026-06-09T23:55+02:00: Created with the guard's unit tests after the CRAP report flagged `wait_for_ready` at the 30.0 threshold (0% coverage on a CC-5 function).
