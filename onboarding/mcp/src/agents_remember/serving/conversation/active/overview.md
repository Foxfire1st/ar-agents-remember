# Active Conversation Serving Route Overview

## Purpose

This route projects an exact running harness conversation into normalized items, canonical status, and resumable mutation envelopes. Its three HTTP wires are an authorized conversation page, on-demand child-history hydration, and an SSE event stream. The present mapper registry and capability dispatch include Codex, Claude, Pi, and Eve. The active projection serves Chats; orchestration delegates its seat-state classification to this route's canonical status functions rather than deriving another verdict from rendered events or PTY output.

The route treats native evidence as authority and refuses to manufacture a missing session or native identity. Codex uses native pages for persisted thread history; Pi uses durable native entries and eager continuation. Claude has no active native-page channel: its user submissions enter through exact submission echoes, ordered with evidence frames. Eve uses the evidence stream without native pages or transcript echoes. The retained transcript channel is an echo substrate, never a general history pager.

Recovery reconstructs from the available authority channels and gives a replacement projector a new event generation. Reconstruction is an idempotence design intent, not a present guarantee that an evicted live window reproduces every former item. Event generation mismatch requires re-paging rather than continuing across unrelated sequence chains. Page cursors instead carry the literal generation label `native` and an ordinal boundary; their intended survival across projector replacement still depends on the same app secret, authorized identity, and reconstructable ordering.

## Hot Path Summary

`api.py` owns the three route handlers, cursor-input parsing, typed HTTP refusal mapping, and explicit SSE serialization. Each handler obtains the installed runtime and resolves server-side authorization. `service.py` then serializes resolution for the named session, offloads catalog and bridge reads, verifies `expectedBridgeEpoch` against submission authority, and builds the native identity before reusing or replacing a projector. Missing/not-running/dead sessions, missing protocol endpoints, unsupported mappers, and absent native identity fail with typed refusals.

For a page, the service verifies an optional signed page cursor against the authorized identity and clamps the limit to 1–500. The coordinator hydrates once, then captures the chronological item window, event cursor, status, snapshot, and completeness result under the apply lock. It refreshes a dirty native tip there; it does not run a fresh full-channel poll on every page. Capabilities are assembled afterward from the captured snapshot.

For events, `after` and `Last-Event-ID` must agree when both are supplied; at least one resume cursor is required. Signature, purpose, identity binding, event generation, and retention floor are checked before `StreamingResponse` is returned. Subscriber attachment and replay capture have no intervening await. The stream sends a cursor-free connection comment, replay envelopes marked `resume-replay`, then live envelopes. Frames include the event cursor as SSE id and a 2000 ms retry hint. A gap frame ends the generator; detach runs in `finally`.

For child history, the caller names one child in the POST path. The route carries that id through the service and facade to child-history projection. Local eligibility requires a native-page mapper without eager continuation, a non-parent id, and membership in discovered live threads. This is the concrete backend predicate; operator/effective selection is inherited caller-side intent, not an additional focus predicate demonstrated by these active-route functions. Parent paging does not eagerly walk all discovered children.

## Construction And Ownership

The service is cached per `ConversationRuntime`, owns a random 32-byte signing secret, and keeps at most 32 registered projectors through LRU eviction. Weakly held per-session locks serialize projector resolution and replacement. Explicit `release_session` de-registers and closes a projector; application close closes all registered projectors.

`ProjectedSession` groups identity, authorization, catalog entry, mapper, and secret. The facade constructs one mutation stream and one agent authority, then supplies the same `SessionProjectionSpine` and `BridgeReaders` to native ingestion, echo ingestion, child history, and the rebuild coordinator. These bundles make shared session/epoch ownership explicit and reduce accidental mixed wiring; the frozen dataclasses do not independently validate that arbitrary supplied members agree. `BridgeReaders` binds evidence, native pages, transcript, provenance, and snapshot to the installed control port.

The facade owns polling and lifecycle. The coordinator owns hydration locking, native-first rebuild order, channel polling, snapshot/status observation, atomic page capture, and provenance batches. Native ingestion owns source watermarks, completeness, parent native walks, frame mapping, and per-thread live/native twin suppression. Echo ingestion owns Claude's turn-order zipper. Child-history projection owns eligibility, same-child singleflight, native acquisition, and child-local retry state. Agent authority owns foreign-thread binding and registry-backed roster reconciliation. Interaction projection owns singular and multiplexed pending-item lifecycles. Mutation stream owns the store, event generation/sequence, retained envelopes, and subscriber fan-out.

