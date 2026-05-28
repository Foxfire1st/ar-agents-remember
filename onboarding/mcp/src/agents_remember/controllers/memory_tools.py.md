# mcp/src/agents_remember/controllers/memory_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/memory_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`memory_tools.py` is the controller surface for drift checks, memory quality,
route-index refresh, memory initialization, memory baseline, and memory
carryover MCP tools.

## Code Commentary

The module resolves target repositories through MCP settings, builds
coordination-contained paths, and delegates to memory quality, route index,
memory init, baseline, and carryover services. Drift checks use the onboarding
drift summary path; closeout quality checks use the broader memory quality gate.

## Invariants And Boundaries

- Memory tool repo IDs must be allowed by MCP settings.
- Drift report artifacts remain temporary coordination artifacts, not durable
  onboarding content.
- Baseline and carryover logic belongs in the memory service modules, not in
  MCP transport wiring.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Memory response models cover drift, quality, route-index, init, baseline, and carryover tools. | [memory.py](agents-remember-md/mcp/src/agents_remember/models/memory.py) |
| Route index generation is owned by the kernel route-index module. | [route_index.py](agents-remember-md/mcp/src/agents_remember/kernel/route_index.py) |

## Update History

- 2026-05-28T19:52+02:00: Created when memory/onboarding MCP controllers moved into their own domain module.
