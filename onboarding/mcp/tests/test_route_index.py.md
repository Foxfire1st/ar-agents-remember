# mcp/tests/test_route_index.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/tests/test_route_index.py`                         |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-18T20:03+02:00                                 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`             |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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

The contamination case is carried by two named helpers on `RouteIndexTests` rather than one long
body: `_write_scoped_fixture` commits the in-scope tree (including a path-rule-excluded file that
still carries a sidecar, plus a `.gitignore`), and `_assert_contamination_is_invisible_to_git`
writes the artifacts a real checkout accumulates and pins which of them
`git ls-files --others --exclude-standard` still offers — those are exactly the candidates the
census has to reject on its own rules.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Source census validates the root and freezes tracked/untracked membership plus eligible paths. | "def route_index_source_snapshot" | mcp/src/agents_remember/kernel/route_index_census.py:41-41 |
| Rendering consumes one snapshot and writes only changed index bytes. | "def build_route_indexes" | mcp/src/agents_remember/kernel/route_index.py:184-230 |
| Shared Git execution scrubs selectors and uses surrogate-preserving decoding. | "def git_environment" | mcp/src/agents_remember/kernel/git_command.py:94-94 |
| Matrix sections cover contamination, symlink/sparse/gitlink identity, selectors, failures, non-UTF-8 paths, and convergence. | `RouteIndexTests` | mcp/tests/test_route_index.py:82-907 |

## Cross-Repo References

No sibling repository evidence is required; linked-worktree fixtures are created locally.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 8 citation finding(s); scoped recheck clean.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 self-file line citation. The matrix-sections row ended on the `unittest.main()` guard; it now runs L199-L907 — the shared `_write_scoped_fixture` helper through the last line of `test_non_git_source_root_fails_instead_of_walking_the_filesystem` in the 911-line file. Repeat convergence is proven by the `written == 0` re-build assertions at L503-L511, L808-L818, and L858-L876.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 quality gate: the contamination test was split for
  complexity into `_write_scoped_fixture` and `_assert_contamination_is_invisible_to_git`, so Logic
  now names both helpers and what each one owns; the rest of the diff is `ruff format` reflow,
  mostly the nested `with patch(...)` / `assertRaisesRegex(...)` pairs becoming parenthesized
  context groups. All fourteen test methods keep their names and assertions, and the self-citation
  L199-L911 was re-checked: it still starts at the contamination material and now ends exactly at
  the file's last line.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the exact Git/path-rule census, ignored/generated
  exclusion, symlink/sparse/deletion/gitlink/non-UTF-8 identity, selector isolation, typed failure,
  linked-worktree equivalence, and zero-write repeat matrix.
- 2026-05-19T03:23+02:00 — Created onboarding for route-index generator tests; verification remains
  pinned until closeout commits the source change.
