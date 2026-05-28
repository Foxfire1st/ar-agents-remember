# mcp/src/agents_remember/controllers/coordination_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/coordination_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`coordination_tools.py` exposes the `resolve_context` MCP controller.

## Code Commentary

The controller validates the requested repo ID against MCP settings, normalizes
optional contract/worktree paths inside the coordination root, narrows topology
to supported values, calls `resolve_coordination_context()`, and serializes the
result with `context_to_dict()`.

## Invariants And Boundaries

- MCP settings are the authority for allowed repos and workspace roots.
- Caller-provided coordination paths must remain under the configured
  coordination root.
- Topology values should stay explicit rather than free-form strings.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runtime/coordination response models include `ResolveContextResponse`. | [runtime.py](agents-remember-md/mcp/src/agents_remember/models/runtime.py) |
| Coordination context resolver owns the actual context construction. | [coordination_context_resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |

## Update History

- 2026-05-28T19:52+02:00: Created when resolver MCP control moved into its own controller module.
