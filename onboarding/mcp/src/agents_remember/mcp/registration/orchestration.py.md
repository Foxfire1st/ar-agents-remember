# mcp/src/agents_remember/mcp/registration/orchestration.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/mcp/registration/orchestration.py`       |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated            | 2026-07-31T15:31+02:00                                            |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                        |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_orchestration_tools(server, config)` declares the cross-agent messaging surface: the three
operator-inbox tools (`operator_inbox_post`, `operator_inbox_poll`, `operator_inbox_consume`) and
`orchestration_nudge_manager`.

## Code Commentary

### Logic

`operator_inbox_post` splits its arguments four ways:

- `InboxAddress(lifecycle_id, agent_id, recipient_role)` — the mailbox key.
- `InboxMessage(ask, response, message_kind, gate_id, artifact_path)` — the content.
- `InboxPoster(created_by, created_via, sender_agent_id, sender_role)` — who sent it.
- `HostedDelivery(enabled=deliver_to_hosted)` — whether the entry is also pushed into the
  recipient's live hosted session through the terminal paste seam. The durable row stays
  dashboard-visible either way.

**Attribution is fixed in this declaration, not taken from the caller.** `created_by="model"` and
`created_via="cli"` are literals in the body, and `operator_inbox_consume` likewise sends
`consumed_by="model"` / `consumed_via="cli"`. Over MCP this route is always the model's; trusted
dashboard code calls `operator_inbox_post_payload` directly with developer/dashboard attribution.
An agent therefore cannot post or consume as the developer.

`operator_inbox_poll` forwards the three mailbox keys flat. Consuming is explicit and separate —
polling never consumes — and repeated `operator_inbox_consume(entry_id)` calls are idempotent
against the append-only inbox log.

`orchestration_nudge_manager` keeps two different agents apart, which is the point of its packing:
`NudgeTarget(agent_id, lifecycle_id)` is the **manager being nudged**, `NudgeSubject(subject,
agent_id, lifecycle_id, artifact_path)` is the **seat the nudge is about**. Collapsing them would
nudge the wrong mailbox. `reason` is a `NudgeReason` and `rate_limit_seconds` defaults to 900.

### Invariants And Boundaries

- Never accept `created_by` / `consumed_by` from the caller on this surface.
- Keep `NudgeTarget` and `NudgeSubject` distinct.
- Delivery mechanics, rate limiting, expectation rows and owner-routing live in
  `mcp/tools/operator_inbox.py`, `mcp/tools/orchestration.py` and `controlplane/`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three inbox payload builders and the hosted-delivery seam. | `operator_inbox_post_payload` | mcp/src/agents_remember/mcp/tools/operator_inbox.py:19-36; mcp/src/agents_remember/mcp/tools/operator_inbox.py:50-65; mcp/src/agents_remember/mcp/tools/operator_inbox.py:68-83 |
| `NudgeTarget` / `NudgeSubject` and the nudge builder. | `NudgeSubject` | mcp/src/agents_remember/mcp/tools/orchestration.py:7-12; mcp/src/agents_remember/mcp/tools/orchestration.py:19-37 |
| `HostedDelivery` — the delivery bundle the post declaration builds. | `HostedDelivery` | mcp/src/agents_remember/serving/dispatch_brief.py:45-54 |
| `InboxAddress`, `InboxMessage`, `InboxPoster`, `AgentRole`, `InboxMessageKind`. | `AgentRole` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:17-42; mcp/src/agents_remember/controlplane/operator_inbox_records.py:53-61; mcp/src/agents_remember/controlplane/operator_inbox_records.py:101-123 |
| Fixed model attribution and the target/subject split proved through a live server. | `test_operator_inbox_post_over_mcp_is_always_attributed_to_the_model` | mcp/tests/test_mcp_registration_wiring.py:1202-1213; mcp/tests/test_mcp_registration_wiring.py:1271-1297 |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 4 citation rows with
  builder, model-record and wiring-test anchors (operator_inbox.py, orchestration.py,
  operator_inbox_records.py, test_mcp_registration_wiring.py). Zero findings remain.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The four messaging
  declarations moved out of `server.py`; post now packs `InboxAddress`/`InboxMessage`/`InboxPoster`/
  `HostedDelivery` and the nudge packs `NudgeTarget`/`NudgeSubject`, with model/cli attribution still
  fixed in the declaration. Verification metadata pinned to the pre-change commit until closeout
  stamps the L2 code commit.
