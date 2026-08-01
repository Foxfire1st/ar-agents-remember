# test_served_state_conformance.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_served_state_conformance.py`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T08:45+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Conformance for the **served** state contract (`serving/served_state.py`) — the sibling of
`test_tool_response_conformance.py` for the surface that had no equivalent. Nothing anywhere
validated `/api/state`, the SSE `snapshot` event, or the projection *as served*: both keys of the
serve-time tail (`servingBuild`, `supervisorHeartbeat`) were injected into the dumped projection
with nothing declaring them, so the emitted body validated against no model at all —
`WorkspaceProjection` (`extra="forbid"`) included (L3-L8).

The suite drives the **real** route and the **real** SSE generator and validates what comes back
against `ServedWorkspaceProjection`, pinning the three shapes the assembly is allowed to take:
the 200 body carries the tail, the 304 branch carries no body at all, and a `delta` event is a bare
projection node — the asymmetry that stops the tail from being a projection field (L10-L14).

## Code Commentary

### Logic

#### `ServedStateTailTests` (L213-L257) — the tail is exactly the model's extension

- `test_tail_keys_are_the_declared_extension_over_the_projection` (L216-L222): the set difference
  `ServedWorkspaceProjection.model_fields - WorkspaceProjection.model_fields` must equal
  `SERVED_TAIL_FIELDS`, **and** the assembled `served_state_tail(...)` must produce exactly those
  keys. The declaration and the assembly cannot drift apart silently.
- `test_absent_halves_contribute_no_keys` (L224-L231): `stream_events` may be driven with neither
  collaborator or with only one; **a missing half is a missing key, never a null placeholder**.
- `test_the_two_halves_serialize_under_opposite_null_rules` (L233-L243): the build stamp **omits**
  what it could not prove (`commit`, `dirty`); the heartbeat **reports** a never-ticked supervisor
  as an explicit `null` (`lastTickAt`, `ageSeconds`). One shared `exclude_none` dump cannot do
  both, which is why `served_state_tail` is two dumps.
- `test_the_tail_is_json_native` (L245-L248): it is merged into a dict handed to
  `JSONResponse`/`ServerSentEvent`, so a pydantic model in there would only fail at encode time.
- `test_serving_only_fields_stay_out_of_the_persisted_projection` (L250-L257): the second consumer.
  `latest-state.json` is a `WorkspaceProjection` artifact, so declaring the tail on the projection
  would have put serve-time facts into it.

#### `ServedStateRouteConformanceTests` (L260-L352) — `/api/state`, for real

The class builds a real app (`create_app(_config(tmp), cadence=ProjectionCadence(interval=100))`,
L277-L280 — `interval=100` so prime publishes once and the ETag is stable for the 304 leg) and
disables the app's own supervisor loop in `setUp` (L267-L274), so the heartbeat row is entirely
this test's to write while the route still reads and serves it exactly as in production.

- `test_state_body_validates_against_the_served_model` (L310-L328) makes four claims in order:
  (a) the body **is** a `ServedWorkspaceProjection`, with a stale heartbeat six hours past the 60s
  cutoff; (b) it is **not** a bare `WorkspaceProjection` — `assertRaises(ValidationError)`, the
  assertion that used to be unmakeable because nothing declared the tail; (c) it carries no key
  beyond what the served model declares; (d) `_assert_populated` (L285-L308).
- `test_a_never_ticked_supervisor_still_serves_a_valid_body` (L330-L338): no heartbeat row at all —
  the nulls are reported rather than dropped, `stale` still reads true, and the body still
  validates.
- `test_the_304_branch_serves_the_etag_and_no_body` (L340-L352): the change gate must survive the
  tail being declared. The heartbeat is volatile and deliberately outside the content revision, so
  the test moves it (6h → 9h) between requests and requires **304, the same ETag, and
  `content == b""`**.

#### `ServedSnapshotConformanceTests` (L355-L410) — the SSE side and the asymmetry

