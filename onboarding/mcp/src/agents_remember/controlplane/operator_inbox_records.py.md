# mcp/src/agents_remember/controlplane/operator_inbox_records.py

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| repository             | agents-remember                                                     |
| path                   | `mcp/src/agents_remember/controlplane/operator_inbox_records.py`    |
| doc_type               | `file-level-onboarding`                                             |
| lastUpdated            | 2026-07-10T01:14+02:00                                              |
| lastVerifiedCommitHash |                                                                     `5b49fa85a51d527a5a216a88c361c08246c759d0`|
| lastVerifiedCommitDate |                                                                     2026-07-10T05:00:02+02:00|
| governingOverview      | `overview.md`                                                       |

## Governing Overview

[overview.md](overview.md)

## Purpose

Defines the persisted `ar-operator-inbox-entry/v1` snapshot used to queue a
durable operator or agent-to-agent message that can be pushed into a hosted
session and/or polled by an external chat.

## Code Commentary

### 260707-HFX2-L13 Chain And Transition Fields

Pending inbox rows may now carry `leafKey` and `subjectAgentId`, preserving the leaf whose progress
must be checked and the seat whose inactivity/completion produced the signal. `rungTransitionAt` is
the ladder-only redundant timestamp used by the five-minute safety floor; unlike general `ts`, it is
not changed by delivery or renewal. `create_operator_inbox_entry` accepts and serializes the chain
fields without changing older rows that omit them.

### Logic

`OPERATOR_INBOX_RECORD_SCHEMA` is the wire tag. `OperatorInboxState` is
`pending | consumed | ladder-resolved`, `OperatorInboxVia` is `chat | dashboard | cli`,
`AgentRole` addresses orchestration identities (`orchestrator`, `manager`,
`worker`, `reviewer`, and — as of 260703-L12 — `strategist`, so the spawn-first sprint
planner can post/receive role-addressed inbox rows). **260707-HFX-L7** adds
`system-specialist`: the investigate-first provider-degradation seat needs its own inbox address
alongside `orchestrator`/`manager` since it is dispatched and reports through the same durable
mailbox as every other role. **260707-HFX-L12** adds `architect` and `curator`: HFX-L6 landed
doctrine (`architect.md`, `orchestrator.md`, `SKILL.md`) instructing the orchestrator to post a
`decision-item` inbox row to `recipient_role="architect"` and the architect to post a
`decision-ruling` back, but the schema itself still rejected both roles — a master-exit BLOCK
finding (Finding 1, `notes/reports/260707-HFX-master-exit-verdict.md`) that this leaf closes.
`InboxMessageKind` classifies the row, and now also carries `degradation-alert` (260707-HFX-L7) —
the row kind the provider degradation detector posts to the orchestrator and every active manager
on a state-change transition (see `providers/degradation.py`) — and, as of 260707-HFX-L12,
`decision-item`/`decision-ruling` — the architect/orchestrator decision relay pair the doctrine
above mandates, now genuinely round-trippable (proven by
`test_decision_item_relay_round_trip_between_orchestrator_and_architect` in
`mcp/tests/test_operator_inbox.py`, which posts a `decision-item` to `architect`, polls it, then
posts a `decision-ruling` back to `orchestrator`). `InboxDeliveryState` records hosted push state.
`require_inbox_address(...)` rejects entries with no lifecycle id, agent id, or
recipient role.

`OperatorInboxEntry` is a strict Pydantic record. It stores the mailbox keys
(`lifecycleId`, `agentId`, `recipientRole`), optional `gateId`, sender role/id,
message kind, optional artifact path, the originating `ask`, the message
`response`, creation attribution, hosted delivery metadata, and optional consume
attribution. `create_operator_inbox_entry(...)` returns a `pending` snapshot using
caller-minted `entry_id` and `now`. `consume_operator_inbox_entry(...)` returns a
later `consumed` snapshot while preserving the original post and delivery
metadata.

**260707-HFX2-L1** (R1 ack semantics + R4 routing): adds `attemptCount`,
`lastAttemptAt`, `nextAttemptAt`, and `escalatedAt` — the redelivery schedule
riding every entry, because `delivered` is never terminal and consume=ack is
the only terminal outcome (F-A/F-V proved pasted != perceived). Also adds
`ownerRole`/`ownerAgentId`/`ownerLifecycleId`: the ROUTED address
(`controlplane/signal_routing.py`) stamped once at post time from catalog
spawn provenance, distinct from the caller-supplied `recipientRole`.
`create_operator_inbox_entry(...)` gained matching `owner_*` keyword params.