`store.py` owns item idempotence, chronological ordinals, revisioned changes, block reconciliation, delta application, and input provenance without I/O or cursor minting. `cursor.py` owns branded token minting, signature verification, field binding, and typed cursor errors. `status.py` owns the canonical evidence classification, revisioned active envelope, and seat projection. `capabilities.py` owns conservative harness-specific declarations and delegates interrupt evidence to the control capability authority; Eve telemetry is also delegated there. `agent_history.py` defines child-local outcomes and the stable unavailable/recovered item.

Strict wire models now live in `models/conversations/`, with ports in `serving/ports.py`. Request composition and authorization belong to the parent conversation route; per-harness grammars belong to sibling `projectors/`; dormant list/read/open belongs to `library/`; control operations, attachments, and telemetry authority belong to the control route. This route consumes those seams rather than owning their implementation. The projector child overview governs its component files, while the sibling mapper overview governs harness grammars.

## Invariants And Boundaries

Authorization and cursor possession are separate. Request authorization resolves the installed server-side local operator binding using the ASGI peer address, not browser principal/tenant claims. Active tokens bind principal, tenant, AR session, bridge epoch, harness, vendor conversation, project scope, schema, purpose, and position. Their HMAC-SHA256 signature is truncated to 32 hexadecimal characters. Active page/event brands are distinct from each other and from library brands. Integrity/schema/purpose failures are 400; caller/session binding failures are 403; epoch and event-continuation failures are 409. Identity resolution precedes token decoding in the service; decoding precedes the requested page slice or stream attachment.

The HTTP mapper handles epoch mismatch before the general control-error family, maps authorization to 403, unavailable composition/control to 503, and uses cursor/session subclasses' declared statuses. Unrecognized exceptions are re-raised: typed routine refusals are covered, not every possible failure. All three routes declare response models and `CONVERSATION_RESPONSES`; events additionally declare `text/event-stream`. Child acquisition failures are local outcomes inside an HTTP 200 body's `status`/`code`, while parent authorization/bridge refusals use HTTP errors. The event response model describes an envelope's data, not automatic validation of the streaming response. Explicit `JSONResponse` and `StreamingResponse` returns bypass automatic response-model serialization.

Hydration uses a separate lock and begins with a projection reset, snapshot acquisition, parent native history when supported, then evidence, echo, native continuation, and provenance. Blocking bridge reads are offloaded with `asyncio.to_thread`; this includes catalog resolution whose lock/file access otherwise blocks the event loop. Parent tip refresh and ordinary polling are serialized by the apply lock. Child native I/O runs outside that lock, with each page's projection mutations inside it. Opaque source cursors pass through unchanged; the bridge reader owns their meaning and continuation.

Child reads share one shielded task per id and allow at most 64 distinct in-flight tasks. Already-walked children return `already-hydrated`; ineligible ids return `not-eligible`; capacity refusal returns `unavailable` with `child-history-capacity` directly. Only `NativeHistoryUnavailable` and `NativeHistoryLimitExceeded` are converted by the acquisition task into a stable child-local unavailable row. A successful retry replaces that row with recovered state and marks the child walked. Other errors are not silently recast as those outcomes. Parent completeness remains parent-scoped; child history does not supply a global completeness verdict.

Evidence mapping preserves transport thread identity. A missing/parent thread id stays in the parent bucket; foreign evidence is agent-bound, with unknown registry statuses remaining `unknown` and absent paths remaining absent. Malformed or clipped live evidence becomes safe unknown-vendor evidence, with a foreign-thread tag when available; raw payloads remain server-side. Parent native mapping also converts malformed/clipped shapes to unknown-vendor evidence. The child walker calls the mapper directly, filters roster outputs, scopes mapped item ids, and binds them to the requested child; its error conversion is the narrower typed acquisition family above.

Live/native twin suppression is per thread and suppresses outputs by recorded live turn id, a user request id, or an already-matched native sibling turn. It does not merge disjoint live/native item ids or fabricate a shared id. The recorded sets concern observed live content and unknown-vendor turn ids, not an explicit settlement-only predicate. Native history runs before the first live poll during initial rebuild, with empty live sets; the inherited mid-session hydration-overlap limitation remains recorded.

Claude echo ingestion consumes only `role == "user"` transcript entries; other roles advance the transcript watermark without creating echo items. The zipper orders user echoes and evidence turn bodies without timestamps. Initial incomplete evidence has a retained-tail realignment path; after hydration, an advancing evidence eviction floor voids the zipper guarantee and causes an ordering fault. Evidence-tip regression likewise causes an ordering fault. This preserves the intent behind review F3 and the mixed-role 2.1.216 correction without promoting the transcript deque to history authority.

