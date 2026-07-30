# Active Conversation Serving Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/active/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/active/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash | `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate | 2026-07-30T13:59:13+02:00|

## What This Area Is

This route is the implemented active conversation serving slice. It
projects the exact running Codex, Claude, and Pi conversations into the normalized active
conversation/status authority and exposes three registered production wires — the authorized
native-hydrated page, selected-child history hydration, and the resumable SSE event stream —
consumed identically by Chats and orchestration. Every wire re-authorizes: the request dependencies
resolve the caller and the
runtime, `expectedBridgeEpoch` is verified against the live submission authority per request,
and every cursor is signature-checked and re-bound against the authorized identity before any
lookup or header.

Hydration is native-authority only: codex persisted-thread pages and pi durable-entry pages are
history authority where they exist, the bounded live evidence window is the live tail, and the
1,000-entry TranscriptEntry deque is never paged as history (Claude user submissions arrive only
through the adapter's exact submission echo). Recovery re-pages native authority — an evicted or
restarted projector rehydrates the identical projection and mints a new cursor generation, so
stale event cursors reset loudly instead of mixing sequences.

## Hot Path Summary

Start with `api.py` for page/events, selected-child history, and the typed pre-stream error ladder. `service.py` is
the per-app authority (cursor secret, epoch verification per wire, atomic page+eventCursor,
bounded projector LRU), `projector/` the decomposed per-session engine (native hydration,
bounded polls, echo zipper, total-order envelopes, gap mechanics, and per-thread sub-agent
demux with per-thread twin suppression), `store.py` the idempotence authority
(native-id dedupe, tool block union, delta buffering, provenance application, roster-aware
upsert guards), `cursor.py` the
signed cursor mint/verify boundary, `status.py` the canonical status classification both Chats
and orchestration consume, `capabilities.py` the fixture-gated per-session evidence, and
`factories.py` running-session resolution plus identity proof. Per-harness frame grammars live
in the sibling `projectors/` route.

## What Belongs Here

| Path | Role |
| --- | --- |
| `api.py` | The three registered routes (page, selected-child history, events) plus the O4 typed-error ladder and explicit SSE frames. |
| `agent_history.py` | Child-local hydration outcomes and stable unavailable/recovered projection rows. |
| `service.py` | Per-app service: cursor secret, epoch checks, atomic page+cursor assembly, pre-stream cursor checks, bounded projector LRU. |
| `projector/` | Per-session component graph: public facade, hydration/poll coordinator, source ingestion, child history, interactions, mutations, retention, subscriber fan-out, gap+close. |
| `store.py` | Idempotent projection store: append/upsert/delta application, tool block union, provenance resolution, page slicing. |
| `cursor.py` | HMAC-signed purpose-branded page/event cursors and the typed cursor error family. |
| `status.py` | Canonical `ConversationStatusService`: the one evidence classification, revisioned envelope, single seat projection. |
| `capabilities.py` | Exact-session capability evidence per harness; contract-only honesty (no version demotion). |
| `factories.py` | Running-session resolution, live identity proof, server-issued identity digest, typed session errors. |
| `__init__.py` | Package marker. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Strict wire grammar, cursor brands, canonical vocabulary | `mcp/src/agents_remember/serving/conversation/models.py` (the parent contract route). |
| Runtime composition, authorization ruling, request dependencies, child-router mounting | `mcp/src/agents_remember/serving/conversation/` (consumed, never edited). |
| Per-harness native frame mapping grammars | `mcp/src/agents_remember/serving/conversation/projectors/` (the sibling mapper route). |
| Dormant native list/read/exact open | `mcp/src/agents_remember/serving/conversation/library/`. |
| Control operations, attachments, telemetry projections | The control route. |
| The IPC evidence/native-page/provenance substrate | `serving/harness_control_*.py` (consumed read-only). |

## Structures Found Here

- Two FastAPI routes on the prefix `/api/terminal/{ar_session_id}/conversation` with every
  typed refusal mapped subclass-before-base to one precise HTTP status (no raw 500 for routine
  refusals — the O4 idiom), and explicit SSE wire frames over `StreamingResponse` so all
  validation precedes headers.
- Purpose-branded HMAC-SHA256-signed cursors binding principal/tenant/session/epoch/harness/
  vendor/scope/generation/schema; the per-app random secret is never persisted and the binding
  re-check per wire is the real authorization mechanism.
- An app-scoped service holding a bounded (32) LRU of reconstructable projectors; eviction or
  expiry rehydrates from native authority and establishes a new cursor generation.
- A per-session engine with bounded everything (1 s polls, 500-frame evidence pages, 200-frame
  native pages, 1000-envelope retention, 256-deep subscriber queues, 64×64 delta buffering,
  64-record provenance batches, 30 s consumer TTL, 5-failure authority-loss ladder).
- One canonical status classification with a revision that advances only on semantic change,
  consumed identically by the Chats page/SSE and by orchestration's seat projection.
- Per-session capability evidence enabled only from landed installed-runtime fixture rows.
  THE CONTRACT IS THE ONLY GATE: `capabilities_for`
  discards the snapshot, no version-string comparison demotes any feature, and an un-probed native
  shape stays `unverified` with a never-probed contract reason (the observed version is informational
  evidence only). The prior read-time observed-version demotion is removed.
- One typed `gap {requiresRepage, closeAfterEvent}` per established-stream failure class
  (retention overflow, generation change, ordering fault) — retained so the sequence chain stays
  hole-free, delivered even to a full queue, never an HTTP reset.

## Operating Model

1. Each handler invokes the two L0 dependencies in-handler, verifies the expected bridge epoch
   against the live submission authority, and lets the service resolve the exact session through
   the factory (catalog row, liveness, control endpoint, harness projector, proven native
   identity).
2. The projector hydrates from native authority (native pages where they exist, the live
   evidence window, the echo channel, eager continuation for pi) under a hydration lock, then
   polls the bounded channels; every blocking IPC read is offloaded off the event loop.
3. The store applies mapper outputs idempotently — appends dedupe by native id, tool-call
   upserts union blocks by `block_id`, deltas buffer bounded until their item/block exists,
   provenance resolves exactly once per request id through the real authority batch.
4. Status observations fold into the canonical envelope; a status mutation emits only on
   revision advance. The page captures window + eventCursor under the apply lock after the
   latest poll, so a subscriber cannot miss an intervening event.
5. Subscriptions decode and generation-check the resume cursor before any stream exists; replay
   attaches and snapshots with no interleaving await; established failures emit one typed gap
   and close.

## Main Flows

### Authorized page

1. Authorization + epoch verification; session resolution fails typed (404/409/503) before any
   projection work.
2. `before` page cursor decodes against the authorized identity (cross-principal/session 403,
   wrong epoch 409, tampered 400); the projector captures the ordinal window, fresh page cursor,
   event cursor, canonical status, and capabilities atomically.

### Resumable event stream

1. Dual resume inputs (`after` + `Last-Event-ID`) must agree; the event cursor binds purpose,
   caller, session, epoch, and the live projector generation — mismatches fail typed pre-stream.
2. Replay delivers retained envelopes after the cursor (marked `resume-replay`), then live
   envelopes in total order; a gap mutation closes the stream after its frame.
3. Epoch flip, ordering fault, or sustained authority loss emits exactly one typed gap with the
   exact reason and closes; recovery is re-paging native authority with a fresh cursor.

### Selected-child history

1. The POST route resolves the same authorization, exact session, and bridge epoch as page/events.
2. Only the effective selected child is eligible. Same-child callers share one shielded task;
   native IPC/source waits run outside the projector apply lock, and bounded page mutation runs
   inside it.
3. Typed unavailable/limit outcomes become one child-local retry state. Parent paging/SSE and
   sibling hydration continue.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `api.py` | route/mapping authority | Keeps every typed refusal on its precise HTTP status; a raw 500 here violates the O4 contract. | covered |
| `agent_history.py` | child-local outcome model | Keeps unavailable/recovered history state bound to one child without changing parent health. | covered |
| `service.py` | serving authority | The one boundary where epoch, cursor, and session checks complete before any page or stream. | covered |
| `projector/` | projection component graph | Native hydration and the totally ordered, honestly-gapping event stream are divided by mutable authority without changing the public projector surface. | covered |
| `store.py` | idempotence authority | Rehydration/replay reproduce the identical projection; tool blocks converge, never drop. | covered |
| `cursor.py` | cursor authority | Every active token's mint/verify boundary; tampering or cross-purpose use fails closed. | covered |
| `status.py` | status authority | The only evidence classification; both Chats and orchestration consume it. | covered |
| `capabilities.py` | capability evidence | Capability honesty: supported only with fixture evidence; an un-probed contract stays `unverified` (contract-only gate, no version demotion). | covered |
| `factories.py` | session resolution | Exact running-session and native-identity proof; no state is ever manufactured. | covered |

## Local Invariants And Traps

- Possession of a cursor is never authorization: every wire re-resolves the caller and re-binds
  every decoded cursor field.
- Page + eventCursor are atomic under the projector's apply lock; dual resume inputs must agree
  before headers.
- The transcript deque is never history authority; Claude user items come only from the exact
  submission echo, zipped by turn order without timestamps (an advancing evidence-eviction floor
  voids the zipper and gaps `ordering-fault` — review F3). The echo poller
  consumes ONLY `role=="user"` transcript entries; assistant/result entries are advanced past (the
  evidence/terminal path owns them), so a mixed-role 2.1.216 transcript no longer mints spurious
  `claude:echo: unrecognized submission echo shape` unknown-vendor rows.
- Dormant per-session state is released on the idle-break: `projector._release_dormant_state` frees
  the FULL heavy projection (ProjectionStore items/order, the
  `_live_turn_ids`/`_live_request_ids` live-turn sets, retention and pending frames) and retires the shell, so a
  dead session's heavy state frees within ~30-60s of the last subscriber leaving instead of at
  32-LRU eviction; `matches()` then returns False so the next access re-creates a fresh projector.
  `service.release_session` can de-register + close a projector explicitly, but is NOT wired into
  terminate/retire this leaf (reviewer F1 accepted-bounding disposition — the leak is closed by
  bounding + idle-release; the wiring locus is recorded in the file sidecar).
- Tool-call upserts union blocks by `block_id`; whole-item replacement would silently discard
  the invocation (review F1).
- Hosted codex live notifications and `thread/read` history use DISJOINT id namespaces (live
  UUID/`msg_*` vs positional `item-N`) for the same settled turn, so id-keyed dedupe can never
  converge them; the projector's native-tip re-walk drops any native output whose turn was already
  settled live — matched by turn id, submitted `clientId` (renumber-robust), or an already-anchored
  sibling — so a live turn is never re-projected as an `unknown-input`/`native-history` twin
  (proven before/after on the real codex wire). Suppression only; nothing merged across ids or
  fabricated. At hydration both live sets are empty (native walk precedes the first poll), so
  prior-session native history hydrates in full; mid-session hydration-overlap is a recorded,
  un-hardened boundary.
- Multiplexing: the engine demuxes every evidence/native-page frame by its verbatim
  `thread_id` into parent vs sub-agent buckets (`None`/parent id = parent, byte-identical to
  the pre-multiplexing behavior); twin suppression (F1) and pending-interaction projection run PER THREAD. The
  singular slot carries the parent's OLDEST pending; EVERY tuple entry projects (agent entries
  labeled, concurrent parent-thread entries beyond the oldest plainly — the adapter keeps a
  per-thread pending map, so concurrent parent pendings are normal traffic), the singular-slot
  entry is never double-projected, and a slot ROTATION resolves the evicted id while the id
  rotated into the slot stays live under the singular path. Malformed agent-thread frames degrade to agent-tagged
  unknown-vendor evidence — never stream-fatal, never leaked into the parent's view. Agent identity
  is fill-only from registry evidence, never fabricated; unmapped statuses stay `unknown`. The
  thread-scoped `refresh_agent_native` walk is production-wired only through selected-child
  hydration. It is same-child singleflight, capped at 64 concurrent reads, and catches only typed
  native-history outcomes; it never runs as an eager all-child page loop.