`test_snapshot_validates_and_delta_carries_no_tail` (L364-L394) drives the real `stream_events`
generator off a primed `Projector`: the first frame is a `snapshot` whose `data` validates as a
`ServedWorkspaceProjection` carrying both tail halves and no undeclared key; then a delta is
broadcast and the second frame is asserted to be **one bare projection node** — `event ==
"lifecycle"`, `set(delta.data) & set(SERVED_TAIL_FIELDS) == set()`, and
`LifecycleProjection.model_validate(delta.data)`. A delta is not a state body, so the
whole-workspace tail has nothing there to be a field of.

`test_a_snapshot_without_a_tail_is_still_a_valid_served_body` (L396-L410) covers the path both tail
fields are optional *for*: `stream_events(projector)` with neither collaborator.

#### The fixture is populated on purpose (L16-L24, `_populate` L134-L173)

Built over an empty temp directory — which is what this file used to do — `lifecycles`,
`enclosures`, `engineProcesses` and `providers` all came back as `[]`, so the 200 body validated
against `ServedWorkspaceProjection` **without a single projection node ever being constructed**:
the assertions covered the serve-time tail and the top-level key set, and drift *inside* the dump
could not be caught.

`_populate` writes the three inputs that make those collections real: two leaf enclosure contracts
at different lifecycle positions (one still working, one landed and reclaimed — `_write_enclosure`,
L103-L131, using `amend_contract(contract, ContractCells(...))` for the landed cells), one observer
`lifecycle.started` event, and one provider `current.json` snapshot. `_assert_populated`
(L285-L308) then refuses a body whose collections are empty, and asserts *identities* rather than
counts: the lifecycle id, both enclosure worktree names, both distinct `cleanup` values (so a
projection that collapsed the contract's state cells would fail), and that the Engine Room admits
only the still-live worktree group.

`_config` (L86-L100) deliberately declares **no** `providers` entry: `read_providers` projects the
`current.json` snapshot on disk rather than the configured scopes, so declaring a scope would make
the projection tick try to *refresh* it against a real provider runtime — the same served bytes,
with a stack trace in the log for a collaborator this file is not testing.

### Conventions

`sys.path.insert(0, str(MCP_SRC))` after the third-party `fastapi.testclient` import (L38-L41) —
the suite idiom. Fixed `_TS` / `_REPO` / `_LEAVES` module constants (L79-L83) keep the fixture
deterministic. The async class is `unittest.IsolatedAsyncioTestCase`; the generator legs always
`await gen.aclose()` in a `finally`. `_tick_supervisor(age=timedelta(...))` (L282-L283) writes the
heartbeat row directly through `SupervisorHeartbeatStore(...).tick(now=...)`.

### Invariants And Boundaries

- The served body must validate against `ServedWorkspaceProjection` **and must not** validate
  against `WorkspaceProjection`. Both halves of that are the contract.
- `SERVED_TAIL_FIELDS` must stay exactly the served model's extension over the projection; the
  test asserts the declaration and the assembly against each other, in that direction.
- A missing tail half is an absent key, never `null`. Inside the heartbeat payload, a never-ticked
  supervisor is an explicit `null`, never an absent key. The two rules are opposite on purpose.
- The tail must not enter `latest-state.json`.
- A `delta` frame carries no tail key.
- The 304 path must keep firing while the heartbeat age moves — the heartbeat stays outside the
  content revision.
- The fixture must stay populated. Every shape assertion in this file is worth exactly as much as
  the projection it was made over, and `_assert_populated` is what keeps that true.
- The suite drives the real route and the real generator; substituting a hand-built body would
  re-open the gap it exists to close.

### Todos

None recorded. The route-wide sibling for the other 60 HTTP routes is
`test_serving_response_conformance.py`.

## Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md`
records `No entries configured yet.`), so every claim here is proven by repository source.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local test module; live retrieval was not available and the registry is empty. | `system/sources.md` — "No entries configured yet." | — |

