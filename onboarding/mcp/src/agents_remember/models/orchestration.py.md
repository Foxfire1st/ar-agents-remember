# mcp/src/agents_remember/models/orchestration.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Strict public response model for the `orchestration_nudge_manager` MCP tool.

## Code Commentary

### Logic

`OrchestrationNudgeManagerResponse` extends `ToolResponse` with the nudge
`status`, `reason`, `nudgeId`, formatted `message`, and optional inbox delivery
fields (`entryId`, `deliveryState`, `deliveredToSession`) for non-rate-limited
push attempts.

### Conventions

The model follows the strict AR-owned response-contract pattern. Optional fields
default to `None` so `_tool_payload(... exclude_none=True)` omits them when a
rate-limited nudge does not enqueue an inbox entry.

### Invariants And Boundaries

- This is a response contract only; request validation is in `server.py` and the
  payload builder.
- Register the tool response in `models/tool_registry.py` whenever this model is
  exposed publicly.

## Evidence

### Repo-Internal References

- The `orchestration_nudge_manager_payload` builder returns this response through `_tool_payload`. [1]
- The response registry maps the administrative orchestration nudge operation to this model. [2]
