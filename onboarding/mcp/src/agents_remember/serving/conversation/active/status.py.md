# mcp/src/agents_remember/serving/conversation/active/status.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/status.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The canonical conversation status authority (leaf R3): the one revisioned mapping from
`AdapterSnapshot` evidence to the canonical `ConversationStatus` vocabulary, consumed
identically by the Chats serving routes (through the active projector) and by orchestration
(through `hosted_control_projection.snapshot_turn_state`). Neither consumer maps adapter
evidence on its own, and neither derives state from rendered events, PTY output, or the last
timeline mutation.

## Code Commentary

### Logic

`classify_process` (L91-L100) maps adapter control state to the canonical process vocabulary
(connected/starting/disconnected/failed). `classify_turn` (L103-L140) maps activity/raw
evidence to one canonical turn evidence value: pending interaction (exact, carrying the
interaction id), blocked-without-interaction (`declared-external-wait`), running
(`active-native-turn`, codex-only turn id from raw, L193-L200), settling (per-harness raw keys —
claude `claudeStatus`/`retryAttempt`, pi `isCompacting`/`auto_retry_start`, L203-L234), and
idle+ready (`settled-dispatchable`); unusable evidence returns `None` so callers retain their
last known turn state. `snapshot_seat_turn_state` (L178-L190) is the single orchestration seat
projection: `seat_turn_state_for` (L155-L175) reproduces the pre-canonical mapping exactly
(live turn states → `working`, wait states → `awaiting-input`, settled-with-connected →
`turn-ended`, else `stale`), pinned over the full control×activity product.
`ConversationStatusService` (L252-L447) folds observations into the revisioned envelope per
exact identity: `_apply` (L307-L348) prefers observed terminal settlements (exact strength,
interrupted/failed map directly, completed settles) over activity classification, preserves a
completed outcome across the settling → ready transition (L331-L338), and `_set_turn`
(L350-L379) advances state only on semantic change. The revision (L283-L300) advances only on
semantic transitions — turn/process/stale changes; freshness timestamps are derived metadata
recomputed per observation under the same revision (`_envelope` L419-L447), never a mutation
trigger. Staleness is one liveness-sweep cadence plus slack (`STALE_AFTER_MS` L46), and the
observation bound is honestly `poll` (L49).

### Conventions

Evidence-first classification: unknown evidence never becomes `ready` (enforced by the contract
model), and a session without usable turn evidence keeps its last known turn state while
process/freshness evidence advances honestly. Terminal outcomes feed the canonical machine from
native evidence only.

### Invariants And Boundaries

- This module is the ONLY classification of adapter evidence into the canonical vocabulary;
  consumers never re-map `AdapterSnapshot` fields.
- Revision never advances for polling cadence or timestamps — equal-revision envelopes are
  semantically identical.
- Orchestration parity is exact by construction: the seat projection consumes the same
  classification, never a parallel mapping.
- The orchestration entry point stays signature-compatible (`snapshot_turn_state` delegates with
  an optional harness parameter); `terminal_liveness.py` is untouched.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The canonical vocabulary and
revision rules are the repository-owned strict wire contract cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this authority. | — | — |

## Repo-Internal References

The canonical evidence→state map and status envelope models live in the parent contract module;
orchestration consumes this authority through the one delegated projection; the projector feeds
it observations and terminal settlements.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `CANONICAL_TURN_STATE_BY_EVIDENCE` fixes the evidence-to-turn-state vocabulary this service classifies into. | L432-L445 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| `ConversationStatus` and its freshness/process/turn products define the revisioned envelope shape. | L521-L583 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Orchestration's `snapshot_turn_state` delegates here with a documented function-local import; signature unchanged. | L70-L90 | [hosted_control_projection.py](agents-remember/mcp/src/agents_remember/serving/hosted_control_projection.py) |
| The projector observes snapshots and pending terminal settlements through this service per poll. | L272-L284 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| `SeatTurnState` is the orchestration vocabulary the single projection rule emits. | L38 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |

## Cross-Repo References

No cross-repository implementation participates in this status authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the canonical
  status authority — the one evidence classification, revisioned envelope, single seat
  projection, terminal-outcome handling. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