- A `role=="user"` item's input-authority triple (`lane` + `source` + `provenance`) is ONE resolved
  unit: the store preserves it intact across a native re-map (`_preserved_input_authority`), and only
  `apply_provenance` resolves it. Splitting it (a re-map adopting the candidate `unknown-input` lane
  while keeping the resolved `exact` provenance) violates `preserve_input_authority` but is stored
  SILENTLY because `model_copy(update=…)` skips validation, 500-ing only at route/SSE re-validation —
  which is exactly why the triple stays coupled (H2/F4).
- A full subscriber queue still receives exactly one retained overflow gap + close; the gap
  consumes a sequence so the chain stays hole-free for all consumers (review F2).
- `totalItems` is emitted only when the native walk completed and the evidence window never
  evicted; unknown evidence never becomes `ready`.
- Active cursors are non-interchangeable with the library cursor family, and page/event brands
  are non-interchangeable with each other.
- Sync IPC reads never run on the event loop (`asyncio.to_thread`), a production responsiveness
  rule, not a test workaround.

## Repo-Internal References

The parent contract route supplies the wire grammar and composition seams; the IPC substrate
supplies the validated evidence/native-page/provenance reads; the sibling `projectors/` route
owns the per-harness frame grammars; orchestration consumes the canonical status through the
delegated seat projection. Four new test suites prove the contract, three of them through the
engine/store and one over a real socket.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The request dependencies are the only consumption seam the handlers use. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |
| The validated IPC reads are the only substrate channels polled. | L270-L360 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The evidence/native-page/provenance products define the polled shapes. | L310-L380 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| Orchestration's delegated seat projection consumes the canonical classification. | L70-L90 | [hosted_control_projection.py](agents-remember/mcp/src/agents_remember/serving/hosted_control_projection.py) |
| The foundation pin asserts exactly the two owned active routes while library/control stay empty. | L32-L56 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The four focused suites cover status, mappers, engine/store, and production routes. | L1-L8 | [mcp/tests overview](../../../../../tests/overview.md) |

