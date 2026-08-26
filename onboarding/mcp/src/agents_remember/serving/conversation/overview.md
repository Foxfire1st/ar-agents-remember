# Structured Conversation Contract Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/overview.md` |
| parentOverview | [`serving/overview.md`](../overview.md) |
| lastUpdated | 2026-08-12T04:15+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|

## What This Area Is

### 260731-EFA-L23 Route Delta

L23 updates the conversation boundary for native Codex executable resolution and product-agnostic initialize diagnostics: the plane resolves the native executable, while exact client identity remains the handshake authority.

This route is the production-owned semantic boundary for native-authoritative structured Chats.
It defines one normalized wire grammar for current conversations, dormant native history,
capability evidence, status, telemetry, control-operation state, attachments, and authoritative
queued withdrawal recovery. It also fixes the two read ports and the three independently owned
FastAPI child-router seams that later production leaves implement.

It also owns the one-time runtime composition repair: an immutable
app-scoped `ConversationRuntime` authority binds the existing server authorities (scope, terminal
catalog/host, effective harness registry, liveness clock/config, capability evidence) plus an
explicit server-resolved local-operator authorization resolver, installed exactly once on the app
through the stable root registration. Child leaves consume it only through two narrow request
dependencies; they never edit the shared composition again.

The `active/` child is an implemented subsystem with its own route-local
overview, and the per-harness mapper grammars live in a sibling `projectors/` route with its
own overview: the authorized native-hydrated page and resumable SSE event routes, the signed
page/event cursor authority, the per-app serving service and per-session projector engines, the
idempotent projection store, the canonical status service both Chats and orchestration consume,
and the fixture-gated capability evidence landed inside the active ownership seam without
touching this contract, the composition, or the library/control shells. This overview stays the
contract and composition governor; the implemented slices are governed by
`active/overview.md` and `projectors/overview.md`.

The `library/` child is an implemented subsystem with its own route-local
overview: the authorized dormant native list/read routes, live capability gates, the signed
cursor/key authority, and the idempotent exact open/status/reconcile service landed inside the
library ownership seam without touching this contract, the composition, or the active/control
shells. This overview stays the contract and composition governor; the library overview governs
the implemented slice. Its Codex connection uses the current Desktop host-first initialize
identity and reuses the exact requested client name/version for response validation; no runtime or
model-facing identity token participates in that handshake.

The `control/` child is an implemented subsystem with its own route-local
overview: the authoritative human control surface — seventeen registered routes for exact-turn
interrupt, the source-aware operation queue with cockpit-only withdrawal and bounded recovery, typed
attachment stage/rebind/submit, read-only effective policy, and evidence-bound telemetry — landed
inside the control ownership seam without touching this contract, the composition, or the
active/library slices. It consumes the closed control-plane substrate (native interrupt write,
paged never-bodies operation timeline, asset channel, pre-tombstone recovery payload) and the
preserved evidence terminal identity read-only. This overview stays the contract and composition
governor; the control overview governs the implemented slice. All three child routers (`active`,
`library`, `control`) are now implemented subsystems; none is a behavior-empty shell.

This is deliberately a contract and composition route. It does not project vendor events, read a
native history store, implement control actions, persist a duplicate conversation database, or
render a UI.

## Hot Path Summary

Start with `models/conversations/` for identity, cursor, status, capability, operation, attachment,
withdrawal, and sub-agent participant grammar
(`ConversationAgentRef`, per-item `agent`, library agent rows, `agents_note`); use `ports.py`
to see the only two read boundaries. `runtime.py` defines the
immutable app-scoped authority bundle, `authorization.py` the server-resolved local-operator
ruling, and `dependencies.py` the two request seams children consume. `router.py` installs the
runtime once and composes the `active`, `library`, and `control` child routers, mounted
once through `harness_control_api.register_harness_control_routes`. The implemented active
serving slice is governed by `active/overview.md`, the per-harness mapper grammars by
`projectors/overview.md`, the implemented library slice by `library/overview.md`, and the
implemented control slice by `control/overview.md`.

## What Belongs Here

| Path | Role |
| --- | --- |
| `models/` contracts | Moved by 260731-EFA-L9 to `models/conversations/`; this route consumes them through the canonical `serving/ports.py` surface. |
| `response_contract.py` | The declared HTTP response contract for the 25 conversation routes: the three route-assembled shapes `models.py` never held, and the six shared `responses=` tables. |
| `ports.py` | Re-exports the canonical read/control ports from `serving/ports.py`. |
| `runtime.py` | The immutable app-scoped authority bundle, installed exactly once per app. |
| `authorization.py` | Server-resolved local single-user operator ruling; loopback-only, fail closed. |
| `dependencies.py` | The two narrow request dependencies child leaves consume. |
| `router.py` | One root composition seam for three disjoint child routers plus the runtime install. |
| `active/` | Implemented active conversation serving slice, governed by its own route-local overview. |
| `projectors/` | Per-harness active mapper grammars, governed by their own route-local overview. |
| `library/` | Implemented dormant native library slice, governed by its own route-local overview. |
| `control/` | Implemented authoritative control and operation-projection slice, governed by its own route-local overview. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Vendor protocol transport and native process lifecycle | Existing harness adapter modules under `mcp/src/agents_remember/serving/`. |
| Durable agent-to-agent/operator inbox authority | `mcp/src/agents_remember/controlplane/` and its existing serving adapters. |
| Browser conversation rendering and composer state | `dashboard/src/`. |
| Locked Claude/Pi native dependency process | `mcp/native_helpers/conversation_library/`. |

