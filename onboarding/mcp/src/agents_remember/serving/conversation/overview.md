# Structured Conversation Contract Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/overview.md` |
| parentOverview | [`serving/overview.md`](../overview.md) |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|

## What This Area Is

This route is the production-owned semantic boundary for native-authoritative structured Chats.
It defines one normalized wire grammar for current conversations, dormant native history,
capability evidence, status, telemetry, control-operation state, attachments, and authoritative
queued withdrawal recovery. It also fixes the two read ports and the three independently owned
FastAPI child-router seams that later production leaves implement.

Since 260718-CHATS-L0 it also owns the one-time runtime composition repair: an immutable
app-scoped `ConversationRuntime` authority binds the existing server authorities (scope, terminal
catalog/host, effective harness registry, liveness clock/config, capability evidence) plus an
explicit server-resolved local-operator authorization resolver, installed exactly once on the app
through the stable root registration. Child leaves consume it only through two narrow request
dependencies; they never edit the shared composition again.

Since 260718-CHATS-L1 the `active/` child is an implemented subsystem with its own route-local
overview, and the per-harness mapper grammars live in a new sibling `projectors/` route with its
own overview: the authorized native-hydrated page and resumable SSE event routes, the signed
page/event cursor authority, the per-app serving service and per-session projector engines, the
idempotent projection store, the canonical status service both Chats and orchestration consume,
and the fixture-gated capability evidence landed inside the active ownership seam without
touching this contract, the composition, or the library/control shells. This overview stays the
contract and composition governor; the implemented slices are governed by
`active/overview.md` and `projectors/overview.md`.

Since 260718-CHATS-L2 the `library/` child is an implemented subsystem with its own route-local
overview: the authorized dormant native list/read routes, live capability gates, the signed
cursor/key authority, and the idempotent exact open/status/reconcile service landed inside the
library ownership seam without touching this contract, the composition, or the active/control
shells. This overview stays the contract and composition governor; the library overview governs
the implemented slice.

Since 260718-CHATS-L3 the `control/` child is an implemented subsystem with its own route-local
overview: the authoritative human control surface — seventeen registered routes for exact-turn
interrupt, the source-aware operation queue with cockpit-only withdrawal and bounded recovery, typed
attachment stage/rebind/submit, read-only effective policy, and evidence-bound telemetry — landed
inside the control ownership seam without touching this contract, the composition, or the
active/library slices. It consumes the closed L2E control-plane substrate (native interrupt write,
paged never-bodies operation timeline, asset channel, pre-tombstone recovery payload) and the
L3E-preserved evidence terminal identity read-only. This overview stays the contract and composition
governor; the control overview governs the implemented slice. All three child routers (`active`,
`library`, `control`) are now implemented subsystems; none is a behavior-empty shell.

This is deliberately a contract and composition route. It does not project vendor events, read a
native history store, implement control actions, persist a duplicate conversation database, or
render a UI.

## Hot Path Summary

Start with `models.py` for identity, cursor, status, capability, operation, attachment, and
withdrawal grammar; use `ports.py` to see the only two read boundaries. `runtime.py` defines the
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
| `models.py` | Stable strict wire vocabulary and authority-product validation. |
| `ports.py` | Exactly two read protocols: active conversation and dormant native library. |
| `runtime.py` | The immutable app-scoped authority bundle, installed exactly once per app. |
| `authorization.py` | Server-resolved local single-user operator ruling; loopback-only, fail closed. |
| `dependencies.py` | The two narrow request dependencies child leaves consume. |
| `router.py` | One root composition seam for three disjoint child routers plus the runtime install. |
| `active/` | Implemented active conversation serving slice (L1), governed by its own route-local overview. |
| `projectors/` | Per-harness active mapper grammars (L1), governed by their own route-local overview. |
| `library/` | Implemented dormant native library slice (L2), governed by its own route-local overview. |
| `control/` | Implemented authoritative control and operation-projection slice (L3), governed by its own route-local overview. |

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
- `ActiveConversationPort` and `ConversationLibraryPort`; lifecycle/control authority is explicitly
  not a third port.
