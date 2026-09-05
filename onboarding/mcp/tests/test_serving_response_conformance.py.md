# test_serving_response_conformance.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_serving_response_conformance.py`   |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated | 2026-09-05T08:46+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `overview.md`                                      |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The enforcement for the declared HTTP response contract (`serving/response_contract.py`) across
**all 63 HTTP routes** the serving app registers. It is the sibling of
`test_served_state_conformance.py`, widened from one route to the whole surface.

It exists because **declaration-only checks do not establish runtime response behavior**. The route
inventory, hazard, per-route conformance, and declared-surface-coverage suites below drive actual
responses and validate them. cit:([`ServingRouteInventoryTests`; `ValidatedRouteHazardTests`; `ServingResponseConformanceTests`; "class DeclaredSurfaceCoverageTests(unittest.TestCase):"], mcp/tests/test_serving_response_conformance.py:537-669; mcp/tests/test_serving_response_conformance.py:672-741; mcp/tests/test_serving_response_conformance.py:841-952; mcp/tests/test_serving_response_conformance_live.py:492-492)

## Code Commentary

### Logic

#### cit:([`validate_wire`], mcp/tests/test_serving_response_conformance.py:211-231) — what pins camelCase

`validate_wire(model, body)` calls `TypeAdapter(model).validate_python(body, by_alias=True,
by_name=False)`. The field-name and conversation tests cited below exercise that alias-validation
boundary directly.

cit:([`field_name_form`], mcp/tests/test_serving_response_conformance.py:234-248) rewrites a real body into field-name form so the rule is *proved*
load-bearing rather than asserted. cit:([`test_a_field_name_body_fails_the_declared_contract`], mcp/tests/test_serving_response_conformance_cases_1.py:275-300)
drives
`GET /api/terminal/sessions`, shows the route really answers `tmuxName`, shows the old plain
validation **accepts** the rewritten `tmux_name` body, and shows `validate_wire` rejects it.
cit:([`test_the_conversation_wire_is_pinned_to_camel_case_too`], mcp/tests/test_serving_response_conformance_cases_1.py:302-322)
pins the same axis on the 25
conversation routes, which dump `by_alias=True` by hand.

#### `DeclaredSurfaceCoverageTests` — the score, stated as a number

cit:([`declared_pairs`], mcp/tests/test_serving_response_conformance.py:194-208) is the denominator: every `(method, path, status)` triple the app
declares. cit:([`DRIVEN`], mcp/tests/test_serving_response_conformance.py:272-272) is the conformance ledger;
cit:([`_driven_pairs`], mcp/tests/test_serving_response_conformance_live.py:458-481) re-runs the driving classes when the module was
run partially, so a coverage number is never computed from a partial run.

`test_the_conformance_table_accounts_for_every_declared_pair` pins three numbers,
"so neither side can move without a decision":

- **292** declared `(method, path, status)` triples
- **139** driven against a real body
- **153** declared-and-undriven

The 153 are not a suppression list. `UNDRIVEN_DECLARATIONS` is **39 route rows**,
each carrying a written reason, and the test asserts it **EXACTLY**
(`assertEqual(_grouped(declared - driven), UNDRIVEN_DECLARATIONS)`) — so a declaration that stops
being driven has to be added by hand, and a leg that becomes drivable has to be removed. The
reasons group into: one shared refusal table over seventeen conversation routes (reaching each
typed failure needs a real bridge driven into a stale epoch / rejected operation / dead socket
mid-write); the library surface, whose 200s need a real vendor binary with an installed native
history store; the projection surface's 503 "not primed yet", a startup race the fixtures
deliberately do not have; and the harness-control 503s, which need a bridge that accepts a
connection and then fails.

**Record the shortfall as a number, not as an implication of completeness.** 153 of 292 declared
legs are not driven. What changed with this suite is that the remainder is *counted*: before it,
the driving tests kept a `self.checked` set that no assertion ever read, **88 of 286** pairs were
driven, and **seven declared models could be made mathematically unsatisfiable** — a required `str`
retyped to `int` — without one test going red.

