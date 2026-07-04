# mcp/src/agents_remember/mcp/tools/orchestration.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/mcp/tools/orchestration.py`      |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-07-04T12:31+02:00                                    |
| lastVerifiedCommitHash |                                                           `6b940141fc319f1d2d18b2c94fd9e9a213d43141`|
| lastVerifiedCommitDate |                                                           2026-07-04T12:52:03+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[overview.md](overview.md)

## Purpose

Payload builder for the public `orchestration_nudge_manager` tool, which records
an L2 orchestration nudge and pushes the nudge text to a manager through the
generalized operator inbox.

## Code Commentary

### Logic

`orchestration_nudge_manager_payload(...)` requires either a manager agent id or
manager lifecycle id before writing. It formats a reason-specific nudge message,
records an `OrchestrationNudgeRecord` under the observer root with rate limiting,
logs an `orchestration.nudge` observer event, and, when not rate-limited, calls
`operator_inbox_post_payload(...)` with `sender_role="system"`,
`recipient_role="manager"`, and `message_kind="nudge"`. The response reports the
nudge id, nudge state, queued inbox entry id, and delivery fields when a hosted
manager session receives the push.

### Conventions

This builder stays transport-thin: nudge policy lives in `controlplane/`, inbox
posting lives in `mcp/tools/operator_inbox.py`, and `_tool_payload` owns response
validation.

### Invariants And Boundaries

- A nudge without a manager address is rejected before any log or inbox write.
- Rate-limited nudges are observable events but do not enqueue another stdin push.
- The manager push uses the same durable inbox substrate as other agent-to-agent
  messages, so missed hosted delivery can still be polled.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Nudge record and rate-limit policy live in controlplane. | [orchestration_nudges.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_nudges.py) |
| Agent-to-agent message enqueue and hosted-session push live in the operator inbox builder. | [operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| Response validation uses the public orchestration response model. | [orchestration.py](agents-remember/mcp/src/agents_remember/models/orchestration.py) |

## Update History

- 2026-07-04T12:31+02:00 - L3: created the orchestration nudge tool card. Verification metadata pinned until closeout stamps the L3 commit.
