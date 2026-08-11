# harness_control_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T08:54+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

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
itself. The declarations are the contract; `mcp/tests/test_serving_response_conformance.py`
drives each route and validates the real body against them under `extra="forbid"`. In
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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This route module composes existing normalized launch, exact-session client, liveness, and catalog
boundaries rather than duplicating their policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| The pre-session catalog supplies the dynamic cached envelope and failed-refresh quarantine. | `HarnessCapabilityCatalog` | mcp/src/agents_remember/serving/harness_capability_catalog.py:81-196 |
| The exact-session client reads advertised capabilities and applies model/effort setters. | `read_control_capabilities` | mcp/src/agents_remember/serving/harness_control_client.py:144-151 |
| The exact-session client distinguishes first-byte ambiguity from a request accepted before disconnect. | `_exchange_control` | mcp/src/agents_remember/serving/harness_control_client.py:534-568 |
| The exact-session client submits whole messages and preserves request correlation. | `submit_control_prompt` | mcp/src/agents_remember/serving/harness_control_client.py:214-252 |
| The exact-session client reconciles a possibly lost submission by request id and bridge epoch. | `reconcile_control_prompt` | mcp/src/agents_remember/serving/harness_control_client.py:273-303 |
| Public serializers deliberately omit the internal raw evidence mapping. | `public_receipt_json` | mcp/src/agents_remember/serving/harness_control_models.py:217-228 |
| The app registers these routes and passes `config.coordination_root` into the one `ConversationRuntime` scope. | "register_harness_control_routes(" | mcp/src/agents_remember/serving/app.py:269-269 |
| The app feeds complete launch selection into the shared opener via `resolve_terminal_open_selection`. | "resolve_terminal_open_selection(" | mcp/src/agents_remember/serving/_app_terminal_routes.py:234-234 |
| The declared models and the shared `SESSION_CONTROL_RESPONSES` table these ten routes name, plus the two submit-only refusals. | `SESSION_CONTROL_RESPONSES`; `PreDispatchFailureRefusal` | mcp/src/agents_remember/serving/response_contract.py:162-168; mcp/src/agents_remember/serving/response_contract.py:1072-1079 |
| The suite that enforces the declarations by driving every route and validating the real body. | `test_harness_control_routes_conform` | mcp/tests/test_serving_response_conformance_cases_2.py:265-407 |
| Route tests pin refresh, raw-free public responses, exact correlation, liveness-before-support ordering, and honest set results. | `test_pre_session_capabilities_freeze_envelope_and_refresh` | mcp/tests/test_serving_harness_control_api.py:129-147 |
| The structured-conversation root installs the one runtime and composes active, library, and control ownership behind one registration function. | "def register_conversation_routes" | mcp/src/agents_remember/serving/conversation/router.py:22-22 |
| The immutable runtime authority and scope types this registration constructs. | `ConversationRuntime` | mcp/src/agents_remember/serving/conversation/runtime.py:55-78 |
| The server-resolved local-operator resolver bound into the runtime. | `LocalOperatorAuthorizationResolver` | mcp/src/agents_remember/serving/conversation/authorization.py:69-105 |
| The foundation suite pins this file as the sole global conversation registration seam. | `test_global_registration_has_one_stable_inclusion_seam` | mcp/tests/test_conversation_foundation.py:110-122 |

## Cross-Repo References

No external repository boundary is implemented; the routes address AR-owned local adapters and
catalog state.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

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

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 14 repository-reference citations and normalized 1 prose citation (14/14 anchored and sourced; scoped citation check clean).

- 2026-08-01T08:54+02:00 — 260731-EFA-L4 curator: recorded the ten `response_model`
  declarations with their exact lines, the shared `SESSION_CONTROL_RESPONSES` table (which is
  the liveness-first 404/409/503 ladder this card already documented, transcribed once), and the
  three deliberate deviations — the seat-less pre-session capability route's own `{404, 503}`,
  `/submit`'s widened 409 (reused request id) and 503 (`PreDispatchFailureRefusal`, the one
  retry-safe certificate), and `/interaction-response`'s widened 409 (nothing pending). Noted
  that the raw-free public shape is now *declared* by `PublicReceiptWire` /
  `PublicReconciliationWire`, so an adapter-private `raw` key on the wire is a conformance
  failure. Repaired 2 stale citations: the `pendingInteractions` self-citation L458-L466, which
  the leaf's 99 added lines moved and which already ran two lines past the end of the `_ok(...)`
  call — now `_answer_interaction` L537-L541; and the `app.py` row, whose `L946-L1049;
  L1339-L1349` did not hold the named material even at the leaf base (that span is
  `_task_document_response`/`_dismissal_response` and a `TerminalLaunchRequest` block) — replaced
  with L752-L770, the `register_harness_control_routes` call carrying
  `coordination_root=config.coordination_root`, and L1440-L1446, the
  `resolve_terminal_open_selection` call. Verification metadata pinned until closeout stamps the
  L4 commit.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `mcp/tests/test_serving_harness_control_api.py`. The five properties the claim names are no longer
  one contiguous block (the file has grown to 894 lines), so L103-L252 was replaced with the exact
  tests: refresh at L129-L147 and L154-L159, honest set results plus exact submit correlation plus
  raw-free authority/status/withdraw at L171-L313, reconcile correlation at L482-L518, and
  liveness-before-support ordering
  (`test_status_order_is_unknown_or_dead_then_live_unsupported_then_native`) at L677-L725.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the three route registrars and the shared `control_entry` / `_control_route` / `_ok` / per-class failure-responder spine; wire contract unchanged.
- 2026-07-26T15:34 — 260718-CHATS-L7 curator: documented the additive `pendingInteractions` list on
  the snapshot route (multiplexed sub-agent pendings, review R6) in Logic and Invariants; the
  singular `pendingInteraction` contract is unchanged. Verification metadata stays pinned to the
  pre-commit source history until closeout (the L7 change is uncommitted).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the one-time composition binding —
  the required `coordination_root` keyword, construction of the immutable `ConversationRuntime`
  from existing authorities (including the server-resolved local-operator resolver), and the
  install-once registration that keeps later child leaves out of this file. Verification metadata
  remains pinned until closeout stamps the candidate commit.

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: documented the single structured-conversation
  root registration seam and the intentional absence of child behavior. Existing source
  verification remains pinned to committed truth; closeout owns the candidate stamp.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented authority/status/withdraw routes, epoch/privacy
  gates, 64-id bounds, conflicts, and the sole retry-safe certificate.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the daemon contract sidecar for
  complete-pair launch, pre/live advertise, honest exact-session set, reliable whole-message submit,
  raw-free public evidence, and liveness-first status ordering. Verification remains empty until
  closeout stamps the new source file.
