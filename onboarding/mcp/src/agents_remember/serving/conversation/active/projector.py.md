# mcp/src/agents_remember/serving/conversation/active/projector.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T00:02+02:00 |
| lastVerifiedCommitHash | `a401e3dba0bc6e9723451edbfdefb8d77c42945d`|
| lastVerifiedCommitDate | 2026-07-27T00:27:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The active session projector engine: one projector per running session/epoch. It
hydrates the projection from native authority (native pages where the harness has them, the
live evidence window otherwise), keeps it current through bounded IPC polls, mints the totally
ordered event stream with bounded retention, and closes established streams with one typed
`gap` on epoch/generation/ordering loss. The 1,000-entry TranscriptEntry deque is never paged
as history authority. The ONE projector also serves a multiplexed
session: harness sub-agent threads (codex collab threads, claude sidechains) are demuxed out
of the same evidence/snapshot stream and projected as first-class conversation participants
carrying a `ConversationAgentRef`, never as anonymous parent content.

## Code Commentary

### Logic

`ActiveSessionProjector` (L209-L1406) binds one exact identity plus mapper and owns hydration,
polling, the store, the status service, retention, and subscriber fan-out. Hydration
(`_rebuild` L402-L439) re-derives the whole projection from native authority: native-page walks
for harnesses that have them (`_walk_native_pages` L441-L473 — failing closed honest-partial
for ephemeral codex threads), the live evidence window, the echo channel, eager native
continuation for pi, provenance resolution, and a first snapshot observation. `_rebuild` also
primes `self._snapshot` BEFORE the evidence walk (L419-L422)
so multiplexed agent frames hydrate with the identity the adapter's `agentRegistry` already
bound; the fresh read later in hydration still owns status/interaction authority. `page`
(L301-L339) captures the window, event cursor, and status under `_apply_lock` after refreshing
the native tip and driving the per-thread agent native backfill — the atomic page+eventCursor
the design demands; `total_items` is emitted only
when the native walk completed, the evidence window never evicted, and no zipper frames pend
(L318-L322). Poll cycle (`poll_once` L368-L391) runs the four channels then folds the snapshot
into canonical status, emitting a status mutation only on revision advance. Channels:
`_poll_evidence` (L597-L628) pages the bounded evidence window and raises
`ZipperEvidenceEvicted` (L111-L119) when an advancing eviction floor voids the echo zipper's
turn-order guarantee (review finding F3 — one `ordering-fault` gap + close; non-echo harnesses
just clear totals honestly) and `EvidenceTimelineRegressed` (L122-L129) when the bridge
re-baselines its tip backward; `_poll_transcript_echo` (L734-L786) is the Claude echo zipper —
it consumes ONLY `role == "user"` transcript entries as submission echoes; assistant/result
entries (claude_stream_state emits `role="assistant"`/`"result"`) are advanced past by
recording their sequence and continuing, never fed to the user-only echo mapper (feeding them
was what minted the spurious `claude:echo: unrecognized submission echo shape` rows observed on the live wire). For a user echo the adapter accepts one turn at a
time, so echoes and frames merge by strict turn order without timestamps, flushing a turn's
frames through its result before the next user item; `_poll_native_continuation` (L1010-L1032)
eagerly re-reads pi entries so live items always carry native identity; `_resolve_provenance`
(L1034-L1049) batches pending user items through the real submission-provenance authority.