## Structures Found Here

- Strict immutable camel-case Pydantic wire models with unknown fields forbidden.
- Purpose-branded active-page, active-event, library-list, library-read, library-key, resume-target,
  and operation-fingerprint values.
- Stable native and active conversation identities, normalized content blocks, revisions, global
  ordinals, provenance, status, page/event, capability, telemetry, attachment, queue, and recovery
  DTOs.
- First-class sub-agent participant grammar: `ConversationAgentRef`
  (evidence-bound identity with the honest `agent <short-id>` fallback, never fabricated), an
  additive per-item `agent`, and library agent rows (`ConversationLibraryAgentRow`) with the
  capability-honest `agents_note` that must carry the exact native reason when sub-agent
  conversations are unavailable.
- `ActiveConversationPort` and `ConversationLibraryPort`; lifecycle/control authority is explicitly
  not a third port.
- Three child routers with separate prefixes and one root registration function, all implemented
  inside their owned seams: `active` carries exactly its two routes, `library` its five
  routes, and `control` its seventeen routes.
- Frozen `ConversationScope`/`ConversationRuntime` composition types with fail-closed install and
  retrieval (`ConversationCompositionError` on missing, duplicate, foreign, or missing-member
  bindings); no module-level instance exists.
- The `ConversationAuthorizationResolver` protocol and the production
  `LocalOperatorAuthorizationResolver`: one OS-resolved local operator bound to the canonical
  workspace, loopback-only at request time, cross-principal rejection via `require`.
- Two request-level dependencies (`get_conversation_runtime`, `resolve_conversation_authorization`)
  as the only child-facing consumption seam.

## Operating Model

1. Vendor-specific projectors or library resolvers observe native state and map it into the strict
   types in `models.py` without promoting unknown evidence.
2. Active readers use exact AR session plus bridge-epoch identity and active-only cursors.
3. Dormant history readers use authorization/project scope, library-only cursors and keys, and a
   server-private native resume target.
4. Capability support is fixture/evidence-bound and demotes only on failed
   or never-run **contract verification** against the running harness — never on a runtime/helper
   version comparison. Version strings survive as informational metadata only; no version-string
   comparison gates a capability anywhere in this route (grep-proven at the seven former gate sites).
5. Control implementations publish revisioned operation products; contradictory phase/outcome,
   identity/rollback, acknowledgement/settlement, or recovery states fail validation.
6. The harness-control composition constructs the one `ConversationRuntime` from authorities it
   already holds and the root router installs it once while mounting active, library, and control
   ownership; later leaves add endpoints only inside their assigned child module and reach every
   authority through the two request dependencies.
7. Authorization is resolved on the server: the local operator identity comes from the OS and the
   canonical workspace at composition, and each request must arrive from a loopback TCP peer;
   browser-supplied principal/tenant claims have no input channel and non-loopback peers fail
   closed.

## Main Flows

### Current conversation read and stream

1. Identify the exact active native conversation through `ActiveConversationPort.identify`.
2. Page using an `ActivePageCursor`; stream using an `ActiveEventCursor`.
3. On an established-stream gap, emit the explicit gap mutation, require repage, and close rather
   than silently resetting.

### Dormant native history and exact resume

1. List within an authorization-bound canonical project scope.
2. Read history with a distinct library-read cursor and stable native identity.
3. Resolve a server-private native resume target; it is not a public authorization grant.

### Authoritative queued withdrawal recovery

1. Only a queued cockpit operation may expose a withdrawal reference and redacted preview.
2. Withdrawal races native dispatch through the owning authority in the later control service.
3. Exact draft text and attachment recovery appear only on a successful withdrawn response;
   pending-recovery projections remain raw-free.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `models.py` | contract/policy | Prevents identity, provenance, capability, status, and operation contradictions at the public boundary. | covered |
| `ports.py` | boundary | Keeps active and dormant history reads distinct and prevents control authority from becoming a read-store port. | covered |
| `runtime.py` | composition authority | Binds the existing server authorities into one immutable app-scoped value; broken or duplicate composition fails closed at startup or request entry. | covered |
| `authorization.py` | authorization ruling | Resolves the one local operator on the server, keeps browser identity claims out of resolution, and fails closed off loopback. | covered |
| `dependencies.py` | consumption seam | Keeps child leaves off `app.state` and the composition; the only request fact used is the TCP peer. | covered |
| `router.py` | composition | Owns the single registration seam (runtime install plus root mount) and isolates later leaf ownership. | covered |
| `active/api.py` | implemented routes | Owns the two active production routes (page + resumable events) and the O4 typed-error ladder inside its seam. | covered |
| `library/api.py` | implemented routes | Owns the five native-library routes and the O4 error-status ladder inside its seam. | covered |
| `control/api.py` | implemented routes | Owns the seventeen control routes (interrupt, queue/withdrawal recovery, attachments, policy, telemetry) and the O4 error ladder inside its seam. | covered |

