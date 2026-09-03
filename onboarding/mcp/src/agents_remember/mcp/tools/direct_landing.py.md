# mcp/src/agents_remember/mcp/tools/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/tools/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
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
`application.lifecycle.direct_landing.direct_landing_tool(config, request)` and wraps the result with
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
| The payload builder `direct_landing_payload` wraps the application result with the standard envelope. | `direct_landing_payload` | mcp/src/agents_remember/mcp/tools/direct_landing.py:16-20 |
| The standard `_tool_payload` envelope converts one application result into its protocol-ready response. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:76-78 |
| Registered as a public tool. | `PUBLIC_TOOLS` | mcp/src/agents_remember/mcp/tools/base.py:10-70 |
| The registration declaration. | `_register_direct_landing_tools` | mcp/src/agents_remember/mcp/registration/closeout.py:33-79 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR provenance-debt repair: split the envelope row so `direct_landing_payload` cites only its definition in direct_landing.py:16-20 and `_tool_payload` cites only its definition in base.py:76-78. `_tool_payload` previously resolved 3 times because the row cited both files and the name occurs twice in direct_landing.py (import line 13, call line 20) plus once as the base.py definition; each claim now maps to exactly one definition and verifies uniquely.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed the application adapter to its canonical `application.lifecycle.direct_landing` import path; this payload builder's behavior is unchanged.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation (L16-R8):
  the payload builder registered through the closeout registration group. Verified at code commit
  a9d50e08.
