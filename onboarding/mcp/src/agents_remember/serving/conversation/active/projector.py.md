# mcp/src/agents_remember/serving/conversation/active/projector.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:00+02:00 |
| lastVerifiedCommitHash | `68b3205526dae210cd902eef39d93c4f4352c2d4`|
| lastVerifiedCommitDate | 2026-07-21T01:12:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The active session projector engine (leaf R2/R4): one projector per running session/epoch. It
hydrates the projection from native authority (native pages where the harness has them, the
live evidence window otherwise), keeps it current through bounded IPC polls, mints the totally
ordered event stream with bounded retention, and closes established streams with one typed
`gap` on epoch/generation/ordering loss. The 1,000-entry TranscriptEntry deque is never paged
as history authority.

## Code Commentary

### Logic

`ActiveSessionProjector` (L134-L791) binds one exact identity plus mapper and owns hydration,
polling, the store, the status service, retention, and subscriber fan-out. Hydration
(`_rebuild` L297-L315) re-derives the whole projection from native authority: native-page walks
for harnesses that have them (`_walk_native_pages` L317-L347 — failing closed honest-partial
for ephemeral codex threads), the live evidence window, the echo channel, eager native
continuation for pi, provenance resolution, and a first snapshot observation. `page` (L213-L234)
captures the window, event cursor, and status under `_apply_lock` after refreshing the native
tip — the atomic page+eventCursor the design demands; `total_items` is emitted only when the
native walk completed and the evidence window never evicted (L219). Poll cycle (`poll_once`
L263-L284) runs the four channels then folds the snapshot into canonical status, emitting a
status mutation only on revision advance. Channels: `_poll_evidence` (L359-L385) pages the
bounded evidence window and raises `ZipperEvidenceEvicted` (L109-L117) when an advancing
eviction floor voids the echo zipper's turn-order guarantee (review finding F3 — one
`ordering-fault` gap + close; non-echo harnesses just clear totals honestly);
`_poll_transcript_echo` (L398-L447) is the Claude echo zipper — the adapter accepts one turn at
a time, so echoes and frames merge by strict turn order without timestamps, flushing a turn's
frames through its result before the next user item; `_poll_native_continuation` (L474-L496)
eagerly re-reads pi entries so live items always carry native identity; `_resolve_provenance`
(L498-L511) batches pending user items through the real submission-provenance authority.
Malformed known shapes become preserved unknown-vendor evidence (L453-L472), never stream
failures. Interaction transitions (L535-L600) upsert/resolve interaction items from the snapshot
authority. Envelopes mint with total order — sequence, `previousCursor` chain, generation-scoped
event id (L611-L624) — and `_publish` (L658-L675) retains every envelope and, on a full
subscriber queue, mints ONE shared `retention-overflow` gap per sweep (retained, keeping the
sequence hole-free for all consumers) and delivers exactly one gap + close sentinel via
`_offer_evicting` (L716-L725, review finding F2). `GapMutation.requested_after` names the last
good retained cursor (L695-L698). The poll loop (L738-L777) maps epoch mismatch to a
`generation-changed` gap, zipper/validation failures to `ordering-fault`, and sustained
authority loss (5 consecutive read failures, L102) to a final `generation-changed` gap — the
next page reports the session truth. Projectors idle-stop with no subscribers
(`CONSUMER_TTL_SECONDS` L101) and `matches()` (L195-L203) keys replacement on
session+epoch+vendor identity.

### 260718-CHATS-L5 F1 — live-settled-natives filter (disjoint-id-namespace twin suppression)

On a hosted codex `+ Chat` thread the two projection channels use DISJOINT id namespaces for the
same settled turn: the live notification channel emits UUID/`msg_*` item ids while `thread/read`
returns positional `item-N` ids. `ProjectionStore.apply_item` dedupes by item id, so the two can
NEVER converge, and `_refresh_native_tip`'s post-turn native re-walk (`_walk_native_pages` from
`cursor=None`) re-projected every settled turn as a SECOND `unknown-input`/`native-history` twin
(L4 verdict F1, deterministic 2/2 turns on the real wire; the user twin rendered as an
authority-downgraded `unknown-input` row beside its resolved live twin).