Tool-call upserts union blocks by `block_id`, preserving sibling invocation/result blocks; the candidate wins a shared block id. A candidate streaming phase does not regress a terminal tool phase. Notice upserts retain an existing `final-message` block when the candidate omits it; this is omission retention, not unconditional first-wins when a new final-message block is supplied. Explicit Codex/Claude roster pairs also retain terminal truth against unqualified native-history nonterminal replay, while registry-backed current lifecycle evidence is distinguished as live authority.

User input authority is the coupled lane/source/provenance triple. Native re-maps preserve it, including during equality comparison, and provenance acquisition alone resolves pending inputs to cockpit, controlled-terminal, or durable-inbox authority. Other harness items may transition between live and native-history sources. This retains the H2/F4 intent: splitting a resolved input triple can create an invalid item because `model_copy(update=...)` skips validation. The old assertion that this necessarily fails at automatic active-route/SSE response re-validation is not supported by the explicit response construction.

Deltas before an item are buffered for at most 64 items and 64 deltas per item. When the item exists but the target block does not, the store mints the block and emits a full upsert rather than concealing the live output. Buffered deltas are discarded for mapper-supplied blocks carrying authoritative nonempty aggregate content, avoiding duplicate prefixes; other buffered deltas apply and may mint missing blocks. Item appends deduplicate by item id and normalized equal upserts are no-ops. Native-id convergence and identical reconstruction are design aims with the stated live/native and authority-window limits.

Interaction projection consumes the singular pending slot and additional tuple entries carrying a nonempty raw `threadId`. It skips the singular id, leaves additional parent-thread entries untagged, and tags foreign-thread entries from registry/interaction evidence. Slot rotation resolves the displaced id; an id moving into the singular slot is protected from multiplexed cleanup. Clearing an interaction without an observed outcome marks its phase unknown with that reason. The producer's oldest-parent-slot convention and well-formed tuple entries are inherited substrate expectations; this projection does not independently establish oldest ordering or project entries missing thread identity.

Status classification is evidence-first: pending interaction, external wait, active native turn, settling/retry/compaction, and healthy idle map to canonical states. Missing usable turn evidence retains the prior active turn while process/freshness still evolve. Unknown-strength evidence cannot establish ready. Native settlement takes precedence over snapshot classification for that observation; completed/unknown settlement first enters settling, while interrupted/failed settlement retains its outcome. `TurnTransition` couples state, strength, turn id, waiting, reason, and terminal outcome. Its inherited intent is to prevent independently chosen weak evidence from displacing strong evidence, but the current setter compares equality and replaces a changed candidate without a strength-ranking veto. This is a local implementation distinction, not proof that the whole path has no precedence protection.

Status revision changes for process/turn/strength/stale changes rather than timestamp aging alone. Staleness applies only to working, settling, retrying, or compacting turns after more than 15 seconds without sequence change; quiet ready/waiting/needs-input states remain healthy. Seat projection maps active states to working and waits to awaiting-input. A ready seat claims turn-ended only after a prior working/awaiting-input/stale claim; a fresh ready-idle or healthy boot with no prior turn claim makes no new claim. Orchestration uses the same classification and projection functions, not the active service's persisted envelope state.

Capability declarations use contract evidence rather than installed-version demotion. `capabilities_for` uses explicit keyed dispatch and forwards the snapshot; it does not discard it or fall through to another harness's feature set. Claude live/history-completeness rows retain the never-probed contract reason. Codex reasoning/tools/diffs and Pi thinking/tools/diffs remain conservative unverified declarations where captured fixture gates are absent. Eve has its own declared fixture evidence for live text, thinking, tools, interactions, and policy challenges, no structured diffs or native-history pages, and partial bounded-window completeness. These source declarations are historical evidence descriptions, not a fresh runtime acceptance result. Dormant listing/open, attachment staging, steer/follow-up, and other unavailable rows must not be inferred into existence from a fixture name.

Known numeric bounds are a 32-projector registry, 1-second poll interval, 500-frame evidence pages, 200-frame native pages, 1000 retained envelopes, 256-entry subscriber queues, 64×64 delta backlog, 64-record provenance batches, 64 concurrent child reads, a 30-second consumer TTL, and five consecutive control-read failures before authority-loss closure. These do not mean every collection or walk has a fixed cap: the active store/order, live-turn/request sets, and echo pending-frame list can grow during an active projector lifetime, and a walk may consume multiple bounded pages. Idle polling retires the shell and releases store, retention, echo/native sets, agent state, child state, and interaction tracking when no subscriber remains after the consumer deadline. `matches` then rejects the retired projector. The inherited ~30–60 second dead-state-release claim is historical timing, not a measured deadline here.

