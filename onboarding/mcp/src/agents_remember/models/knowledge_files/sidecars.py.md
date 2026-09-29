# mcp/src/agents_remember/models/knowledge_files/sidecars.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/sidecars.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Local knowledge beside the onboarding Markdown (MIK-R21 rules 1 and 5):** the file sidecar
`onboarding/<source path>.json` (`ar-onboarding-file/v1`), the route sidecar
`onboarding/<route>/overview.json` (`ar-onboarding-route/v1`), their realization and proof entries,
and the `knowledge/layout.json` marker (`ar-memory-layout/v2`) whose presence means a memory tree is
converted. It also records the definitions of *onboarding route* and *governing route*.

## Code Commentary

### Logic

- `_Entry` (`invariant`, `anchor`, `origin?`) refuses an anchor with `path`: realization and proof
  anchors always sit in the sidecar's own file. `RealizationEntry` adds `id` (`RLZ-…`), `role` and
  `rationale`; `ProofEntry` adds `id` (`PRF-…`) and `facet`.
- `RealizationRole` is `primary-authority`, `enforcement`, `propagation-persistence`, `support`,
  `presentation`, `unclassified` — the hand-off template's `incidental` is deliberately absent.
- `FileSidecar` has `path`, `references` (the `[n]` table), `realizes` (required, may be empty) and
  `proves?` (test sidecars). Its validator refuses repeated entry IDs and any reference anchor whose
  `path` equals the sidecar's own path (it must be omitted instead).
- `RouteSidecar` has `path` (a repository directory, or `.` for the root route) and `references`;
  every anchor names its path. The route-index fields (`sourceScope`, `childRoutes`, `coveredFiles`,
  `routingTerms`, `hotPath`, `fallback`) are refused by `extra="forbid"`: they stay in the generated
  `overview.index.json` cache.
- `RoutePath` (public since MIK-R04, leaf 260928-MIK-L04) is the annotated route-directory type: `min_length` 1, the path length limit, and `AfterValidator(_require_route_path)`, so it accepts a repository-relative path or `.` exactly as `RouteSidecar.path` does. `FamilyRecord.routes` uses it; `RouteSidecar` itself is unchanged.
- `LayoutMarker` holds `conversion` only.

### Conventions

- Schema constants (`FILE_SIDECAR_SCHEMA`, `ROUTE_SIDECAR_SCHEMA`, `LAYOUT_MARKER_SCHEMA`) and
  `ROOT_ROUTE_PATH` are declared here and reused by `documents.py`.

### Invariants And Boundaries

- A sidecar owns realizations and proofs; no record repeats them.
- The generated route index is a cache and never part of a committed route sidecar.
- "A sidecar without Markdown holds no references" is the validator's rule (MIK-R22), not enforced here.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The anchor and reference shapes come from `shapes.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| Entry anchors omit `path`. | `_Entry` | mcp/src/agents_remember/models/knowledge_files/sidecars.py:60-71 |
| The role vocabulary. | `RealizationRole` | mcp/src/agents_remember/models/knowledge_files/sidecars.py:50-56 |
| Own-file anchors omit `path`; entry IDs are unique. | `FileSidecar` | mcp/src/agents_remember/models/knowledge_files/sidecars.py:89-108 |
| A route directory type shared with family routes: a repository path or `.`. | `_require_route_path`; `RoutePath` | mcp/src/agents_remember/models/knowledge_files/sidecars.py:111-112; mcp/src/agents_remember/models/knowledge_files/sidecars.py:115-118 |
| Route sidecar: `.` for the root, every anchor names its path. | `RouteSidecar` | mcp/src/agents_remember/models/knowledge_files/sidecars.py:121-133 |
| Route-index fields are refused on a route sidecar. | "coveredFiles" | mcp/tests/test_knowledge_file_formats.py:441-441 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — the new public `RoutePath` type (MIK-R04 ruling Q3).** One Logic bullet and one row added. `RouteSidecar` was re-pointed by the exact six-line shift, its claim unchanged. No verification stamp was advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