**260707-HFX2-L4** (R1/R2, escalation ladder rung marker): adds `rung: int = 0` — the ladder's own
position marker for the row (0 = not yet escalated; 1 = renudged; 2 = skip-level re-addressed; 3 =
surfaced to the developer attention queue, terminal). `escalatedAt` (reserved by HFX2-L2) is now
genuinely re-stamped by `OperatorInboxStore.advance_rung` on EVERY rung transition, so it always
names "since when has this row sat at its CURRENT rung" — the anchor the ladder's own SLA/dwell
check (`escalation_ladder.rung_due`) reads — rather than merely "was this row ever escalated."

**260707-HFX2-L8** (dead-seat storm fix): adds the terminal non-ack state
`ladder-resolved` plus `ladderResolvedAt`/`ladderResolvedReason`. This is the durable end state for
a pending row whose ladder has reached the terminal rung and whose target seat is provably not live;
it is distinct from `consumed`, so the ack path remains the only "agent picked this up" terminal.
`consume_operator_inbox_entry` now returns any non-pending row unchanged, preserving that separation.

### Conventions

The record mirrors gate records: camelCase persisted fields, a `schema` alias,
literal states, and pure helper functions that do not write disk.

### Invariants And Boundaries

- Append a new snapshot for consumption; do not mutate the pending entry in
  place.
- An entry must carry at least one mailbox key (`lifecycleId`, `agentId`, or
  `recipientRole`).
- This is the persisted record, not the public MCP response contract; responses
  live in `models/operator_inbox.py`.

### Todos

None.

## Docs References

The observable-lifecycle design defines gates as durable append-only truth and
describes pull-style return channels for blocked agents; this inbox is the
external-chat pull implementation of that idea.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Gate records are durable, attributed, append-only decision facts; return channels above them must not lose an approval. | L220-L231; L251-L266 | [observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The inbox record declares schema/state/via literals and requires lifecycle or agent addressing. | L9-L18 | [operator_inbox_records.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_records.py) |
| `OperatorInboxEntry` preserves mailbox keys, ask, response, creation attribution, and consume attribution. | L21-L40 | [operator_inbox_records.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_records.py) |
| Create and consume helpers are pure snapshot builders. | L43-L90 | [operator_inbox_records.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_records.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: added leaf/subject routing provenance and the
  independent rung-transition timestamp used by supervisor chain suppression and the dwell floor.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8: `OperatorInboxState` gains `ladder-resolved` plus
  `ladderResolvedAt`/`ladderResolvedReason`; consume no longer converts non-pending terminal rows
  into acked rows. Verification metadata pinned until closeout stamps the HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (P-15 tier 3, escalation ladder): `OperatorInboxEntry`
  gains `rung: int = 0`, the ladder's own position marker; `escalatedAt` (reserved since HFX2-L2) is
  now genuinely re-stamped on every rung transition by `OperatorInboxStore.advance_rung`. No shape
  change to `create_operator_inbox_entry`/`consume_operator_inbox_entry` themselves. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T14:05+02:00 — 260707-HFX2-L1: `OperatorInboxEntry` gains the R1
  ack/backoff fields (`attemptCount`/`lastAttemptAt`/`nextAttemptAt`/
  `escalatedAt`) and the R4 routed-owner fields
  (`ownerRole`/`ownerAgentId`/`ownerLifecycleId`); `create_operator_inbox_entry`
  gained matching `owner_*` params. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L1 commit.
- 2026-07-08T04:15+02:00 — 260707-HFX-L12 (master-exit BLOCK fix leaf): `AgentRole` gains
  `architect` and `curator`; `InboxMessageKind` gains `decision-item` and `decision-ruling`. Closes
  master-exit Finding 1 — the HFX-L6-landed decision-item relay doctrine was unrepresentable in this
  schema, so the exact call `architect.md`/`orchestrator.md`/`SKILL.md` instruct agents to make
  raised `pydantic.ValidationError`. No shape/behavior change to the record helpers themselves — four
  Literal members added, pinned by the new round-trip test in `test_operator_inbox.py`. Verification
  metadata pinned until closeout stamps the HFX-L12 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact (small): `AgentRole` gains
  `system-specialist` so the provider-degradation investigator is inbox-addressable, and
  `InboxMessageKind` gains `degradation-alert` for the detector's role-addressed state-change
  alerts. No shape/behavior change to the record helpers themselves — two Literal members added.
  Verification metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): `AgentRole` gains the `strategist` literal so the new spawn-first portfolio seat is addressable on the inbox like the other orchestration roles. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-04T12:31+02:00 - L3: generalized the inbox record from external-chat
  operator responses to agent-addressed durable messages with sender/recipient
  role metadata, message kinds, artifact paths, and hosted delivery state.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: persistent operator inbox entry record plus pure create/consume helpers. Verification metadata pinned until closeout stamps the task-10 code commit.