The claim that does hold without exception is the weaker one:
`test_every_route_has_at_least_one_driven_status` asserts **every one of the 63
routes is driven on at least one status**, which is what makes the ledger a list of unexercised
*legs* rather than of unexercised routes.

`test_the_open_status_map_is_total_over_the_declared_outcomes` asserts
`_OPEN_STATUS_BY_OUTCOME` covers every declared `OpenConversationOperation.outcome`; it is what
removed an undeclared 500 that the old `.get(..., 500)` could answer with a full operation body.

#### `ServingRouteInventoryTests` — the surface, and the one structural exemption

The walk happens inside a **started** app (`stack.enter_context(TestClient(self.app))`),
because `add_api_route` is legal from the lifespan and a pre-startup walk would miss such a route
entirely.

- `test_every_http_route_declares_a_response_model`: no HTTP route may lack one.
- `test_the_websocket_is_exempt_because_it_structurally_cannot_declare_one`: the
  exemption is **by route class, not by a path skip-list** — an `APIWebSocketRoute` has no
  `response_model` attribute at all, and the test asserts that absence, so the exemption cannot
  quietly widen to swallow a future undeclared HTTP route. The one socket is
  `/api/terminal/{session}`.
- `test_the_declared_surface_is_the_whole_surface`: **63 HTTP + 1 websocket**, pinned.
- `test_no_registration_form_escapes_the_walker`: a kind the walker does not model is
  refused. FastAPI's own doc routes are excluded by the URLs the app reports for them, never by a
  hard-coded path list.
- `test_the_mounted_surface_is_pinned`: mounts == `[""]` (`serving/static.py` mounts
  the cockpit bundle at `/`).
- `test_every_declared_refusal_status_names_a_model` and
  `test_a_modelless_responses_entry_is_a_304_or_a_declared_sse_media_type`: a
  `responses` entry without a model would let a refusal shape drift while still looking declared,
  and `declared_model` would fall back to the route's **success** model for that status. Carrying a
  `content` key does not excuse it; the only modelless entries allowed are pinned by name —
  `("/api/events", 200)`, `("/api/state", 304)`, `("/api/stream", 200)`,
  `("/api/terminal/{ar_session_id}/conversation/events", 200)`.

#### cit:([`walk_routes`], mcp/tests/test_serving_response_conformance.py:125-158) and `RouteWalkerTests`

The inventory is an argument of the form "these are all the routes, and all of them declare a
model"; its first clause is a claim about the walker, so each registration form is registered,
**served**, and then found at the path it actually answered on:

- `include_router` — FastAPI keeps the included router behind one opaque `_IncludedRouter`; the 25
  conversation routes live inside one, so a test reading `app.routes` alone would have seen 38 of
  the 63. The inner `route.path` does **not** carry the prefix, so the walker applies
  `include_context.prefix` itself.
- `app.mount` — a starlette `Mount` whose `.routes` is the mounted app's own table.
- `app.router.add_route` — a plain starlette `Route`: serves HTTP 200 JSON, is neither an
  `APIRoute` nor an `APIWebSocketRoute`, and would be stepped over by every `isinstance` filter.
- registration from inside the lifespan.

#### `ValidatedRouteHazardTests`

`GET /api/terminal/sessions` and `GET /api/harnesses` return a bare `dict`, so unlike the other 61
FastAPI validates them for real — and a drifted payload is answered as **HTTP 500**, not passed
through. On `/api/terminal/sessions` that is a 68-key body assembled by hand from a
58-optional-field dataclass that is actively grown. `_emitted_keys` therefore **AST
scans** `TerminalCatalogEntry.to_json` (an instance cannot prove the set, because every optional key
goes through `_present_fields` and is absent when `None`) and
`test_the_catalog_wire_model_covers_every_key_to_json_emits` asserts set **equality in
both directions** against `TerminalCatalogEntryWire`'s aliases, plus `len(emitted) == 68` so a scan
reading zero keys cannot satisfy the equality. This fires when the field is added — earlier than
the runtime 500, and earlier than a conformance run, which only sees the fields its fixture
happens to populate.