- Three child routers with separate prefixes and one root registration function, all implemented
  inside their owned seams: `active` carries exactly its two L1 routes, `library` its five L2
  routes, and `control` its seventeen L3 routes.
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
4. Capability support is fixture/evidence-bound and demotes on runtime/helper mismatch.
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
| `active/api.py` | implemented routes | Owns the two L1 active production routes (page + resumable events) and the O4 typed-error ladder inside its seam. | covered |
| `library/api.py` | implemented routes | Owns the five L2 native-library routes and the O4 error-status ladder inside its seam. | covered |
| `control/api.py` | implemented routes | Owns the seventeen L3 control routes (interrupt, queue/withdrawal recovery, attachments, policy, telemetry) and the O4 error ladder inside its seam. | covered |

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
  child's two routes (L1), the `library` child's five routes (L2), and the `control` child's
  seventeen routes (L3). Add or change behavior only inside the assigned child module; this contract
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
port, helper, fixture, and registration boundaries. The L0 composition repair is pinned by its own
composition and authorization contract suites.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Cursor brands, identity bindings, strict wire configuration, and provenance authority are centralized in the contract module. | L25-L194; L315-L403 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Canonical status, capability evidence, open rollback, withdrawal recovery, and fixture non-promotion are fail-closed products. | L406-L678; L786-L889; L924-L1082; L1233-L1250 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Exactly two read ports separate active exact-session reads from dormant native library reads. | L27-L87 | [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py) |
| Three behavior-empty child routers compose through one stable root that now also installs the one runtime. | L7-L32 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The immutable runtime/scope types, install-once binding, and fail-closed retrieval define the app-scoped composition authority. | L47-L101 | [runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |
| The server-resolved local-operator resolver, loopback-only classification, and cross-principal rejection define the authorization ruling. | L48-L105 | [authorization.py](agents-remember/mcp/src/agents_remember/serving/conversation/authorization.py) |
| The two request dependencies are the only child-facing consumption seam and consult only the TCP peer. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |
| The production composition constructs the one runtime from existing authorities and installs it exactly once. | L144-L162 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| The foundation suite verifies two-port topology, child ownership (the active child's exact two L1 routes, the library child's exact five L2 routes, and the control child's exact seventeen L3 routes), one registration seam, exact helper pins, and fixture non-promotion. | L21-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The composition contract suite proves single installation, duplicate/missing/foreign/missing-member failure, per-app isolation, no import-time singleton, and no production identity-injection or fixture/PTY reliance. | L106-L260 | [test_conversation_runtime_composition.py](agents-remember/mcp/tests/test_conversation_runtime_composition.py) |
| The authorization contract suite proves local-operator identity, loopback-only resolution, fail-closed peers, no identity input channel, ignored browser claims, and cross-principal rejection in both directions. | L109-L282 | [test_conversation_authorization.py](agents-remember/mcp/tests/test_conversation_authorization.py) |

## Cross-Repo References

No cross-repository implementation participates in this route. The resolved memory policy allows
no neighboring repository, and the native helper is part of this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant cross-repo evidence found. | — | — |

## Docs References

The resolved `Domain Documentation` registry has no entries. This route therefore uses the
repository-owned contract, fixtures, and tests as its direct evidence and does not fabricate an
external citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this contract gate. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Public route-registration facade. |
| `models.py` | [`models.py.md`](models.py.md) | covered | Stable normalized grammar and authority guards. |
| `ports.py` | [`ports.py.md`](ports.py.md) | covered | Exact two-port read boundary. |
| `runtime.py` | [`runtime.py.md`](runtime.py.md) | covered | Immutable app-scoped composition authority. |
| `authorization.py` | [`authorization.py.md`](authorization.py.md) | covered | Server-resolved local-operator ruling. |
| `dependencies.py` | [`dependencies.py.md`](dependencies.py.md) | covered | Child-facing request dependency seam. |
| `router.py` | [`router.py.md`](router.py.md) | covered | Root child-router composition plus runtime install. |
| `active/__init__.py` | [`active/__init__.py.md`](active/__init__.py.md) | covered | Active route package marker. |
| `active/api.py` | [`active/api.py.md`](active/api.py.md) | covered | The two L1 active production routes plus the O4 mapping authority. |
| `active/service.py` | [`active/service.py.md`](active/service.py.md) | covered | Per-app serving authority (L1). |
| `active/projector.py` | [`active/projector.py.md`](active/projector.py.md) | covered | Per-session projection engine (L1). |
| `active/store.py` | [`active/store.py.md`](active/store.py.md) | covered | Idempotent projection store (L1). |
| `active/cursor.py` | [`active/cursor.py.md`](active/cursor.py.md) | covered | Signed page/event cursor authority (L1). |
| `active/status.py` | [`active/status.py.md`](active/status.py.md) | covered | Canonical status service (L1). |
| `active/capabilities.py` | [`active/capabilities.py.md`](active/capabilities.py.md) | covered | Exact-session capability evidence (L1). |
| `active/factories.py` | [`active/factories.py.md`](active/factories.py.md) | covered | Running-session factory (L1). |
| `projectors/__init__.py` | [`projectors/__init__.py.md`](projectors/__init__.py.md) | covered | Mapper protocol, channel bindings, registry (L1). |
| `projectors/common.py` | [`projectors/common.py.md`](projectors/common.py.md) | covered | Strict parsing, output types, provenance builders (L1). |
| `projectors/codex.py` | [`projectors/codex.py.md`](projectors/codex.py.md) | covered | Codex frame grammar (L1). |
| `projectors/claude.py` | [`projectors/claude.py.md`](projectors/claude.py.md) | covered | Claude frame grammar + submission echo (L1). |
| `projectors/pi.py` | [`projectors/pi.py.md`](projectors/pi.py.md) | covered | Pi entry/event grammar (L1). |
| `library/__init__.py` | [`library/__init__.py.md`](library/__init__.py.md) | covered | Library route package marker. |
| `library/api.py` | [`library/api.py.md`](library/api.py.md) | covered | Five L2 native-library routes plus the O4 mapping authority. |
| `library/service.py` | [`library/service.py.md`](library/service.py.md) | covered | List/read re-authorization orchestration (L2). |
| `library/open_service.py` | [`library/open_service.py.md`](library/open_service.py.md) | covered | Idempotent exact open ledger/service (L2). |
| `library/cursor.py` | [`library/cursor.py.md`](library/cursor.py.md) | covered | Signed cursor/key/resume-target authority (L2). |
| `library/scope.py` | [`library/scope.py.md`](library/scope.py.md) | covered | Narrow-only canonical scope authority (L2). |
| `library/gates.py` | [`library/gates.py.md`](library/gates.py.md) | covered | Live production-path capability gates (L2). |
| `library/factories.py` | [`library/factories.py.md`](library/factories.py.md) | covered | Per-app shared bundle and caller-bound builders (L2). |
| `library/helper_host.py` | [`library/helper_host.py.md`](library/helper_host.py.md) | covered | Locked helper process host (L2). |
| `library/codex.py` | [`library/codex.py.md`](library/codex.py.md) | covered | Direct Codex app-server port (L2). |
| `library/codex_normalize.py` | [`library/codex_normalize.py.md`](library/codex_normalize.py.md) | covered | Codex thread-item normalization (L2). |
| `library/claude.py` | [`library/claude.py.md`](library/claude.py.md) | covered | Helper-backed Claude port (L2). |
| `library/pi.py` | [`library/pi.py.md`](library/pi.py.md) | covered | Helper-backed Pi port (L2). |
| `library/normalize_common.py` | [`library/normalize_common.py.md`](library/normalize_common.py.md) | covered | Shared normalization primitives (L2). |
| `library/errors.py` | [`library/errors.py.md`](library/errors.py.md) | covered | Leaf-local typed error family (L2). |
| `control/__init__.py` | [`control/__init__.py.md`](control/__init__.py.md) | covered | Control route package marker. |
| `control/api.py` | [`control/api.py.md`](control/api.py.md) | covered | The seventeen L3 control routes plus the O4 mapping authority. |
| `control/service.py` | [`control/service.py.md`](control/service.py.md) | covered | Per-app control service authority (L3). |
| `control/refs.py` | [`control/refs.py.md`](control/refs.py.md) | covered | Opaque signed control-reference authority (L3). |
| `control/capabilities.py` | [`control/capabilities.py.md`](control/capabilities.py.md) | covered | Control-domain capability gate (L3). |
| `control/operations.py` | [`control/operations.py.md`](control/operations.py.md) | covered | Exact-turn interrupt ledger (L3, R1). |
| `control/queue_projection.py` | [`control/queue_projection.py.md`](control/queue_projection.py.md) | covered | Source-aware queue projection (L3, R2). |
| `control/previews.py` | [`control/previews.py.md`](control/previews.py.md) | covered | Preview/digest transforms (L3). |
| `control/withdrawals.py` | [`control/withdrawals.py.md`](control/withdrawals.py.md) | covered | Cockpit-only withdrawal + bounded recovery (L3, R3). |
| `control/recovery_assembly.py` | [`control/recovery_assembly.py.md`](control/recovery_assembly.py.md) | covered | Recovery content/digest/ref assembly (L3, R3). |
| `control/attachments.py` | [`control/attachments.py.md`](control/attachments.py.md) | covered | Typed attachment lifecycle (L3, R4). |
| `control/asset_spool.py` | [`control/asset_spool.py.md`](control/asset_spool.py.md) | covered | Confined staged-bytes filesystem boundary (L3, R4). |
| `control/policy.py` | [`control/policy.py.md`](control/policy.py.md) | covered | Read-only effective-policy projection (L3, R5). |
| `control/telemetry.py` | [`control/telemetry.py.md`](control/telemetry.py.md) | covered | Evidence-bound telemetry (L3, R6). |

## Child Overviews

| Child Route | Overview | Why It Exists |
| --- | --- | --- |
| `active/` | [`active/overview.md`](active/overview.md) | The L1-implemented active conversation serving: the two authorized routes, signed cursor authority, per-app service and projector engines, idempotent store, canonical status, capabilities, factory — a coherent implemented subsystem. |
| `projectors/` | [`projectors/overview.md`](projectors/overview.md) | The L1 per-harness active mapper grammars: protocol/registry, shared primitives, codex/claude/pi mappers — a coherent implemented subsystem. |
| `library/` | [`library/overview.md`](library/overview.md) | The L2-implemented dormant native library: authorized list/read, live gates, signed token authority, and idempotent exact open — a coherent implemented subsystem. |
| `control/` | [`control/overview.md`](control/overview.md) | The L3-implemented authoritative control surface: seventeen routes, the opaque signed reference authority, the per-app service with bounded ledgers, and the R1–R6 owning modules over the closed L2E/L3E substrate — a coherent implemented subsystem. |

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
  now implemented by the L3 control slice (pending its closeout); only browser rendering remains a
  separately gated L4 implementation. The active slice is implemented in L1 and the library slice in
  L2; Claude library, active, and control/telemetry surfaces stay `unverified` until a real installed
  2.1.211 session passes the replay/version gate, and only codex cumulative token usage is a landed
  supported telemetry metric.

## Update History

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
