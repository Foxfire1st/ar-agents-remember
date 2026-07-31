# mcp/src/agents_remember/controlplane/operator_inbox_records.py

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| repository             | agents-remember                                                     |
| path                   | `mcp/src/agents_remember/controlplane/operator_inbox_records.py`    |
| doc_type               | `file-level-onboarding`                                             |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                       |

## Governing Overview

[overview.md](overview.md)

## Purpose

Defines the persisted `ar-operator-inbox-entry/v1` snapshot used to queue a
durable operator or agent-to-agent message that can be pushed into a hosted
session and/or polled by an external chat.

## Code Commentary

### 260707-HFX2-L20 Terminal-Dominant Snapshot Fold

`fold_operator_inbox_entries` centralizes the current-state projection. Pending snapshots remain
last-wins until a terminal `consumed` or `ladder-resolved` snapshot is observed; later stale pending
delivery snapshots are ignored, while later terminal snapshots preserve idempotent terminal updates.

### 260707-HFX2-L17 Seat-Scoped Inbox Rows

`OperatorInboxEntry` and its constructor now carry optional `seatRole` beside `leafKey`. Supervisor
signals and later redelivery/escalation retain which role on the leaf produced the condition while
owner addressing remains a separate routed field family.

### 260707-HFX2-L14 Chain And Transition Fields

Pending inbox rows may now carry `leafKey` and `subjectAgentId`, preserving the leaf whose progress
must be checked and the seat whose inactivity/completion produced the signal. `rungTransitionAt` is
the ladder-only redundant timestamp used by the five-minute safety floor; unlike general `ts`, it is
not changed by delivery or renewal. `create_operator_inbox_entry` accepts and serializes the chain
fields without changing older rows that omit them.

### Logic

`OPERATOR_INBOX_RECORD_SCHEMA` is the wire tag. `OperatorInboxState` is
`pending | consumed | ladder-resolved`, `OperatorInboxVia` is `chat | dashboard | cli`,
`AgentRole` addresses orchestration identities (`orchestrator`, `manager`,
`worker`, `reviewer`, and — as of 260703-L14 — `strategist`, so the spawn-first sprint
planner can post/receive role-addressed inbox rows). **260707-HFX-L7** adds
`system-specialist`: the investigate-first provider-degradation seat needs its own inbox address
alongside `orchestrator`/`manager` since it is dispatched and reports through the same durable
mailbox as every other role. **260707-HFX-L14** adds `architect` and `curator`: HFX-L7 landed
doctrine (`architect.md`, `orchestrator.md`, `SKILL.md`) instructing the orchestrator to post a
`decision-item` inbox row to `recipient_role="architect"` and the architect to post a
`decision-ruling` back, but the schema itself still rejected both roles — a master-exit BLOCK
finding (Finding 1, `notes/reports/260707-HFX-master-exit-verdict.md`) that this leaf closes.
`InboxMessageKind` classifies the row, and now also carries `degradation-alert` (260707-HFX-L7) —
the row kind the provider degradation detector posts to the orchestrator and every active manager
on a state-change transition (see `providers/degradation.py`) — and, as of 260707-HFX-L14,
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
attribution. `create_operator_inbox_entry(message, *, entry_id, now, routing, poster)` returns a
`pending` snapshot using caller-minted `entry_id` and `now`.
`consume_operator_inbox_entry(...)` returns a later `consumed` snapshot while preserving the
original post and delivery metadata.

**The five frozen parameter objects (260731-EFA-L2)** are the module's public vocabulary for
posting; every caller builds them instead of passing nineteen keywords:

- **`InboxAddress(lifecycle_id=None, agent_id=None, recipient_role=None)`** — the mailbox a row is
  delivered to. At least one of the three must be set, which is exactly what
  `require_inbox_address` enforces; they are one address, never independently meaningful.
