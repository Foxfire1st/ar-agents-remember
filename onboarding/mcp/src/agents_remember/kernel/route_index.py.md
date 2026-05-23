# mcp/src/agents_remember/kernel/route_index.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/route_index.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:09+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`route_index.py` generates `overview.index.json` files for route-local
onboarding overviews.

## Code Commentary

### Logic

The package copy preserves the shared route-index builder used by C-05. It
discovers route overviews, covered sidecars, child routes, source counts,
routing terms, hot-path summaries, and writes or dry-runs one index per route.

### Invariants And Boundaries

- `route_index_refresh` uses configured repo and memory roots.
- Index generation is deterministic and supports dry-run.
- Do not mix provider search logic into route indexing; this is onboarding
  routing metadata only.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `route_index_refresh` calls `build_route_indexes()`. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-05-23T13:09+02:00: Copied into the MCP package for Phase 04.
