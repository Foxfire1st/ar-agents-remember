# mcp/src/agents_remember/serving/served_state.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/served_state.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T15:10+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[serving overview](overview.md)

## Purpose

`served_state.py` declares what `GET /api/state` and the SSE `snapshot` frame ACTUALLY put on
the wire, which is not a `WorkspaceProjection`. It is that projection plus a two-key serve-time
tail — `servingBuild` (which process is answering) and `supervisorHeartbeat` (how long ago the
supervisor last ticked, as of *this* response). Both keys were written into an
already-validated, already-dumped dict with nothing declaring them, so the emitted object was
outside its own model: feeding a served body back through `WorkspaceProjection`
(`model_config = ConfigDict(extra="forbid")`, `observer/projection.py` L967-L970) raised on the
two extra keys. This module is that missing declaration, plus the one function that builds the
tail.

## Code Commentary

### Logic

Two exports and one constant, all small:

- **`ServedWorkspaceProjection(WorkspaceProjection)`** (L47-L55) adds exactly
  `servingBuild: ServingBuildPayload | None = None` and
  `supervisorHeartbeat: SupervisorHeartbeatPayload | None = None`. Both are OPTIONAL rather
  than required, because `stream_events(projector)` driven with neither a build stamp nor a
  heartbeat reader serves a snapshot with neither key, and that is a valid served body — the
  conformance suite drives that path.
- **`SERVED_TAIL_FIELDS`** (L58-L60) names the two keys as data: exactly this model's extension
  over the projection it wraps, so the assembly and the contract cannot drift apart silently.
- **`served_state_tail(*, build, heartbeat)`** (L63-L78) returns the JSON-ready tail dict to be
  merged onto a **copy** of the memoized projection dump. It is two `model_dump` calls and not
  one, because the two halves serialize under opposite rules: a missing build fact is OMITTED
  (`build.payload().model_dump(mode="json", exclude_none=True)` — absence is not a fabricated
  claim), while a missing heartbeat fact is an explicit NULL
  (`heartbeat.model_dump(mode="json")`, no `exclude_none` — a supervisor that never ticked is a
  reported state, not a missing key). `exclude_none` is recursive, so one shared dump could not
  express both.

Both call sites are in `serving/app.py` and both are one line: `stream_events` does
`payload.update(served_state_tail(build=build, heartbeat=supervisor_heartbeat))` under
`if delta.event == "snapshot"` (L328-L329), and `_state_response` does the same against
`runtime.build` and `_supervisor_heartbeat_payload(runtime)` (L980-L982).

### Conventions

Field names here are the **wire** names (`servingBuild`, `supervisorHeartbeat`), not snake_case
with an alias generator — they mirror `WorkspaceProjection`, whose fields are already camelCase
by declaration. The two payload types are owned by the modules that produce them
(`ServingBuildPayload` in `build_info.py`, `SupervisorHeartbeatPayload` in
`supervisor_heartbeat.py`); this module only composes them.

### Invariants And Boundaries

- **The tail is deliberately NOT on `WorkspaceProjection`.** The module docstring records five
  reasons in ascending order of cost, and all five are load-bearing:
  1. **Layer.** `Projector` builds the projection at TICK time; both keys are serving-layer
     facts computed at SERVE time (`_supervisor_heartbeat_payload` is explicitly "the tick age
     at RESPONSE time"). A tick-time model cannot hold a per-response value.
  2. **The dump memo.** `app._ProjectionBodyCache` (`app.py` L246-L276) memoizes the ~1.3 MB
     projection dump per published instance *because* the volatile tail is merged onto a
     shallow copy afterwards. Projection fields would sit inside the memo and would have to be
     either stale or uncached; the memo saves a measured 13.7-16.5 ms per request.
  3. **The ETag.** The heartbeat is deliberately outside the projector's content revision, so a
     volatile age never busts the ETag. As a projection field it would change every tick and the
     `304` path would stop firing.
  4. **A second consumer.** `observer.projection_store.write_projection` persists
     `WorkspaceProjection` into `latest-state.json`; serving-only fields must not enter that
     artifact's schema.
  5. **Shape.** Only the SSE `snapshot` carries the tail. A `delta` frame is one projection
     node, not a state body, so there is nothing there for a whole-workspace stamp to be a field
     of.
- **The body is assembled, not dumped from one model — and that is the point.** Validating a
  `ServedWorkspaceProjection` per request would re-parse the whole ~1.3 MB body and hand back
  exactly what the memo exists to save. The enforcement therefore lives in
  `mcp/tests/test_served_state_conformance.py`, which drives the real route and the real
  generator and validates what actually came back.
- **`SERVED_TAIL_FIELDS` is the only permitted extension.** Anything else added to the served
  body is undeclared and fails the served-state conformance suite against `extra="forbid"`.

### Todos

None specific to this module. The wider "declare every route's response" contract lives in
`serving/response_contract.py` and `serving/conversation/response_contract.py`.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available. The served-state contract is repository-local.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The model extends the observer's projection and composes two serving-owned payload models; both
consumers are one-line merges in the serving app, and the enforcement is a dedicated conformance
suite rather than per-request validation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The strict base this model extends: `WorkspaceProjection` with `extra="forbid"`, which is what made the two injected keys a contract violation. | L967-L970 | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The build half of the tail, and the `exclude_none` honest-unknown rule `served_state_tail` applies to it. | `ServingBuildPayload`; `ServingBuild.payload` | [build_info.py](build_info.py.md) |
| The heartbeat half of the tail, serialized WITHOUT `exclude_none` so a never-ticked supervisor reports explicit nulls. | `SupervisorHeartbeatPayload` | [supervisor_heartbeat.py](supervisor_heartbeat.py.md) |
| The two consumers: the SSE snapshot merge and the `/api/state` merge onto a copy of the memoized dump, plus the memo itself. | L246-L276; L328-L329; L978-L982 | [app.py](app.py.md) |
| The suite that validates the real route's and the real generator's output against `ServedWorkspaceProjection`, since per-request validation is deliberately not done. | `test_served_state_conformance` | [test_served_state_conformance.py](agents-remember/mcp/tests/test_served_state_conformance.py) |

## Cross-Repo References

No external repository boundary is involved; this is the serving app's own wire shape.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the two
  `observer/projection.py` citations — the Purpose prose and the first reference row — after that
  module was restructured. `L957-L960` → `L967-L970`; read there: `class WorkspaceProjection`
  (L967), its docstring (L968) and `model_config = ConfigDict(extra="forbid")` (L970). No body
  claim changed.

- 2026-08-01T08:05+02:00 — 260731-EFA-L4 curator: created for the new
  `serving/served_state.py`. Documented `ServedWorkspaceProjection` (the two serve-time keys
  that `/api/state` and the SSE `snapshot` were injecting into an already-dumped, undeclared
  dict), `SERVED_TAIL_FIELDS`, and `served_state_tail`'s deliberate two-dump split (build
  omitted via `exclude_none`, heartbeat nulled without it). Recorded the five reasons the tail
  is NOT a `WorkspaceProjection` field — layer, the `_ProjectionBodyCache` memo, the ETag
  revision, `latest-state.json`, and the snapshot-only shape — and that enforcement is
  `test_served_state_conformance.py` rather than per-request validation. Verification metadata
  is a placeholder pinned to the leaf base `abc7cbcc`; closeout stamps the real commit.
