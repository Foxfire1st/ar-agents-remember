# mcp/src/agents_remember/kernel/route_index.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/route_index.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`route_index.py` generates `overview.index.json` files for route-local
onboarding overviews.

## Code Commentary

### Logic

The package copy preserves the shared route-index builder used by C-05. It
discovers route overviews, covered sidecars, child routes, source counts,
routing terms, hot-path summaries, and writes or dry-runs one index per route.
Its ignored source directories include Codex's project-local `.codex` harness
folder so MCP settings, skills, and harness config do not become route-index
source candidates. The module only writes indexes; the unused
`load_route_index(index_path)` reader was removed, so no public loader is
exported from here.

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

- 2026-05-31T12:50+02:00 — Removed the unused `load_route_index(index_path) -> dict[str, Any]` reader from the source (dead code, no remaining callers); noted in Logic that the module only writes indexes and exports no public loader (1.0.0 review remediation).
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` kept `.codex` as the Codex harness exclusion and removed the old `.agents` exclusion.
- 2026-05-24T09:23+02:00: Updated after route indexing kept `.codex` as the harness-folder exclusion and removed the old `.agents` exclusion.
- 2026-05-23T13:09+02:00: Copied into the MCP package for Phase 04.
