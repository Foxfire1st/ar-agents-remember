# mcp/src/agents_remember/kernel/route_index.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/kernel/route_index.py`           |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-07-31T00:00+02:00                                   |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`               |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                                   |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

`route_index.py` renders deterministic `overview.index.json` availability metadata for every
route-local onboarding overview from one caller-authorized source snapshot.

## Code Commentary

### Logic

`build_route_indexes()` requires explicit `code_root`, `onboarding_root`, repository identity, and
`StorageSettings`. It calls `route_index_source_snapshot()` once, then reuses the snapshot's
unfiltered `repository_paths` for sidecar/source membership and its path-rule-filtered
`eligible_paths` for route source counts. It discovers overview topology in onboarding, derives
covered sidecars, child routes, routing terms, and hot-path summaries, serializes stable JSON, and
writes only when bytes differ. There is no filesystem source walker and no late `Path.is_file()`
membership decision.

Routing-term extraction decides which identifier hints are worth indexing in two named steps
(260731-EFA-L2): `_is_source_anchor(token)` rejects tokens shorter than three characters and
anything in `GENERIC_ANCHOR_WORDS`, then defers to `_has_code_shape(token)` — one boolean
expression that is true when the token's own spelling marks it as an identifier rather than prose.
Any one signal is enough: a dotted or slashed path, snake_case, an embedded digit, an all-caps
constant, or an interior capital (camelCase / PascalCase). The signals and their outcomes are
exactly the previous early-return chain's; only the shape test now has a name.

### Conventions

The builder owns rendering; `route_index_census.py` owns exact Git/path-rule source identity.
Generated indexes are derived metadata and are regenerated rather than copied or hand-edited.
`dry_run` computes the same result without writes.

### Invariants And Boundaries

- One frozen snapshot supplies both repository membership and path-rule eligibility for the whole
  generation pass; counts and covered files cannot observe different filesystem moments.
- Ignored/generated exclusions, symlinks, sparse paths, deletions, gitlinks, non-UTF-8 names, and
  ambient Git selectors are census concerns and must not be reimplemented here.
- The repository name and storage rules are required authority from coordination context or the
  official carryover preflight; the builder must not invent defaults.
- A second build with unchanged source/onboarding inputs must report zero writes and byte-identical
  indexes.
- Indexes support retrieval routing; they are not hand-authored semantic truth.

### Todos

None known for the MX-FIX-4 rendering boundary.

## Docs References

No Domain Documentation source is configured for this repository. The behavior is defined by
package source and deterministic production-path tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The census validates the Git root and freezes tracked/untracked membership plus path-rule eligibility. | L1-L226 | [route_index_census.py](agents-remember/mcp/src/agents_remember/kernel/route_index_census.py) |
| MCP refresh supplies resolved repository and storage authority. | L80-L110 | [memory_tools.py](agents-remember/mcp/src/agents_remember/controllers/memory_tools.py) |
| Closeout preview/apply forwards `context.storage` explicitly. | L345-L363 | [onboarding.py](agents-remember/mcp/src/agents_remember/worktrees/modules/onboarding.py) |
| The regression matrix proves identity, exclusions, typed failures, and repeat convergence. | L199-L907 | [test_route_index.py](agents-remember/mcp/tests/test_route_index.py) |

## Cross-Repo References

Generated indexes can describe configured sibling repositories, but the builder contract is owned
inside this package.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation whose end ran
  past `mcp/tests/test_route_index.py` (911 lines, of which L909-L911 are the `unittest.main()`
  trailer). Narrowed the regression-matrix range to L199-L907 and re-read it: it now opens on the
  extracted `_write_scoped_fixture`/`_assert_contamination_is_invisible_to_git` helpers and still
  covers identity (L329, L768, L822), exclusions (L258, L544), typed failures (L642, L675, L739,
  L891), and repeat convergence (`written == 0` on the second build at L503-L511, L808-L818,
  L858-L876).
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911` armed with no exemptions):
  `_is_source_anchor`'s six-return chain became a length/generic-word guard plus the new
  `_has_code_shape(token)` boolean. Same tokens accepted, same tokens rejected — a regenerated
  index is byte-identical. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: route generation now consumes one explicit
  repository/storage-authorized Git census for membership, eligibility, counts, and covered files.
- 2026-05-31T12:50+02:00 — Removed the unused `load_route_index(index_path)` reader; the module
  writes indexes only (1.0.0 review remediation).
- 2026-05-24T10:06+02:00 — Refreshed verification metadata after source commit `f48a346` kept
  `.codex` as the Codex harness exclusion and removed the old `.agents` exclusion.
- 2026-05-24T09:23+02:00 — Updated after route indexing kept `.codex` as the harness-folder
  exclusion and removed the old `.agents` exclusion.
- 2026-05-23T13:09+02:00 — Copied into the MCP package for Phase 04.