## Repo-Internal References

The suite holds one declaration shut against one route and one generator, so its evidence is the
served-state module plus the two producers of the tail.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The contract under test: `ServedWorkspaceProjection`, `SERVED_TAIL_FIELDS`, `served_state_tail`, and the five reasons the tail lives here rather than on `WorkspaceProjection` (layer, the dump memo, the ETag, `latest-state.json`, and the snapshot/delta shape asymmetry). | L1-L63 | [served_state.py](agents-remember/mcp/src/agents_remember/serving/served_state.py) |
| The route and the SSE generator driven for real; the tail rides the `snapshot` only. | `create_app`; `stream_events` L300-L330 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The build half of the tail, whose payload omits what it could not prove (`commit`, `dirty`, `dashboardBuild`). | `ServingBuildPayload` L43-L63; `ServingBuild.payload` L77-L88 | [build_info.py](agents-remember/mcp/src/agents_remember/serving/build_info.py) |
| The heartbeat half, which reports a never-ticked supervisor as explicit nulls, plus the store the fixture ticks. | `SupervisorHeartbeatPayload`, `SupervisorHeartbeatStore.tick` | [supervisor_heartbeat.py](agents-remember/mcp/src/agents_remember/serving/supervisor_heartbeat.py) |
| The base projection the served model extends, and the `LifecycleProjection` node a delta frame must validate as. | `WorkspaceProjection`, `LifecycleProjection` | [projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The second consumer that must not gain serve-time fields. | `write_projection` L157-L164 | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The contract writer the enclosure fixture uses, including the typed `ContractCells` amendment for the landed leaf. | `default_contract`, `amend_contract`, `write_contract` | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The route-wide sibling: the same job for the other 60 HTTP routes, against each route's own declaration. | `DeclaredSurfaceCoverageTests` | [test_serving_response_conformance.py](agents-remember/mcp/tests/test_serving_response_conformance.py) |
| The serving suite that owns the ETag change gate and the build stamp in general; this file only pins that the declared tail does not break them. | `StateEtagTests`, `BuildInfoTests` | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |

## Cross-Repo References

The reviewed behaviour is wholly repository-local. The served camelCase body is consumed by the
cockpit bundle, which lives in this same repository under `dashboard/`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repository references found; the served projection's consumer is the in-repo cockpit. | `dashboard/src/types/projection.ts` | [projection.ts](agents-remember/dashboard/src/types/projection.ts) |

## Update History

- 2026-08-01T08:45+02:00 — 260731-EFA-L4 curator: created for the new served-state conformance
  suite, verified against the current 414-line source. Recorded the three classes and their exact
  ranges (`ServedStateTailTests` L213-L257, `ServedStateRouteConformanceTests` L260-L352,
  `ServedSnapshotConformanceTests` L355-L410); that the route class drives the real `/api/state`
  through `create_app` + `TestClient` with the app's own supervisor loop disabled so the heartbeat
  row is the test's to write; the four-part 200 assertion including the deliberate
  `assertRaises(ValidationError)` against the bare `WorkspaceProjection`; the **304 branch** —
  same ETag, empty body, asserted while the volatile heartbeat age moves from 6h to 9h; and the
  **snapshot/delta asymmetry** — a snapshot is a `ServedWorkspaceProjection`, a delta is one bare
  `LifecycleProjection` node carrying none of `SERVED_TAIL_FIELDS`. Also recorded the opposite null
  rules of the two tail halves, the populated-fixture requirement (`_populate` L134-L173 /
  `_assert_populated` L285-L308) without which the whole file validated an empty scaffold, and why
  `_config` declares no provider scope. Verification metadata pinned to the pre-leaf source
  authority (`abc7cbcc74921cdcb57a61529445f61641e919e7`) as a placeholder until closeout stamps the
  L4 code commit — this source file is new and not yet committed.
