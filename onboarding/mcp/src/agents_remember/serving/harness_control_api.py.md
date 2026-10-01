# harness_control_api.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the harness-neutral daemon request/response boundary for pre-session advertise,
complete-pair launch selection, exact-session capability reads and model/effort sets, reliable
whole-message submit, and same-request reconciliation. It freezes the server contract later UI and
settings work may consume without implementing those surfaces here. It is also the
single global mounting seam for the independently owned structured-conversation child routers, and
the one-time construction site of the immutable app-scoped
`ConversationRuntime` authority those children consume.

## Code Commentary

### 260731-EFA-L4 Current Delta — All Ten Routes Declare Their Response Contract

Every route this module registers now names a `response_model`, and the models live in
`serving/response_contract.py`:

| Route | Model | Line |
| --- | --- | --- |
| `GET /api/harnesses/{harness}/capabilities` | `HarnessCapabilityEnvelope` | L231-L237 |
| `GET /api/terminal/{session}/capabilities` | `CapabilitySnapshotWire` | L255-L259 |
| `POST .../set-model` | `SetResultWire` | L267-L271 |
| `POST .../set-effort` | `SetResultWire` | L279-L283 |
| `GET .../submission-authority` | `SubmissionAuthorityWire` | L295-L299 |
| `POST .../submission-status` | `SubmissionStatusBatchWire` | L307-L311 |
| `POST .../withdraw` | `WithdrawalResultWire` | L330-L334 |
| `POST .../submit` | `PublicReceiptWire` | L355-L369 |
| `POST .../reconcile` | `PublicReconciliationWire` | L390-L394 |
| `POST .../interaction-response` | `InteractionAnswered` | L414-L424 |

**The shared `SESSION_CONTROL_RESPONSES` table is the liveness-first status ladder already
documented below, transcribed once**: `404 UnknownSessionRefusal` (no live, bridge-backed seat),
`409 UnsupportedSeatRefusal | BridgeEpochMismatchRefusal` (no control endpoint, or a stale
caller epoch), `503 StatusRefusal` (the bridge refused or is unreachable). It is exactly what
`_control_route` plus `_control_failure_response` can produce, so every exact-session route
declares it unmodified.

**Three routes deviate, each for a reason already in this file's design:**

- The **pre-session** capability route has no seat at all, so it declares its own
  `{404, 503}` (`StatusRefusal` both) rather than the session table.
- **`/submit`** spreads the session table and then *widens* two statuses, because it adds two
  refusals no other control route can produce: a reused request id (the caller's own
  contradiction) on 409, and `PreDispatchFailureRefusal` on 503 — the one certificate that
  proves zero socket bytes and is therefore retry-safe.
- **`/interaction-response`** widens 409 the same way, for the refusal `_interaction_failure_response`
  alone can emit: nothing pending.

None of this validates at runtime — every handler here returns a `JSONResponse` built by `_ok`
or a failure responder, and FastAPI applies `response_model` only to values it serializes
itself. The declarations remain the contract. The former route-conformance suite was retired;
no present route-validation pass is implied by those declarations. In
particular, `PublicReceiptWire` / `PublicReconciliationWire` now *declare* the raw-free public
shape the Invariants below already required — an adapter-private `raw` key reaching the wire is
a conformance failure, not just a review finding.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### Logic

`resolve_terminal_open_selection` accepts either no native selection or a complete model/effort pair
for an AR built-in harness. A partial pair, plain terminal, or non-native harness fails before spawn;
a valid pair becomes the existing `ResolvedLaunch` rather than a second launch mechanism.

`register_harness_control_routes` installs one pre-session capability route and five exact-session
routes. The pre-session route delegates to `HarnessCapabilityCatalog`, including explicit refresh.
Live routes first require a catalog row that is running and still alive, then require a native
control endpoint. Capability and setter calls go through the exact-session client. Submit sends the
entire message plus caller request id through `submit_control_prompt`; reconcile queries the same id.
Setter domain outcomes remain HTTP 200 as normalized `SetResult` evidence.

Before defining its harness-control endpoints, the registration function performs the one-time
composition binding: it constructs the single `ConversationRuntime` from authorities already in
hand — a `ConversationScope` pairing `workspace_root` with the newly required `coordination_root`
keyword, the catalog, host, harness registry, liveness clock/config, the same pre-session
capability catalog its own routes use, and a `LocalOperatorAuthorizationResolver.for_workspace(...)`
— and passes it to `register_conversation_routes(app, conversation_runtime)`, which installs it on
`app.state` exactly once and mounts the unchanged composed root. The root owns active,
native-library, and control child routers; all three remain behavior-empty. This binding block is
the only shared application registration edit, so later child owners consume the runtime through
the request dependencies and never collide in `app.py` or this module again. The registration
accepts no identity or resolver parameter: production authorization is always the server-resolved
local operator.

Submit and reconciliation use public serializers that retain normalized correlation, timestamps,
acceptance/state, and detail while omitting adapter-private `raw`. Transport/discovery unavailability
is distinct from honest adapter acceptance. Async output remains on the existing event, terminal,
transcript, and durable-bus paths.

The snapshot route is multiplex-aware: the serialized snapshot body
now carries an additive `pendingInteractions` list — every pending interaction across the
multiplexed threads, each serialized through the same `pending_interaction_json` shape — beside the
untouched singular `pendingInteraction` parent-thread slot.
Consumers reading only the singular field see exactly the pre-multiplexing contract. Both keys
are declared on `InteractionAnswered`, because both are emitted.

### Conventions