#### The driving classes

- `ServingResponseConformanceTests`: one real request per route through the real app. `_check`
  records the driven triple, asserts the status, resolves
  `declared_model(route, status)` — `responses[status]["model"]` when there is one, `response_model`
  otherwise — and validates through `validate_wire`. The fixture is deliberately
  shaped to reach shapes a declaration named and nothing drove: a **second, memory-less repo** is
  the only input that reaches `OnboardingPartnerNone`, the fifth member of
  `GET /api/files/onboarding`'s union; a `legacy` seat with no control endpoint is the only input
  that reaches `/paste`'s 409 `unsupported` leg. `_client` uses a **loopback peer** because conversation authorization is loopback-only
  — the default `testclient` host would turn every conversation route into the same 403 — and takes
  a `peer` argument so the 403 leg can be driven deliberately.
- `ConversationSuccessConformanceTests`: real 200/202 bodies off a real control
  bridge, over real uvicorn rather than `TestClient` because the bridge must live on this test's own
  event loop.
- `ConversationCompositionRefusalTests`: the one control refusal `create_app` cannot
  produce, because it always composes a complete `ConversationRuntime`. The routers are
  independently mountable, and a router mounted without its runtime is the state
  `CONTROL_RESPONSES[503]` exists for — declared on all 17 control routes, driven on none until
  this class.
- `StreamContractTests`: the branches a body-shaped model cannot express — the bare `304` with an
  empty body, the SSE frames off the real generators, and (via the `serve` helper, a real uvicorn on
  a loopback socket) both SSE routes driven **as routes**. `TestClient` cannot drive an SSE
  route: the stream never ends, so a read from inside the portal thread cannot be closed from
  outside it. Driving the generator directly is also what reaches the *second* frame, where the
  snapshot/delta asymmetry lives.

### Conventions

Third-party imports (`fastapi`, `starlette`) precede the `sys.path.insert(0, str(MCP_SRC))`; package
imports and the `_control_plane` test helper follow it — the suite idiom.
Every driving class ends its cases with `COMPLETED.add(f"{type(self).__name__}.{self._testMethodName}")`
so `_driven_pairs()` can tell a partial run from a whole one. Route keys are always the **declared**
path template (`route="/api/terminal/{ar_session_id}/conversation/interrupt"`) even when the request
uses a concrete id, because that is what the route index is keyed on. cit:([`_LivePaneHost`], mcp/tests/test_serving_response_conformance.py:321-349)
mirrors `TerminalHost`'s signatures exactly — an argument the double ignores is still an argument
production passes, so it stays named — and exists so the liveness sweep does not delete every
seeded catalog row before `GET /api/terminal/sessions` is conformance-tested.

### Invariants And Boundaries

- The suite must keep **driving** routes. An assertion that only reads declarations enforces
  nothing on 59 of the 63 handlers.
- `validate_wire`'s `by_alias=True, by_name=False` pairing is load-bearing and must not be relaxed
  to a plain `validate_python`; `field_name_form` exists to keep that provable.
- `UNDRIVEN_DECLARATIONS` is asserted **exactly**, never as a subset. It is a ledger, not a
  suppression list.
- The three headline numbers (292 / 139 / 153) are pinned deliberately. Moving any of them is a
  decision, and the ledger row must move with it.
- Every route must stay driven on at least one status; that is the claim that holds without
  exception.
- The websocket exemption stays **structural** (no `response_model` attribute), never a path list.
- The walker must model every registration form the app can dispatch, and the inventory must refuse
  any kind it does not model.
