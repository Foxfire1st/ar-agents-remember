# mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-09T22:10+02:00                     |
| lastVerifiedCommitHash | `6beccd0545a2d5c161059715d5ed7830917eba03`|
| lastVerifiedCommitDate | 2026-06-09T22:39:28+02:00|
| governingOverview      | `../../../requirements/codegraphcontext.txt.md` |

## Governing Overview

[CodeGraphContext requirements onboarding](../../../requirements/codegraphcontext.txt.md)

## Purpose

`watch_guard.py` is the watcher container entrypoint guard, a package-owned
Docker build asset baked into the managed CodeGraphContext runner image as
`/usr/local/bin/cgc-watch-guard.py`. It prevents the poisoned-watch failure
mode found in the 2026-06-09 incident: after a Docker daemon restart,
`restart: unless-stopped` revives the watcher in arbitrary order relative to
FalkorDB, and upstream cgc's "already indexed" check can latch the watcher
into watch-only mode over an empty or partial graph, silently skipping the
initial scan forever.

## Code Commentary

### Logic

The guard runs before `cgc watch` (the watcher Compose service overrides the
image's `cgc` entrypoint with `python /usr/local/bin/cgc-watch-guard.py`).
It waits up to `CGC_GUARD_WAIT_SECONDS` (default 300) for FalkorDB to answer a
genuine PONG — a `LOADING` reply raises `BusyLoadingError` and counts as not
ready. It then counts File nodes for `FALKORDB_GRAPH_NAME` using
`GRAPH.RO_QUERY` and deletes the graph key when the count is below
`CGC_MIN_INDEXED_FILES` (default 1, i.e. only provably empty graphs), so
upstream cgc's own indexed check fails and triggers the initial scan. Finally
it `os.execvp`s `cgc` with the original arguments.

### Invariants And Boundaries

- The content probe must stay `GRAPH.RO_QUERY`: plain `GRAPH.QUERY` auto-creates
  the empty graph key — the exact poison state the guard exists to clear.
- Every failure path degrades to exec'ing `cgc` (cgc owns its own error
  handling); the guard must never block the watcher permanently.
- The guard uses the `redis` client already installed as a cgc dependency; the
  runner image has no `redis-cli` binary.
- Lives in the Docker layer, not as an upstream cgc patch, so it survives cgc
  version bumps; canonical source is root `providers/docker/codegraphcontext/`,
  this package copy is sync-managed.

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | L1-L3 | [system/sources.md](../../../../../../../../../../../../../system/sources.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The guard waits for a genuine PONG, clears poisoned graph keys below the threshold, and execs cgc with the original arguments. | L1-L115 | [watch_guard.py](agents-remember/mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py) |
| The CGC Dockerfile copies the guard to `/usr/local/bin/cgc-watch-guard.py` during runner image build. | L13-L16 | [Dockerfile](agents-remember/mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/Dockerfile) |
| The watcher Compose template sets the guard as the watcher service entrypoint. | L14-L22 | [codegraphcontext.watcher.yaml.tmpl](agents-remember/mcp/src/agents_remember/package_data/runtime/providers/compose/codegraphcontext.watcher.yaml.tmpl) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is required; the guard only talks to the managed FalkorDB backend inside the Compose network. | n/a | n/a |

## Update History

- 2026-06-09T22:10+02:00: Created with the watcher self-heal entrypoint for the CGC persistence-and-readiness task (2.5.0).
