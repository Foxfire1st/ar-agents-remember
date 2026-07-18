# mcp/tests/test_route_index.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/tests/test_route_index.py`                         |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-18T20:03+02:00                                 |
| lastVerifiedCommitHash | `7ca29c3b6dd2c0184253e2690f1ebe78c511573b`             |
| lastVerifiedCommitDate | 2026-07-18T20:18:51+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`test_route_index.py` is the production-path regression matrix for deterministic route-index
source census, path-rule eligibility, generated-byte convergence, and typed failures.

## Code Commentary

### Logic

Core fixtures still verify route topology, source scope, covered sidecars, child routes, routing
terms, hot-path summaries, and `sidecar_status`. MX-FIX-4 extends them with real Git repositories and
explicit storage rules. The matrix proves ignored/generated contamination exclusion; exact tracked
and untracked path identity; symlinks independent of target state; sparse checkout and matched
deletion behavior; gitlink exclusion; all eight ambient repository selectors; typed command,
timeout, `OSError`, and `lstat` failures; non-UTF-8 filenames; and non-repository refusal.

Regular checkout, clean linked worktree, and selector-contaminated generation must produce complete
byte-identical index sets. Every successful first pass is followed by a second pass that reports no
writes, so determinism is tested as convergence rather than only value-level equality.

### Conventions

Fixtures invoke the production builder and Git runner boundary. Synchronization and concrete repo
states replace mocked filesystem walks. Expected failures assert both the typed wrapper and preserved
cause where applicable.

### Invariants And Boundaries

- Repository membership and path-rule eligibility are observed once per generation.
- Ignored paths, excluded generated outputs, gitlinks, and matched deletions cannot contaminate
  source counts or covered files.
- Symlink identity is link-owned; target appearance does not trigger a rewrite.
- Ambient Git selectors cannot redirect production commands.
- Sparse/full and deletion-equivalent states produce identical bytes.
- Successful repetition is exactly zero writes; failures stay typed and do not silently fall back to
  a filesystem walk.

### Todos

Refresh verification metadata only after the code candidate is committed during closeout.

## Docs References

No Domain Documentation source is configured for this repository. The test matrix exercises local
production code and real Git fixtures.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Source census validates the root and freezes tracked/untracked membership plus eligible paths. | L1-L226 | [route_index_census.py](agents-remember/mcp/src/agents_remember/kernel/route_index_census.py) |
| Rendering consumes one snapshot and writes only changed index bytes. | L101-L249 | [route_index.py](agents-remember/mcp/src/agents_remember/kernel/route_index.py) |
| Shared Git execution scrubs selectors and uses surrogate-preserving decoding. | L9-L42 | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| Matrix sections cover contamination, symlink/sparse/gitlink identity, selectors, failures, non-UTF-8 paths, and convergence. | L199-L911 | [test_route_index.py](agents-remember/mcp/tests/test_route_index.py) |

## Cross-Repo References

No sibling repository evidence is required; linked-worktree fixtures are created locally.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the exact Git/path-rule census, ignored/generated
  exclusion, symlink/sparse/deletion/gitlink/non-UTF-8 identity, selector isolation, typed failure,
  linked-worktree equivalence, and zero-write repeat matrix.
- 2026-05-19T03:23+02:00 — Created onboarding for route-index generator tests; verification remains
  pinned until closeout commits the source change.
