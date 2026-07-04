# mcp/src/agents_remember/controlplane

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| sourceRoute            | `mcp/src/agents_remember/controlplane`         |
| doc_type               | `route-local-overview`                         |
| lastUpdated            | 2026-07-04T12:32+02:00                      |
| lastVerifiedCommitHash | `277f27a33b35aed8235cbb3c1ae2b5633cc88b22`     |
| lastVerifiedCommitDate | 2026-07-05T01:30:08+02:00|
| governingOverview      | `../../../overview.md`                         |

## Purpose

`controlplane/` owns control-plane records: the gate control plane (task 6), the
operator/agent inbox (task 10/L3), orchestration artifact/nudge helpers (L3), the
task-23/24 interaction-retention policy, and task-28 lifecycle-scoped attention
acknowledgements. Gates are attributed decision points on a lifecycle; the inbox
is the pull-based return channel for chats the dashboard does not host and the
durable substrate for agent-to-agent messages that may also be pushed into
hosted sessions; nudge rows record rate-limited manager nudges. Attention
acknowledgement rows hide one current queue occurrence. Lifecycle-bound acknowledgements disappear with their
lifecycle; Task 29 S7 keeps only targetless actionable-drift acknowledgements current
across that prune boundary because their source item is repository/branch-scoped rather
than lifecycle-scoped. These rows are throwaway interaction data, not durable task records.

## Hot Path Summary

A gate is publicly opened for agent workflow through `lifecycle_gate`, which
creates the `GateRecord`, blocks the ambient lifecycle with the ask, and
keeps the public tool call waiting until the gate is decided or a gate-specific inbox response exists.
Decisions (`gate_decide`) and listing
(`gate_list`) remain public control-plane tools; lower-level create/wait builders
are compatibility internals in `mcp/tools/gates.py`. The builders append
`GateRecord` snapshots to `GateStore`. Lifecycle-scoped gate creation expires any
previous open gate before opening the new one, so each lifecycle has one current
actionable gate. L4 adds policy-governed delegated approvals: default policy is
all-human; non-human orchestration decisions are valid only for explicitly
delegated gate kinds, never for human-pinned integration/push/cleanup gates, and
never by the owning lifecycle itself. Gate records can attach reviewer-verdict
evidence refs, and policies may require that evidence before a delegated decision
binds. Task 23/24 adds the retention boundary: cancel,
non-enforcement wait pickup, dismiss, clear, consume, and the 24-hour TTL physically delete throwaway
interaction rows. Start at `records.py` for the
entity, then `store.py` for the append-only log (co-located with the observer
event log under `observer_root`). `gate_policy.py` owns the validated
delegation schema and attribution checks. `enforcement.py`'s `evaluate_gate` is
the pure kind-generic policy resolver; `evaluate_closeout_gate` remains the
closeout wrapper `worktree_closeout_apply` obeys.

Operator/agent messages are queued with `OperatorInboxEntry` snapshots and
stored through `OperatorInboxStore`. The inbox log lives under
`observer_root/workspace/operator-inbox.jsonl`; entries carry `lifecycleId`
and/or `agentId` and/or `recipientRole`, preserve sender/recipient role metadata,
message kind, optional artifact path, originating ask, response, and hosted
delivery state while pending, and are deleted when the agent consumes them, the
developer dismisses the stale pickup warning, or TTL compaction removes them.
L3 adds `orchestration_nudges.py` for rate-limited manager nudges and
`orchestration_artifacts.py` for turn-report, master-handover, and escalation
packet helpers.

Attention dismissals use `AttentionDismissalStore` under
`observer_root/workspace/attention-dismissals.jsonl`, but unlike gates the file is a compact current
set rather than history. Dismissing a lifecycle-bound attention row upserts one acknowledgement; each
projection tick prunes acknowledgements whose lifecycle is no longer live. Gate-open attention rows are
consumed by cancelling/deleting the gate source itself. Targetless actionable-drift dismissals are the
only repository-scoped exception: they stay as current acknowledgements until superseded by a newer drift
signal, while targetless provider-down dismissals are not accepted.

## Layout

