# mcp/src/agents_remember/mcp/tools/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/tools/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tools overview](overview.md)

## Purpose

Payload builder for the direct landing operation (L16-R8): wraps the application boundary result
in the standard `_tool_payload` envelope so the registered `direct_landing` tool speaks the same
wire shape as every other public tool.

## Code Commentary

### Logic

`direct_landing_payload(config, request)` calls
`application.direct_landing.direct_landing_tool(config, request)` and wraps the result with
`_tool_payload("direct_landing", ...)`.

### Conventions

Follows the standard tools/ directory pattern: one payload builder per tool, thin, no logic.

### Invariants And Boundaries

- The `direct_landing` name is registered in `PUBLIC_TOOLS` and
  `TOOL_RESPONSE_MODELS` (`DirectLandingResponse`).
- This module builds payloads only; registration lives in `mcp/registration/closeout.py`.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload envelope wrapping the application result. | `direct_landing_payload`; `_tool_payload` | mcp/src/agents_remember/mcp/tools/direct_landing.py:16-20; mcp/src/agents_remember/mcp/tools/base.py:74-76 |
| Registered as a public tool. | `PUBLIC_TOOLS` | mcp/src/agents_remember/mcp/tools/base.py:10-70 |
| The registration declaration. | `_register_direct_landing_tool` | mcp/src/agents_remember/mcp/registration/closeout.py:33-79 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation (L16-R8):
  the payload builder registered through the closeout registration group. Verified at code commit
  a9d50e08.