## Cross-Repo References

No cross-repository implementation participates in this route. All three harnesses are local
subprocesses reached through this repository's own adapters, and the resolved memory policy
allows no neighboring repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant cross-repo evidence found. | — | — |

## Docs References

The resolved `Domain Documentation` registry has no entries. This route therefore uses the
repository-owned contract, IPC substrate, fixtures, and tests as its direct evidence and does
not fabricate an external citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this serving gate. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Active route package marker. |
| `api.py` | [`api.py.md`](api.py.md) | covered | The three registered routes and the O4 error ladder. |
| `agent_history.py` | [`agent_history.py.md`](agent_history.py.md) | covered | Selected-child hydration outcomes and visible recovery rows. |
| `service.py` | [`service.py.md`](service.py.md) | covered | Per-app serving authority. |
| `projector/` | [`projector/overview.md`](projector/overview.md) | covered | Per-session projection component graph and its ten file-level sidecars. |
| `store.py` | [`store.py.md`](store.py.md) | covered | Idempotent projection store. |
| `cursor.py` | [`cursor.py.md`](cursor.py.md) | covered | Signed cursor authority. |
| `status.py` | [`status.py.md`](status.py.md) | covered | Canonical status service. |
| `capabilities.py` | [`capabilities.py.md`](capabilities.py.md) | covered | Exact-session capability evidence. |
| `factories.py` | [`factories.py.md`](factories.py.md) | covered | Running-session factory. |