| Module        | Owns                                                                          |
| ------------- | ----------------------------------------------------------------------------- |
| `records.py`  | `GateRecord` (`ar-gate-record/v1`) + pure `create_gate` / `decide_gate` / `expire_gate` / `coerce_gate_kind`; the `GateKind` / `GateState` / `DecidedVia` Literals, `GateEvidenceRef`, and `DECISION_STATES`. `GateKind` is the full l-01 gate spine (slice 09 added `plan-approval` / `worktree-intent` / `push-approval`); `closeout-approval` IS the commit gate — no separate `commit-approval`. |
| `store.py`    | `GateStore`: lifecycle/workspace gate logs beside the event log; `current()` folds by gate id (last-wins), while `delete`/`compact` physically remove throwaway interaction rows. |
| `enforcement.py` | `evaluate_closeout_gate` (pure closeout-gate policy) + `CloseoutGuard` — the binding rule `worktree_closeout_apply` reads (slice 6b). |
| `operator_inbox_records.py` | `OperatorInboxEntry` (`ar-operator-inbox-entry/v1`) + pure create/consume helpers for durable operator/agent inbox snapshots, including role/message/artifact and delivery metadata. |
| `operator_inbox_store.py` | `OperatorInboxStore`: workspace inbox log, pending filters by lifecycle/agent/recipient role, delivery-state snapshots, idempotent store consume, public delete/dismiss paths, and TTL compaction. |
| `orchestration_artifacts.py` | Strict turn-report, master-handover, and escalation packet helpers for the L2/L3 orchestration frame. |
| `orchestration_nudges.py` | `OrchestrationNudgeRecord` + `OrchestrationNudgeStore`: append-only, rate-limited manager nudge attempts plus message/artifact helpers. |
| `gate_policy.py` | `GatePolicy` / `GatePolicyRule`, built-in policy names, human-pinned/delegable kind validation, and delegated-decision attribution/evidence checks. |
| `enforcement.py` | `evaluate_gate` (pure kind-generic gate policy resolver) + `GateGuard`; `evaluate_closeout_gate` / `CloseoutGuard` remain the closeout wrapper `worktree_closeout_apply` reads. |
| `operator_inbox_records.py` | `OperatorInboxEntry` (`ar-operator-inbox-entry/v1`) + pure create/consume helpers for external-chat inbox snapshots. |
| `operator_inbox_store.py` | `OperatorInboxStore`: workspace inbox log, pending filters by lifecycle/agent, idempotent store consume, public delete/dismiss paths, and TTL compaction. |
| `attention_dismissals.py` | `AttentionDismissalRecord` + `AttentionDismissalStore`: compact current acknowledgement rows for attention queue dismissals, with physical prune by live lifecycle id and a targetless actionable-drift exception. |
| `interaction_retention.py` | Shared 5-minute pickup/wait and 24-hour interaction TTL policy helpers. |
| `__init__.py` | Package export surface (gate records/store/enforcement + operator inbox records/store). |

The `gate_*` MCP tools live in `mcp/tools/gates.py` (config-rooted, building a
`GateStore(observer_root(config))`); their response models are `models/gates.py`.
The `operator_inbox_*` MCP tools live in `mcp/tools/operator_inbox.py`; their
response models are `models/operator_inbox.py`.

## Invariants And Boundaries

- **Records + a pure policy, not the mutation.** Creating/deciding a gate writes
  durable history (`records.py`/`store.py`); `gate_policy.py` validates which
  roles can decide which gate kinds; `enforcement.py` decides whether an
  approved gate permits the guarded operation — but the *mutation* (refusing the
  closeout, marking the gate `applied`) lives in the worktree tool
  (`worktrees/modules/closeout.py`), which imports the I/O-free policy.
- **Interaction records are disposable.** Gate/inbox rows remain modeled records while pending, and
  lifecycle-bound attention acknowledgement rows remain only while their lifecycle is live; targetless
  actionable-drift acknowledgement rows are current repo/branch records, not history. Response, cancel,
  dismiss, clear, consume, lifecycle prune, and TTL cleanup physically delete them. Durable task docs, contracts,
  commits, and ledgers carry lifecycle history.
- **Single current lifecycle gate.** A lifecycle may have only one open durable gate; creating a new
  lifecycle-scoped gate appends an `expired` snapshot for older open gates rather than deleting them.