Multiplexed sub-agent demux (OQ-1). Every evidence frame is classified by
`_frame_agent_thread` (L646-L657) on its verbatim `thread_id`: `None` or the projection
identity's `vendor_conversation_id` maps to the parent bucket — byte-identical to the
pre-multiplexing behavior — anything else is one agent thread. The mapper receives the demux context
(`parent_thread_id=self._identity.vendor_conversation_id`, L923-L929). Agent-thread outputs
then pass through `_bind_agent` (L974-L1008), which attaches a `ConversationAgentRef` resolved
by `_agent_ref` (L949-L972) from the LAST polled snapshot's `raw['agentRegistry']`, crossed
through `_REGISTRY_AGENT_STATUS` (L144-L158 — anything outside the table, e.g. `unresolved`/
`idle`, honestly stays `unknown`). Mapper-tagged items (roster rows, agent turn-results) keep
their own evidence-bound ref; the registry only FILLS what the frame could not know
(`agent_path`, a still-`unknown` status). A malformed known shape still degrades to preserved
unknown-vendor evidence (L930-L943) — never a stream failure, never guessed — and since
fix-round finding 4 a malformed AGENT-thread frame is tagged with the agent's ref too, so its
evidence lands in the agent's view, never the parent's. Deltas and turn outcomes carry no item
payload and pass through unbound.

Per-thread F1 buckets. The live-settled-natives filter's flat sets became
`dict[str | None, set[str]]` keyed by demux bucket (L265-L271): `None` is the parent bucket
(byte-identical to the pre-multiplexing flat sets); each agent thread gets its own so a parent native
re-walk can never be suppressed by an agent thread's colliding turn id. `_record_live_turn`
(L659-L683) and `_drop_live_settled_natives` (L685-L732) take the bucket; the parent walk
passes `None` (L456-L460), an agent walk passes its thread id. A turn registers as live-settled
ONLY from content-bearing items: `_record_live_turn` adds a turn id when a `MappedItem`'s kind
is in `_CONTENT_ITEM_KINDS` (L204-L206 — message/tool-call/tool-result/thinking/plan) or a
preserved `MappedUnknownVendor` carries one; a bare `MappedTurnOutcome` no longer registers.
Lifecycle frames alone prove nothing about content delivery — a fast agent can emit lifecycle
while its items never reach the connection — so the twin suppression must not drop a native
backfill that is the turn's only content source. `_agent_threads_live`
(L272-L274) records which agent threads produced live-evidence items — the eligibility gate
for the per-thread native re-walk.

Page-driven per-thread native backfill (OQ-1 / fix-round finding 3, no longer latent).
`page()` drives `_backfill_agent_threads` (L483-L501) on every call: every live agent thread
gets ONE lazy native walk per projector, tracked by `_agent_native_walked` (L275-L276, cleared
in `_rebuild` L417 and `_release_dormant_state` L1394); `_walk_agent_native_pages` (L527-L575)
returns bool, and a failed or guard-refused walk stays unwalked so the next page retries. The
vendor's auto-attach of sub-agent listeners is best-effort and a fast agent can outrun it, so
live wire delivery of agent content can be incomplete (roster and completion crossed the live
wire, the agents' content did not); `thread/read` remains the authority. The walk
thread-scopes every native item id through `_scope_agent_native_item` (L577-L593) to
`<threadId>:<nativeId>` — the evidence handle is scoped the same way (L543-L545): positional
native ids (`item-N`) are unique per thread, never across the multiplex, and a forked agent
thread replays the parent's items under the SAME ids, so the store's id-keyed dedupe would
otherwise let the agent's copies overwrite the parent's items (parent content carrying an
agent's ref). The walk mints NO roster items from collab/`subAgentActivity` records (filtered
by the `codex-agent-` id prefix, L551-L564): roster minting belongs to the live channel and the
parent's native walk, and nested-agent spawn records reference OTHER threads, so minting them
here would duplicate/misattribute roster rows. Outputs are F1-filtered under the thread's own
bucket and agent-bound; the walk fails closed exactly like the parent walk (HarnessControlError
→ honestly partial live window, the next page retries). `refresh_agent_native` (L503-L525)
stays the public per-thread seam the page loop (and the codex-agents suite) drives:
native-page harnesses only, never the parent thread, only once the agent produced live items.
Completeness bookkeeping (`_native_complete`/`total_known`) stays parent-scoped: an agent walk
is additive and never widens the page's total assertion.

Multiplexed pending interactions (R6). `_apply_interaction_transitions`
(L1071-L1083) keeps the singular-slot parent path and adds ROTATION semantics: when the slot's
interaction id CHANGES (the adapter's per-thread pending map rotates the next-oldest parent
pending into the slot once the oldest settles), the evicted id settles exactly as if the slot
had emptied — a rotation is a resolution, not only an emptying.
`_apply_agent_interaction_transitions` (L1085-L1125) projects EVERY server request in
`snapshot.pending_interactions`: agent-thread requests become interaction-lane items labeled by
`_interaction_agent_ref` (L1127-L1139 — registry identity plus the adapter-bound
`raw['agentLabel']` as nickname), while concurrent PARENT-thread pendings beyond the singular
slot's oldest project plainly with no agent ref (concurrent parent pendings are normal vendor
traffic now that the adapter keeps a per-thread pending map). Entries without a valid
`raw['threadId']` are still skipped, and the singular-slot entry (same interaction id) is never
double-projected; an id rotated OUT of the tuple INTO the singular slot stays live there — the
singular path owns its resolution. Cleared interactions otherwise resolve per id, mirroring the
singular path; `_pending_agent_interaction_ids` (L277) tracks which are currently projected.

