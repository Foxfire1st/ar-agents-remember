# mcp/src/agents_remember/serving/conversation/active/status.py

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

cit:([`classify_process`], mcp/src/agents_remember/serving/conversation/active/status.py:101-110) maps adapter control state to the canonical process vocabulary
(connected/starting/disconnected/failed). cit:([`classify_turn`], mcp/src/agents_remember/serving/conversation/active/status.py:113-150) maps activity/raw
evidence to one canonical turn evidence value: pending interaction (exact, carrying the
interaction id), blocked-without-interaction (`declared-external-wait`), running
(`active-native-turn`, codex-only turn id from raw, L193-L200), settling (per-harness raw keys —
claude `claudeStatus`/`retryAttempt`, pi `isCompacting`/`auto_retry_start`, L203-L234), and
idle+ready (`settled-dispatchable`); unusable evidence returns `None` so callers retain their
last known turn state. cit:([`snapshot_seat_turn_state`], mcp/src/agents_remember/serving/conversation/active/status.py:205-223) is the single orchestration seat
projection: cit:([`seat_turn_state_for`], mcp/src/agents_remember/serving/conversation/active/status.py:165-202) reproduces the pre-canonical mapping exactly
(live turn states → `working`, wait states → `awaiting-input`, settled-with-connected →
`turn-ended`, else `stale`), pinned over the full control×activity product.
cit:([`ConversationStatusService`], mcp/src/agents_remember/serving/conversation/active/status.py:306-508) folds observations into the revisioned envelope per
exact identity: cit:([`_apply`], mcp/src/agents_remember/serving/conversation/active/status.py:361-412) prefers observed terminal settlements (exact strength,
interrupted/failed map directly, completed settles) over activity classification, preserves a
completed outcome across the settling → ready transition, and cit:([`_set_turn`], mcp/src/agents_remember/serving/conversation/active/status.py:414-434) advances state only on semantic change. The revision
advances only on semantic transitions — turn/process/stale changes; freshness timestamps are derived metadata
recomputed per observation under the same revision cit:([`_envelope`], mcp/src/agents_remember/serving/conversation/active/status.py:480-508), never a mutation
trigger. Staleness is one liveness-sweep cadence plus slack cit:([`STALE_AFTER_MS`], mcp/src/agents_remember/serving/conversation/active/status.py:52-52), and the
observation bound is honestly `poll` cit:([`OBSERVATION_BOUND`], mcp/src/agents_remember/serving/conversation/active/status.py:65-65).

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

## Evidence

### Docs References

The resolved `Domain Documentation` registry has no entries. The canonical vocabulary and
revision rules are the repository-owned strict wire contract cited below.

No configured domain documentation was available for this authority.

### Repo-Internal References

The canonical evidence→state map and status envelope models live in the parent contract module;
orchestration consumes this authority through the one delegated projection; the projector feeds
it observations and terminal settlements.

- "CANONICAL_TURN_STATE_BY_EVIDENCE" fixes the evidence-to-turn-state vocabulary this service classifies into (declared in models/conversations/status.py since L9). [1]
- `ConversationStatus` and its freshness/process/turn products define the revisioned envelope shape. [2]
- Orchestration's `snapshot_turn_state` delegates here with a documented function-local import; signature unchanged. [3]
- The projector observes snapshots and pending terminal settlements through this service per poll. [4]
- `SeatTurnState` is the orchestration vocabulary the single projection rule emits. [5]

### Cross-Repo References

No cross-repository implementation participates in this status authority.

No meaningful cross-repo references found.

## 260718-CHATS-L5I Current Delta

Status freshness now reflects evidence-expected active states rather than making a quiet, ready conversation look stale. Fresh active pages and events retain their canonical turn state and cursor semantics while genuine working or settlement evidence can still surface staleness.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

**`TurnTransition`** (`state`, `strength`, `turn_id`, `reason`, `waiting`, `terminal_outcome`) is
now the single argument of the internal `_set_turn(transition, *, now)`: **one proposed turn-state
change, and the evidence strength that justifies it**. The state, its turn, what it is waiting on
and how it ended are one observation; the strength is what decides whether this observation may
overwrite the last one. Deciding them separately is how a weak observation overwrites a strong one.
The precedence rules themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