- **Honest attribution → enforceable.** `decidedBy` (actor/session/lifecycle),
  `decidedVia` (chat/dashboard/cli/orchestration), and `decidingRole` are
  separate. MCP self-decisions stay model/cli and non-binding; delegated
  orchestration decisions name a distinct deciding lifecycle/session and must
  satisfy the configured `GatePolicy` before they are appended or consumed.
- Gates co-locate under `observer_root`, mirroring the event substrate; no new
  storage root.
- Inbox entries require `lifecycleId`, `agentId`, or `recipientRole`; an
  unaddressed response has no external mailbox or hosted-session target.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Gates mirror the observer event substrate (envelope + append-only JSONL store). | [observer/store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| Gate policy validation and delegated decision checks. | [gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |
| The `gate_*` payload builders that drive this substrate. | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| Gate response models. | [models/gates.py](agents-remember/mcp/src/agents_remember/models/gates.py) |
| The inbox record/store pair provides the external-chat pull return channel. | [operator_inbox_records.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_records.py) and [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| The attention acknowledgement store keeps current lifecycle-scoped queue dismissals only. | [attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |

## Update History

- 2026-07-05T01:32+02:00 — No route impact: orchestration_artifacts `template_path` root renamed with the unified skill folder (`l-01-agent-lifecycles`); resolution logic and the route model are unchanged (260703-L9).
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: added the
  `gate_policy.py` schema/validator, generalized enforcement to a kind-generic
  resolver, and documented delegated orchestration attribution plus reviewer
  evidence refs. Human-pinned integration/push/cleanup gates remain
  non-delegable. Verification metadata pinned until closeout stamps the L4
  commit.
- 2026-07-04T12:31+02:00 - L3 route impact: the inbox is now generalized for
  agent-to-agent addressing with role/message/artifact/delivery metadata, and
  the route adds orchestration artifact and rate-limited nudge helpers.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: attention dismissals now document the targetless
  actionable-drift exception, preserving only current repo/branch drift acknowledgements while
  lifecycle-bound rows continue to prune with live lifecycle ids. Verification metadata pinned until
  closeout stamps the task-29 code commit.
- 2026-06-28T03:05+02:00 — Task 28 S5.2: added `attention_dismissals.py` as compact lifecycle-scoped attention acknowledgement state; projection pruning removes rows for non-live lifecycles and gate-open items are consumed by gate cancellation/deletion. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-26T18:43+02:00 — Regression fix: route now records that public
  `lifecycle_gate` waits without an exposed timeout and ignores stale
  lifecycle-scoped inbox rows that are not tied to the newly opened gate.
- 2026-06-26T17:05+02:00 — Regression fix: route now records that
  `lifecycle_gate` performs the bounded gate/inbox wait itself after creating
  the gate and blocking the lifecycle; it is no longer described as wait-state
  initialization only.
- 2026-06-26T14:16+02:00 — Task 25: route overview now describes `lifecycle_gate` as the public gate-opening workflow and classifies lower-level create/wait builders as compatibility internals.
- 2026-06-25T13:20+02:00 — Task 23/24: added interaction-retention policy to the route and changed gate/inbox framing from permanent logs to disposable interaction rows with delete/TTL cleanup paths.
- 2026-06-25T07:26+02:00 — Task 19: gates now include the `expired` state/helper for replacing older
  open lifecycle gates, and the route exposes the `gate_response_wait` wait-plus-inbox helper while
  keeping decisions and messages separate. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: added `operator_inbox_records.py` and `operator_inbox_store.py` to the route, documenting the external-chat pull channel as a control-plane sibling to gates. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S2): `records.py`'s `GateKind` Literal gained `plan-approval`, `worktree-intent`, and `push-approval` — the full l-01 gate spine; refreshed the `records.py` Layout row (and noted `closeout-approval` IS the commit gate, no separate `commit-approval`). The route's record-vs-policy split and store/enforcement modules are unchanged. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: the route gained enforcement — `enforcement.py` (`evaluate_closeout_gate` + `CloseoutGuard`), the pure closeout-gate policy `worktree_closeout_apply` obeys. Revised the "record, not enforcement" framing: the *policy* is here (I/O-free), the *mutation* stays in the worktree tool. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the gate control-plane substrate route (`records.py` + `store.py` + facade). Verification metadata pinned until closeout stamps the 6a code commit.