Envelopes mint with total order — sequence, `previousCursor` chain, generation-scoped event id
(`_mint_envelope` L1206-L1220) — and `_publish` (L1254-L1271) retains every envelope and, on a
full subscriber queue, mints ONE shared `retention-overflow` gap per sweep (retained, keeping
the sequence hole-free for all consumers) and delivers exactly one gap + close sentinel via
`_offer_evicting` (L1310-L1319, review finding F2). `GapMutation.requested_after` names the
last good retained cursor (L1290-L1292). The poll loop (`_run` L1341-L1375) maps epoch
mismatch to a `generation-changed` gap, zipper/validation failures to `ordering-fault`, and
sustained authority loss (5 consecutive read failures, L104) to a final `generation-changed`
gap — the next page reports the session truth. Projectors idle-stop with no subscribers past
`CONSUMER_TTL_SECONDS` (L103); at that idle-break `_release_dormant_state` (L1377-L1395)
CLEARS the full heavy projection — a fresh `ProjectionStore`, the per-thread live-turn and
request buckets, `_agent_threads_live`, `_agent_native_walked`, `_pending_agent_interaction_ids`, the retained SSE envelopes
(`_retention`), the retention floor, and any pending frames — and sets `_closed`, so a dead
session's memory is freed immediately instead of lingering as a registered tombstone until
32-LRU eviction; `matches()` (L283-L291) returns False while closed, so
the next access re-creates a fresh projector keyed on session+epoch+vendor identity.

### Live-settled-natives filter (disjoint-id-namespace twin suppression)

On a hosted codex `+ Chat` thread the two projection channels use DISJOINT id namespaces for the
same settled turn: the live notification channel emits UUID/`msg_*` item ids while `thread/read`
returns positional `item-N` ids. `ProjectionStore.apply_item` dedupes by item id, so the two can
NEVER converge, and `_refresh_native_tip`'s post-turn native re-walk (`_walk_native_pages` from
`cursor=None`) re-projected every settled turn as a SECOND `unknown-input`/`native-history` twin
(deterministic 2/2 turns on the real wire; the user twin rendered as an
authority-downgraded `unknown-input` row beside its resolved live twin).

