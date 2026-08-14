# mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-09T22:10+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../requirements/codegraphcontext.txt.md`                              |

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

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | `# Sources` | system/sources.md:1-3 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The guard waits for a genuine PONG, clears poisoned graph keys below the threshold, and execs cgc with the original arguments. | `clear_poisoned_graph` | mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py:72-85 |
| The CGC Dockerfile copies the guard to `/usr/local/bin/cgc-watch-guard.py` during runner image build. | "/usr/local/bin/cgc-watch-guard.py" | mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/Dockerfile:16-16 |
| The watcher Compose template sets the guard as the watcher service entrypoint. | "cgc-watch-guard.py" | mcp/src/agents_remember/package_data/runtime/providers/compose/codegraphcontext.watcher.yaml.tmpl:25-25 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is required; the guard only talks to the managed FalkorDB backend inside the Compose network. | n/a | n/a |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the four `n/a`-anchor
  table citations (guard, Dockerfile, watcher template, `system/sources.md`) with exact anchors
  and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 line citation that ran past the end of
  `watch_guard.py` (cited L1-L115; the file is 110 lines). Narrowed it to L41-L106, the exact span
  the claim describes: cit:([`wait_for_ready`], mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py:41-53), cit:([`indexed_file_count`], mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py:56-69),
  cit:([`clear_poisoned_graph`], mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py:72-85), and `main` ending at the `os.execvp("cgc", ...)` call on L106.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/watch_guard.py`
  since the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 2
  line(s), joining implicitly concatenated string literals back onto single lines. Checked by
  parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-06-09T22:10+02:00: Created with the watcher self-heal entrypoint for the CGC persistence-and-readiness task (2.5.0).