## Local Invariants And Traps

- Active and library cursor families are non-interchangeable and must remain bound to purpose,
  authorization, identity/scope, and generation.
- Unknown input and terminal-controlled input never masquerade as exact native evidence.
- `ready` cannot be derived from unknown evidence; waiting and terminal states retain matching
  evidence products.
- `supported`/`partial` capability claims require exact runtime-fixture evidence; fixture presence
  alone never enables a capability.
- Open/failure rollback products are bidirectional: no-launch outcomes carry no spawned identity,
  while identity-bearing failures require catalog proof and the phase-matching rollback state.
- Withdrawal raw recovery is a successful-response-only privacy boundary. Lists and failures stay
  raw-free.
- All three child API modules are implemented inside their own overview's governance: the `active`
  child's two routes, the `library` child's five routes, and the `control` child's
  seventeen routes. Add or change behavior only inside the assigned child module; this contract
  route stays the grammar/composition governor and gains no endpoints of its own.
- `models.py` is intentionally declaration-heavy. Add behavior in focused services rather than
  turning the contract module into a projector or store.
- Exactly one `ConversationRuntime` exists per app; it binds only existing authorities and adds no
  store, index, lifecycle authority, opener, or behavior methods of its own.
- The local-operator ruling is loopback-only and has no principal/tenant input channel; any remote
  or multi-user requirement invalidates it and needs a separate authentication design, not a
  fallback here. HTTP status mapping of the typed `AuthorityError` is owned by the child leaves
  that add behavior routes.

## Repo-Internal References

The contract is pinned by hostile product-matrix tests and by a topology suite that checks route,
port, helper, fixture, and registration boundaries. The runtime composition repair is pinned by its own
composition and authorization contract suites.

