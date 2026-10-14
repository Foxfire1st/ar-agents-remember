# mcp/src/agents_remember/mcp/tools/operator_inbox.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Transport-thin response adapters for retained internal `operator_inbox_*` operations. They delegate post, poll, consume, and
supersede behavior to the application layer, then validate the returned dictionaries through
`_tool_payload`.

## Code Commentary

### 260707-HFX2-L20 Durable Consume (terminal semantics superseded by N16)

`operator_inbox_consume_payload` does not physically delete the inbox id. For an unstamped pending
row, the store appends optional `consumedAt`/`consumedBy`/`consumedVia` attribution without changing
its state, retry schedule, or expectations. An already-stamped or non-pending row is returned
unchanged with `consumedNow=False`. Terminal folding protects formal terminal states such as
`landed` and `superseded` from stale pending snapshots; consumption itself is not terminal.

### 260707-HFX2-L13 Completion Wake Routing

Completion-wake routing is no longer implemented in this MCP adapter. The application post command
delegates to `serving.operator_inbox_posts`, where `_post_address` derives the current owner and leaf
anchor, `_persist_post` persists the durable row and starts a briefed-by expectation only for a configured
dispatch target, and `_deliver_post` attempts
optional hosted delivery. For `turn-report` and `master-handover`, that serving owner replaces stale
caller-supplied addressing with the resolved current owner; ordinary peer addressing remains explicit.

### Current Adapter Signatures

```python
operator_inbox_post_payload(config: McpRuntimeConfig, *, address: Any, message: Any,
                            poster: Any, delivery: Any = None) -> dict[str, Any]
registered_operator_inbox_post_payload(config: McpRuntimeConfig,
                                       request: OperatorInboxPostRequest) -> dict[str, Any]
operator_inbox_poll_payload(config: McpRuntimeConfig, *, lifecycle_id: str | None,
                            agent_id: str | None, recipient_role: Any = None,
                            include_terminal: bool = False) -> dict[str, Any]
operator_inbox_consume_payload(config: McpRuntimeConfig, *, entry_id: str,
                               consumed_by: str, consumed_via: Any) -> dict[str, Any]
operator_inbox_supersede_payload(config: McpRuntimeConfig, *, entry_id: str, reason: str,
                                 superseded_by: str = "model") -> dict[str, Any]
```

The direct post adapter annotates its bundles as `Any` and forwards them to the application
boundary, whose typed concepts are `InboxAddress`, `InboxMessage`, `InboxPoster`, and
`HostedDelivery`. The adapter's literal delivery default is `None`; the application resolves
`delivery or HOSTED_DELIVERY`. The retained `registered_operator_inbox_post_payload` helper
passes a composed `OperatorInboxPostRequest` to the application, which constructs the bundles
and overrides delivery `enabled` from `request.deliver_to_hosted`. Serving also resolves delivery
collaborators; these are not unchanged bundles end-to-end. The helper's name does not imply a
current public registrar: the removed orchestration registrar is not registered.

### Logic

Each retained internal adapter delegates once to its application counterpart and passes that result
through `_tool_payload`. The application layer roots `OperatorInboxStore` under `observer_root(config)`,
composes post requests, polls pending rows (plus retained terminal markers when `include_terminal=True`),
and exposes attribution-only consume and explicit supersede operations. The serving post owner derives
completion routing, persists entries, starts briefed-by expectations for configured dispatch targets,
and attempts hosted delivery using the configured redelivery floor. Consume only stores
and returns attribution; it neither fulfills an expectation nor changes state or retry scheduling.
Supersede explicitly transitions a pending row to `superseded`, stamps its terminal reason and author,
and clears its retry schedule without claiming acknowledgement or landing.

The internal adapter accepts caller-supplied attribution. The removed orchestration registrar is
not a current public operator-inbox route. Internal structural messaging sets model/cli attribution
in its own serving call; the dashboard supplies trusted developer/dashboard attribution.

### Conventions

The MCP functions stay transport-thin: application and serving modules own composition, persistence,
routing, delivery, attribution, and terminal transitions; this file owns response adaptation through `_tool_payload`.
Attribution is explicit rather than inferred.

### Invariants And Boundaries

- Retained internal adapters do not themselves fix poster attribution; their trusted callers own it.
  The deleted registrar supplies no current public MCP attribution guarantee.
- The dashboard serving endpoint calls `serving.operator_inbox_posts.post_operator_inbox_entry`
  directly with trusted developer/dashboard attribution; it does not route through this MCP adapter.
- Polling requires at least one mailbox key because an unaddressed read would
  not represent an addressable agent inbox.
- Consume does not physically delete the row or make it terminal. Attribution-stamped pending rows
  remain pending and pollable; default polling excludes terminal states, while `include_terminal=True`
  exposes retained terminal markers. Terminal folding, not consumption, prevents stale pending
  snapshots from reversing formal terminal states.
- Hosted push delivery is opportunistic. Correlated adapter acceptance at a turn boundary can land
  a row; explicit supersession is a separate terminal transition and never a false acknowledgement.
  Consume changes neither terminality nor the floor-aware retry schedule.

### Todos

None.

## Evidence

### Docs References

The observable-lifecycle design describes pull-based return channels over
durable gate state; these retained internal builders support pull-mailbox callers that
cannot receive direct session injection.

- Passive/active pull and gate-wait are the return-channel layers available when push cannot be guaranteed. [1]

### Repo-Internal References

- The retained internal MCP adapters delegate post, registered-post helper, poll, consume, and supersede commands to the application layer and validate each response through `_tool_payload`; the registered-post helper is not a current public registrar. [2]
- The application layer roots the store, composes post requests, polls pending entries with optional terminal inspection, records consume attribution without fulfilling expectations, and explicitly supersedes pending entries without a false acknowledgement. [3]
- The serving post owner derives routing, persists the row, starts briefed-by expectations only for configured dispatch targets, and performs optional hosted delivery. [4]
- Hosted delivery reads the supervisor redelivery floor and passes it into the delivery attempt. [5]

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
