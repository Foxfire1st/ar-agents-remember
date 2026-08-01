# test_serving_response_conformance.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_serving_response_conformance.py`   |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-01T10:40+02:00                             |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`         |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The enforcement for the declared HTTP response contract (`serving/response_contract.py`) across
**all 61 HTTP routes** the serving app registers. It is the sibling of
`test_served_state_conformance.py`, widened from one route to the whole surface.

It exists because **the declaration cannot be the gate**. FastAPI applies `response_model` only to
values it serializes itself: a handler returning a `Response` instance is handed back untouched and
never reaches `serialize_response`. **57 of the 61 handlers do exactly that**, and two more are
async-generator SSE routes — so on **59 of 61** the decorator buys an OpenAPI schema and validates
nothing at runtime. A suite that only asserted "every route declares a model" would have gone green
the moment the decorators landed and would have caught no drift on those 59 routes ever
(L7-L13; `response_contract.py` L8-L20).

So the tests here **drive the real routes and validate what actually came back**.

## Code Commentary

### Logic

#### `validate_wire` (L211-L231) — what pins camelCase

`validate_wire(model, body)` is `TypeAdapter(model).validate_python(body, by_alias=True,
by_name=False)`, and that pairing is the whole point. Both `WireResponse` and
`conversation/models.WireModel` set `populate_by_name=True`, so a plain
`TypeAdapter(...).validate_python(body)` accepts `identity_digest` exactly as happily as
`identityDigest`: flip one handler's `model_dump(by_alias=True)` to `by_alias=False` and every key
on that route goes snake_case — a total break for the cockpit, which reads the camelCase names —
while every model still validates and the suite still reports all green.

`by_name=False` closes it: **only the alias is accepted**, so a key that arrived in field-name form
is an undeclared key against `extra="forbid"` and fails. Models with no alias generator
(`HttpDetailRefusal`, and the non-wire models the unions reach) are unaffected — with no alias to
prefer, pydantic still matches the field name, which for them *is* the wire name.

`field_name_form` (L234-L248) rewrites a real body into field-name form so the rule is *proved*
load-bearing rather than asserted:
`test_a_field_name_body_fails_the_declared_contract` (L1149-L1174) drives
`GET /api/terminal/sessions`, shows the route really answers `tmuxName`, shows the old plain
validation **accepts** the rewritten `tmux_name` body, and shows `validate_wire` rejects it.
`test_the_conversation_wire_is_pinned_to_camel_case_too` (L1176-L1196) pins the same axis on the 25
conversation routes, which dump `by_alias=True` by hand.

#### `DeclaredSurfaceCoverageTests` (L2435-L2492) — the score, stated as a number

`declared_pairs(app)` (L194-L208) is the denominator: every `(method, path, status)` triple the app
declares. `DRIVEN` (L260) is filled by each `_check` as it runs (L852-L878; L1910-L1922; L2144;
L2201; L2213), and `_driven_pairs()` (L2409-L2432) re-runs the driving classes when the module was
run partially, so a coverage number is never computed from a partial run.

`test_the_conformance_table_accounts_for_every_declared_pair` (L2458-L2469) pins three numbers,
"so neither side can move without a decision":

- **286** declared `(method, path, status)` triples
- **133** driven against a real body
- **153** declared-and-undriven

The 153 are not a suppression list. `UNDRIVEN_DECLARATIONS` (L2271-L2386) is **39 route rows**,
each carrying a written reason, and the test asserts it **EXACTLY**
(`assertEqual(_grouped(declared - driven), UNDRIVEN_DECLARATIONS)`) — so a declaration that stops
being driven has to be added by hand, and a leg that becomes drivable has to be removed. The
reasons group into: one shared refusal table over seventeen conversation routes (reaching each
typed failure needs a real bridge driven into a stale epoch / rejected operation / dead socket
mid-write); the library surface, whose 200s need a real vendor binary with an installed native
history store; the projection surface's 503 "not primed yet", a startup race the fixtures
deliberately do not have; and the harness-control 503s, which need a bridge that accepts a
connection and then fails.

**Record the shortfall as a number, not as an implication of completeness.** 153 of 286 declared
legs are not driven. What changed with this suite is that the remainder is *counted*: before it,
the driving tests kept a `self.checked` set that no assertion ever read, **88 of 286** pairs were
driven, and **seven declared models could be made mathematically unsatisfiable** — a required `str`
retyped to `int` — without one test going red (L254-L258; L2438-L2442).

