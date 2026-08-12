# test_served_state_conformance.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_served_state_conformance.py`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T08:45+02:00                           |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`       |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Conformance for the **served** state contract (`serving/served_state.py`) — the sibling of
`test_tool_response_conformance.py` for the surface that had no equivalent. Nothing anywhere
validated `/api/state`, the SSE `snapshot` event, or the projection *as served*: both keys of the
serve-time tail (`servingBuild`, `agentNotifierHeartbeat`) were injected into the dumped projection
with nothing declaring them, so the emitted body validated against no model at all —
`WorkspaceProjection` (`extra="forbid"`) included cit:(["class ServedWorkspaceProjection"], mcp/src/agents_remember/serving/served_state.py:48-48).

The suite drives the **real** route and the **real** SSE generator and validates what comes back
against `ServedWorkspaceProjection`, pinning the three shapes the assembly is allowed to take:
the 200 body carries the tail, the 304 branch carries no body at all, and a `delta` event is a bare
projection node — the asymmetry that stops the tail from being a projection field cit:(["def served_state_tail"], mcp/src/agents_remember/serving/served_state.py:71-71).

## Code Commentary

### Logic

#### cit:([`ServedStateTailTests`], mcp/tests/test_served_state_conformance.py:213-257) — the tail is exactly the model's extension

- cit:([`test_tail_keys_are_the_declared_extension_over_the_projection`], mcp/tests/test_served_state_conformance.py:216-222): the set difference
  `ServedWorkspaceProjection.model_fields - WorkspaceProjection.model_fields` must equal
  `SERVED_TAIL_FIELDS`, **and** the assembled `served_state_tail(...)` must produce exactly those
  keys. The declaration and the assembly cannot drift apart silently.
- cit:([`test_absent_halves_contribute_no_keys`], mcp/tests/test_served_state_conformance.py:224-231): `stream_events` may be driven with neither
  collaborator or with only one; **a missing half is a missing key, never a null placeholder**.
- cit:([`test_the_two_halves_serialize_under_opposite_null_rules`], mcp/tests/test_served_state_conformance.py:233-243): the build stamp **omits**
  what it could not prove (`commit`, `dirty`); the heartbeat **reports** a never-ticked supervisor
  as an explicit `null` (`lastTickAt`, `ageSeconds`). One shared `exclude_none` dump cannot do
  both, which is why `served_state_tail` is two dumps.
- cit:([`test_the_tail_is_json_native`], mcp/tests/test_served_state_conformance.py:249-252): it is merged into a dict handed to
  `JSONResponse`/`ServerSentEvent`, so a pydantic model in there would only fail at encode time.
- cit:([`test_serving_only_fields_stay_out_of_the_persisted_projection`], mcp/tests/test_served_state_conformance.py:250-257): the second consumer.
  `latest-state.json` is a `WorkspaceProjection` artifact, so declaring the tail on the projection
  would have put serve-time facts into it.

#### cit:([`ServedStateRouteConformanceTests`], mcp/tests/test_served_state_conformance.py:260-352) — `/api/state`, for real

The class builds a real app (`create_app(_config(tmp), cadence=ProjectionCadence(interval=100))`,
L277-L280 — `interval=100` so prime publishes once and the ETag is stable for the 304 leg) and
disables the app's own agent-notifier loop in `setUp` cit:(["class ServedStateRouteConformanceTests"], mcp/tests/test_served_state_conformance.py:264-275), so the heartbeat row is entirely
this test's to write while the route still reads and serves it exactly as in production.

- cit:([`test_state_body_validates_against_the_served_model`], mcp/tests/test_served_state_conformance.py:310-328) makes four claims in order:
  (a) the body **is** a `ServedWorkspaceProjection`, with a stale heartbeat six hours past the 60s
  cutoff; (b) it is **not** a bare `WorkspaceProjection` — `assertRaises(ValidationError)`, the
  assertion that used to be unmakeable because nothing declared the tail; (c) it carries no key
  beyond what the served model declares; (d) cit:([`_assert_populated`], mcp/tests/test_served_state_conformance.py:285-308).
- cit:([`test_a_never_ticked_agent_notifier_still_serves_a_valid_body`], mcp/tests/test_served_state_conformance.py:340-349): no heartbeat row at all —
  the nulls are reported rather than dropped, `stale` still reads true, and the body still
  validates.
- cit:([`test_the_304_branch_serves_the_etag_and_no_body`], mcp/tests/test_served_state_conformance.py:340-352): the change gate must survive the
  tail being declared. The heartbeat is volatile and deliberately outside the content revision, so
  the test moves it (6h → 9h) between requests and requires **304, the same ETag, and
  `content == b""`**.

#### cit:([`ServedSnapshotConformanceTests`], mcp/tests/test_served_state_conformance.py:355-410) — the SSE side and the asymmetry

