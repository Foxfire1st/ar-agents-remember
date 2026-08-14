# mcp/src/agents_remember/mcp/tools/orchestration.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/mcp/tools/orchestration.py`      |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-07-31T15:31+02:00                                    |
| lastVerifiedCommitHash |                                                           `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |                                                           2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[overview.md](overview.md)

## Purpose

Payload builder for the public `orchestration_nudge_manager` tool, which records
an L2 orchestration nudge and pushes the nudge text to a manager through the
generalized operator inbox.

## Code Commentary

### Logic

`orchestration_nudge_manager_payload(config, *, reason, target: NudgeTarget, subject: NudgeSubject,
rate_limit_seconds=900)`.

Two local frozen dataclasses (260731-EFA-L2) keep two different agents apart:

- `NudgeTarget(agent_id, lifecycle_id)` — the **manager the nudge is delivered to**. At least one
  must be present; a nudge with no addressee has no mailbox to land in, and the builder raises
  `ValueError` before any log or inbox write.
- `NudgeSubject(subject, agent_id, lifecycle_id, artifact_path)` — **what the nudge is about**: the
  subject line naming the stalled work, the seat whose silence or missing turn report triggered it,
  and the artifact that evidences it.

The builder formats a reason-specific nudge message from `subject.subject` / `subject.artifact_path`,
records an `OrchestrationNudgeRecord` under the observer root with rate limiting (target ids on
`targetAgentId`/`targetLifecycleId`, subject ids on `subjectAgentId`/`subjectLifecycleId`), logs an
`orchestration.nudge` observer event, and, when not rate-limited, calls
`operator_inbox_post_payload(...)` with an `InboxAddress` carrying `recipient_role="manager"`, an
`InboxMessage` with `message_kind="nudge"`, and an `InboxPoster(created_by="system",
created_via="cli", sender_role="system")`. The response reports the nudge id, nudge state, queued
inbox entry id, and delivery fields when a hosted manager session receives the push.

### Conventions

This builder stays transport-thin: nudge policy lives in `controlplane/`, inbox
posting lives in `mcp/tools/operator_inbox.py`, and `_tool_payload` owns response
validation.

### Invariants And Boundaries

- A nudge without a manager address is rejected before any log or inbox write.
- Keep `NudgeTarget` and `NudgeSubject` distinct: collapsing them would nudge the wrong mailbox.
- Rate-limited nudges are observable events but do not enqueue another stdin push.
- The manager push uses the same durable inbox substrate as other agent-to-agent
  messages, so missed hosted delivery can still be polled.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Nudge record and rate-limit policy live in controlplane. | `OrchestrationNudgeStore` | mcp/src/agents_remember/controlplane/orchestration_nudges.py:41-125 |
| Agent-to-agent message enqueue and hosted-session push live in the operator inbox builder. | `operator_inbox_post_payload` | mcp/src/agents_remember/mcp/tools/operator_inbox.py:19-36 |
| Response validation uses the public orchestration response model. | `OrchestrationNudgeManagerResponse` | mcp/src/agents_remember/models/orchestration.py:12-22 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 3 citation claims; scoped recheck clean (0 findings).

- 2026-07-31T15:31+02:00 — 260731-EFA-L2: the seven flat keyword arguments became `target:
  NudgeTarget` + `subject: NudgeSubject`, and the inbox post now travels as `InboxAddress` /
  `InboxMessage` / `InboxPoster`. Rate limiting, event logging and the response shape are unchanged.
  Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-04T12:31+02:00 - L3: created the orchestration nudge tool card. Verification metadata pinned until closeout stamps the L3 commit.