The claim that does hold without exception is the weaker one:
`test_every_route_has_at_least_one_driven_status` (L2471-L2482) asserts **every one of the 61
routes is driven on at least one status**, which is what makes the ledger a list of unexercised
*legs* rather than of unexercised routes.

`test_the_open_status_map_is_total_over_the_declared_outcomes` (L2484-L2492) asserts
`_OPEN_STATUS_BY_OUTCOME` covers every declared `OpenConversationOperation.outcome`; it is what
removed an undeclared 500 that the old `.get(..., 500)` could answer with a full operation body.

#### `ServingRouteInventoryTests` (L495-L627) — the surface, and the one structural exemption

The walk happens inside a **started** app (`stack.enter_context(TestClient(self.app))`, L506-L509),
because `add_api_route` is legal from the lifespan and a pre-startup walk would miss such a route
entirely.

- `test_every_http_route_declares_a_response_model` (L512-L518): no HTTP route may lack one.
- `test_the_websocket_is_exempt_because_it_structurally_cannot_declare_one` (L520-L530): the
  exemption is **by route class, not by a path skip-list** — an `APIWebSocketRoute` has no
  `response_model` attribute at all, and the test asserts that absence, so the exemption cannot
  quietly widen to swallow a future undeclared HTTP route. The one socket is
  `/api/terminal/{session}`.
- `test_the_declared_surface_is_the_whole_surface` (L532-L537): **61 HTTP + 1 websocket**, pinned.
- `test_no_registration_form_escapes_the_walker` (L539-L561): a kind the walker does not model is
  refused. FastAPI's own doc routes are excluded by the URLs the app reports for them, never by a
  hard-coded path list.
- `test_the_mounted_surface_is_pinned` (L563-L570): mounts == `[""]` (`serving/static.py` mounts
  the cockpit bundle at `/`).
- `test_every_declared_refusal_status_names_a_model` (L572-L595) and
  `test_a_modelless_responses_entry_is_a_304_or_a_declared_sse_media_type` (L597-L627): a
  `responses` entry without a model would let a refusal shape drift while still looking declared,
  and `declared_model` would fall back to the route's **success** model for that status. Carrying a
  `content` key does not excuse it; the only modelless entries allowed are pinned by name —
  `("/api/events", 200)`, `("/api/state", 304)`, `("/api/stream", 200)`,
  `("/api/terminal/{ar_session_id}/conversation/events", 200)`.

#### `walk_routes` (L125-L158) and `RouteWalkerTests` (L701-L780)

The inventory is an argument of the form "these are all the routes, and all of them declare a
model"; its first clause is a claim about the walker, so each registration form is registered,
**served**, and then found at the path it actually answered on:

- `include_router` — FastAPI keeps the included router behind one opaque `_IncludedRouter`; the 25
  conversation routes live inside one, so a test reading `app.routes` alone would have seen 36 of
  the 61. The inner `route.path` does **not** carry the prefix, so the walker applies
  `include_context.prefix` itself.
- `app.mount` — a starlette `Mount` whose `.routes` is the mounted app's own table.
- `app.router.add_route` — a plain starlette `Route`: serves HTTP 200 JSON, is neither an
  `APIRoute` nor an `APIWebSocketRoute`, and would be stepped over by every `isinstance` filter.
- registration from inside the lifespan (L766-L780).

#### `ValidatedRouteHazardTests` (L630-L698)

`GET /api/terminal/sessions` and `GET /api/harnesses` return a bare `dict`, so unlike the other 59
FastAPI validates them for real — and a drifted payload is answered as **HTTP 500**, not passed
through. On `/api/terminal/sessions` that is a 52-key body assembled by hand from a
36-optional-field dataclass that is actively grown. `_emitted_keys` (L647-L685) therefore **AST
scans** `TerminalCatalogEntry.to_json` (an instance cannot prove the set, because every optional key
goes through `_present_fields` and is absent when `None`) and
`test_the_catalog_wire_model_covers_every_key_to_json_emits` (L687-L698) asserts set **equality in
both directions** against `TerminalCatalogEntryWire`'s aliases, plus `len(emitted) == 52` so a scan
reading zero keys cannot satisfy the equality. This fires when the field is added — earlier than
the runtime 500, and earlier than a conformance run, which only sees the fields its fixture
happens to populate.

#### The driving classes