Envelope sequencing and retained gaps express the continuity intent. Epoch mismatch and sustained control authority loss map to generation-changed; evidence/zipper regression and validation/mapping failures map to ordering-fault. Gaps require re-page and close-after-event. Queue overflow creates and retains one overflow gap per publication pass, advances sequence, and uses evicting offers for overflowing queues. General `gap()` instead uses non-evicting offers that suppress `QueueFull`. The overflow gap is not directly broadcast to non-overflowing queues in that pass. Thus review F2's universal full-queue delivery and hole-free-all-consumers claims remain intent requiring qualification; retention and sequence advancement alone do not demonstrate them.

`totalItems` is emitted only when parent native completeness and evidence-window completeness are true and no echo frames remain pending. It counts the store's projected order, not a vendor-global history guarantee. Unknown native shapes remain unknown-vendor evidence rather than guessed semantics.

## Historical And Verification Limits

This proposal is source-only at the stated checkout head. The complete input card was read and its supplied SHA256 matched. No tests, product imports, IPC calls, runtime execution, network lookup, sync, or publication were performed. Original route/status/coverage metadata, reference identities, sidecars, and excluded tables remain the parent Curator's preservation responsibility.

The inherited four-suite claim, real-socket/service/status/forgery validation prescriptions, real Codex before/after twin-suppression observation, Claude live end-to-end claim, and captured fixture narratives are historical reports rather than fresh acceptance. Their original execution witnesses were not examined here. Preserve the named review limits: F1 tool-block loss and accepted bounding/idle-release disposition; F2 overflow continuity; F3 echo eviction ordering; H2/F4 coupled input authority; H3 Claude fixture-promotion follow-on; and mid-session hydration overlap. The old statement that active `release_session` was not wired into terminate/retire is retained as that leaf's historical wiring limit; this bounded source review does not establish present whole-application absence.

The former route-conformance suite is reported as retired. Its ledger named undriven parent-bridge 400/403/409/422/503 legs on each route and the events 200 requiring a live bridge plus live uvicorn together; it reported 404 driven on all three. Those exact named limits remain historical, with no current test verdict. Response declarations provide no present validation pass. The L4 report of six required-but-nullable contract fields being corrected belongs to the parent model history and is not independently re-certified here.

The 260731-EFA-L2 grouping rationale, L4 response declarations, L16 catalog-resolution offload after the 2026-08-05 ABBA incident, and L9 model/port relocation retain their enduring intent without reproducing milestone chronology. Current source confirms the grouped construction, declarations, offload, and relocated imports; it does not independently reproduce the incident or delivery evidence.

The inherited claims of no participating cross-repository implementation, no permitted neighboring repository, and an empty Domain Documentation registry describe the earlier evidence/policy scope. No external registry or memory policy was consulted in this source-only pass. They must not be presented as freshly resolved policy. Reference currentness and fresh execution evidence remain separate from the source description.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/active/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/active/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |

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

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): The request dependencies are the only consumption seam the handlers use. [1]
- Retained reference account (no fresh execution or acceptance inferred): The validated IPC reads are the only substrate channels polled. [2]
- Retained reference account (no fresh execution or acceptance inferred): The evidence/native-page/provenance products define the polled shapes. [3]
- Retained reference account (no fresh execution or acceptance inferred): Orchestration's delegated seat projection consumes the canonical classification. [4]

- Three authorized routes return explicit responses, with typed refusal mapping and SSE replay/gap closure. [5]
- Peer-address authorization is server-resolved rather than a browser identity claim. [6]
- Session resolution and bridge reads are offloaded; epoch checks precede projector reuse/replacement; request cursors are checked after identity resolution. [7]
- Current mapper registration includes Eve, with distinct native/echo/continuation flags. [8]
- Snapshot forwarding and explicit capability dispatch replace the card's discard claim. [9]
- Atomic page capture refreshes native tip without a full new poll and requires an empty echo backlog for total completeness. [10]
- Child eligibility is mapper/non-parent/discovered-thread based; bounded shielded singleflight distinguishes capacity from acquisition failures. [11]
- Live/native suppression records observed live turn/request ids and suppresses by thread bucket. [12]
- Full-queue handling differs between general gap and overflow; overflow gaps are not directly offered to healthy queues in the same pass. [13]
- Store growth is lifetime-based; delta buffering is capped, and missing blocks are minted rather than buffered. [14]
- Coupled input authority, tool unions, notice omission retention, and roster replay guards have distinct predicates. [15]
- Transition grouping does not itself rank strength; settlement precedence exists in the caller. [16]
- Status staleness is limited to evidence-expected states; orchestration delegates canonical seat classification. [17]
- Multiplexed pending entries require nonempty thread identity and skip the singular id. [18]
- Shared bundles express construction intent, while idle retirement releases component state. [19]