| Finding | Anchor | Source |
| --- | --- | --- |
| Cursor brands, identity bindings, strict wire configuration, provenance authority, and the sub-agent participant grammar are centralized in the contract module. |"class ConversationEventEnvelope"|mcp/src/agents_remember/models/conversations/stream_events.py:88-88|
| Canonical status, capability evidence, library agent rows, open rollback, withdrawal recovery, and fixture non-promotion are fail-closed products. |"class ConversationEventEnvelope"|mcp/src/agents_remember/models/conversations/stream_events.py:88-88|
| Exactly two read ports separate active exact-session reads from dormant native library reads. | "class ActiveConversationPort" | mcp/src/agents_remember/serving/ports.py:62-62 |
| Three owned child routers — all implemented, none behavior-empty — compose through one stable root that also installs the one runtime. | "def register_conversation_routes" | mcp/src/agents_remember/serving/conversation/router.py:22-22 |
| The immutable runtime/scope types, install-once binding, and fail-closed retrieval define the app-scoped composition authority. | "class ConversationRuntime" | mcp/src/agents_remember/serving/conversation/runtime.py:59-59 |
| The server-resolved local-operator resolver, loopback-only classification, and cross-principal rejection define the authorization ruling. | "class ConversationAuthorizationResolver" | mcp/src/agents_remember/serving/conversation/authorization.py:34-34 |
| The two request dependencies are the only child-facing consumption seam and consult only the TCP peer. | "def resolve_conversation_authorization" | mcp/src/agents_remember/serving/conversation/dependencies.py:28-28 |
| `create_app` CONSTRUCTS the one runtime from existing authorities and hands it to the harness-control registration, which INSTALLS it exactly once through its single `register_conversation_routes(app, runtime)` call. | "def create_app", "def register_harness_control_routes" | mcp/src/agents_remember/serving/app.py:243-243; mcp/src/agents_remember/serving/harness_control_api.py:186-186 |
| The strict response contract for the 25 conversation routes: the three shapes assembled at a route that had no model at all, plus the six `responses=` tables the child APIs spread. | "class WireResponse" | mcp/src/agents_remember/serving/response_contract.py:89-89 |
| The foundation suite verifies two-port topology, child ownership (the active child's exact two routes, the library child's exact five routes, and the control child's exact seventeen routes), one registration seam, exact helper pins, and fixture non-promotion. | "test_exactly_two_conversation_ports_exist" | mcp/tests/test_conversation_foundation.py:24-24 |
| The composition contract suite proves single installation, duplicate/missing/foreign/missing-member failure, per-app isolation, no import-time singleton, and no production identity-injection or fixture/PTY reliance. | `_NoSessionHost` | mcp/tests/test_conversation_runtime_composition.py:42-47 |
| The authorization contract suite proves local-operator identity, loopback-only resolution, fail-closed peers, no identity input channel, ignored browser claims, and cross-principal rejection in both directions. | "test_loopback_peers_resolve" | mcp/tests/test_conversation_authorization.py:130-130 |

## Cross-Repo References

No cross-repository implementation participates in this route. The resolved memory policy allows
no neighboring repository, and the native helper is part of this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant cross-repo evidence found. | — | — |

## Docs References

The resolved `Domain Documentation` registry has no entries. This route therefore uses the
repository-owned contract, fixtures, and tests as its direct evidence and does not fabricate an
external citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this contract gate. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Public route-registration facade. |
| `models.py` | [`models.py.md`](models.py.md) | covered | Stable normalized grammar and authority guards. |
| `response_contract.py` | [`response_contract.py.md`](response_contract.py.md) | covered | Declared HTTP response contract for the conversation surface. |
| `ports.py` | [`ports.py.md`](ports.py.md) | covered | Exact two-port read boundary. |
| `runtime.py` | [`runtime.py.md`](runtime.py.md) | covered | Immutable app-scoped composition authority. |
| `authorization.py` | [`authorization.py.md`](authorization.py.md) | covered | Server-resolved local-operator ruling. |
| `dependencies.py` | [`dependencies.py.md`](dependencies.py.md) | covered | Child-facing request dependency seam. |
| `router.py` | [`router.py.md`](router.py.md) | covered | Root child-router composition plus runtime install. |
| `active/__init__.py` | [`active/__init__.py.md`](active/__init__.py.md) | covered | Active route package marker. |
| `active/api.py` | [`active/api.py.md`](active/api.py.md) | covered | The two active production routes plus the O4 mapping authority. |
| `active/service.py` | [`active/service.py.md`](active/service.py.md) | covered | Per-app serving authority. |
| `active/projector.py` | [`active/projector.py.md`](active/projector.py.md) | covered | Per-session projection engine. |
| `active/store.py` | [`active/store.py.md`](active/store.py.md) | covered | Idempotent projection store. |
| `active/cursor.py` | [`active/cursor.py.md`](active/cursor.py.md) | covered | Signed page/event cursor authority. |
| `active/status.py` | [`active/status.py.md`](active/status.py.md) | covered | Canonical status service. |
| `active/capabilities.py` | [`active/capabilities.py.md`](active/capabilities.py.md) | covered | Exact-session capability evidence. |
| `active/factories.py` | [`active/factories.py.md`](active/factories.py.md) | covered | Running-session factory. |
| `projectors/__init__.py` | [`projectors/__init__.py.md`](projectors/__init__.py.md) | covered | Mapper protocol, channel bindings, registry. |
| `projectors/common.py` | [`projectors/common.py.md`](projectors/common.py.md) | covered | Strict parsing, output types, provenance builders. |
| `projectors/codex.py` | [`projectors/codex.py.md`](projectors/codex.py.md) | covered | Codex frame grammar. |
| `projectors/claude.py` | [`projectors/claude.py.md`](projectors/claude.py.md) | covered | Claude frame grammar + submission echo. |
| `projectors/pi.py` | [`projectors/pi.py.md`](projectors/pi.py.md) | covered | Pi entry/event grammar. |
| `library/__init__.py` | [`library/__init__.py.md`](library/__init__.py.md) | covered | Library route package marker. |
| `library/api.py` | [`library/api.py.md`](library/api.py.md) | covered | Five native-library routes plus the O4 mapping authority. |
| `library/service.py` | [`library/service.py.md`](library/service.py.md) | covered | List/read re-authorization orchestration. |
| `library/open_service.py` | [`library/open_service.py.md`](library/open_service.py.md) | covered | Idempotent exact open ledger/service. |
| `library/cursor.py` | [`library/cursor.py.md`](library/cursor.py.md) | covered | Signed cursor/key/resume-target authority. |
| `library/scope.py` | [`library/scope.py.md`](library/scope.py.md) | covered | Narrow-only canonical scope authority. |
| `library/gates.py` | [`library/gates.py.md`](library/gates.py.md) | covered | Live production-path capability gates. |
| `library/factories.py` | [`library/factories.py.md`](library/factories.py.md) | covered | Per-app shared bundle and caller-bound builders. |
| `library/helper_host.py` | [`library/helper_host.py.md`](library/helper_host.py.md) | covered | Locked helper process host. |
| `library/codex.py` | [`library/codex.py.md`](library/codex.py.md) | covered | Direct Codex app-server port. |
| `library/codex_normalize.py` | [`library/codex_normalize.py.md`](library/codex_normalize.py.md) | covered | Codex thread-item normalization. |
| `library/claude.py` | [`library/claude.py.md`](library/claude.py.md) | covered | Helper-backed Claude port. |
| `library/pi.py` | [`library/pi.py.md`](library/pi.py.md) | covered | Helper-backed Pi port. |
| `library/normalize_common.py` | [`library/normalize_common.py.md`](library/normalize_common.py.md) | covered | Shared normalization primitives. |
| `library/errors.py` | [`library/errors.py.md`](library/errors.py.md) | covered | Leaf-local typed error family. |
| `control/__init__.py` | [`control/__init__.py.md`](control/__init__.py.md) | covered | Control route package marker. |
| `control/api.py` | [`control/api.py.md`](control/api.py.md) | covered | The seventeen control routes plus the O4 mapping authority. |
| `control/service.py` | [`control/service.py.md`](control/service.py.md) | covered | Per-app control service authority. |
| `control/refs.py` | [`control/refs.py.md`](control/refs.py.md) | covered | Opaque signed control-reference authority. |
| `control/capabilities.py` | [`control/capabilities.py.md`](control/capabilities.py.md) | covered | Control-domain capability gate. |
| `control/operations.py` | [`control/operations.py.md`](control/operations.py.md) | covered | Exact-turn interrupt ledger. |
| `control/queue_projection.py` | [`control/queue_projection.py.md`](control/queue_projection.py.md) | covered | Source-aware queue projection. |
| `control/previews.py` | [`control/previews.py.md`](control/previews.py.md) | covered | Preview/digest transforms. |
| `control/withdrawals.py` | [`control/withdrawals.py.md`](control/withdrawals.py.md) | covered | Cockpit-only withdrawal + bounded recovery. |
| `control/recovery_assembly.py` | [`control/recovery_assembly.py.md`](control/recovery_assembly.py.md) | covered | Recovery content/digest/ref assembly. |
| `control/attachments.py` | [`control/attachments.py.md`](control/attachments.py.md) | covered | Typed attachment lifecycle. |
| `control/asset_spool.py` | [`control/asset_spool.py.md`](control/asset_spool.py.md) | covered | Confined staged-bytes filesystem boundary. |
| `control/policy.py` | [`control/policy.py.md`](control/policy.py.md) | covered | Read-only effective-policy projection. |
| `control/telemetry.py` | [`control/telemetry.py.md`](control/telemetry.py.md) | covered | Evidence-bound telemetry. |

## Child Overviews

| Child Route | Overview | Why It Exists |
| --- | --- | --- |
| `active/` | [`active/overview.md`](active/overview.md) | The implemented active conversation serving: the two authorized routes, signed cursor authority, per-app service and projector engines, idempotent store, canonical status, capabilities, factory — a coherent implemented subsystem. |
| `projectors/` | [`projectors/overview.md`](projectors/overview.md) | The per-harness active mapper grammars: protocol/registry, shared primitives, codex/claude/pi mappers — a coherent implemented subsystem. |
| `library/` | [`library/overview.md`](library/overview.md) | The implemented dormant native library: authorized list/read, live gates, signed token authority, and idempotent exact open — a coherent implemented subsystem. |
| `control/` | [`control/overview.md`](control/overview.md) | The implemented authoritative control surface: seventeen routes, the opaque signed reference authority, the per-app service with bounded ledgers, and the per-area owning modules over the closed control-plane and evidence substrate — a coherent implemented subsystem. |

All three child directories are now implemented subsystems governed by their own route-local
overviews; none remains a behavior-empty ownership shell.

## How To Use This Area

When changing this route, read this overview and the exact file sidecar first. Changes to public
models require the hostile contract matrix; changes to route/port shape require the foundation
topology suite. Do not infer production capability from fixture existence or an empty router;
the implemented slices are documented by `active/overview.md`, `projectors/overview.md`,
`library/overview.md`, and `control/overview.md`.

## Needs Verification

- Control settlement, attachments, telemetry, queue truth, and cockpit-only withdrawal recovery are
  now implemented by the control slice; only browser rendering remains a
  separately gated implementation. The active and library slices are implemented;
  Claude library, active, and control/telemetry surfaces stay `unverified` because their
  frame/history contract has never been probed through a captured production fixture — a
  never-probed contract reason, not a version gate (all version gating has been removed).
  Capturing a claude 2.1.216 runtime fixture and promoting those surfaces to `supported` is the
  honest follow-on now that the gate is gone; only codex cumulative token usage is a landed
  supported telemetry metric.

## Per-Question Interactions Route Impact

The conversation contract now includes structured per-question interactions and the session-direct response path for lifecycle-free seats, while exact-turn native interrupt remains an acknowledgement-then-settlement operation. Active and control capability views share the fixture-backed interrupt verdict; unsupported control features remain separately conservative. Fresh event/page handoff and recovery use server-minted cursors rather than retrying an invalid resume coordinate.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## Sub-Agent Participant Grammar Route Impact

The contract grammar now models harness sub-agents as first-class participants:
`ConversationAgentRef` (evidence-bound identity, honest `agent <short-id>` fallback, never
fabricated), an additive `agent` on `ConversationItem`, library agent rows
(`ConversationLibraryAgentRow`) grouped under each parent row, and the capability-honest
`agents_note` that must carry the exact native reason when sub-agent conversations are
unavailable. The two-port split, runtime composition, authorization ruling, and child prefixes
are unchanged; the multiplexing machinery itself lives in the `active/`, `projectors/`, and
`library/` slices governed by their own overviews.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## 260727-CHATS-IM-L2 Route Impact

The active child keeps the same page/events/history public routes but decomposes its projector
behind an import-compatible package. Selected-child acquisition remains behind the route's
authorization and epoch proof, and typed child-local history failure leaves parent control and
siblings live. Harness-specific source probing remains in the serving adapter layer.

## 260731-EFA-L2 — The Contract Is Untouched; Its Children Grew Vocabulary

**Nothing in this route's contract changed.** `models.py` — the normalized wire grammar, every
`TypeAlias`, discriminated union, envelope and status/telemetry model — emits exactly what it did.
Its only edit was the deletion of five `# noqa: UP040` / `# noqa: UP046` directives that had been
suppressing rules the linter no longer raises, now that Ruff's `target-version` matches the
package's declared Python 3.11 floor rather than 3.13. The runtime composition authority, the two
read ports and the three child-router seams are all as described above.

What a reader must know is where the children's new vocabulary lives, because these are the values
that now cross the seams this route fixes:

| Child route | Value it introduced | The rule it makes structural |
| --- | --- | --- |
| `control/` | `ControlRequest` → `ControlScope` | The verified bridge epoch, not the caller's claimed one, is what refs are minted and decoded against. |
| `control/` | `RefBinding` / `RefTarget` | Mint and decode share one binding value — caller, session, epoch — so the two sides are provably identical. |
| `active/` | `TurnTransition` | A proposed turn state travels with the evidence strength that justifies it, so a weak observation cannot displace a strong one. |
| `active/` | `ProjectedSession` | The five facts a projector must not mix — identity, authorization, controlled row, mapper, signing secret. |
| `library/` | `LibraryBinding` / `OpenRequest` | Per-app authorities bound to one caller; and the joint fingerprint that makes a replayed request id with changed contents a *conflict*, not a second open. |
| `projectors/` | `ItemPlacement` / `_CollabCall` / `_TaskIdentity` | Frame placement resolved once per frame; "well-typed" held as a value; displayed-vs-retained sub-agent identity kept distinct. |

The pattern is the same in every case and is worth carrying into any new child: **facts that are
only correct together stop being separate parameters.** This route's own job — being the semantic
boundary — is unchanged by that, and none of these values belong in `models.py`: they are internal
call shapes, not wire contracts.

## 260731-EFA-L4 — The Contract Grew A Declaration Layer, And Four Models Learned To Validate Their Own Wire

**The wire this route defines did not change. Six field declarations did, and the reason is exact.**

`models.py`'s serializers dump with `exclude_none=True` — active and control both call
`model_dump(mode="json", by_alias=True, exclude_none=True)`. A `None` is therefore DROPPED from the
emitted body, not written as a null. Six fields across four models were nullable but **required**,
so the model could not validate a body it had itself produced. That was invisible until the routes
started declaring these models and the conformance suite fed real responses back through them.
Each is now nullable **and** defaulted to `None`:

| Model | Fields |
| --- | --- |
| `StatusFreshness` | `last_evidence_at`, `age_ms` |
| `ConversationTurnStatus` | `turn_id`, `state_since` |
| `ConversationEventEnvelope` | `previous_cursor` |
| `ConversationPageWindow` | `older_cursor` |

**The emitted bytes are unchanged** — the absent key already meant exactly this `None`. What changed
is that the model now accepts its own output, which is the precondition for any of it being checked.
A later leaf that makes one of these required again breaks nothing on the wire and everything in
`test_serving_response_conformance.py`.

### `response_contract.py` — a second contract module, and why the split is structural

The new `serving/conversation/response_contract.py` exists because everything in it needs
`conversation/models.py`, and importing that from the app-level `serving/response_contract.py` would
pull in the `serving.conversation` package — whose `__init__` mounts the routers, which import the
contract back. `serving/app.py` registers the files/change-set/notes routes before the conversation
ones, so the app-level module must stay importable first. **The seam is the package boundary, not a
convenience**; do not "tidy" the two modules into one.

All 25 conversation routes already DUMPED a strict `WireModel`, so a model existed for nearly every
body — but not one route *declared* it, and three bodies are assembled at the route and had no model
at all. Those three are now declared here: `StagedAttachments` (the attachment operation plus its
receipts), `ConversationSubmitted` (one body shape across 200/202/422), and `AgentHistoryHydrated`
(a typed child failure carried inside a successful 200). `WithdrawQueueAnswer` names the
withdrawn-or-failed union. Everything else reuses the models the handlers already dump.

Six `responses=` tables live here, and they divide by who chooses the status:

- `CONTROL_RESPONSES` / `CONVERSATION_RESPONSES` / `LIBRARY_RESPONSES` are the **refusal** surfaces,
  transcribed from the one mapper each child owns (`control/api._map_typed_error`,
  `library/api._ERROR_STATUS_TABLE` + `_error_response`). Because there is exactly one mapper per
  child, one table per child is the COMPLETE refusal surface of that child's routes.
- `INTERRUPT_OUTCOME_RESPONSES` / `WITHDRAW_OUTCOME_RESPONSES` / `OPEN_OUTCOME_RESPONSES` are
  **outcome** tables: statuses the route picks from the operation's own outcome, where the body is
  the operation and not a refusal. A `pending` open, an acknowledged-but-unsettled interrupt and a
  failed withdrawal are all this route's own answers.

**The trap that these tables encode, and that a future editor will re-hit:** the child APIs spread
them with `{**SHARED, **OUTCOME}`, and that is a **dict merge, not a union**. A bare
`{409: OpenConversationOperation}` entry *deletes* `LIBRARY_RESPONSES[409]` instead of joining it,
declaring on nine (route, status) pairs a model the route cannot produce. Every outcome-table entry
therefore unions in the refusal model the shared table declares for the same status. The
conformance suite caught the un-unioned version on a real 422 from the interrupt route.

The wire grammar, the two-port split, the `ConversationRuntime` composition, the local-operator
authorization ruling and the three child prefixes are all unchanged.

## 260731-EFA-L16 — Blocking Resolution Leaves The Event Loop (Children Carry The Detail)

Both child routes now keep their blocking catalog reads off the uvicorn event loop: control's
`resolve_entry` went async at the service choke point (`conversation/control` carries the call
site sweep), and active's projector resolution offloads the same `resolve_running_entry` read
(`conversation/active` carries it). The conversation wire contracts are untouched — this was an
availability repair, not a vocabulary change.

## 260731-EFA-L9 Route Impact — Contract Grammar Moved To Models

The contract grammar left this route: `models.py` and the five `_models_*` split files are gone,
moved verbatim into `models/conversations/` (with `serving/conversation/models.py` receiving no
forwarding shim). `ports.py` is now a thin re-export of the canonical `serving/ports.py` port
surface (the two read ports plus the control/terminal seams). This overview remains the contract
and composition governor for the conversation route; the wire-model governance lives at
`models/conversations/overview.md`. The `active`/`library`/`control` child routes are unchanged.

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator route review: L23 updates the conversation boundary for native Codex executable resolution and product-agnostic initialize diagnostics: the plane resolves the native executable, while exact client identity remains the handshake authority. Verification provenance remains closeout-owned.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: recorded the conversation route's
  current host-first initialize boundary and exact request-client validation in its library child.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the grammar move to
  `models/conversations/`, the canonical port re-export, and the updated file map.
  Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T22:30+02:00 — 260731-EFA-L16 route impact: recorded the event-loop offload across both child routes; wire contracts untouched. Verification metadata pinned until closeout stamps the code commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and converted the history `create_app` citation; exact non-fixing check returns zero
  findings.

- 2026-08-01T09:10+02:00 — 260731-EFA-L4 curator: recorded the two source changes in this route.
  (1) Six fields across four `models.py` models became nullable AND defaulted, because the
  serializers dump `exclude_none=True` and a required-but-nullable field made those models unable to
  validate their own emitted body — the emitted bytes are unchanged. (2) The new
  `conversation/response_contract.py` declares the 25 routes' responses; recorded why the module
  split is an import-cycle boundary rather than a preference, which three bodies had no model at
  all, how the six tables divide into refusal surfaces and outcome surfaces, and the
  `{**a, **b}`-is-a-merge trap the outcome tables exist to work around. Added the module to
  `What Belongs Here`, the file-level map and the reference table. Repaired 7 line citations. Six in
  the fail-closed-products row, all moved by the `models.py` edits (+5/+10/+15/+20 by band):
  canonical status L429-L552 → L429-L562 (now reaches `ConversationStatus.reject_false_ready`, which
  the old end cut off), capability evidence L640-L737 → L655-L752 (`CapabilityEvidence` →
  `ConversationCapabilities`), library agent rows L755-L775 → L775-L795
  (`ConversationLibraryAgentRow`, previously only its `class` line), open rollback L811-L912 →
  L831-L932 (`OpenConversationOperation` including `_phases_by_outcome`, `_failure_rollbacks` and
  `require_coherent_rollback`, which the old end cut off), withdrawal recovery L983-L1097 →
  L1003-L1117 (`AttachmentRecoveryRef` → `PendingWithdrawalRecoveryList`), fixture non-promotion
  L1245-L1262 → L1265-L1282 (`RuntimeFixtureObservation`/`RuntimeFixtureEvidence`, whose
  `enables_capabilities: Literal[False]` is at L1281). Seventh: the composition row cited
  `harness_control_api.py` L144-L162, which is `resolve_terminal_open_selection` and was wrong
  BEFORE this leaf; the claim was also wrong on its face — construction happens in
  cit:(["def create_app"], mcp/src/agents_remember/serving/app.py:243-243), and `harness_control_api.py` L182-L195 is where the single
  `register_conversation_routes(app, runtime)` install call sits. Corrected the router row's
  "three behavior-empty child routers", contradicted by this same file's own text. Verification
  metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations. The
  fail-closed-products row's four ranges no longer covered the products it names, so it now cites
  each one exactly in `models.py`: canonical status L429-L552 (`CanonicalStatusEvidence`,
  `CANONICAL_TURN_STATE_BY_EVIDENCE`, the turn/process/status models and their
  `require_waiting_evidence` / `require_terminal_evidence` / `reject_false_ready` validators),
  capability evidence L640-L737, library agent rows L755-L775, open rollback L811-L912 (the
  `_phases_by_outcome` / `_failure_rollbacks` tables and `require_coherent_rollback`), withdrawal
  recovery L983-L1097, fixture non-promotion L1245-L1262 (`enables_capabilities: Literal[False]`).
  The composition-suite row overran its file (252 lines); its tests are L113-L252. All ranges read
  back; no claim text changed.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: no contract or composition change. `models.py` lost five
  now-unnecessary `noqa: UP040`/`UP046` directives after Ruff's target version was reconciled with
  the 3.11 floor. Added a map of the parameter objects the child routes introduced and the rule each
  makes structural, with the note that they are internal call shapes and deliberately not wire
  contracts. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: the active child now owns a
  route-local `projector/` component graph rather than one monolith, and selected-child history
  crosses the same authorization/epoch boundary as page and events. Codex acquisition probes
  bounded native methods at runtime; typed child failure does not tear down parent control or
  siblings. Verification metadata remains pinned until closeout.

- 2026-07-26T15:52 — 260718-CHATS-L7 curator: documented the sub-agent participant grammar added
  to `models.py` (agent status/ref, per-item `agent`, library agent rows, `agents_note`) and
  re-anchored the stale `models.py` citation ranges in this overview's reference table (the
  grammar blocks moved; the file is now 1305 lines). Route contract, composition, and child
  ownership are unchanged; multiplexing detail is routed to the child overviews. Aggregate
  route-index generation remains manager-owned; verification metadata stays pinned (L7 uncommitted).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected this route's capability doctrine to
  the landed contract-verification rule (developer ruling 04:55, R4). The Operating Model's
  "demotes on runtime/helper mismatch" clause and the Needs-Verification "passes the replay/version
  gate" clause were both FALSE after the version-gate removal — a capability is now supported when
  its contract probe verifies against the running harness and demotes only on failed or never-run
  verification; version strings are informational metadata only; no version-string comparison gates
  a capability at any of the seven former sites (grep-proven). Claude's `unverified` surfaces now
  carry a never-probed contract reason, not a version reason. The wire grammar, two-port split,
  `ConversationRuntime` composition, and child prefixes are unchanged. Verification metadata stays
  pinned until closeout stamps the candidate commit.