- `ServingResponseConformanceTests` (L786-L1864): one real request per route through the real app.
  `_check` (L852-L878) records the driven triple, asserts the status, resolves
  `declared_model(route, status)` — `responses[status]["model"]` when there is one, `response_model`
  otherwise (L172-L182) — and validates through `validate_wire`. The fixture is deliberately
  shaped to reach shapes a declaration named and nothing drove: a **second, memory-less repo** is
  the only input that reaches `OnboardingPartnerNone`, the fifth member of
  `GET /api/files/onboarding`'s union (L806-L813; L885-L898); a `legacy` seat with no control
  endpoint is the only input that reaches `/paste`'s 409 `unsupported` leg (L829-L831).
  `_client` (L842-L850) uses a **loopback peer** because conversation authorization is loopback-only
  — the default `testclient` host would turn every conversation route into the same 403 — and takes
  a `peer` argument so the 403 leg can be driven deliberately.
- `ConversationSuccessConformanceTests` (L1870-L2117): real 200/202 bodies off a real control
  bridge, over real uvicorn rather than `TestClient` because the bridge must live on this test's own
  event loop.
- `ConversationCompositionRefusalTests` (L2120-L2147): the one control refusal `create_app` cannot
  produce, because it always composes a complete `ConversationRuntime`. The routers are
  independently mountable, and a router mounted without its runtime is the state
  `CONTROL_RESPONSES[503]` exists for — declared on all 17 control routes, driven on none until
  this class.
- `StreamContractTests` (L2153-L2265): the branches a body-shaped model cannot express — the bare
  `304` with an empty body (L2203-L2213), the SSE frames off the real generators, and (via the
  `serve` helper, L268-L291, a real uvicorn on a loopback socket) both SSE routes driven **as
  routes** for the first time in this repository (L2185-L2201). `TestClient` cannot drive an SSE
  route: the stream never ends, so a read from inside the portal thread cannot be closed from
  outside it. Driving the generator directly is also what reaches the *second* frame, where the
  snapshot/delta asymmetry lives (L2215-L2252).

### Conventions

Third-party imports (`fastapi`, `starlette`) precede the `sys.path.insert(0, str(MCP_SRC))`
(L62-L69); package imports and the `_control_plane` test helper follow it — the suite idiom.
Every driving class ends its cases with `COMPLETED.add(f"{type(self).__name__}.{self._testMethodName}")`
so `_driven_pairs()` can tell a partial run from a whole one. Route keys are always the **declared**
path template (`route="/api/terminal/{ar_session_id}/conversation/interrupt"`) even when the request
uses a concrete id, because that is what the route index is keyed on. `_LivePaneHost` (L321-L352)
mirrors `TerminalHost`'s signatures exactly — an argument the double ignores is still an argument
production passes, so it stays named — and exists so the liveness sweep does not delete every
seeded catalog row before `GET /api/terminal/sessions` is conformance-tested.

### Invariants And Boundaries

- The suite must keep **driving** routes. An assertion that only reads declarations enforces
  nothing on 59 of the 61 handlers.
- `validate_wire`'s `by_alias=True, by_name=False` pairing is load-bearing and must not be relaxed
  to a plain `validate_python`; `field_name_form` exists to keep that provable.
- `UNDRIVEN_DECLARATIONS` is asserted **exactly**, never as a subset. It is a ledger, not a
  suppression list.
- The three headline numbers (286 / 133 / 153) are pinned deliberately. Moving any of them is a
  decision, and the ledger row must move with it.
- Every route must stay driven on at least one status; that is the claim that holds without
  exception.
- The websocket exemption stays **structural** (no `response_model` attribute), never a path list.
- The walker must model every registration form the app can dispatch, and the inventory must refuse
  any kind it does not model.
- SSE routes are driven over a real socket, not `TestClient`.

### Todos

The 153 undriven legs are the standing debt, itemised at L2271-L2386. The largest tranches need a
real vendor harness (the library surface's 200s) or a control bridge that fails mid-write (the
conversation refusal table and the harness-control 503s); neither is modelled by the current
fixtures.

## Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md`
records `No entries configured yet.`). One third-party behaviour is load-bearing and is recorded
from the code that observes it rather than from vendor documentation: FastAPI's
`fastapi.routing.get_request_handler` returns a `Response` instance untouched and never reaches
`serialize_response`, which is why 59 of the 61 declarations validate nothing at runtime.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local test module; live retrieval was not available and the registry is empty. | `system/sources.md` — "No entries configured yet." | — |

## Repo-Internal References

