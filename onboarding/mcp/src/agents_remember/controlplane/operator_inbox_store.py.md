# mcp/src/agents_remember/controlplane/operator_inbox_store.py

| Field                  | Value                                                             |
| ---------------------- | ----------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/controlplane/operator_inbox_store.py`    |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash |                                                                   `fdff55f2921d7aaa8ba240c11087d02c15a170d7`|
| lastVerifiedCommitDate |                                                                   2026-07-10T15:53:23+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

File-backed operator inbox store for short-lived polling plus hosted-session
delivery metadata.

## Code Commentary

### 260707-HFX2-L17 Pair-Preserving Renewal

`renew` can refresh `seatRole` with `leafKey` and subject identity when one coalesced supervisor
condition re-fires. Pair identity therefore survives readdressing to a replacement manager and
prevents same-text findings for different roles from becoming one row.

### 260707-HFX2-L13 Transition And Readdress Mutations

`advance_rung` atomically stamps `ts`, `rung`, `escalatedAt`, and `rungTransitionAt`, so every
successful transition resets both the ordinary dwell and redundant minimum-floor anchors. `renew`
can refresh `leafKey`/`subjectAgentId` and, when explicitly requested, rewrite both direct and owner
addresses to the currently resolved manager while keeping the same durable row id. Normal renewal
does not touch either rung anchor.

### Logic

`OperatorInboxStore(observer_root)` writes one workspace log:
`workspace/operator-inbox.jsonl`. `append(record)` creates the parent directory
and appends a strict JSON snapshot. `read()` validates each JSONL row back into
`OperatorInboxEntry`, and `current()` folds by entry id, last snapshot wins.

`list_pending(lifecycle_id, agent_id, recipient_role)` requires at least one
mailbox key, then returns pending entries matching every supplied key. That means
a lifecycle poll, an agent poll, a role poll, or a combined poll all use the same
log without duplicating entries. `record_delivery(...)` appends a delivery-state
snapshot for a queued message. `consume(entry_id, ...)` appends one consumed snapshot and
returns `(entry, True)` the first time; repeated consumes return the existing
consumed entry with `False`.

Task 23/24 added physical cleanup. `delete(entry_id)` removes all snapshots for
one inbox entry, `delete_by_gate(gate_id)` removes entries associated with a
cleared/dismissed gate, and `compact(now=...)` prunes consumed or 24h-expired
entries through `interaction_retention.inbox_keep_ids`. The public consume tool
now deletes the entry after returning the consumed payload.

260707-HFX2-L1 (R1/R3 ack semantics + redelivery): `record_delivery(...)` now
bumps `attemptCount`, stamps `lastAttemptAt`, and schedules a durable
`nextAttemptAt` (via `inbox_backoff.next_attempt_at`) on EVERY attempt,
including a confirmed `delivered` paste -- consume is the only call that stops
the schedule, because `delivered` is never terminal (pasted != perceived).
`list_redeliverable(now=..., rate_limit_seconds=...)` selects pending rows past
their backoff window and clear of the per-target rate limit
(`inbox_backoff.redeliverable`) -- the pure selection L2's sweep drives
redelivery from; this store itself never redelivers on its own (no in-memory
timer). `mark_escalated(entry_id, now=...)` stamps the reserved `escalatedAt`
field the ladder (HFX2-L4) will set -- this store only reserves the transition.
HFX2-L9 extends that path with the 900-second production floor: `record_delivery` accepts
`redelivery_floor_seconds` and passes it into `next_attempt_at`, while `list_redeliverable` still
defaults through `inbox_backoff.DEFAULT_RATE_LIMIT_SECONDS` when the caller supplies no override.
Below-floor values are refused in `inbox_backoff`, not silently shortened here.

260707-HFX2-L4 (R1/R2, the ladder's own transition): `advance_rung(entry_id, *, rung, now)` stamps
the ladder's next rung AND re-anchors `escalatedAt` to `now` in the SAME snapshot, so the next
rung's SLA/dwell check is measured from this transition, not the row's original creation. Distinct
from `mark_escalated` (HFX2-L2's reserved, rung-agnostic "this row is now escalatable" stamp) —
`escalation_ladder`/`serving/supervisor.py`'s `_escalate_rung` is the only caller of `advance_rung`.

260707-HFX2-L8 adds sweep-scale operation support and the ladder terminal state. `record_delivery`,
`list_redeliverable`, `mark_escalated`, and `advance_rung` accept an optional folded `current`
snapshot so the supervisor can reuse one in-sweep index instead of refolding
`operator-inbox.jsonl` once per finding. `mark_ladder_resolved(entry_id, now, reason, current=...)`
appends a `state="ladder-resolved"` snapshot, clears `nextAttemptAt`, and reports whether this call
performed the terminal transition. `compact(now=...)` prunes those ladder-resolved ids through the
shared retention policy, bounding the log after a fleet of retired seats has terminated.

### Conventions

The store follows the gate store's append/read/fold pattern, but uses a shared
workspace inbox log because external chats and orchestration agents may address
by lifecycle, agent, role, or combinations of those keys.

### Invariants And Boundaries

- Current state is a fold while entries are pending; consumed/dismissed/expired
  entries are throwaway interaction data and can be physically removed.
- A `ladder-resolved` row is terminal but not acked; it is excluded from redelivery and eligible for
  compaction.
- Delivery scheduling may inherit the store default or take a caller floor, but the effective floor is
  validated in `inbox_backoff` and cannot be below 900 seconds.
- Polling without `lifecycle_id`, `agent_id`, or `recipient_role` is invalid
  because it has no mailbox boundary.
- This store owns persistence only; MCP payload shapes and attribution routing
  live in `mcp/tools/operator_inbox.py`.

### Todos

None.

## Docs References

The observable-lifecycle design describes passive/active pull as the durable
return-channel family; this store supplies the durable mailbox for external
agents that cannot receive dashboard session injection.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Pull-based return channels sit above durable gate truth and resume on the next poll/poke when push is unavailable. | L251-L266 | [observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The inbox log is `workspace/operator-inbox.jsonl`, and append/read/current preserve JSONL history. | L15-L53 | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| Pending filters match supplied lifecycle and/or agent keys. | L55-L70 | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| Consume is idempotent and appends a consumed snapshot only once. | L72-L93 | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| Delivery snapshots thread `redelivery_floor_seconds` into `next_attempt_at`, and redeliverable selection defaults to the shared backoff floor. | L89-L155 | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: made coalesced inbox renewal preserve the current
  leaf-role subject pair through owner readdressing.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: made rung advancement stamp both dwell anchors
  and allowed coalesced supervisor rows to preserve chain fields and readdress the current manager.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: threaded the effective 900-second redelivery floor
  through `record_delivery(..., redelivery_floor_seconds=...)` and preserved the shared default for
  `list_redeliverable`. Verification metadata pinned until closeout stamps the 260707-HFX2-L9
  commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8: added optional snapshot-aware mutation/selection paths,
  `mark_ladder_resolved`, and compaction of ladder-resolved terminal ids so supervisor sweeps avoid
  per-finding log folds and dead-seat storms leave bounded inbox logs. Verification metadata pinned
  until closeout stamps the HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (R1/R2, escalation ladder): added `advance_rung` — stamps
  the ladder's next rung and re-anchors `escalatedAt` in the same snapshot, distinct from HFX2-L2's
  rung-agnostic `mark_escalated`. `serving/supervisor.py::_escalate_rung` is the sole caller.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T14:00+02:00 — 260707-HFX2-L1: R1 ack semantics (attempt/backoff
  fields on `record_delivery`, delivered is never terminal) + R3 redelivery
  (`list_redeliverable`, `mark_escalated`), reusing the `inbox_backoff` module's
  pure math. Verification metadata pinned until closeout stamps the
  260707-HFX2-L1 commit.
- 2026-07-04T12:31+02:00 - L3: added recipient-role pending filters and
  `record_delivery(...)` snapshots so hosted push outcomes stay attached to the
  durable inbox row. Verification metadata pinned until closeout stamps the L3
  commit.
- 2026-06-25T13:10+02:00 — Task 23/24: added delete, delete-by-gate, and compaction so consumed/dismissed/expired operator-inbox entries do not accumulate forever.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: append-only workspace inbox store with lifecycle/agent pending filters and idempotent consume. Verification metadata pinned until closeout stamps the task-10 code commit.
