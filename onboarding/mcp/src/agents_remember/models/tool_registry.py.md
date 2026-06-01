# mcp/src/agents_remember/models/tool_registry.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/tool_registry.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0` |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`tool_registry.py` maps public MCP tool names to their response model classes.

## Code Commentary

`PUBLIC_TOOL_RESPONSE_MODELS` is the enforcement registry consumed by
`mcp.tools._tool_payload()`. It currently covers all public core, runtime,
memory, skill install, provider, worktree, and benchmark tools.

The module docstring fixes a deliberate two-tier response-model convention.
Tools whose response shape is fully AR-owned register a STRICT model
(`StrictResponseModel` / `ResponseModel` / `ToolResponse`, `extra="forbid"`) so
the field set is a drift-proof contract; `context_packet` (`ContextPacketV2`),
`ping`, and `server_info` are the exemplars. Tools that surface provider-native
or raw diagnostic detail (CodeGraphContext, GrepAI, Docker, watcher output)
register a FLEXIBLE model (`FlexibleResponseModel` / `FlexibleToolResponse`,
`extra="allow"`) on purpose: the upstream provider owns that payload, so extra
fields are tolerated rather than rejected. This is tolerated drift, not
un-validated input -- the envelope (`ok`/`operation`/`tokens`) is still typed.
Pick STRICT unless the payload genuinely embeds provider-native detail.

## Invariants And Boundaries

- The registry keys must equal `mcp.tools.PUBLIC_TOOLS`.
- Adding or removing a public tool requires updating this registry and the
  schema coverage tests.
- The registry is response-only; it does not own request validation.
- A FLEXIBLE (`extra="allow"`) entry is a tolerated-drift surface for
  provider-native payloads, not a license to skip validation; the typed
  envelope still applies. AR-owned shapes must register a STRICT model.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Payload builders validate through this registry. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Tests assert exact coverage between `PUBLIC_TOOLS` and this registry. | [test_models.py](agents-remember-md/mcp/tests/test_models.py) |

## Update History

- 2026-06-01T20:45+02:00 — Registered `worktree_abandon` → `WorktreeAbandonResponse` in `PUBLIC_TOOL_RESPONSE_MODELS`.
- 2026-05-31T12:30+02:00 — Documented the deliberate STRICT vs FLEXIBLE response-model two-tier convention now fixed in the module docstring (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created for the public tool response model coverage registry.