The suite is the enforcement half of a two-part arrangement: the declarations live in the contract
modules, and everything that proves them lives here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The declared contract under test, including why the declaration alone is not the gate (57 `Response`-returning handlers, 2 SSE generators, 2 dict-returning routes) and the `*_RESPONSES` refusal tables. | L1-L60 | [response_contract.py](agents-remember/mcp/src/agents_remember/serving/response_contract.py) |
| The conversation surface's own declarations, kept in a separate module because they need `conversation/models.py` while `serving/app.py` imports the file/notes/change-set routes first. | `CONTROL_RESPONSES`, `CONVERSATION_RESPONSES` | [conversation/response_contract.py](agents-remember/mcp/src/agents_remember/serving/conversation/response_contract.py) |
| The app whose started route table is walked, and the SSE generator `StreamContractTests` drives directly. | `create_app`, `stream_events` L300-L330 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The 52-key producer the hazard scan reads, and the `_present_fields` conditionality that is why an AST scan is used instead of a constructed instance. | `TerminalCatalogEntry.to_json`, `_present_fields` | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| The wire model whose aliases that scan is compared against, set-equal in both directions. | `TerminalCatalogEntryWire` | [response_contract.py](agents-remember/mcp/src/agents_remember/serving/response_contract.py) |
| The open-status map asserted total over the declared outcomes, and the `_open_call` that indexes it directly. | `_OPEN_STATUS_BY_OUTCOME` | [conversation/library/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/api.py) |
| The control router mounted without a runtime to reach the composition 503. | `router`, `_map_typed_error` | [conversation/control/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/api.py) |
| The raw event stream whose `ready` marker is the one frame `/api/events` mints and therefore the only one it can honestly declare. | `stream_raw_events` | [events.py](agents-remember/mcp/src/agents_remember/serving/events.py) |
| The served-state tail whose keys a `delta` frame must not carry — the asymmetry the `/api/stream` declaration rests on. | `SERVED_TAIL_FIELDS` L58-L60 | [served_state.py](agents-remember/mcp/src/agents_remember/serving/served_state.py) |
| The control-bridge harness fixtures the success conformance class drives (`FakeControlAdapter`, `make_harness`, `OPERATOR`). | `FakeControlAdapter`, `make_harness` | [_control_plane.py](agents-remember/mcp/tests/_control_plane.py) |
| The single-route sibling this suite was widened from, which owns `/api/state`'s assembled body and the SSE snapshot. | `ServedStateRouteConformanceTests`, `ServedSnapshotConformanceTests` | [test_served_state_conformance.py](agents-remember/mcp/tests/test_served_state_conformance.py) |

## Cross-Repo References

The routes, models and fixtures are all repository-local. The declared camelCase wire is a real
boundary — the cockpit frontend reads those key names — but the consumer lives in this same
repository under `dashboard/`, so it is recorded here rather than as a cross-repo dependency.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repository references found; the camelCase wire's consumer is the in-repo cockpit bundle. | `dashboard/src/types/projection.ts` | [projection.ts](agents-remember/dashboard/src/types/projection.ts) |

## Update History

- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): repaired one citation. The
  `SERVED_TAIL_FIELDS` row cited `served_state.py` L61-L63, which is two blank lines plus the
  `def served_state_tail(` signature — a different symbol. `SERVED_TAIL_FIELDS` is declared at L58
  with its docstring at L59-L60, so the range is now L58-L60. No body text changed.
- 2026-08-01T08:40+02:00 — 260731-EFA-L4 curator: created for the new 61-route response-contract
  enforcement suite. Verified against the current 2496-line source rather than against the
  commissioning brief. Recorded why the declaration cannot be the gate (57 handlers return a
  `Response`, 2 are SSE generators, so 59 of 61 declarations validate nothing at runtime —
  L7-L13, matching `response_contract.py` L8-L20); `validate_wire`'s `by_alias=True, by_name=False`
  as the thing that pins camelCase over `populate_by_name=True`, and `field_name_form` as the proof
  that it is load-bearing (L211-L248; L1149-L1174); and the coverage ledger stated as a number —
  **286 declared triples, 133 driven, 153 undriven**, with `UNDRIVEN_DECLARATIONS` counted
  independently as **39 route rows summing to exactly 153 statuses** and asserted EXACTLY
  (L2271-L2386; L2458-L2469). The card says the shortfall plainly and does not let "every route is
  driven on at least one status" (L2471-L2482) stand in for completeness. Also recorded the
  structural websocket exemption, the pinned 61+1 surface, the four modelless `responses` entries,
  the four registration forms `walk_routes` models and `RouteWalkerTests` drives for real, the
  52-key `to_json` hazard scan, and the four driving classes including the SSE-over-real-socket
  legs. Verification metadata pinned to the pre-leaf source authority
  (`abc7cbcc74921cdcb57a61529445f61641e919e7`) as a placeholder until closeout stamps the L4 code
  commit — this source file is new and not yet committed.
