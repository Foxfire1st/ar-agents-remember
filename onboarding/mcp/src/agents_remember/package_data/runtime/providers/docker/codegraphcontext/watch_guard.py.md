# mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py

## Governing Overview

[CodeGraphContext requirements onboarding](../../requirements/codegraphcontext.txt.md)

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

## Evidence

### Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

- No relevant external documentation source is configured for this file. [1]

### Repo-Internal References

- The guard waits for a genuine PONG, clears poisoned graph keys below the threshold, and execs cgc with the original arguments. [2]
- The CGC Dockerfile copies the guard to `/usr/local/bin/cgc-watch-guard.py` during runner image build. [3]
- The watcher Compose template sets the guard as the watcher service entrypoint. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is required; the guard only talks to the managed FalkorDB backend inside the Compose network.
