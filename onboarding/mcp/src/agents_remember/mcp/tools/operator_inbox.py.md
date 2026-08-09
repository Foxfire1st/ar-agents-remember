# mcp/src/agents_remember/mcp/tools/operator_inbox.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/tools/operator_inbox.py`        |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`|
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[overview.md](overview.md)

## Purpose

Transport-thin response adapters for the `operator_inbox_*` MCP tools. They delegate post, poll,
consume, and supersede behavior to the application layer, then validate the returned dictionaries through
`_tool_payload`.

## Code Commentary

### 260707-HFX2-L20 Durable Consume

`operator_inbox_consume_payload` returns the same response contract but no longer physically deletes
the inbox id. Since 260713-TES-L4 the consume adapter is attribution-only (N16): the underlying
store stamps `consumedAt`/`consumedBy`/`consumedVia` and leaves `state` untouched — nothing
mechanical hangs off it.

### 260713-TES-L4 Terminal Inspectability And Supersession Adapters

`operator_inbox_poll_payload` gained `include_terminal: bool = False` and forwards it to the
application poll (N11 terminal markers inside their retention window).
`operator_inbox_supersede_payload(config, *, entry_id, reason, superseded_by="model")` is the
new adapter for the explicit-supersession tool (R11); it delegates to
`operator_inbox_supersede_tool` (which calls `mark_superseded`) and validates the response.

### 260707-HFX2-L13 Completion Wake Routing

Completion-wake routing is no longer implemented in this MCP adapter. The application post command
delegates to `serving.operator_inbox_posts`, where `_post_address` derives the current owner and leaf
anchor, `_persist_post` creates the durable row (and, since 260713-TES-L4, NO ack-by expectation
row — N16), and `_deliver_post` attempts optional hosted delivery. Since L4 every owner-addressed
post replaces stale caller-supplied addressing with the resolved current owner (N14);
dispatch-brief stays exact-pinned and ordinary peer addressing remains explicit.

### Current Signatures (260731-EFA-L2)

