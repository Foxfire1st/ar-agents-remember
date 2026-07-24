# harness_control_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the harness-neutral daemon request/response boundary for pre-session advertise,
complete-pair launch selection, exact-session capability reads and model/effort sets, reliable
whole-message submit, and same-request reconciliation. It freezes the server contract later UI and
settings work may consume without implementing those surfaces here. FEUI-L9 also makes this the
single global mounting seam for the independently owned structured-conversation child routers, and
260718-CHATS-L0 makes it the one-time construction site of the immutable app-scoped
`ConversationRuntime` authority those children consume.

## Code Commentary

### Logic

`resolve_terminal_open_selection` accepts either no native selection or a complete model/effort pair
for an AR built-in harness. A partial pair, plain terminal, or non-native harness fails before spawn;
a valid pair becomes the existing L2 `ResolvedLaunch` rather than a second launch mechanism.

`register_harness_control_routes` installs one pre-session capability route and five exact-session
routes. The pre-session route delegates to `HarnessCapabilityCatalog`, including explicit refresh.
Live routes first require a catalog row that is running and still alive, then require a native
control endpoint. Capability and setter calls go through the exact-session client. Submit sends the
entire message plus caller request id through `submit_control_prompt`; reconcile queries the same id.
Setter domain outcomes remain HTTP 200 as normalized `SetResult` evidence.

Before defining its harness-control endpoints, the registration function performs the L0 one-time
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

### Todos

Frontend and settings consumers belong to the separate FEUI and CFGUI masters.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This route module composes existing normalized launch, exact-session client, liveness, and catalog
boundaries rather than duplicating their policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The pre-session catalog supplies the dynamic cached envelope and failed-refresh quarantine. | L80-L195 | [harness_capability_catalog.py](agents-remember/mcp/src/agents_remember/serving/harness_capability_catalog.py) |
| The client implements exact-session advertise/set, first-byte ambiguity, whole-message submit, and reconciliation. | L58-L156; L205-L337 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| Public serializers deliberately omit the internal raw evidence mapping. | L251-L296 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The app registers these routes, passes `config.coordination_root` for the runtime scope, and feeds complete launch selection into the one shared opener. | L946-L1049; L1339-L1349 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| Route tests pin refresh, raw-free public responses, exact correlation, liveness-before-support ordering, and honest set results. | L103-L252 | [test_serving_harness_control_api.py](agents-remember/mcp/tests/test_serving_harness_control_api.py) |
| The structured-conversation root installs the one runtime and composes active, library, and control ownership behind one registration function. | L22-L32 | [conversation/router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The immutable runtime authority and scope types this registration constructs. | L47-L101 | [conversation/runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |
| The server-resolved local-operator resolver bound into the runtime. | L69-L105 | [conversation/authorization.py](agents-remember/mcp/src/agents_remember/serving/conversation/authorization.py) |
| The foundation suite pins this file as the sole global conversation registration seam. | L50-L62 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No external repository boundary is implemented; the routes address AR-owned local adapters and
catalog state.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

The daemon API now exposes authority metadata plus cockpit-only raw-free status and withdrawal, with
status batches limited to 64 ids. Submit/reconcile are epoch-bound and source-tagged. Epoch/id
conflicts return 409 before lifecycle disclosure; only the exact pre-dispatch certificate returns a
retry-safe 503, while possible-write loss remains unknown. The prior frontend-submit todo is closed.

## 260718-CHATS-L5I Current Delta

The harness-control API adds a short liveness memo for control reads and the lifecycle-free interaction-response path. A direct answer is epoch-checked and typed, so a non-pending interaction is reported as such instead of silently disappearing.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

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
