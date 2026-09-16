# mcp/src/agents_remember/serving/conversation/projectors/eve.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/eve.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| lastVerifiedCommitDate | 2026-09-16T13:48:06+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No `Domain Documentation` category is configured for this repository, so no live domain-documentation
pass was available for this file. eve's own published protocol documentation is the external authority
the envelope shape mirrors, and it is cited through the runtime README rather than a documentation
registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source exists in `system/sources.md`; the `{"type","data","meta"}` envelope is eve's published wire contract, cited by the runtime README. | — | — |

## Repo-Internal References

The projector is registered in the sibling `__init__.py` and consumes frames the bridge diverts from
the adapter; its mapper outputs are the engine's input.

| Finding | Anchor | Source |
| --- | --- | --- |
| The projector registers under the `eve` harness id, so every registered harness id has a projector and the engine reaches it without a special case. | `_EveProjector`; `PROJECTORS` | mcp/src/agents_remember/serving/conversation/projectors/__init__.py:115-125; mcp/src/agents_remember/serving/conversation/projectors/__init__.py:128-133 |
| The registered projector declares the durable stream as its only evidence surface, so both other channels fail closed. | `uses_native_pages`; `uses_transcript_echo`; `eager_native_continuation` | mcp/src/agents_remember/serving/conversation/projectors/__init__.py:119-121 |
| The one dispatch, and the deliberate silence of the named control set. | `map_evidence_frame`; `_HANDLERS`; `_silent`; `SILENT_CONTROL_EVENTS` | mcp/src/agents_remember/serving/conversation/projectors/eve.py:94-114; mcp/src/agents_remember/serving/conversation/projectors/eve.py:147-159; mcp/src/agents_remember/serving/conversation/projectors/eve.py:178-181; mcp/src/agents_remember/serving/conversation/projectors/eve.py:316-340 |
| The envelope discriminator is read from the diverted payload, not from an out-of-band carrier, and a frame with none is refused. | `ENVELOPE_TYPE_KEY`; `_parse`; `_Frame` | mcp/src/agents_remember/serving/conversation/projectors/eve.py:76-76; mcp/src/agents_remember/serving/conversation/projectors/eve.py:128-144; mcp/src/agents_remember/serving/conversation/projectors/eve.py:162-175 |
| The only constructor of a turn outcome, and the park that deliberately is not one. | `_settled`; `_waiting_frame`; `_session_parked`; `_PARKED_ITEM` | mcp/src/agents_remember/serving/conversation/projectors/eve.py:91-91; mcp/src/agents_remember/serving/conversation/projectors/eve.py:243-272; mcp/src/agents_remember/serving/conversation/projectors/eve.py:275-276; mcp/src/agents_remember/serving/conversation/projectors/eve.py:689-707 |
| Streaming text mints one item and the completion revises it, with ids derived so delta and completion cannot disagree. | `_appended`; `_completed`; `_channel`; `_completed_channel`; `_channel_item_id`; `_empty_block` | mcp/src/agents_remember/serving/conversation/projectors/eve.py:365-394; mcp/src/agents_remember/serving/conversation/projectors/eve.py:397-435; mcp/src/agents_remember/serving/conversation/projectors/eve.py:721-724; mcp/src/agents_remember/serving/conversation/projectors/eve.py:727-735; mcp/src/agents_remember/serving/conversation/projectors/eve.py:742-745; mcp/src/agents_remember/serving/conversation/projectors/eve.py:752-759 |
| The honest-provenance rule for a durable-record copy whose producer the stream cannot prove. | `_item`; `unknown_input_provenance`; `harness_provenance` | mcp/src/agents_remember/serving/conversation/projectors/eve.py:825-860 |
| The `HarnessId` union gained `eve`, which the projector protocol types `harness_id` with. | `HarnessId` | mcp/src/agents_remember/models/conversations/identity.py:10-10 |
| The cases: one settlement per turn, the park as a notice, cancellation as interrupted, one tool round trip as one item, the preserved unknown event, and silence for recognized control state. | `EveProjectorTests` | mcp/tests/test_eve_product_integration.py:1106-1276 |
| The projector's whole event vocabulary is classified, and the recorded run's types are pinned against it. | `test_the_projector_classifies_the_adapters_whole_event_vocabulary`; `test_the_recorded_run_only_emits_types_the_adapter_can_yield`; `_PINNED_RUN_CENSUS` | mcp/tests/test_eve_product_integration.py:248-264; mcp/tests/test_eve_product_integration.py:1238-1245; mcp/tests/test_eve_product_integration.py:1247-1251 |
| The same facts on frames the real adapter and the real bridge produced in-process, so the fixture is not the only evidence. | `EveAdapterToProjectionIntegrationTests` | mcp/tests/test_eve_product_integration.py:1279-1338 |
| The catalogue's own terminal lift over a cancelled-then-parked page still reports interrupted. | `EveTerminalProjectionTests`; `latest_terminal_evidence` | mcp/tests/test_eve_product_integration.py:1673-1674; mcp/tests/test_eve_product_integration.py:1682-1683; mcp/tests/test_eve_product_integration.py:1691-1695 |

## Cross-Repo References

The frame shapes this projector parses are eve's, as the pinned third-party release emits them; the
AR-owned runtime application is the thing that produces them.

| Finding | Anchor | Source |
| --- | --- | --- |
| The event names this projector switches on are the pinned release's own vocabulary, authored by the AR-owned runtime application's channel. | `turnPolicy` | eve_runtime/agent/channels/eve.ts:17-17; eve_runtime/package.json:14-20 |

## Update History
- 2026-09-16T11:41:33+00:00: Generated citation repair: `test_the_projector_classifies_the_adapters_whole_event_vocabulary`; `test_the_recorded_run_only_emits_types_the_adapter_can_yield`; `_PINNED_RUN_CENSUS` repointed to mcp/tests/test_eve_product_integration.py:1238-1245; mcp/tests/test_eve_product_integration.py:1247-1251; mcp/tests/test_eve_product_integration.py:248-264. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:41:33+00:00: Generated citation repair: `turnPolicy` repointed to eve_runtime/agent/channels/eve.ts:17-17. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: created this card for a file added by the eve
  product-integration change set. Records the two-boundary rule that is this module's reason to exist
  (`turn.*` settles, `session.waiting` parks and never mints a turn outcome; a cancelled turn displays
  as interrupted), the streaming-text rule that one turn shows one revised item rather than a delta
  pile, the by-name silence set with its measured counts from the pinned run, the envelope-type
  discriminator read from the diverted payload, and the honest-provenance rule for a producer the
  stream cannot prove. Verification metadata is pinned to the leaf's synced base commit `ff97072c`
  because the candidate is deliberately uncommitted — the governed closeout stamps the real code
  commit, and no hash or fingerprint was invented here.