HTTP request/response carries immediate command evidence; it does not reinterpret SSE or terminal
events as acknowledgement. JSON field names are camel-case only where the established serving API
already uses them (`requestId`). Vendor-specific response shapes never cross this module.

### Invariants And Boundaries

- Unknown, stopped, and observed-dead sessions are `404`; only a live session without native control
  is `409`; live endpoint/discovery failures are `503`.
- Set responses preserve the adapter's exact acceptance (`echo-verified`, `immediate`, `queued`,
  `unknown`, or `unsupported`) and never synthesize effective values.
- Submit is whole-message protocol delivery, never terminal/composer paste.
- Public submit and reconcile responses never expose adapter-private `raw`, argv, environment, or
  auth payloads.
- This module has no vendor branching, UI code, settings mutation, ACP transport, or Toad host.
- Existing role-based spawn and durable inter-agent bus routes remain separate and intact.
- Structured-conversation child routes mount exactly once through the package root; this module
  does not implement their projector, native-history, control, or renderer behavior.
- The one `ConversationRuntime` is constructed here exactly once per app from existing authorities
  only; a second registration fails closed, and no store, index, lifecycle authority, or second
  opener is created.
- `coordination_root` is a required keyword so the runtime scope always pairs both canonical
  roots; production composition accepts no browser-supplied or injected identity.
- The multiplexed `pendingInteractions` field is strictly additive: the singular
  `pendingInteraction` parent-thread slot keeps its exact pre-multiplexing meaning, and no pending entry is
  dropped, merged, or reordered at this serialization seam.

### Todos

Frontend and settings consumers are separate workstreams outside this module.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

This route module composes existing normalized launch, exact-session client, liveness, and catalog
boundaries rather than duplicating their policy.

- The pre-session catalog supplies the dynamic cached envelope and failed-refresh quarantine. [1]
- The exact-session client reads advertised capabilities and applies model/effort setters. [2]
- The exact-session client distinguishes first-byte ambiguity from a request accepted before disconnect. [3]
- The exact-session client submits whole messages and preserves request correlation. [4]
- The exact-session client reconciles a possibly lost submission by request id and bridge epoch. [5]
- Public serializers deliberately omit the internal raw evidence mapping. [6]
- The app registers these routes and passes `config.coordination_root` into the one `ConversationRuntime` scope. [7]
- The app feeds complete launch selection into the shared opener via `resolve_terminal_open_selection`. [8]
- The shared control-response table declares missing-session, unsupported/stale-seat, and control-unavailable refusals. [9]
- The submit-specific pre-dispatch refusal carries retry-safe and stage evidence for zero socket-byte delivery. [10]


| The structured-conversation root installs the one runtime and composes active, library, and control ownership behind one registration function. | "def register_conversation_routes" | mcp/src/agents_remember/serving/conversation/router.py:22-22 |
| The immutable runtime authority and scope types this registration constructs. | `ConversationRuntime` | mcp/src/agents_remember/serving/conversation/runtime.py:55-78 |
| The server-resolved local-operator resolver bound into the runtime. | `LocalOperatorAuthorizationResolver` | mcp/src/agents_remember/serving/conversation/authorization.py:69-105 |


### Cross-Repo References

No external repository boundary is implemented; the routes address AR-owned local adapters and
catalog state.

No meaningful cross-repo references found.

## Submission Authority Delta

The daemon API now exposes authority metadata plus cockpit-only raw-free status and withdrawal, with
status batches limited to 64 ids. Submit/reconcile are epoch-bound and source-tagged. Epoch/id
conflicts return 409 before lifecycle disclosure; only the exact pre-dispatch certificate returns a
retry-safe 503, while possible-write loss remains unknown. The prior frontend-submit todo is closed.

## Control-Read Liveness And Interaction-Response Delta

The harness-control API adds a short liveness memo for control reads and the lifecycle-free interaction-response path. A direct answer is epoch-checked and typed, so a non-pending interaction is reported as such instead of silently disappearing.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Multiplexed Pending Interactions Delta

The snapshot route now serializes the multiplexed plural pending set: an additive
`pendingInteractions` array (one entry per pending interaction across sub-agent threads, same
`pending_interaction_json` shape) sits beside the unchanged singular parent-thread
`pendingInteraction`. This is the control-plane half of the plural-pendings story — the exact
serialization the validated client's `_snapshot` parser reads back.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

Route registration was regrouped and the repeated per-route boilerplate was named. The registered
paths, payloads and status codes are unchanged.

`register_harness_control_routes(app, runtime)` now delegates to three registrars, each stating what
it owns: `_register_capability_routes` (what a harness can do and how it is currently set:
advertise, read, live set), `_register_submission_routes` (the submission authority's public
surface: its epoch, its ledger, and writes against it) and `_register_interaction_routes` (answering
a vendor's own question, with no lifecycle required anywhere).

The shared spine of every control route is now explicit:

- `control_entry(session)` (a `ControlEntryResolver`) — resolve one seat to its live catalog row,
  **or to the response that refuses the request**.
- `_control_route(...)` — run one control route: resolve the exact seat, make the one bridge call,
  answer for any failure.
- `_ok(content)` — the 200 every successful control route returns, so each route names only its
  payload.
- Failure responders, one per class: `_control_failure_response` (the default — a stale epoch is the
  caller's fault, anything else ours), `_submit_failure_response` (answer a failed cockpit submit by
  what the failure proves about delivery) and `_interaction_failure_response` (interaction answering
  adds one refusal no other control route can produce).
- `_answer_interaction(...)` — answer one pending vendor interaction on an exact seat and report the
  resulting snapshot.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
