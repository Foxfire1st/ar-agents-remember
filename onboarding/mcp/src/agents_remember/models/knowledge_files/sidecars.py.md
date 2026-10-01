# mcp/src/agents_remember/models/knowledge_files/sidecars.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The anchor and reference shapes come from `shapes.py`.

- Entry anchors omit `path`. [1]
- The role vocabulary. [2]
- Own-file anchors omit `path`; entry IDs are unique. [3]
- A route directory type shared with family routes: a repository path or `.`. [4]
- Route sidecar: `.` for the root, every anchor names its path. [5]
- Route-index fields are refused on a route sidecar. [6]

### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.
