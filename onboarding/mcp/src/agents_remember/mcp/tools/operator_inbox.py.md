# mcp/src/agents_remember/mcp/tools/operator_inbox.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/tools/operator_inbox.py`        |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-31T15:31+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[overview.md](overview.md)

## Purpose

Payload builders for the `operator_inbox_*` MCP tools that post, poll, consume,
and optionally push durable operator or agent-to-agent messages.

## Code Commentary

### 260707-HFX2-L20 Durable Consume

`operator_inbox_consume_payload` returns the same response contract but no longer physically deletes
the inbox id after appending its consumed snapshot. Retaining that terminal fact until normal
compaction prevents a concurrent in-flight delivery from recreating a pending current row.

### 260707-HFX2-L13 Completion Wake Routing

Posting now derives both the current owner and leaf anchor from the sender catalog row. For
`turn-report` and `master-handover`, `_post_address` replaces stale caller-supplied addressing with
the resolved current owner before the durable row, ack-by expectation, and optional hosted delivery
are created. The row records `leafKey` and `subjectAgentId`, so later supervisor passes can re-check
chain progress without trusting the old mailbox. Ordinary peer-message addressing remains explicit
and unchanged.

### Current Signatures (260731-EFA-L2)

```python
operator_inbox_post_payload(config, *, address: InboxAddress, message: InboxMessage,
                            poster: InboxPoster, delivery: HostedDelivery = HOSTED_DELIVERY)
operator_inbox_poll_payload(config, *, lifecycle_id, agent_id, recipient_role=None)
operator_inbox_consume_payload(config, *, entry_id, consumed_by, consumed_via, ...)
```

Post's arguments now arrive as four concepts: **where** it goes (`InboxAddress` —
lifecycle/agent/recipient role), **what** it says (`InboxMessage` — ask, response, message kind,
gate id, artifact path), **who** sent it (`InboxPoster` — `created_by`/`created_via` plus the
sender's agent id and role), and **how** it is pushed (`HostedDelivery` from `dispatch_brief.py`,
bundling `enabled` with the catalog/host/paster/readiness/gate seams; `HOSTED_DELIVERY` is the real
default). The internal helpers were threaded the same way — `_post_address` returns an
`InboxAddress` rather than a three-tuple, and `_persist_post` takes one.

### Logic

`_store(config)` roots `OperatorInboxStore` under `observer_root(config)`.
`operator_inbox_post_payload(...)` mints a ULID and timestamp, creates an
`OperatorInboxEntry`, appends it, and returns a strict `operator_inbox_post`
payload with metadata and delivery fields. The trusted caller supplies
`poster.created_by` / `poster.created_via`; `mcp/registration/orchestration.py` fixes those to
`model` / `cli` for the public MCP route, so an agent cannot post as the developer. When the
delivery seams are available and `delivery.enabled` is true, it attempts immediate hosted-session
push through `serving.inbox_delivery`.

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
or observed an already-consumed entry, then retains the terminal snapshot until compaction. Since
260707-HFX2-L1 (R1/R2): when this call is the one
that actually consumed the entry (`consumed_now`), it looks up that entry's pending `ack-by`
expectation row (`ExpectationRowStore.find_by_source`) and marks it `met` — consume=ack is the
ONLY terminal delivery outcome, so this is the one place the ack-by deadline is fulfilled.

HFX2-L14 adds `_redelivery_floor_seconds(config)`: hosted push attempts made directly by this MCP
tool read `settings.supervisor.redeliver_rate_limit_seconds` and pass it into
`deliver_inbox_entry`, so the first send's durable `nextAttemptAt` is scheduled at the same
floor-aware cadence as supervisor redelivery. A missing/injected test config still passes `None`,
which inherits the store default.

### Conventions

The builders stay config-rooted and transport-thin like `gates.py`: persistence
lives in `controlplane/`, response validation happens through `_tool_payload`,
and attribution is explicit rather than inferred.

### Invariants And Boundaries

- Public MCP registration must not let a model claim developer/dashboard
  attribution; `mcp/registration/orchestration.py` fixes model/cli on the `InboxPoster` it builds
  for every MCP call.
- The dashboard serving endpoint calls the post payload builder directly with trusted
  developer/dashboard attribution when the task-11 hosted-session route has no chat to inject into.
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
| Hosted delivery reads the supervisor redelivery floor from agentic settings and passes it to `deliver_inbox_entry`. | L52-L55; L124-L133 | [operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| The tool declarations fix public-route attribution to model/cli. | n/a | [registration/orchestration.py](agents-remember/mcp/src/agents_remember/mcp/registration/orchestration.py) |
| The dashboard serving endpoint fixes trusted developer/dashboard attribution for no-hosted-session responses. | L358-L376 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
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
