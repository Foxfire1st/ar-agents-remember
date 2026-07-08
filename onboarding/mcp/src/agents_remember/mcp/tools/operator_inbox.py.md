# mcp/src/agents_remember/mcp/tools/operator_inbox.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/tools/operator_inbox.py`        |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-08T14:35+02:00 |
| lastVerifiedCommitHash |                                                              `45708bbddf1ddb8a2045faa9fad88fe72603b674`|
| lastVerifiedCommitDate |                                                              2026-07-08T05:51:44+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[overview.md](overview.md)

## Purpose

Payload builders for the `operator_inbox_*` MCP tools that post, poll, consume,
and optionally push durable operator or agent-to-agent messages.

## Code Commentary

### Logic

`_store(config)` roots `OperatorInboxStore` under `observer_root(config)`.
`operator_inbox_post_payload(...)` mints a ULID and timestamp, creates an
`OperatorInboxEntry`, appends it, and returns a strict `operator_inbox_post`
payload with metadata and delivery fields. The trusted caller supplies
`created_by` / `created_via`; the public MCP server fixes those values for its
own route. When catalog/host/paster seams are supplied and
`deliver_to_hosted=True`, it attempts immediate hosted-session push through
`serving.inbox_delivery`.

Since 260707-HFX2-L1: before creating the entry, `operator_inbox_post_payload` resolves (or reuses
the caller-supplied) `TerminalCatalog` and calls `signal_routing.derive_signal_owner(catalog,
sender_agent_id=, message_kind=)` (R4) to derive the routed owner address, stamped onto the entry's
`owner_role`/`owner_agent_id`/`owner_lifecycle_id` fields and echoed on the response. Right after
the store append + compaction, in the SAME call, it writes an `ack-by` expectation row
(`expectation_rows.write_expectation_row`, R2) keyed to the new entry id, with its SLA read from
`orchestration.expectations.defaults` (falling back to `DEFAULT_EXPECTATION_SLA_SECONDS` when
`config` carries no coordination root) — so the deadline is never a forgettable follow-up step.

`operator_inbox_poll_payload(...)` lists pending entries for a lifecycle, agent,
recipient role, or combined mailbox key, serializes each record with the `schema`
alias, and returns `entryCount` plus the entry list.
`operator_inbox_consume_payload(...)` marks
one entry consumed through the store, reports whether this call consumed it now
or observed an already-consumed entry, then deletes the inbox row because the
agent has received the throwaway response. Since 260707-HFX2-L1 (R1/R2): when this call is the one
that actually consumed the entry (`consumed_now`), it looks up that entry's pending `ack-by`
expectation row (`ExpectationRowStore.find_by_source`) and marks it `met` — consume=ack is the
ONLY terminal delivery outcome, so this is the one place the ack-by deadline is fulfilled.

### Conventions

The builders stay config-rooted and transport-thin like `gates.py`: persistence
lives in `controlplane/`, response validation happens through `_tool_payload`,
and attribution is explicit rather than inferred.

### Invariants And Boundaries

- Public MCP registration must not let a model claim developer/dashboard
  attribution; `server.py` fixes model/cli for MCP calls.
- The dashboard serving endpoint calls the post payload builder directly with trusted
  developer/dashboard attribution when the task-11 hosted-session route has no chat to inject into.
- Polling requires at least one mailbox key because an unaddressed read would
  not represent an addressable agent inbox.
- Consumed inbox rows are not durable task records; the payload is returned to
  the caller, then the row is physically deleted.
- Hosted push delivery is opportunistic; the durable row remains pollable unless
  the consumer explicitly consumes it.

### Todos

None.

## Docs References

The observable-lifecycle design describes pull-based return channels over
durable gate state; these builders expose the active pull mailbox for chats that
cannot receive direct session injection.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Passive/active pull and gate-wait are the return-channel layers available when push cannot be guaranteed. | L251-L266 | [observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tool module roots the inbox store under `observer_root(config)` and serializes entries with aliases. | L23-L29 | [operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| Post, poll, and consume payloads append/list/acknowledge inbox entries and return through `_tool_payload`. | L31-L111 | [operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| The MCP server fixes public-route attribution to model/cli. | L932-L977 | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The dashboard serving endpoint fixes trusted developer/dashboard attribution for no-hosted-session responses. | L358-L376 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `operator_inbox_post_payload` now derives R4 routing (`signal_routing.derive_signal_owner`) and writes an atomic R2 `ack-by` expectation row (`expectation_rows.write_expectation_row`) in the SAME call; `operator_inbox_consume_payload` marks that row `met` on ack (consume=ack is the only terminal outcome, R1). Response payload gained `ownerRole`/`ownerAgentId`/`ownerLifecycleId`. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-04T12:31+02:00 - L3: generalized posting/polling for agent roles and
  message kinds, added optional hosted-session delivery through
  `serving.inbox_delivery`, and returned delivery metadata. Verification metadata
  pinned until closeout stamps the L3 commit.
- 2026-06-25T13:10+02:00 — Task 23/24: post opportunistically compacts expired inbox rows and consume deletes the entry after returning the consumed response.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: clarified that `serving.app` now calls `operator_inbox_post_payload` with developer/dashboard attribution when Gate Respond has no hosted session to inject into. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: post, poll, and consume payload builders for the external-chat operator inbox. Verification metadata pinned until closeout stamps the task-10 code commit.
