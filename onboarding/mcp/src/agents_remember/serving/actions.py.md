# mcp/src/agents_remember/serving/actions.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/serving/actions.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-06-28T07:32+02:00                       |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`   |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[overview.md](overview.md)

## Purpose

`actions.py` is the **POST action layer**: pure availability mapping (slice 4b), gate
decisions (slice 6b), task-28 attention dismissals, and task-29 actionable-drift dismissal. Lifecycle transitions
(`resume`/`integrate`/`cleanup`) are validated against the reducer's precomputed
`ActionAvailability` and acknowledged without mutation; gate-decision verbs
(`approve`/`reject`/`request-revision`/`cancel`) carry a `GateDecisionIntent`; `dismiss`
returns a lifecycle-scoped `DismissalIntent`, except `kind=="actionable-drift"` may omit `target` as the
repo-level one-shot signal. The UI is still never the gate *enforcement*.

## Code Commentary

- `ActionRequest` (Pydantic, `extra="forbid"`): optional `target` (a lifecycle id or enclosure name),
  `actor` (the constrained `Actor` literal, default `developer`), optional `gateId`, optional
  `note`, and attention-dismissal fields `itemId` / `kind`. `source` is set server-side to
  `"dashboard"`, never trusted from the body. `target` may be omitted only for a `cancel` carrying a
  concrete `gateId`, for `dismiss` of a `gate-open` item carrying a concrete `gateId`, or for
  targetless `actionable-drift` dismissal.
- `ActionEvaluationContext` is the internal dataclass that carries the request context echoed into
  intents (`actor`, `now`, `gate_id`, `note`, `item_id`, `kind`) so the dispatcher can stay small while
  preserving the public `evaluate_action(...)` call shape.
- `evaluate_action(projection, action, target, *, actor, now, gate_id?, note?, item_id?, kind?) -> ActionOutcome` is
  **pure** and delegates to focused branch helpers:
  - `_find_actions` resolves the target (lifecycle by `id`, then enclosure by `enclosure`) and
    returns its precomputed `actions`, or `None`.
  - `_precomputed_action_outcome` handles lifecycle/enclosure transition actions: unknown target ⇒
    `404 {"status":"unknown-target"}`; action absent from the node's list ⇒ `409
    {"status":"unavailable"}`; present-but-disabled ⇒ `409` with the reducer's `disabledReason` (and
    `nextSafeAction` when set); enabled ⇒ `202` with an attributed intent `{actor,
    source:"dashboard", ts, action, target}`.
  - `_gate_decision_outcome` handles a **gate-decision verb** (`GATE_DECISION_ACTIONS` = approve/reject/request-revision/cancel,
    slice 6b) short-circuits *before* the availability lookup: it returns `202` plus a
    `GateDecisionIntent(lifecycle_id=target, decision=action, gate_id=gate_id, note=note)` on the
    `ActionOutcome`. A `reject` without a non-empty `note` returns
    `400 {"status":"missing-rejection-reason"}` and carries no intent. Missing `target` returns
    `400 missing-target` except for `cancel` with `gateId`, which intentionally supports clearing
    stale workspace gates. The gate's own state is the safety check, so this path never consults
    `ActionAvailability`.
  - `_dismiss_action_outcome` handles the **attention-dismissal verb** (`DISMISS_ACTION = "dismiss"`, task 28 S5.2) short-circuits
    before availability lookup: it requires `itemId`; lifecycle-bound items require the lifecycle
    `target`, while `gate-open`+`gateId` and `actionable-drift` may be targetless. It returns `202` plus
    `DismissalIntent(item_id, dismissed_at, kind, lifecycle_id, gate_id, note)`. Missing `itemId`
    returns `400 missing-item`; unsupported targetless dismissal returns `400 missing-lifecycle`.
- `app.py` owns the routing **and** the one durable side effect (slice 6b): on a lifecycle-targeted
  `gate_decision` it calls `gate_decide_for_lifecycle(… decided_by="developer",
  decided_via="dashboard")`; on gate-id-only `cancel` it calls `gate_decide_payload` against the
  workspace gate log. For a `DismissalIntent`, `app.py` either stores a compact lifecycle
  acknowledgement or cancels/deletes the gate-open source. Otherwise it maps the `ActionOutcome` to a
  `JSONResponse` (projection-not-ready ⇒ `503`).

## Invariants And Boundaries

- **Two families (slice 6b)** — lifecycle transitions stay the 4b no-mutation skeleton;
  gate-decision verbs carry an intent the router records as a developer-attributed decision. The
  UI is never the gate *enforcement* (the mutating MCP tools bind it server-side), but the
  dashboard now records gate *decisions* — deliberately revising the 4b "never mutates" stance.
- **Reducer decides transition safety, never the UI** — transition availability comes from the
  projection's `ActionAvailability`; gate-decision safety is the gate's own state (in the tool layer).
- **Pure evaluator** — `evaluate_action` stays side-effect-free; it only emits the intent. Gate writes
  and attention acknowledgement writes live in `app.py`.
- **Attention dismissal is scoped to its source** — lifecycle rows require a lifecycle `target`,
  gate-open rows may be consumed by gate id, and actionable drift is the one targetless repo-level
  dismissal. A lifecycle-less provider/setup/start alarm cannot create an orphaned suppression row.
- **Reject reason is required** — this is a product/workflow invariant so the agent has an
  actionable reason when a developer rejects a gate.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The precomputed availability + node shapes validated against. | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The `Actor` provenance literal reused for attribution. | [observer/events.py](agents-remember/mcp/src/agents_remember/observer/events.py) |
| The app that routes `POST /api/actions/{action}` to this and executes the gate write. | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The gate write-path the router calls for a gate-decision verb (slice 6b). | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| The compact acknowledgement store used for lifecycle attention dismissals. | [controlplane/attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |
| `_dismiss_action_outcome` allows target omission only for gate-open+gateId or actionable-drift. | L180-L230 | [actions.py](agents-remember/mcp/src/agents_remember/serving/actions.py) |

## Update History

- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: `dismiss` now allows targetless actionable-drift rows
  while preserving lifecycle scope for lifecycle rows and gate-id scope for gate-open consumption.
  Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:58+02:00 — Task 28 sync cleanup: split the pure action dispatcher into
  `ActionEvaluationContext`, `_dismiss_action_outcome`, `_gate_decision_outcome`, and
  `_precomputed_action_outcome` so the touched file no longer carries the Radon D-grade dispatcher
  body. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-28T03:05+02:00 — Task 28 S5.2: added the pure `dismiss` action path with `DismissalIntent`, requiring `itemId` plus lifecycle scope for non-gate items while allowing gate-open consumption by `gateId`. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: made `target` optional only for `cancel` with `gateId`, so stale workspace-shaped gate rows can be deleted without enabling lifecycle-less approve/reject/revision decisions.
- 2026-06-25T07:17+02:00 — Task 19: action requests and gate-decision intents now carry optional targeted `gateId` plus decision `note`, and `reject` requires a non-empty reason before the router records a decision. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: `evaluate_action` now emits a `GateDecisionIntent` for the gate-decision verbs (approve/reject/request-revision/cancel) — staying pure — and `app.py` executes it as a developer/dashboard-attributed gate decision. Revises the 4b "dashboard never mutates gate state" stance for gate *decisions* only. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4b: the POST action skeleton —
  `ActionRequest` + the pure `evaluate_action` / `ActionOutcome` mapping action availability to
  202 / 409 / 404 with attribution, no mutation. Verification metadata pinned until closeout
  stamps the 4b code commit.