- **`InboxOwner(role=None, agent_id=None, lifecycle_id=None)`** — the R4 routed owner a poster
  derives from catalog spawn provenance BEFORE posting, stamped once at creation (and re-stamped
  by a readdressing ladder rung) so redelivery never re-derives it from a catalog snapshot that
  has since moved on.
- **`InboxRouting(address, owner=InboxOwner())`** — the two together. A readdressing rung moves
  the address onto the next owner and rewrites both, which is why they are one routing decision.
- **`InboxSubject(leaf_key=None, seat_role=None, agent_id=None)`** — what a row is *about* as
  opposed to who it goes to. The supervisor coalesces re-fires and the ladder readdresses on
  exactly this triple.
- **`InboxMessage(ask, response, message_kind="message", gate_id=None, artifact_path=None,
  subject=InboxSubject())`** — what the row says and what about.
- **`InboxPoster(created_by, created_via, sender_agent_id=None, sender_role=None)`** — who put the
  row in the inbox.

`InboxOwner` and `InboxSubject` are imported by `operator_inbox_store.py` too — they are the same
owner and the same subject a renewal or a readdressing rung rewrites.

**260707-HFX2-L1** (R1 ack semantics + R4 routing): adds `attemptCount`,
`lastAttemptAt`, `nextAttemptAt`, and `escalatedAt` — the redelivery schedule
riding every entry, because `delivered` is never terminal and consume=ack is
the only terminal outcome (F-A/F-V proved pasted != perceived). Also adds
`ownerRole`/`ownerAgentId`/`ownerLifecycleId`: the ROUTED address
(`controlplane/signal_routing.py`) stamped once at post time from catalog
spawn provenance, distinct from the caller-supplied `recipientRole`. Those three fields are now
carried by `InboxRouting.owner` (an `InboxOwner`); the former `owner_role` / `owner_agent_id` /
`owner_lifecycle_id` keywords on `create_operator_inbox_entry` are gone.

**260707-HFX2-L4** (R1/R2, escalation ladder rung marker): adds `rung: int = 0` — the ladder's own
position marker for the row (0 = not yet escalated; 1 = renudged; 2 = skip-level re-addressed; 3 =
surfaced to the developer attention queue, terminal). `escalatedAt` (reserved by HFX2-L2) is now
genuinely re-stamped by `OperatorInboxStore.advance_rung` on EVERY rung transition, so it always
names "since when has this row sat at its CURRENT rung" — the anchor the ladder's own SLA/dwell
check (`escalation_ladder.rung_due`) reads — rather than merely "was this row ever escalated."

**260707-HFX2-L9** (dead-seat storm fix): adds the terminal non-ack state
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

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Adapter Delivery Evidence

Inbox records retain additive adapter acceptance, reconciliation, and completion evidence while the
row's explicit consume state remains independent.

### 260713-PHA-L6 Rolling Reader Compatibility

The compatibility base permits exactly the optional `adapterDeliveryState` and
`adapterDeliveryDetail` fields for older readers during a serving cutover. Current
`OperatorInboxEntry` fields remain explicitly typed, and unrelated extensions remain rejected;
this is an additive two-field seam, not catch-all parsing. Delivery evidence remains separate from
the explicit consume state.

## Update History
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `InboxAddress`, `InboxOwner`, `InboxRouting`, `InboxSubject`, `InboxMessage`
  and `InboxPoster` parameter objects, and re-signed `create_operator_inbox_entry` from nineteen
  keywords to `(message, *, entry_id, now, routing, poster)`. `require_inbox_address` keeps its
  own keyword signature and is still called with the address's three fields, so the
  at-least-one-mailbox refusal is unchanged. No record field was added, removed or renamed.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented the exact two-field rolling-reader allowlist and
  preserved rejection of unrelated inbox extensions.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented adapter evidence fields without changing consume semantics.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20: added the shared monotonic inbox fold that prevents a
  stale pending delivery snapshot from reversing an already-recorded terminal transition.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added current seat-role subject identity to durable
  inbox rows without changing owner-routing or immutable sender provenance.

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