- SSE routes are driven over a real socket, not `TestClient`.

### Todos

The 153 undriven legs are the standing debt, itemised in `UNDRIVEN_DECLARATIONS`. The largest tranches need a
real vendor harness (the library surface's 200s) or a control bridge that fails mid-write (the
conversation refusal table and the harness-control 503s); neither is modelled by the current
fixtures.

## Docs References

No external Domain Documentation source is configured for this memory repo. The runtime boundary is
recorded by the repository-local route-inventory, hazard, conformance, and surface-coverage tests
cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local test module; live retrieval was not available and the registry is empty. | — | — |

## Repo-Internal References

The suite is the enforcement half of a two-part arrangement: the declarations live in the contract
modules, and everything that proves them lives here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The HTTP response base uses camelCase aliases, forbids unknown fields, and is immutable. | "class WireResponse(" | mcp/src/agents_remember/serving/response_contract.py:89-101 |
| Scoped reads share declared 400/404 refusal envelopes. | "SCOPED_READ_RESPONSES: dict[int" | mcp/src/agents_remember/serving/response_contract.py:1103-1109 |
| Session controls share declared missing, unsupported/stale, and unavailable refusals. | "SESSION_CONTROL_RESPONSES: dict[int" | mcp/src/agents_remember/serving/response_contract.py:1113-1120 |
| Actions share declared invalid, unknown, unavailable, and projection-not-ready refusals. | "ACTION_RESPONSES: dict[int" | mcp/src/agents_remember/serving/response_contract.py:1125-1133 |
| The conversation surface's `CONTROL_RESPONSES` and `CONVERSATION_RESPONSES` tables. | `CONTROL_RESPONSES`; `CONVERSATION_RESPONSES` | mcp/src/agents_remember/serving/conversation/response_contract.py:95-108; mcp/src/agents_remember/serving/conversation/response_contract.py:113-120 |
| The serving app factory and SSE generator under test. |"async def stream_events("; "def create_app("|mcp/src/agents_remember/serving/_app_common.py:116-116; mcp/src/agents_remember/serving/app.py:244-244|
| The `StreamContractTests` suite that drives the SSE seam. | `StreamContractTests` | mcp/tests/test_serving_response_conformance.py:38-38 |
| The producer's `_present_fields` conditionality. | "def _present_fields(" | mcp/src/agents_remember/models/terminal_catalog.py:629-629 |
| The catalog-entry wire model and its aliases. | `TerminalCatalogEntryWire` | mcp/src/agents_remember/serving/response_contract.py:280-346 |
| The open-status map asserted total over the declared outcomes, and the `_open_call` that indexes it directly. | `_OPEN_STATUS_BY_OUTCOME` | mcp/src/agents_remember/serving/conversation/library/api.py:75-84 |
| The control router and typed-error mapper. | `router`; `_map_typed_error` | mcp/src/agents_remember/serving/conversation/control/api.py:87-90; mcp/src/agents_remember/serving/conversation/control/api.py:136-153 |
| The raw event stream's `ready` marker. | `stream_raw_events` | mcp/src/agents_remember/serving/events.py:230-277 |
| The served-state tail field names. | `SERVED_TAIL_FIELDS` | mcp/src/agents_remember/serving/served_state.py:62-66 |
| The control-bridge harness fixtures used by this suite (`FakeControlAdapter`, `make_harness`, `OPERATOR`). | `FakeControlAdapter`; `make_harness` | mcp/tests/_control_plane.py:100-289; mcp/tests/_control_plane.py:386-397 |
| The single-route sibling this suite was widened from, which owns `/api/state`'s assembled body and the SSE snapshot. | `ServedStateRouteConformanceTests`; `ServedSnapshotConformanceTests` | mcp/tests/test_served_state_conformance.py:260-352; mcp/tests/test_served_state_conformance.py:355-410 |

