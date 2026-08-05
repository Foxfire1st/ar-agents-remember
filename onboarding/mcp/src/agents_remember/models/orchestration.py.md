# mcp/src/agents_remember/models/orchestration.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/models/orchestration.py`      |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-04T12:31+02:00                                 |
| lastVerifiedCommitHash |                                                        `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |                                                        2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builder returns this response through `_tool_payload`. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/orchestration.py:27-28 |
| The response registry maps the public tool to this model. | `OrchestrationNudgeManagerResponse`; "orchestration_nudge_manager" | mcp/src/agents_remember/models/tool_registry.py:178-178 |

## Update History

- 2026-08-03T10:20+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 4 assigned citation findings (2 missing anchors and 2 malformed sources); final scoped check is clean.

- 2026-07-04T12:31+02:00 - L3: created the orchestration nudge response model card. Verification metadata pinned until closeout stamps the L3 commit.