```python
operator_inbox_post_payload(config, *, address: InboxAddress, message: InboxMessage,
                            poster: InboxPoster, delivery: HostedDelivery = HOSTED_DELIVERY)
operator_inbox_poll_payload(config, *, lifecycle_id, agent_id, recipient_role=None, include_terminal=False)
operator_inbox_consume_payload(config, *, entry_id, consumed_by, consumed_via, ...)
operator_inbox_supersede_payload(config, *, entry_id, reason, superseded_by="model")
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
composes post requests, lists pending (or pending+terminal, N11) mailbox entries, and consumes/
supersedes entries. The serving post owner derives completion routing, persists entries (no
ack-by expectation rows since N16), and attempts hosted delivery using the configured
agent-notifier redelivery floor. Consume is an attribution marker only — it never meets an
expectation and never changes row state; supersede is the explicit terminal for an overtaken
command (R11).

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
- A consume-marked row stays pending and redeliverable (N16) — the attribution marker never
  changes state; a concurrent in-flight landing still wins the fold.
- Hosted push delivery is opportunistic; the durable row remains pollable unless
  the consumer explicitly consumes it, and its retry schedule is floor-aware when a runtime config is
  present.

### Todos

None.

## Docs References

The observable-lifecycle design describes pull-based return channels over
durable gate state; these builders expose the active pull mailbox for chats that
cannot receive direct session injection.

| Finding | Anchor | Source |
| --- | --- | --- |
| Passive/active pull and gate-wait are the return-channel layers available when push cannot be guaranteed. | `# Observable Lifecycle, Events, and Gates — the Agents Remember 3.0 Design` | docs/design/observable-lifecycle.md:1-402 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The MCP module delegates post, registered-post, poll, and consume commands to the application layer and validates each response through `_tool_payload`. | `operator_inbox_post_payload`; `registered_operator_inbox_post_payload`; `operator_inbox_poll_payload`; `operator_inbox_consume_payload` | mcp/src/agents_remember/mcp/tools/operator_inbox.py:19-36; mcp/src/agents_remember/mcp/tools/operator_inbox.py:39-47; mcp/src/agents_remember/mcp/tools/operator_inbox.py:50-65; mcp/src/agents_remember/mcp/tools/operator_inbox.py:68-83 |
| The application layer roots the store, composes post requests, polls pending entries, and consumes entries while fulfilling acknowledgements. | `_store`; `operator_inbox_post_tool`; `operator_inbox_poll_tool`; `operator_inbox_consume_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:37-38; mcp/src/agents_remember/application/operator_inbox_tools.py:45-65; mcp/src/agents_remember/application/operator_inbox_tools.py:98-123; mcp/src/agents_remember/application/operator_inbox_tools.py:126-150 |
| The serving post owner derives routing (N14 re-resolution for every owner-addressed post), persists the row (no ack-by expectation since N16), and performs optional hosted delivery. | `_post_address`; `_persist_post`; `_deliver_post`; `post_operator_inbox_entry` | mcp/src/agents_remember/serving/operator_inbox_posts.py:99-129; mcp/src/agents_remember/serving/operator_inbox_posts.py:180-191; mcp/src/agents_remember/serving/operator_inbox_posts.py:192-215; mcp/src/agents_remember/serving/operator_inbox_posts.py:216-288 |
| Hosted delivery reads the agent-notifier redelivery floor and passes it into the delivery attempt. | `_redelivery_floor_seconds`; `_deliver_post` | mcp/src/agents_remember/serving/operator_inbox_posts.py:63-68; mcp/src/agents_remember/serving/operator_inbox_posts.py:192-213 |
| The tool declarations fix public-route attribution to model/cli. | `register_orchestration_tools` | mcp/src/agents_remember/mcp/registration/orchestration.py:26-116 |
| The dashboard route delegates to `_operator_inbox_response`, which calls the serving post owner directly and fixes trusted developer/dashboard attribution. | `api_operator_inbox`; "def _operator_inbox_response(" | mcp/src/agents_remember/serving/_app_routes.py:334-334; mcp/src/agents_remember/serving/_app_routes.py:403-409 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `include_terminal` poll adapter
  (N11), the attribution-only consume wording (N16 — no expectation fulfillment, state
  unchanged), the new `operator_inbox_supersede_payload` (R11), and the N14/N16 post-owner
  wording (owner-addressed re-resolution, no ack-by rows, dispatch-brief exact-pinned).
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: regenerated the assigned route/helper and trusted-attribution whole-claim binding with the locked scoped fixer and inspected both extents; no approved semantic claim changes.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: made the route-to-helper ownership explicit, selected both parser-visible functions, and returned the whole trusted-attribution binding to provisional fixer input.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: corrected ownership after the architecture split: this file is an MCP response adapter, application owns commands/store access, serving owns post routing/persistence/delivery, and the dashboard calls the serving owner directly; new bindings remain provisional.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: `operator_inbox_post_payload` took
  `address`/`message`/`poster`/`delivery` parameter objects (`InboxAddress`, `InboxMessage`,
  `InboxPoster`, `HostedDelivery`), and the internal `_post_address`/`_persist_post` helpers were
  threaded with `InboxAddress` instead of tuples; expectation rows are written as `Expectation` +
  `ExpectationSubject` values. Corrected two stale claims while here: attribution is fixed in
  `mcp/registration/orchestration.py`, not `server.py` (registration left that file entirely), and
  the Invariants bullet still said a consumed row is physically deleted — 260707-HFX2-L20 retained
  it until compaction, which the rest of this sidecar already recorded. Verification metadata
  pinned until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20: retained the consumed snapshot after public consume;
  response shape is unchanged and compaction remains the cleanup owner.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: made completion/artifact posts target and wake
  the current manager in the same call, and persisted leaf/subject provenance for later supervisor
  handling. Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: threaded the configured supervisor redelivery floor into
  immediate hosted inbox delivery so first-send scheduling uses the same 900-second floor as later
  redelivery. Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `operator_inbox_post_payload` now derives R4 routing (`signal_routing.derive_signal_owner`) and writes an atomic R2 `ack-by` expectation row (`expectation_rows.write_expectation_row`) in the SAME call; `operator_inbox_consume_payload` marks that row `met` on ack (consume=ack is the only terminal outcome, R1). Response payload gained `ownerRole`/`ownerAgentId`/`ownerLifecycleId`. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-04T12:31+02:00 - L3: generalized posting/polling for agent roles and
  message kinds, added optional hosted-session delivery through
  `serving.inbox_delivery`, and returned delivery metadata. Verification metadata
  pinned until closeout stamps the L3 commit.
- 2026-06-25T13:10+02:00 — Task 23/24 historical behavior: post opportunistically compacted expired
  rows and consume deleted its entry; HFX2-L20 supersedes the latter behavior.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: clarified that `serving.app` now calls `operator_inbox_post_payload` with developer/dashboard attribution when Gate Respond has no hosted session to inject into. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: post, poll, and consume payload builders for the external-chat operator inbox. Verification metadata pinned until closeout stamps the task-10 code commit.