Fix (path (a) — correlate native frames to already-projected live turns; the codex lazy-native path
only, since pi shares one id namespace across channels and claude has no native pages). As each live
evidence frame settles, `_record_live_turn(outputs)` records the turn ids it settled
(`_live_turn_ids`) and the user `clientId`s it submitted (`_live_request_ids`). `_walk_native_pages`
then filters each native frame's mapped outputs through `_drop_live_settled_natives(outputs,
live_native_turns)`: a native output is dropped when its `turn_id ∈ _live_turn_ids` (live-by-turn),
OR when its native user frame carries a `request_id ∈ _live_request_ids` (live-by-client — the
clientId is our own submitted request id and survives verbatim into `thread/read`, so this holds
even if the hosted thread RENUMBERS turn ids), OR when its turn was already anchored earlier in this
walk (live-by-sibling via the walk-scoped `live_native_turns` set — codex stores a turn's items
user-first, so the user frame anchors the turn and its harness siblings drop too). Dropped frames
still advance `_native_cursor`.

Untouched pre-live hydration path (LOAD-BEARING). `_rebuild` CLEARS both live sets before the
hydration walk, and the native walk runs BEFORE the first evidence poll, so at hydration both sets
are empty by construction — a resumed thread hydrates its FULL prior-session native history
(`item-1..item-N`, genuine history, never seen live). Nothing is merged across ids: duplicates are
only SUPPRESSED when the live turn already carries them, never fabricated; L4.R1's item-evidence
turn correlation stays the production path (the fix keys off the same shared `turnId`+`clientId`
evidence, never a guessed identity), the exact-native-id identity rules hold, and no optimistic item
is invented. The H2 store pin operates WITHIN one item id and never crosses these namespaces, so the
two fixes are disjoint. Proven before/after on the real codex 0.144.5 wire (installed regression:
the settled turn projects once; stashed `projector.py` fails `2 != 1`) and on the resumed-thread
mixed prior-history + live-turns edge.

Recorded-not-hardened boundary (L5.R6, medium). The F1 suppression is scoped to turns settled live
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
`asyncio.to_thread`. Resource bounds are explicit constants (L96-L103): 1 s polls, 500-frame
evidence pages, 200-frame native pages, 1000-envelope retention, 256-deep subscriber queues,
64-record provenance batches.

### Invariants And Boundaries

- Recovery re-pages native authority: hydration rebuilds from native pages/evidence reads,
  never from event retention; rehydration reproduces the identical projection with a new cursor
  generation.
- Hosted codex live notifications and `thread/read` history use DISJOINT id namespaces (live
  UUID/`msg_*` vs positional `item-N`) for the same settled turn, so id-keyed dedupe can never
  converge them (L5 F1). The native-tip re-walk drops any native output whose turn was already
  settled live — matched by turn id, by submitted `clientId` (renumber-robust), or by an
  already-anchored sibling — so a live turn is never re-projected as an `unknown-input`/
  `native-history` twin. Suppression only; nothing is merged across ids or fabricated. At hydration
  both live sets are empty (`_rebuild` clears them, the native walk precedes the first poll), so
  prior-session native history hydrates in full. The mid-session hydration-overlap path is a
  recorded, un-hardened boundary (L5.R6).
- The established stream gets exactly one typed gap (`requiresRepage`, `closeAfterEvent`) per
  failure class — never silent loss, never an HTTP reset.
- No raw native payload reaches any public item: unknown shapes carry a safe summary and an
  opaque coordinate evidence ref (`ar-ev:`/`ar-native:`/`ar-echo:`, L781-L788) only.
- Unknown evidence never becomes `ready`; terminal outcomes feed canonical status from native
  evidence only (via `MappedTurnOutcome` → `TurnTerminalEvidence`).

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The evidence/native-page/provenance
seam contracts are the repository-owned L0E substrate cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this engine. | — | — |

## Repo-Internal References

The L0E validated IPC reads are the only substrate channels; the store is the idempotence
authority; the status service owns canonical classification; the mappers are pure frame
grammars; the production-route suite drives this engine over a real socket.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `read_control_evidence`/`read_control_native_page`/`read_control_transcript`/`read_submission_provenance` are the validated L0E reads this engine polls. | L270-L360 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| `EvidencePage`/`NativeEvidencePage`/`SubmissionProvenanceBatch` define the page/batch products. | L320-L380 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The store applies mapper outputs idempotently and converges tool blocks. | L101-L162 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| The status service folds each snapshot plus pending terminal evidence into the canonical envelope. | L283-L300 | [status.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/status.py) |
| The production-route suite proves ordering, idempotence, epoch-flip gap+close, and orchestration parity over a real socket. | L362-L865 | [test_conversation_active_api.py](agents-remember/mcp/tests/test_conversation_active_api.py) |

## Cross-Repo References

No cross-repository implementation participates in this engine.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
