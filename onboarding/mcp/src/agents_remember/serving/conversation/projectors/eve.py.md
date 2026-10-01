# mcp/src/agents_remember/serving/conversation/projectors/eve.py

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The eve active projector: maps eve's durable session-stream records — live and replayed through the
same path — into normalized conversation items, blocks, deltas and turn outcomes, and preserves every
shape it does not classify as `unknown-vendor` evidence instead of guessing a meaning.

It is the seam that makes eve observable through the **existing** conversation product: the same
engine, store, mutation stream, status projection and React components the other three harnesses use.
No dashboard file, component or shell was added for eve — the projector is the whole per-harness
contribution.

Its load-bearing subject is the two-boundary event shape. eve emits `turn.completed` and then
`session.waiting` on the same stream, and the adapter reports the park with adapter kind `completed`
and a `completed` terminal result, because AR's terminal vocabulary has no word for "parked". The park
is genuinely **not** a settlement. A projector that forwarded that result would settle the turn twice,
and — since eve emits `session.waiting` after `turn.cancelled` as well — would display a cancelled turn
as completed.

## Code Commentary

### Logic

`map_evidence_frame()` is the whole dispatch: parse the frame, look the event type up in `_HANDLERS`,
and hand off. It takes `evidence_ref` and `parent_thread_id` both marked unused, for a stated reason —
refs are minted engine-side from the item ids returned, and eve multiplexes nothing, so an evidence
stream is one session. The `_HANDLERS` table maps eve's own event names to handlers, and
`_HANDLERS.update(dict.fromkeys(SILENT_CONTROL_EVENTS, _silent))` installs the deliberately-silent set
in one stroke.

`_parse()` reads the event type from the frame's own envelope under `ENVELOPE_TYPE_KEY` (`"type"`) and
raises `UnmappableShape("eve evidence frame carries no event type in its envelope")` when it is
absent. `ENVELOPE_TYPE_KEY`'s docstring records the decision that matters for a reader of the bridge:
eve's evidence envelope is `{"type", "data", "meta"}` and the bridge diverts the whole envelope
verbatim as `EvidenceFrame.raw`, so the discriminator is read **here, in the layer that maps it** —
exactly as the Claude and Pi projectors read the frame type embedded in their payloads —
and `EvidenceFrame.native_method` is deliberately *not* used. The field survives clipping by
documented contract and crosses the daemon wire verbatim.

Four rules decide where a frame lands, and the module docstring states each as a protocol fact rather
than a preference:

1. **Streaming text is one item, revised.** An `*.appended` frame mints its turn's channel item
   *empty* and delivers the text as a block delta (`MappedBlockDelta`); the matching `*.completed`
   frame carries the authoritative block and **revises that same item** (`MappedItem` with
   `revision=1`). One turn therefore shows one assistant item and one thinking item — never a delta
   pile beside a duplicate aggregate. The channel and its item/block ids are derived
   (`_channel`, `_channel_kind`, `_channel_item_id`, `_channel_block_id`, `_empty_block`) so the
   delta and the completion cannot disagree about which item they mean.
2. **A turn boundary is not a session boundary.** `_settled()` is the only constructor of
   `MappedTurnOutcome`, and only `turn.completed`, `turn.cancelled` and `turn.failed` reach it.
   A cancelled turn settles as `interrupted` with stop reason `"cancelled"`; a failed turn captures
   its message. `_waiting_frame` / `_session_parked` emit exactly one session-scoped `notice` item
   with `turn_id is None` under the single item id `_PARKED_ITEM`, so a second park revises that item
   instead of stacking another. Only `session.completed` / `session.failed` retire the release and
   mint a session-scoped outcome.
3. **Identity is exact, and a frame that names no turn is session-scoped.** `_Frame.turn_id` comes
   from `data.turnId` and nothing else; a frame without one is never attributed to a turn by
   guesswork.
4. **Recognized control state mints nothing; an unrecognized frame is preserved.**
   `SILENT_CONTROL_EVENTS` is consumed *by name* by `_silent`, so session/turn/step framing,
   `action.input.appended`, and compaction/context-clearing produce no timeline row while a genuinely
   unknown event still lands as `unknown-vendor`. The set's docstring gives the measurement: those
   frames are six `step.started`, five `step.completed` and four `action.input.appended` of the 52
   frames in the pinned release's recorded run, so letting them fall through would put
   "unknown vendor event" rows on the most frequent frames and hide the genuinely unknown ones.
   Their treatment matches the adapter's own — none produces a transcript entry.