## Child Overviews

- [`projector/overview.md`](projector/overview.md) governs the decomposed active-session
  projector component graph.
- The per-harness mapper grammars remain governed by the sibling `projectors/` overview, not a
  child of this route.

## How To Use This Area

Read this overview and the exact file sidecar first. Route/error-mapping changes require the
production-route suite over a real socket; engine/store changes require the service suite;
status changes require the status suite plus the orchestration parity product; cursor changes
require the forgery battery. Never page the transcript deque as history, and never infer
capability from fixture existence.

## Needs Verification

- Claude's active surface stays `unverified` with a NEVER-PROBED contract reason ("frame contract
  not yet probed through a captured production fixture … never a version gate"), no longer a
  version-mismatch reason (the version gate was removed). Promoting claude to `supported` needs
  a captured 2.1.216 runtime fixture through the production evidence seam — recorded follow-on
  (worker H3); the end-to-end run now proves the contract live.
- Codex live reasoning/tools/diffs and pi live thinking/tools stay `unverified` until
  installed-runtime fixtures observe those shapes through the production seam.

## Status Semantics And Stream Continuity Route Impact

Active conversations now distinguish a quiet healthy ready state from stale evidence-expected work, bootstrap an event subscription without invalidating a fresh page, and re-page from a new server cursor when a stream cannot prove continuity. The active capability view delegates interrupt evidence to the control gate, eliminating a second local verdict.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## Sub-Agent Multiplexing Route Impact

