# mcp/src/agents_remember/mcp/tools/operator_inbox.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Transport-thin response adapters for the `operator_inbox_*` MCP tools. They delegate post, poll, and
consume behavior to the application layer, then validate the returned dictionaries through
`_tool_payload`.

## Code Commentary

### 260707-HFX2-L20 Durable Consume

`operator_inbox_consume_payload` returns the same response contract but no longer physically deletes
the inbox id after appending its consumed snapshot. Retaining that terminal fact until normal
compaction prevents a concurrent in-flight delivery from recreating a pending current row.

### 260707-HFX2-L13 Completion Wake Routing

Completion-wake routing is no longer implemented in this MCP adapter. The application post command
delegates to `serving.operator_inbox_posts`, where `_post_address` derives the current owner and leaf
anchor, `_persist_post` creates the durable row and ack-by expectation, and `_deliver_post` attempts
optional hosted delivery. For `turn-report` and `master-handover`, that serving owner replaces stale
caller-supplied addressing with the resolved current owner; ordinary peer addressing remains explicit.

### Current Signatures (260731-EFA-L2)

```python
operator_inbox_post_payload(config, *, address: InboxAddress, message: InboxMessage,
                            poster: InboxPoster, delivery: HostedDelivery = HOSTED_DELIVERY)
operator_inbox_poll_payload(config, *, lifecycle_id, agent_id, recipient_role=None)
operator_inbox_consume_payload(config, *, entry_id, consumed_by, consumed_via, ...)
```

The adapter accepts the same four concepts: **where** it goes (`InboxAddress` —
lifecycle/agent/recipient role), **what** it says (`InboxMessage` — ask, response, message kind,
gate id, artifact path), **who** sent it (`InboxPoster` — `created_by`/`created_via` plus the
sender's agent id and role), and **how** it is pushed (`HostedDelivery` from `dispatch_brief.py`,
bundling `enabled` with the catalog/host/paster/readiness/gate seams; `HOSTED_DELIVERY` is the real
default). The application and serving owners receive those bundles unchanged.

### Logic

Each public function delegates once to its application counterpart and passes that result through
`_tool_payload`. The application layer roots `OperatorInboxStore` under `observer_root(config)`,
composes post requests, lists pending mailbox entries, and consumes/acknowledges entries. The serving
post owner derives completion routing, persists entries and ack-by expectations, and attempts hosted
delivery using the configured supervisor redelivery floor. Consume remains the operation that marks
the matching pending ack-by expectation met; the consumed snapshot is retained until compaction.

The trusted caller still supplies `poster.created_by` / `poster.created_via`.
`mcp/registration/orchestration.py` fixes those to `model` / `cli` for the public MCP route, so an
agent cannot post as the developer. The dashboard path supplies trusted developer/dashboard
attribution directly to the serving post owner.

### Conventions

The MCP functions stay transport-thin: application and serving modules own composition, persistence,
routing, delivery, and acknowledgement; this file owns response adaptation through `_tool_payload`.
Attribution is explicit rather than inferred.

### Invariants And Boundaries

- Public MCP registration must not let a model claim developer/dashboard
  attribution; `mcp/registration/orchestration.py` fixes model/cli on the `InboxPoster` it builds
  for every MCP call.
- The dashboard serving endpoint calls `serving.operator_inbox_posts.post_operator_inbox_entry`
  directly with trusted developer/dashboard attribution; it does not route through this MCP adapter.
- Polling requires at least one mailbox key because an unaddressed read would
  not represent an addressable agent inbox.
- A consumed row keeps its terminal snapshot until normal compaction removes it (260707-HFX2-L20);
  it is not deleted at consume time, because a concurrent in-flight delivery could otherwise
  recreate a pending current row.
- Hosted push delivery is opportunistic; the durable row remains pollable unless
  the consumer explicitly consumes it, and its retry schedule is floor-aware when a runtime config is
  present.

### Todos

None.

## Evidence

### Docs References

The observable-lifecycle design describes pull-based return channels over
durable gate state; these builders expose the active pull mailbox for chats that
cannot receive direct session injection.

- Passive/active pull and gate-wait are the return-channel layers available when push cannot be guaranteed. [1]

### Repo-Internal References

- The MCP module delegates post, registered-post, poll, and consume commands to the application layer and validates each response through `_tool_payload`. [2]
- The application layer roots the store, composes post requests, polls pending entries, and consumes entries while fulfilling acknowledgements. [3]
- The serving post owner derives routing, persists the row and ack-by expectation, and performs optional hosted delivery. [4]
- Hosted delivery reads the supervisor redelivery floor and passes it into the delivery attempt. [5]
- The tool declarations fix public-route attribution to model/cli. [6]
- The dashboard route delegates to `_operator_inbox_response`, which calls the serving post owner directly and fixes trusted developer/dashboard attribution. [7]

### Cross-Repo References

No meaningful cross-repo references found.

None.

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.
