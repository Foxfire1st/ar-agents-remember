# mcp/src/agents_remember/serving/eve_events.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/eve_events.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `609756111eb3c239d0563d8631bfd564645bc9d1` |
| lastVerifiedCommitDate | 2026-09-16T10:25:13+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; eve's documented event set is the external authority this table mirrors. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The normalized snapshot, transcript entry, terminal result and event types are AR's existing adapter model, not eve-shaped types. | `AdapterSnapshot`; `TranscriptEntry`; `TerminalResult`; `AdapterEvent`; `AR_EVIDENCE_KEY` | mcp/src/agents_remember/serving/harness_control_models.py:1-260; mcp/src/agents_remember/models/conversations/evidence.py:1-120 |
| The event vocabulary and identity fields the mapping consumes are declared once in the wire module. | `INTERACTION_REQUEST_EVENT_TYPE`; `AUTHORIZATION_REQUIRED_EVENT_TYPE`; `EveStreamEvent.turn_id` | mcp/src/agents_remember/serving/eve_protocol.py:59-70; mcp/src/agents_remember/serving/eve_protocol.py:76-99 |
| Pending interactions are projected into the bounded queue this mapper owns. | `EveInteractionQueue` | mcp/src/agents_remember/serving/eve_interactions.py:34-109 |
| The adapter advances the persisted cursor before handing the event to this mapper, and owns the single replay window the mapper relies on. | `EveSessionAdapter._translate`; `EveEventDeduplicator` | mcp/src/agents_remember/serving/eve_adapter.py:615-644; mcp/src/agents_remember/serving/eve_protocol.py:224-268 |
| Conformance cases assert both directions for each named scenario: the behavior that must happen and the double-render / cross-contamination failure it would otherwise hide. | `EveAdapterIsolationTests`; `EveAdapterSessionCompletionTests`; `EveAdapterQueuePolicyTests`; `EveAdapterSubmissionTests` | mcp/tests/test_eve_adapter.py:1024-1128; mcp/tests/test_eve_adapter.py:959-1023; mcp/tests/test_eve_adapter.py:604-660; mcp/tests/test_eve_adapter.py:371-603 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| The translated event set is eve's published durable stream contract at the pinned release. | supported stream versions; event-type sets | mcp/src/agents_remember/serving/eve_protocol.py:32-56 |

## Update History

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): **no code change in this module
  between the A1 and A2 candidates** — the A2 round strengthened the case that guards this module's
  first invariant rather than the module itself. The card therefore keeps its body, adds the fact that
  the A2 revision made the double-render guard able to fail (premise asserted, duplicate named, whole
  ordered sequence checked), and adds the replay-window owner its mapper depends on. All three citation
  tables were rewritten into the `Finding | Anchor | Source` shape (identifier alone in Anchor,
  `path:start-end` plain in Source), because the superseded `Finding | Citations | Source Path` form is
  a live memory-quality finding family. Verification metadata moves to the leaf's current base
  `e9300687`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a file added by the native
  eve session-adapter change set. Records the three translation rules, the total state precedence, the
  single-owner cursor boundary, and the two negative-knowledge items a successor must not undo
  (double-rendering a block; treating `session.waiting` as session retirement). Verification metadata
  is pinned to the leaf's base commit `67b21aeb` because the candidate is deliberately uncommitted —
  the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