The projection engine is now multiplexed: every evidence/native-page frame is demuxed by its
verbatim `thread_id` into parent vs sub-agent buckets, twin suppression (F1) and
pending-interaction projection run PER THREAD, malformed agent-thread frames degrade to
agent-tagged unknown-vendor evidence (never stream-fatal, never leaked into the parent's view),
and the singular slot carries the parent's OLDEST pending while every tuple entry projects —
concurrent parent-thread pendings beyond the oldest project plainly (no agent ref) now that the
adapter keeps a per-thread pending map, and a singular-slot ROTATION resolves the evicted id with
the rotated id staying live under the singular path. The store gained roster-aware upsert
guards (terminal-phase no-regression on block-less lifecycle tagging upserts; roster-notice
final-message first-wins retention). The thread-scoped `refresh_agent_native` walk is now
production-wired only for the selected/effective child. Parent page assembly no longer walks every
discovered child; child I/O is singleflight and outside the apply lock, and typed failure is a local
retry state. The three routes, cursor authority, per-app service, and status contract remain one
coherent slice.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## Codex Selected-Child History Route Impact

The active slice now treats child discovery and child content acquisition separately. Metadata/live
events mint the roster; a validated effective focus invokes the third route to hydrate only one
child. The projector's external read is outside `_apply_lock`, same-child calls singleflight, and
64 concurrent reads are the explicit safety bound required by unlocked external I/O. Typed
unavailable/limit outcomes upsert one child-local row and can recover on retry; parent/sibling
projection stays live.

Opaque native-history cursors flow end to end. The adapter-level reader, not the projector, owns
source paging and continuation. Parent completeness stays parent-scoped.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: replaced the deleted
  `projector.py` monolith mapping with the `projector/` component graph and linked its route-local
  overview and file-level sidecars. The public projector contract and behavioral invariants are
  unchanged; verification metadata remains pinned until closeout.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: updated the active route from two to three
  wires, replaced latent/page-driven child backfill with selected-focus hydration, added
  `agent_history.py` to the route map, and documented unlocked I/O, singleflight, necessary
  capacity, typed local recovery, and opaque cursors. Verification metadata remains pinned while
  uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the concurrent-parent-pending
  projection rework — every tuple entry projects (concurrent parent-thread entries beyond the
  singular slot's oldest plainly, never skipped for matching the projection's thread id), the
  singular slot carries the parent's OLDEST pending, and a slot ROTATION resolves the evicted id
  while the rotated id stays live under the singular path. The two routes, cursor authority,
  service, and status contract are unchanged. Aggregate route-index generation remains
  manager-owned; verification metadata stays pinned (remediation uncommitted).
- 2026-07-26T15:52 — 260718-CHATS-L7 curator: documented the multiplexed engine (per-thread
  demux/F1/pendings, degrade-not-fatal agent frames, fill-only agent identity, latent
  `refresh_agent_native`) and the store's roster-aware upsert guards; refreshed the Hot Path
  Summary and added the multiplexing invariant. The two routes, cursor authority, service, and
  status contract are unchanged. Aggregate route-index generation remains manager-owned;
  verification metadata stays pinned (L7 uncommitted).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the half-time functional truths landed
  in this slice. R4 version-gate REMOVAL (developer ruling 2026-07-21) — corrected the now-false
  read-time observed-version demotion doctrine to the contract-only gate (`capabilities.py` discards
  the snapshot; claude reasons are never-probed contract language, not the installed-vs-locked
  mismatch). R3 — the echo poller consumes only `role=="user"` transcript entries so a 2.1.216
  mixed-role transcript no longer mints `claude:echo` unknown-vendor rows. R5 —
  `projector._release_dormant_state` frees the full heavy projection on the idle-break and
  `service.release_session` de-registers a projector (unwired from terminate/retire this leaf; F1
  accepted-bounding). The two routes, cursor authority, per-app service, and status contract are
  unchanged. Verification stays pinned until L5F closeout stamps the candidate commit.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: recorded the two production-E2E hardening truths
  landed in this slice — the projector's F1 live-settled-natives filter (disjoint live vs
  `thread/read` id namespaces, twin suppression by turn-id / submitted `clientId` / walk-scoped
  sibling, full prior-session hydration because both live sets are empty at the hydration walk, and
  the L5.R6 mid-session-overlap recorded boundary) and the store's H2/F4 input-authority pin (the
  `lane`+`source`+`provenance` triple stays coupled for user items across a native re-map; the silent
  `model_copy` split that 500-ed the active page only at re-validation). Both proven before/after (F1
  on the real codex 0.144.5 wire). The two routes, cursor authority, per-app service, and status
  contract are unchanged. Verification metadata stays pinned until L5 closeout stamps the candidate
  commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the governing overview for the
  implemented active conversation serving slice — the two authorized routes, cursor authority,
  per-app service, projector engine, idempotent store, canonical status, capability evidence,
  and session factory — after same-reviewer PASS-WITH-NOTES closed findings F1–F3 across one
  fix round. Verification is blank because the new source route is uncommitted; closeout owns
  its first source stamp.