## Cross-Repo References

The routes, models, fixtures, and dashboard projection type are all repository-local; the projection
type is recorded separately below as an in-repo boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The in-repo workspace projection wire type. | `WorkspaceProjection` | dashboard/src/types/projection.ts:817-830 |


## 260831-CCR-L23 Requirement-Route Surface

L23 grew the serving surface from 61 to 63 HTTP routes (both declared by
`serving/requirements.py` with the shared scoped-read refusal table). The
conformance fixture gained `_seed_requirements`, and the driving class now seeds
a requirements root alongside notes/changeset/task-doc; the declared-surface coverage
ledger advanced from 286/133 to 292/139 declared/driven pairs (153 undriven legs
unchanged), and the per-route conformance driver covers the requirement endpoints'
success/refusal shapes through `test_serving_response_conformance_cases_2.py`.

## L23 Contract-Backed Conformance Fixture

The response-conformance changeset now constructs a real series contract and a
leaf whose source is the master's work branch. Public response checks therefore
exercise the same task-derived ancestry topology as production instead of a
standalone leaf branch.

## 260821-CLIVE-L2 Addressable Fixtures and Readiness Boundary

Series and leaf fixtures now place their worktree-group enclosure roots independently of task-side
contract paths, then publish locators/manifests for both. The request client also crosses one
bounded projector-readiness boundary before checking route models, preventing startup timing from
being mistaken for response-contract failure.

| Finding | Anchor | Source |
| --- | --- | --- |
| Series and leaf fixtures publish the normal lifecycle address chain from their enclosure roots. | `_seed_changeset` | mcp/tests/test_serving_response_conformance.py:416-482 |
| The shared client waits only through the bounded 503 readiness window and then requires 200. | `_await_projector_ready` | mcp/tests/test_serving_response_conformance.py:829-838 |

## Update History

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated the base model and three refusal tables. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.
- 2026-09-05T06:24:16+00:00: Generated citation repair: "async def stream_events("; "def create_app(" repointed to mcp/src/agents_remember/serving/_app_common.py:116-116; mcp/src/agents_remember/serving/app.py:244-244. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `WorkspaceProjection` repointed to dashboard/src/types/projection.ts:817-830. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the 63-route surface, the requirement fixtures (`_seed_requirements`) and the 292/139 declared/driven ledger advance for the new requirement endpoints.

- 2026-08-31T12:00+02:00 — A005 refreshed the terminal-catalog hazard oracle to the reviewed
  68-key wire and 58 optional model fields. Verification remains closeout-owned.

- 2026-08-25T23:04+02:00 — L2 memory-quality repair: migrated the remaining two-column evidence table to anchored current-source citations after re-reading each claim; preserved all prior rationale and history.

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: refreshed the catalog hazard contract to the
  current 66-key wire and 56 optional model fields after adding the private dispatch receipt.
  Verification remains closeout-owned; no executable test result is claimed.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 curator: repaired the `_present_fields` citation range (terminal_catalog.py:597 → 600) surfaced by the leaf-scoped quality check; no content impact. Verification metadata remains closeout-owned.

- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-12T20:10+02:00 — L23 curator: documented super/master/leaf fixture lineage for response conformance; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_serving_response_conformance.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): repaired one citation. The
  `SERVED_TAIL_FIELDS` row cited `served_state.py` L61-L63, which is two blank lines plus the
  `def served_state_tail(` signature — a different symbol. `SERVED_TAIL_FIELDS` is declared at L58
  with its docstring at L59-L60, so the range is now L58-L60. No body text changed.
- 2026-08-01T08:40+02:00 — 260731-EFA-L4 curator: created the 61-route response-contract
  enforcement suite card. Its current sections and reference rows record the declaration boundary,
  camelCase validation, coverage ledger, structural websocket exemption, route inventory, hazard scan,
  and SSE-over-real-socket classes without retaining superseded line-number prose.
