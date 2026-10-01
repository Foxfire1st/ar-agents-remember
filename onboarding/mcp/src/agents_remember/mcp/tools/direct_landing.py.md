# mcp/src/agents_remember/mcp/tools/direct_landing.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- The payload builder `direct_landing_payload` wraps the application result with the standard envelope. [1]
- The standard `_tool_payload` envelope converts one application result into its protocol-ready response. [2]
- Registered as a public tool. [3]
- The registration declaration. [4]

### Cross-Repo References

No meaningful cross-repository reference applies.
