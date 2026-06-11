# mcp/src/agents_remember/controllers/memory_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/memory_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`memory_tools.py` is the controller surface for drift checks, memory quality,
route-index refresh, memory initialization, memory baseline, and memory
carryover MCP tools.

## Code Commentary

The module resolves target repositories through MCP settings, builds
coordination-contained paths, and delegates to memory quality, route index,
memory init, baseline, and carryover services. Repo resolution and
path confinement use the shared `_guards` helpers (`require_repo`,
`require_within_coordination`) so the security boundary lives in one place.
Drift checks use the onboarding drift summary path; closeout quality checks
use the broader memory quality gate. `memory_baseline_status_tool` reports
`ok=False` when the baseline state is `blocked-drift`.

## Invariants And Boundaries

- Memory tool repo IDs must be allowed by MCP settings; disallowed IDs and
  paths escaping `coordination_root` raise `AuthorityError` (via the `_guards`
  helpers).
- Drift report artifacts remain temporary coordination artifacts, not durable
  onboarding content.
- Baseline and carryover logic belongs in the memory service modules, not in
  MCP transport wiring.
- The effectful controllers (`route_index_refresh_tool`, `memory_init_tool`,
  `memory_baseline_adopt_tool`) default `dry_run=False` (act-by-default);
  `dry_run=true` previews. Carryover uses explicit plan/apply tools (no flag).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Memory response models cover drift, quality, route-index, init, baseline, and carryover tools. | [memory.py](agents-remember/mcp/src/agents_remember/models/memory.py) |
| Route index generation is owned by the kernel route-index module. | [route_index.py](agents-remember/mcp/src/agents_remember/kernel/route_index.py) |

## Update History

- 2026-05-31T12:30+02:00 — Repo/path guards moved to shared `_guards` (require_repo/require_within_coordination) raising AuthorityError, and memory_baseline_status now returns ok=False on blocked-drift (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created when memory/onboarding MCP controllers moved into their own domain module.
