# mcp/src/agents_remember/models/orchestration.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/models/orchestration.py`      |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-04T12:31+02:00                                 |
| lastVerifiedCommitHash |                                                        `6b940141fc319f1d2d18b2c94fd9e9a213d43141`|
| lastVerifiedCommitDate |                                                        2026-07-04T12:52:03+02:00|
| governingOverview      | `overview.md`                                          |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The payload builder returns this response through `_tool_payload`. | [orchestration.py](agents-remember/mcp/src/agents_remember/mcp/tools/orchestration.py) |
| The response registry maps the public tool to this model. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |

## Update History

- 2026-07-04T12:31+02:00 - L3: created the orchestration nudge response model card. Verification metadata pinned until closeout stamps the L3 commit.