cit:([`test_snapshot_validates_and_delta_carries_no_tail`], mcp/tests/test_served_state_conformance.py:364-394) drives the real `stream_events`
generator off a primed `Projector`: the first frame is a `snapshot` whose `data` validates as a
`ServedWorkspaceProjection` carrying both tail halves and no undeclared key; then a delta is
broadcast and the second frame is asserted to be **one bare projection node** — `event ==
"lifecycle"`, `set(delta.data) & set(SERVED_TAIL_FIELDS) == set()`, and
`LifecycleProjection.model_validate(delta.data)`. A delta is not a state body, so the
whole-workspace tail has nothing there to be a field of.

cit:([`test_a_snapshot_without_a_tail_is_still_a_valid_served_body`], mcp/tests/test_served_state_conformance.py:396-410) covers the path both tail
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
cit:([`_assert_populated`], mcp/tests/test_served_state_conformance.py:285-308) then refuses a body whose collections are empty, and asserts *identities* rather than
counts: the lifecycle id, both enclosure worktree names, both distinct `cleanup` values (so a
projection that collapsed the contract's state cells would fail), and that the Engine Room admits
only the still-live worktree group.

cit:([`_config`], mcp/tests/test_served_state_conformance.py:86-100) deliberately declares **no** `providers` entry: `read_providers` projects the
`current.json` snapshot on disk rather than the configured scopes, so declaring a scope would make
the projection tick try to *refresh* it against a real provider runtime — the same served bytes,
with a stack trace in the log for a collaborator this file is not testing.

### Conventions

`sys.path.insert(0, str(MCP_SRC))` after the third-party `fastapi.testclient` import cit:(["fastapi.testclient"], mcp/tests/test_served_state_conformance.py:38-41) —
the suite idiom. Fixed `_TS` / `_REPO` / `_LEAVES` module constants cit:(["_REPO ="], mcp/tests/test_served_state_conformance.py:83-83) keep the fixture
deterministic. The async class is `unittest.IsolatedAsyncioTestCase`; the generator legs always
`await gen.aclose()` in a `finally`. `_tick_agent_notifier(age=timedelta(...))` cit:([`_tick_agent_notifier`], mcp/tests/test_served_state_conformance.py:288-291) writes the
heartbeat row directly through `AgentNotifierHeartbeatStore(...).tick(now=...)`.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local test module; live retrieval was not available and the registry is empty. | — | — |

## Repo-Internal References

The suite holds one declaration shut against one route and one generator, so its evidence is the
served-state module plus the two producers of the tail.

| Finding | Anchor | Source |
| --- | --- | --- |
| The contract under test: `ServedWorkspaceProjection`, `SERVED_TAIL_FIELDS`, `served_state_tail`, and the five reasons the tail lives here rather than on `WorkspaceProjection` (layer, the dump memo, the ETag, `latest-state.json`, and the snapshot/delta shape asymmetry). | "class ServedWorkspaceProjection", "def served_state_tail" | mcp/src/agents_remember/serving/served_state.py:48-48; mcp/src/agents_remember/serving/served_state.py:71-71 |
| The route and the SSE generator driven for real; the tail rides the `snapshot` only. |"def create_app("; "async def stream_events("|mcp/src/agents_remember/serving/_app_common.py:115-115; mcp/src/agents_remember/serving/app.py:230-230|
| The build half of the tail, whose payload omits what it could not prove (`commit`, `dirty`, `dashboardBuild`). | `ServingBuildPayload` | mcp/src/agents_remember/serving/build_info.py:43-63 |
| The heartbeat half, which reports a never-ticked agent-notifier as explicit nulls, plus the store the fixture ticks. | `AgentNotifierHeartbeatPayload` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:31-55 |
| The base projection the served model extends, and the `LifecycleProjection` node a delta frame must validate as. | `WorkspaceProjection` | mcp/src/agents_remember/observer/projection.py:990-1009 |
| The second consumer that must not gain serve-time fields. | `write_projection` | mcp/src/agents_remember/serving/projections/projection_store.py:158-164 |
| The contract writer the enclosure fixture uses, including the typed `ContractCells` amendment for the landed leaf. | `default_contract`; `amend_contract`; `write_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:199-227; mcp/src/agents_remember/worktrees/worktree_contract.py:343-393; mcp/src/agents_remember/worktrees/worktree_contract.py:472-475 |
| The route-wide sibling: the same job for the other 60 HTTP routes, against each route's own declaration. | "class DeclaredSurfaceCoverageTests(unittest.TestCase):" | mcp/tests/test_serving_response_conformance_live.py:486-486 |
| The serving suite that owns the ETag change gate and the build stamp in general; this file only pins that the declared tail does not break them. | `StateEtagTests`; `BuildInfoTests` | mcp/tests/test_serving.py:557-641; mcp/tests/test_serving_cli.py:36-181 |

## Cross-Repo References

The reviewed behaviour is wholly repository-local. The served camelCase body is consumed by the
cockpit bundle, which lives in this same repository under `dashboard/`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository references found; the served projection's consumer is the in-repo cockpit. | "export interface WorkspaceProjection" | dashboard/src/types/projection.ts:542-542 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T10:40+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: converted the history `(L…)`
  citations and rebound the contract/projection rows; exact non-fixing check returns zero
  findings.

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
