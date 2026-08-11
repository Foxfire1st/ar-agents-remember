# mcp/src/agents_remember/controlplane/operator_inbox_records.py

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| repository             | agents-remember                                                     |
| path                   | `mcp/src/agents_remember/controlplane/operator_inbox_records.py`    |
| doc_type               | `file-level-onboarding`                                             |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                                       |

## Governing Overview

[overview.md](overview.md)

## Purpose

Defines the append-only operator-inbox record and its structural address, routed owner, subject, and
delivery evidence. Task-document plus role is stable; exact agent/lifecycle/session fields are
private correlations.

## Code Commentary

### Logic

`InboxRouting` couples the current delivery address with its derived owner. `InboxSubject`
records what seat a message concerns. `OperatorInboxEntry` persists both structural fields and
adapter evidence; folding never lets a later stale pending snapshot reverse a terminal row.
`consume_operator_inbox_entry` is attribution only and does not drive delivery or terminality.

### Conventions

Whole ask/response messages are one durable row. Landed truth comes from correlated adapter
acceptance at a turn boundary.

### Invariants And Boundaries

- Ordinary messages remain structurally addressable across replacement.
- Dispatch brief is the only internally exact-pinned message kind.
- Model consume is optional attribution, not acknowledgement authority.
- Persistence precedes delivery attempts.

### Todos

Named legacy escalation fields remain parse-only until their durability schema is migrated.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Address, owner, subject, and message are explicit value objects. | `InboxAddress` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:40-108 |
| The durable row separates structural identity from delivery correlations. | `OperatorInboxEntry` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:149-222 |
| Consume preserves state and only stamps attribution. | `consume_operator_inbox_entry` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:290-313 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T14:29+02:00 — Re-read `InboxAddress` and widened its citation to include the
  dataclass declaration; verification metadata remains unchanged for governed closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 4 citation rows with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.
- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded that
  `OperatorInboxCompatibleRecord` now inherits `durable_store.DurableRecord`, so `OperatorInboxEntry`
  carries the contract's validated `schemaVersion` (unknown major rejected, unknown minor accepted,
  no version branch in any reader) while deliberately keeping its own `extra="allow"` plus
  `reject_unknown_extensions` instead of the contract's blanket `extra="forbid"` — the single
  declared `extra`-policy divergence among the six record types, kept because the named
  two-field forward-compatibility allowlist pre-dates the contract. Recorded that `schema` and
  `schemaVersion` answer different questions. Repaired all three pre-existing Repo-Internal
  citations, which pointed at L9-L18, L21-L40 and L43-L90 in a 307-line file and named symbols that
  are not in those ranges. Verification metadata pinned until closeout stamps the L5 commit.
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
