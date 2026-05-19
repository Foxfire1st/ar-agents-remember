# route_index.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/_shared/agents_remember/route_index.py` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-19T03:23+02:00                                 |
| lastVerifiedCommitHash | `5b26015bb3e9deec8113b1a69a12608bba82cc27`             |
| lastVerifiedCommitDate | 2026-05-19T03:27:34+02:00|

## Purpose

This module generates route-level `overview.index.json` files for Agents Remember onboarding trees. The indexes give C-04 cheap availability metadata: which route overviews exist, which child routes hang below them, which source files already have file-level sidecars, what source scope the route governs, and which hot-path hints should be tried before opening full overview prose.

## Code Commentary

### Logic

`build_route_indexes` discovers every `overview.md` under an onboarding root, maps each overview to a source route, computes covered file sidecars that still point at real source files, derives child-route relationships, counts source files in each route scope, and writes an adjacent `overview.index.json` for each route. Each index includes schema metadata, `sourceScope`, `childRoutes`, `coveredFiles`, `coverageCounts`, `routingTerms`, `hotPath`, and fallback semantics. `sidecar_status` is the public helper for callers that need to classify a source path as sidecar-present, sidecar-absent inside the route, or out-of-scope.

### Conventions

The generator treats route indexes as derived metadata. It does not maintain long missing-sidecar lists; absence is inferred from `sourceScope` plus `coveredFiles`. File-level sidecars are any mirrored markdown file that is not an overview, entity catalog, generated index, or bootstrap artifact, and only sidecars whose source file still exists are listed as covered. Hot-path summaries are copied from the owning overview's `## Hot Path Summary` section, while candidate and anchor hints are derived mechanically from routes, covered files, child routes, code spans, file tokens, and source-shaped identifiers.

### Invariants And Boundaries

The source tree remains authoritative. The generator may write generated index files under the onboarding root, but it does not edit source files or author onboarding prose. `routingTerms` are broad routing support; `hotPath.anchorHints` are stronger source-search anchors but still hints, not proof. Sparse memory is supported: an overview-only route still gets `sourceScope`, empty `coveredFiles`, coverage counts, and a fallback telling readers to infer sidecar absence instead of probing.

### Todos

After closeout commits this new source file, refresh verification metadata to the committed source revision.

## Docs References

No external domain documentation applies to this repository-local generated-index helper.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The schema constants, result type, and `build_route_indexes` entry point define the generated index format and write/unchanged accounting. | L12-L17; L104-L205 | [route_index.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/route_index.py) |
| `sidecar_status` classifies source paths using normalized path text, `coveredFiles`, and `sourceScope` rather than filesystem probing for every possible sidecar. | L212-L220 | [route_index.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/route_index.py) |
| Route overview discovery, file-sidecar discovery, child-route derivation, and source-file counting build route coverage from current onboarding and source state. | L224-L289 | [route_index.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/route_index.py) |
| Routing terms and hot-path fields are derived from routes, covered files, child routes, copied overview summary text, code spans, file tokens, and source-shaped identifiers. | L291-L386 | [route_index.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/route_index.py) |
| Bootstrap artifacts, overviews, entity catalogs, and generated index files are excluded from file-level sidecar coverage. | L467-L476 | [route_index.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/route_index.py) |

## Cross-Repo References

No sibling repository evidence is needed for this shared helper.

## Update History

- 2026-05-19T03:23+02:00: Created onboarding for the new route-index generator. Verification metadata remains pinned until closeout commits the source change.
