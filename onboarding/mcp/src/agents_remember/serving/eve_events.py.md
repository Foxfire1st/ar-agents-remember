# mcp/src/agents_remember/serving/eve_events.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Translate eve's documented stream events into the normalized AR adapter event model, and own the one
eve session's normalized state, transcript accumulator and pending interactions. The module docstring
states the three rules the whole mapping follows; each is a protocol guarantee rather than a
preference, and they are the reason this file is load-bearing rather than mechanical.

## Code Commentary

### Logic

`EveEventMapper` is constructed per bridge epoch and driven by `translate(event, cursor=...)`. A
`_HANDLERS` table maps event type to handler; **an event type absent from that table becomes additive
vendor detail** (`eve:<type>`) rather than state the adapter cannot prove.

Three rules govern every mapping:

1. **Deltas are display, completions are content.** `message.appended`/`reasoning.appended` are
   emitted as `delta` events carrying a *streaming* transcript entry; the authoritative finalized
   block is materialized once from `message.completed`/`reasoning.completed`. A block is therefore
   never rendered twice, and a turn cancelled before its completion contributes no assistant text —
   exactly what eve discards from durable history on cancellation. `message.completed` with a `null`
   message is eve's documented intentional-silence delivery: a `state` event with no transcript entry.
2. **Turn boundaries are not session boundaries.** `turn.completed`/`turn.failed`/`turn.cancelled`
   settle one turn; `session.waiting` completes a turn *while leaving the session usable* and carries
   `wait: "next-user-message"`; only `session.completed`/`session.failed` retire the session.
   `_session_waiting` deliberately emits `kind="completed"` with a terminal `TerminalResult`, because
   the turn is what the caller was waiting on.
3. **Identity is exact.** `_require_turn_id` refuses any turn-scoped event naming a turn this session
   never opened, so an interleaved child or parallel session cannot mutate another task's state.
   `turn.started` is the one turn-scoped event whose identity is established by its own arrival.

State precedence in `_derive` is deliberate and total: a caller stating both axes wins, then a pending
input request (which refuses further deliveries), then a stated activity, then the control state, then
the session's own liveness. `publish()` builds the snapshot from explicit inputs plus the mapper's own
state, and the **stream cursor is deliberately not an input**: the mapper is the single owner of the
position it publishes, so a caller cannot publish a snapshot disagreeing with the cursor its own
events advanced.

`bind_session` records the durable id native evidence proved **and publishes it**, so a restarted
bridge can report which session it attached to before any new event arrives.

### Conventions

- Snapshot extras carry `vendorProtocol: "eve-http-session/v1"` and `streamCursor`.
- `EveEventPayload` chooses one payload combination per native event instead of threading five
  independently defaulted switches through every handler.
- Transcript `raw` always records `eveEventType`, `eveEventIndex`, `eveEventId` and `turnId`, so an
  entry stays traceable to the exact durable frame.
- Action results correlate on `callId`; the retained tool-name map is bounded at
  `TOOL_ENTRY_LIMIT` (512) and only labels a result, never gates one.

### Invariants And Boundaries

- **A finalized block is materialized from its completion event only.** Rendering both the deltas and
  the completion would double the block; this is the defect the change set's evidence explicitly
  fails on, and the A2 revision strengthened the case that detects it (the assertion now establishes
  its own premise, names the duplicated block, and checks the ordered assistant sequence).
- **`session.waiting` is not session retirement.** It completes a turn and leaves the session usable
  for the next message.
- **An unknown turn id is a refusal, not an application.**
- The tool-name map bound degrades a *label* when it evicts; a call whose entry was evicted still
  produces its result entry from the frame's own fields. The bound never degrades an event.
- Unmapped event types (`message.received`, `step.started`, `step.completed`, `result.completed`,
  `subagent.*`, `approval.*`, `action.input.appended`) cross as evidence without being reinterpreted
  into AR state.
- `set_model`/`set_effort` honesty is a property of this module's advertised catalog shape, declared
  in the adapter: eve's model and effort are compiled application values, so both are advertised
  `session_settable: False` rather than offered as controls that silently do nothing.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; eve's documented event set is the external authority this table mirrors.

### Repo-Internal References

- The normalized snapshot, transcript entry, terminal result and event types are AR's existing adapter model, not eve-shaped types. [1]
- The event vocabulary and identity fields the mapping consumes are declared once in the wire module. [2]
- Pending interactions are projected into the bounded queue this mapper owns. [3]
- The adapter advances the persisted cursor before handing the event to this mapper, and owns the single replay window the mapper relies on. [4]
- Conformance cases assert both directions for each named scenario: the behavior that must happen and the double-render / cross-contamination failure it would otherwise hide. [5]

### Cross-Repo References

- The translated event set is eve's published durable stream contract at the pinned release. [6]