`_item()` is the single item constructor and the honest-provenance rule lives in it: an
`unknown-input` lane item is a durable-record copy whose producer the stream cannot prove, so it takes
`unknown_input_provenance`; everything else takes `harness_provenance`. Items are built with
`revision=1, global_ordinal=1` and the engine owns the real values.

### Conventions

- Every handler is registered by eve's own event name; the module never switches on the payload shape
  to infer the event type.
- A frame that cannot be parsed by its declared keys becomes `unknown-vendor` evidence with the frame
  preserved — never a guessed message, tool or control meaning.
- `_LIVE_ORIGIN` is the one provenance origin string, because every frame the projector sees — live or
  replayed — is a record in eve's durable stream.
- `_Placement` and `_Voice` carry the per-item routing (item id, turn id, lane, source, role, kind,
  phase) so a handler declares *what* it produces and one constructor decides *how*.

### Invariants And Boundaries

- **`session.waiting` must never produce a `MappedTurnOutcome`.** This is the module's reason to
  exist; a projector change that maps the park to a turn outcome reintroduces the double settlement
  and mislabels a cancelled turn as completed.
- **A cancelled turn is `interrupted`, never `completed`.** The catalogue's terminal lift reports
  `interrupted` for that turn, and the UI renders the amber interrupted line.
- **One turn mints exactly one turn outcome.** `_settled` is the only path to one.
- **A frame whose envelope carries no `type` fails closed.** The projector refuses it rather than
  guessing from `data`; the retired design that carried the type out of band is not this module's
  contract.
- **An unclassified event stays visible.** Silently dropping is reserved for the named
  `SILENT_CONTROL_EVENTS` set, and adding a name to that set is a claim that the adapter also renders
  no transcript entry for it.
- **The projector holds no IO, no clock and no engine state.** It is a pure frame grammar; ordinals,
  revisions, provenance resolution and envelopes belong to the engine in the sibling `active/` route,
  and the `_item()` `global_ordinal=1, revision=1` defaults are placeholders the engine overwrites.
- **No native-history page.** eve does not expose one, so `map_native_frame` fails closed rather than
  inventing a page.

### Todos

None known. `map_transcript_echo` exists for the engine's submission echo and is exercised through the
adapter-to-projection integration cases rather than a dedicated case of its own.

## Evidence

### Docs References

No `Domain Documentation` category is configured for this repository, so no live domain-documentation
pass was available for this file. eve's own published protocol documentation is the external authority
the envelope shape mirrors, and it is cited through the runtime README rather than a documentation
registry.

No configured `Domain Documentation` source exists in `system/sources.md`; the `{"type","data","meta"}` envelope is eve's published wire contract, cited by the runtime README.

### Repo-Internal References

The projector is registered in the sibling `__init__.py` and consumes frames the bridge diverts from
the adapter; its mapper outputs are the engine's input.

- The projector registers under the `eve` harness id, so every registered harness id has a projector and the engine reaches it without a special case. [1]
- The registered projector declares the durable stream as its only evidence surface, so both other channels fail closed. [2]
- The one dispatch, and the deliberate silence of the named control set. [3]
- The envelope discriminator is read from the diverted payload, not from an out-of-band carrier, and a frame with none is refused. [4]
- The only constructor of a turn outcome, and the park that deliberately is not one. [5]
- Streaming text mints one item and the completion revises it, with ids derived so delta and completion cannot disagree. [6]
- The honest-provenance rule for a durable-record copy whose producer the stream cannot prove. [7]
- The `HarnessId` union gained `eve`, which the projector protocol types `harness_id` with. [8]
- The cases: one settlement per turn, the park as a notice, cancellation as interrupted, one tool round trip as one item, the preserved unknown event, and silence for recognized control state. [9]
- The projector's whole event vocabulary is classified, and the recorded run's types are pinned against it. [10]
- The same facts on frames the real adapter and the real bridge produced in-process, so the fixture is not the only evidence. [11]
- The catalogue's own terminal lift over a cancelled-then-parked page still reports interrupted. [12]

### Cross-Repo References

The frame shapes this projector parses are eve's, as the pinned third-party release emits them; the
AR-owned runtime application is the thing that produces them.

- The event names this projector switches on are the pinned release's own vocabulary, authored by the AR-owned runtime application's channel. [13]
