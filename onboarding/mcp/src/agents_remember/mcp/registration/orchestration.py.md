# mcp/src/agents_remember/mcp/registration/orchestration.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/mcp/registration/orchestration.py`       |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `b7f09a4dc992a7a450a0a37e704475e66df79746`                        |
| lastVerifiedCommitDate | 2026-08-09T21:31:32+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_orchestration_tools(server, config)` declares the cross-agent messaging surface by
delegating, in the original publication order, to `_register_operator_inbox_tools` and
`_register_manager_nudge_tools`: the four operator-inbox tools (`operator_inbox_post`,
`operator_inbox_poll`, `operator_inbox_consume`, `operator_inbox_supersede` since
260713-TES-L4) followed by `orchestration_nudge_manager`.

## Code Commentary

### Logic

The two private registrars are structural groups only. The public registrar calls inbox first and
manager nudge second, preserving FastMCP's advertised order while keeping every registrar below
the repository's hard 100-line function limit; every published tool signature and forwarding body
is unchanged.

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

`operator_inbox_poll` forwards the mailbox keys plus `include_terminal` (N11 terminal
inspectability). Consuming is explicit and separate — polling never consumes — and repeated
`operator_inbox_consume(entry_id)` calls are idempotent against the append-only inbox log
(attribution-only since N16). `operator_inbox_supersede(entry_id, reason, superseded_by="model")`
declares the explicit-supersession tool (R11): an overtaken command becomes terminal
`superseded` without a false ack and is skipped by every retry/evaluation path.

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
| Fixed model attribution and the target/subject split proved through a live server. | `test_operator_inbox_post_over_mcp_is_always_attributed_to_the_model` | mcp/tests/test_mcp_registration_wiring_tests_2.py:454-465 |

## Update History

- 2026-08-09T21:10+02:00 — Master integration gate repair: split the 116-line public registrar
  into same-module inbox and manager-nudge registrars, with the public registrar delegating in
  the original order. Published signatures, names, attribution, and forwarding are unchanged;
  the hard function-length and registrar-shape rails now pass. Verification metadata stays
  pinned until closeout.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `operator_inbox_supersede`
  declaration (R11), the `include_terminal` poll parameter (N11), and the attribution-only
  consume wording (N16). Verification metadata pinned until closeout stamps the 260713-TES-L4
  commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 4 citation rows with
  builder, model-record and wiring-test anchors (operator_inbox.py, orchestration.py,
  operator_inbox_records.py, test_mcp_registration_wiring.py). Zero findings remain.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The four messaging
  declarations moved out of `server.py`; post now packs `InboxAddress`/`InboxMessage`/`InboxPoster`/
  `HostedDelivery` and the nudge packs `NudgeTarget`/`NudgeSubject`, with model/cli attribution still
  fixed in the declaration. Verification metadata pinned to the pre-change commit until closeout
  stamps the L2 code commit.
