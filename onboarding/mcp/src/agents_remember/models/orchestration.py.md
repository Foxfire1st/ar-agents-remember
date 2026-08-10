# mcp/src/agents_remember/models/orchestration.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/models/orchestration.py`      |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-04T12:31+02:00                                 |
| lastVerifiedCommitHash |                                                        `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |                                                        2026-08-10T12:28:42+02:00|
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
| The `orchestration_nudge_manager_payload` builder returns this response through `_tool_payload`. | "def orchestration_nudge_manager_payload(" | mcp/src/agents_remember/mcp/tools/orchestration.py:19-36 |
| The response registry maps the public tool to this model. | "orchestration_nudge_manager": OrchestrationNudgeManagerResponse | mcp/src/agents_remember/models/tool_registry.py:180-180 |

## Update History

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-03T10:20+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 4 assigned citation findings (2 missing anchors and 2 malformed sources); final scoped check is clean.

- 2026-07-04T12:31+02:00 - L3: created the orchestration nudge response model card. Verification metadata pinned until closeout stamps the L3 commit.