- 2026-07-21T11:00+02:00 — No route impact: reviewed the 260718-CHATS-L5 production-E2E hardening
  (three source edits) against this contract/composition route — the wire grammar, two-port split,
  `ConversationRuntime` composition, local-operator authorization ruling, and the three child
  prefixes are all unchanged. The projector twin-projection fix (F1 disjoint-id-namespace
  suppression) and the store input-authority pin (H2/F4) land inside the `active/` slice; the codex
  disjoint-namespace truth is a `projectors/` grammar property; the terminal-liveness H1 quarantine
  is a `serving/` change. Detail is routed to `active/overview.md`, `projectors/overview.md`, and the
  `serving/` governor. Verification metadata unchanged.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: documented the `control/` child's
  shell→implemented transition — the seventeen registered routes, the opaque signed reference
  authority, the per-app service with bounded ledgers and per-session locks, and the R1–R6 owning
  modules over the closed L2E/L3E substrate — with child-overview governance routed to the new
  `control/overview.md`, all fourteen control file-map rows, the filled `control/api.py`
  load-bearing row, the seventeen-route foundation pin, and the "all three children implemented"
  invariant. The wire grammar, two-port split, composition, and public prefixes are unchanged.
  Verification metadata stays pinned at the L1 code commit until L3 closeout stamps the candidate
  commit.
- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  library content with the L1 active/projectors content after the master memory branch advanced
  (`fbc6907` → `900a7da`). Both implemented-slice descriptions, both child-overview rows, and
  all map rows survive; `control/` is now the only behavior-empty shell; verification metadata
  stays pinned at the L2 code commit until L1 closeout stamps the L1 candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: documented the active child's
  shell→implemented transition and the new `projectors/` sibling route — the two authorized
  production routes, signed cursor authority, per-app service and projector engines, idempotent
  store, canonical status service (now also backing orchestration), fixture-gated capabilities,
  and the per-harness mapper grammars — with child-overviews governance routed to
  `active/overview.md` and `projectors/overview.md`. The wire grammar, two-port split,
  composition, and public prefixes are unchanged; the `library/` slice is L2's (landed
  separately) and `control/` stays a behavior-empty shell. Verification metadata remains pinned
  until closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the library child's transition
  from behavior-empty shell to the implemented L2 slice governed by the new
  `library/overview.md` — five owned routes, live gates, signed token authority, and the
  idempotent exact open — with the active/control shells, wire grammar, two-port split,
  composition, and public prefixes unchanged. Verification metadata remains pinned until
  closeout stamps the candidate commit.
- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the one-time runtime composition
  repair — the immutable app-scoped `ConversationRuntime` authority, the server-resolved
  local-operator authorization ruling, the two child-facing request dependencies, and the
  install-once root registration — plus their composition and authorization contract suites. The
  wire grammar, two-port split, child ownership shells, and public prefixes are unchanged.
  Verification metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the governing overview for the stable
  structured-conversation grammar, exact two-port split, three behavior-empty route owners,
  evidence/cursor/operation authority, and withdrawal-recovery privacy boundary. Verification is
  blank until closeout commits and stamps the new source.