Fix (path (a) — correlate native frames to already-projected live turns; the codex lazy-native path
only, since pi shares one id namespace across channels and claude has no native pages). As each live
evidence frame settles, `_record_live_turn(outputs, bucket)` records the turn ids whose CONTENT
crossed (`_live_turn_ids[bucket]` — a turn id registers only from a `MappedItem` whose kind is in
`_CONTENT_ITEM_KINDS`, or from a preserved unknown-vendor output carrying one, never from a bare
turn outcome, so a lifecycle-only turn is not mistaken for delivered content) and the user
`clientId`s it submitted (`_live_request_ids[bucket]`) —
the bucket is the demuxed thread (`None` = parent). `_walk_native_pages`
then filters each native frame's mapped outputs through `_drop_live_settled_natives(outputs,
live_native_turns, bucket)`: a native output is dropped when its `turn_id` is in the bucket's live
turn set (live-by-turn), OR when its native user frame carries a `request_id` in the bucket's live
request set (live-by-client — the clientId is our own submitted request id and survives verbatim
into `thread/read`, so this holds even if the hosted thread RENUMBERS turn ids), OR when its turn
was already anchored earlier in this walk (live-by-sibling via the walk-scoped `live_native_turns`
set — codex stores a turn's items user-first, so the user frame anchors the turn and its harness
siblings drop too). Dropped frames still advance `_native_cursor`.

Untouched pre-live hydration path (LOAD-BEARING). `_rebuild` CLEARS both live maps (and
`_agent_threads_live`, `_agent_native_walked`, and `_pending_agent_interaction_ids`) before the hydration
walk, and the native walk runs BEFORE the first evidence poll, so at hydration both sets are empty
by construction — a resumed thread hydrates its FULL prior-session native history
(`item-1..item-N`, genuine history, never seen live). Nothing is merged across ids: duplicates are
only SUPPRESSED when the live turn already carries them, never fabricated; item-evidence
turn correlation stays the production path (the fix keys off the same shared `turnId`+`clientId`
evidence, never a guessed identity), the exact-native-id identity rules hold, and no optimistic item
is invented. The H2 store pin operates WITHIN one item id and never crosses these namespaces, so the
two fixes are disjoint. Proven before/after on the real codex 0.144.5 wire (installed regression:
the settled turn projects once; stashed `projector.py` fails `2 != 1`) and on the resumed-thread
mixed prior-history + live-turns edge.

Recorded-not-hardened boundary (medium). The F1 suppression is scoped to turns settled live
in THIS projector run. A distinct, un-observed path — a FRESH projector hydrating MID-SESSION whose
bounded live-evidence buffer still replays turns already persisted in `thread/read` — could in
principle overlap at the single hydration walk (where both live sets are empty). That was not the
proven failure, was not observed by the reviewer, and a complete fix (evidence-before-native
reordering) would disturb native/live chronological ordering; it is left as a recorded second-half
consideration. Invalidation signal: a live capture of that overlap on a real reconnect.

### Conventions

Native pages are history authority where they exist (codex persisted threads, pi entries); the
bounded evidence window is the live tail; the transcript channel carries ONLY the Claude
submission echo (user submissions), never history. All blocking IPC reads are offloaded via
`asyncio.to_thread`. Resource bounds are explicit constants (L98-L105): 1 s polls, 500-frame
evidence pages, 200-frame native pages, 1000-envelope retention, 256-deep subscriber queues,
64-record provenance batches. Agent identity is registry-filled, never fabricated: a
`ConversationAgentRef` carries at minimum the bare thread id with `status="unknown"`, and the
registry may lag the evidence stream by one poll cycle — roster items carry their own
frame-derived status regardless.

### Invariants And Boundaries

- Recovery re-pages native authority: hydration rebuilds from native pages/evidence reads,
  never from event retention; rehydration reproduces the identical projection with a new cursor
  generation.
- Hosted codex live notifications and `thread/read` history use DISJOINT id namespaces (live
  UUID/`msg_*` vs positional `item-N`) for the same settled turn, so id-keyed dedupe can never
  converge them (F1). The native-tip re-walk drops any native output whose turn was already
  settled live — matched by turn id, by submitted `clientId` (renumber-robust), or by an
  already-anchored sibling — so a live turn is never re-projected as an `unknown-input`/
  `native-history` twin — and a turn counts as settled live only when its content crossed (a
  `_CONTENT_ITEM_KINDS` item or preserved unknown-vendor evidence), so a lifecycle-only turn
  never suppresses the backfill that is its only content source. Suppression only; nothing is
  merged across ids or fabricated. The
  suppression state is bucketed PER THREAD: the parent walk consults only
  the parent bucket, so an agent thread's colliding turn id can never suppress parent history
  (and vice versa). At hydration all buckets are empty (`_rebuild` clears them, the native walk
  precedes the first poll), so prior-session native history hydrates in full. The mid-session
  hydration-overlap path is a recorded, un-hardened boundary.
- Agent demux is evidence-keyed and fail-closed: the demux key is the frame's
  verbatim `thread_id` against the identity's `vendor_conversation_id`; a frame without a thread
  (or with the parent id) is the parent exactly as in the pre-multiplexing behavior. A malformed agent-thread frame degrades
  to preserved unknown-vendor evidence tagged with the AGENT's ref — it never kills the stream,
  is never guessed, and never leaks into the parent's view (fix-round finding 4). A
  `ConversationAgentRef` is never fabricated beyond the bare id: `agent_path`/status come only
  from the adapter's registry, and unmapped registry statuses stay `unknown`.
- The per-thread native backfill is page-driven and honest-partial: `page()` walks each live
  agent thread's native history once per projector (`_agent_native_walked`; a failed or refused
  walk stays unwalked so the next page retries), native-page harnesses only, never the parent
  thread, gated on the agent having produced live items, and additive only — completeness
  bookkeeping (`_native_complete`/`total_known`) stays parent-scoped, so an agent walk never
  widens the page's total assertion (fix-round finding 3). Walked item ids are thread-scoped
  (`<threadId>:<nativeId>`) so a forked agent thread's replayed `item-N` copies can never
  overwrite the parent's items, and an agent walk mints no roster rows (the `codex-agent-`
  filter) — roster minting belongs to the live channel and the parent's native walk.
- Multiplexed interactions keep the singular parent slot authoritative (R6): the slot carries the
  parent's OLDEST pending, every `pending_interactions` tuple entry projects (agent entries
  labeled by `_interaction_agent_ref`; concurrent parent-thread entries beyond the oldest project
  plainly, never skipped for matching the projection's own thread id — only a missing/non-string
  `raw['threadId']` skips), the singular-slot entry is never double-projected, a singular-slot
  ROTATION resolves the evicted id while the id rotated into the slot stays live under the
  singular path, and cleared interactions otherwise resolve per id exactly like the singular path.
- The established stream gets exactly one typed gap (`requiresRepage`, `closeAfterEvent`) per
  failure class — never silent loss, never an HTTP reset.
- No raw native payload reaches any public item: unknown shapes carry a safe summary and an
  opaque coordinate evidence ref (`ar-ev:`/`ar-native:`/`ar-echo:`, L1399-L1406) only.
- Unknown evidence never becomes `ready`; terminal outcomes feed canonical status from native
  evidence only (via `MappedTurnOutcome` → `TurnTerminalEvidence`).
- Only `role == "user"` transcript entries are consumed as Claude submission echoes; assistant/
  result entries are advanced past (their sequence recorded) and never fed to the user-only echo
  mapper, so no spurious `claude:echo` unknown-vendor row is minted.
- A projector that goes dormant (no subscribers past the consumer TTL) releases its heavy
  projection at the idle-break and marks itself closed; it must never be re-driven after
  `_release_dormant_state` — the next access re-creates a fresh projector rather than reviving the
  emptied one. Nothing else may hold a live reference to a released projection's `ProjectionStore`
  or id-sets (the `_agent_threads_live`/`_agent_native_walked`/`_pending_agent_interaction_ids` sets are
  released the same way).

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The evidence/native-page/provenance
seam contracts are the repository-owned IPC substrate cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this engine. | — | — |

## Repo-Internal References

The validated IPC reads are the only substrate channels; the store is the idempotence
authority; the status service owns canonical classification; the mappers are pure frame
grammars; the production-route suite drives this engine over a real socket. The
snapshot/frame grammar carries the multiplexing fields this engine demuxes
on, and a dedicated codex sub-agent suite pins the per-thread behavior including the
page-driven per-thread native backfill and its thread-scoped ids.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `read_control_evidence`/`read_control_native_page`/`read_control_transcript`/`read_submission_provenance` are the validated IPC reads this engine polls; `read_control_native_page` takes the optional `thread_id` selector for multiplexed harnesses. | L326-L418 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| `EvidenceFrame.thread_id` is the demux key and `AdapterSnapshot.pending_interactions` carries the multiplexed agent pendings this engine projects. | L226-L234; L471-L478 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| `EvidencePage`/`NativeEvidencePage`/`SubmissionProvenanceBatch` define the page/batch products. | L482-L533 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The store applies mapper outputs idempotently and converges tool blocks. | L124-L214 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| The status service folds each snapshot plus pending terminal evidence into the canonical envelope. | L320-L338 | [status.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/status.py) |
| The production-route suite proves ordering, idempotence, epoch-flip gap+close, and orchestration parity over a real socket. | L374-L919 | [test_conversation_active_api.py](agents-remember/mcp/tests/test_conversation_active_api.py) |
| The codex sub-agent suite pins the multiplexed projection: demux, roster/agent refs, per-thread F1 buckets, the page-driven agent native backfill (thread-scoped ids, no roster minting from spawn records, walk-once marking), and the concurrent-parent-pendings projection with the singular-rotation resolution semantics. | L1-L930 | [test_conversation_projector_codex_agents.py](agents-remember/mcp/tests/test_conversation_projector_codex_agents.py) |

## Cross-Repo References

No cross-repository implementation participates in this engine.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Live Tail And Page Completeness Delta

The projector now carries the live Claude tail, pending evidence, and page completeness with stricter ordering boundaries. It keeps non-turn trailing frames from being treated as user/assistant turn bodies and preserves honest recovery when a resumable projection cannot establish a coherent sequence.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-27T00:02+02:00 — 260718-CHATS-L7R curator: recorded the sub-agent surface remediation —
  `page()` now drives a per-thread native backfill loop (`_backfill_agent_threads`: one lazy walk
  per live agent thread per projector, `_agent_native_walked` walk-once tracking, failed/refused
  walks stay unwalked so the next page retries, the set cleared in rebuild/dormant) because the
  vendor's best-effort auto-attach lets a fast agent outrun live delivery (`thread/read` stays the
  authority); the agent walk thread-scopes native item ids (`_scope_agent_native_item` →
  `<threadId>:<nativeId>`) so a forked thread's replayed `item-N` copies cannot overwrite parent
  items, and mints no roster rows (the `codex-agent-` filter — nested spawn records reference
  other threads); `_record_live_turn` now registers a turn as live-settled only from
  content-bearing items (`_CONTENT_ITEM_KINDS`; a bare `MappedTurnOutcome` no longer registers),
  so a lifecycle-only turn never suppresses the backfill that is its only content source.
  `refresh_agent_native` is no longer latent — the page loop is its production driver. Re-anchored
  every citation below the change (the file grew 1343 → 1409 lines) and refreshed the reference
  rows (client reads L326-L418, models demux L226-L234;L471-L478, page/batch L482-L533, codex
  suite L1-L930). Verification metadata stays pinned — the change is uncommitted.
- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the concurrent-parent-pending
  projection rework: `_apply_agent_interaction_transitions` now projects EVERY pending in the
  tuple (concurrent parent-thread entries beyond the singular slot's oldest project plainly with
  no agent ref — the adapter's per-thread pending map makes them normal traffic; only a
  missing/non-string `raw['threadId']` skips), and the singular-slot path gained ROTATION
  semantics (a slot id change resolves the evicted id; an id rotated OUT of the tuple INTO the
  slot stays live under the singular path). Re-anchored the citations below the change (the file
  grew 1339 → 1343 lines: `_mint_envelope` L1141-L1155, `_publish` L1189-L1206, `_offer_evicting`
  L1245-L1254, `_run` L1276-L1310, `_release_dormant_state` L1312-L1329, evidence refs
  L1333-L1340) and refreshed the codex-agents suite row (L1-L850). Verification metadata stays
  pinned — the change is uncommitted.
- 2026-07-26T15:34 — 260718-CHATS-L7 curator: harness sub-agents became first-class projection
  participants. Recorded the per-thread demux (`_frame_agent_thread` on the frame's verbatim
  `thread_id`; `parent_thread_id` mapper context), the registry-filled `ConversationAgentRef`
  binding (`_agent_ref`/`_bind_agent` + `_REGISTRY_AGENT_STATUS` — fill-only, never fabricated;
  malformed agent frames degrade to agent-tagged unknown-vendor evidence, never stream-fatal,
  fix-round finding 4), the per-thread F1 twin-suppression buckets (`_live_turn_ids`/
  `_live_request_ids` keyed by thread, `None` = parent, byte-identical pre-L7 behavior), the
  LATENT `refresh_agent_native`/`_walk_agent_native_pages` per-thread backfill seam (no
  production caller, parent-scoped completeness, fix-round finding 3), the multiplexed
  `pending_interactions` projection with the parent-only guard (R6), hydration-time snapshot
  priming, and the dormant-release coverage of the new L7 sets. Refreshed every stale line
  citation against the post-L7 source (the file grew ~890 → 1339 lines), added the
  multiplexing-grammar and codex-agents-suite reference rows. Verification metadata stays
  pinned — the L7 change is uncommitted, so no commit hash can attest it.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded R3 + R5-active. R3: `_poll_transcript_echo`
  now consumes ONLY `role == "user"` transcript entries as echoes and advances past assistant/result
  entries (their sequence recorded), so the spurious `claude:echo: unrecognized submission echo shape`
  rows from image3 no longer mint. R5: the dormant idle-break now calls `_release_dormant_state`, which
  clears the full heavy projection (fresh ProjectionStore, the L5 `_live_turn_ids`/`_live_request_ids`,
  the retained SSE envelopes, retention floor, pending frames) and sets `_closed`, freeing a dead
  session's memory immediately instead of holding it resident as a registered tombstone until 32-LRU
  eviction (`matches()` returns False while closed → next access re-creates a fresh projector).
  Verification metadata stays pinned until L5F closeout stamps the candidate commit.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: documented the F1 live-settled-natives filter —
  the disjoint-id-namespace truth (hosted codex live UUID/`msg_*` ids vs `thread/read` positional
  `item-N`), `_record_live_turn` recording settled turn ids + submitted `clientId`s and
  `_drop_live_settled_natives` suppressing the native-tip re-walk's twins (turn-id match, clientId
  anchoring that survives a turn-id renumber, walk-scoped sibling anchoring), the untouched pre-live
  hydration path (`_rebuild` clears both live sets, native walk precedes the first poll, so
  prior-session history hydrates in full), and the L5.R6 mid-session hydration-overlap
  recorded-not-hardened boundary. Suppression only — nothing merged across ids or fabricated;
  proven before/after on the real codex 0.144.5 wire. Verification metadata stays pinned until L5
  closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the projector
  engine — native hydration, bounded polls, the Claude echo zipper, total-order envelopes,
  bounded retention/fan-out, review-F2/F3 gap mechanics. Verification is blank because the new
  source file is uncommitted; closeout owns its first source stamp.
