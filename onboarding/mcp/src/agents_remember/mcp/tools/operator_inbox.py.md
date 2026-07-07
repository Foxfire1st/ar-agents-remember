# mcp/src/agents_remember/mcp/tools/operator_inbox.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/tools/operator_inbox.py`        |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-04T12:31+02:00                                       |
| lastVerifiedCommitHash |                                                              `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`|
| lastVerifiedCommitDate |                                                              2026-07-07T05:26:14+02:00|
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

`operator_inbox_poll_payload(...)` lists pending entries for a lifecycle, agent,
recipient role, or combined mailbox key, serializes each record with the `schema`
alias, and returns `entryCount` plus the entry list.
`operator_inbox_consume_payload(...)` marks
one entry consumed through the store, reports whether this call consumed it now
or observed an already-consumed entry, then deletes the inbox row because the
agent has received the throwaway response.

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

- 2026-07-04T12:31+02:00 - L3: generalized posting/polling for agent roles and
  message kinds, added optional hosted-session delivery through
  `serving.inbox_delivery`, and returned delivery metadata. Verification metadata
  pinned until closeout stamps the L3 commit.
- 2026-06-25T13:10+02:00 — Task 23/24: post opportunistically compacts expired inbox rows and consume deletes the entry after returning the consumed response.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: clarified that `serving.app` now calls `operator_inbox_post_payload` with developer/dashboard attribution when Gate Respond has no hosted session to inject into. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: post, poll, and consume payload builders for the external-chat operator inbox. Verification metadata pinned until closeout stamps the task-10 code commit.
