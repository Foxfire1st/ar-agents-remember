# mcp/src/agents_remember/serving/actions.py

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
- `ActionEvaluationContext` is the **public request context** every evaluator echoes into intents:
  who asked (`actor`), when (`now`), and every identifier the specific verb needs to name its object
  (`gate_id`, `note`, `item_id`, `kind`). Each evaluator reads a different subset — which is exactly
  why they arrive as one context rather than six optional parameters repeated at every layer. Since
  260731-EFA-L2 the caller builds it: `app.py` constructs the context and passes it in, instead of
  `evaluate_action` assembling one from six keywords.
- `evaluate_action(projection, action, target, context: ActionEvaluationContext) -> ActionOutcome` is
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
  `gate_decision` it calls `gate_decide_for_lifecycle` with a developer/dashboard `GateVerdict`; on
  gate-id-only `cancel` it calls `gate_decide_payload` against the workspace gate log. For a
  `DismissalIntent`, `app.py` either stores a compact lifecycle acknowledgement or cancels/deletes
  the gate-open source. Otherwise it maps the `ActionOutcome` to a `JSONResponse`
  (projection-not-ready ⇒ `503`).
- **This module is the single request-shape authority, and `app.py` now relies on that in code.**
  Since 260731-EFA-L2 `app.py` no longer re-checks the two shapes refused here: it dropped its own
  `missing-gate-id` branch (because `_gate_decision_outcome` already returns `400 missing-target`
  for a decision naming neither a lifecycle nor a gate id, so an intent that reaches the recorder is
  always addressed) and its own `lifecycle_id is not None or kind == "actionable-drift"` re-check
  (because `_dismiss_action_outcome` already returns `400 missing-lifecycle`, so a dismissal that
  reaches the writer is always scoped). Weakening either refusal here now changes `app.py`'s
  behaviour, not just this module's response.

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

## Evidence

### Repo-Internal References

- The precomputed availability + node shapes validated against. [1]
- The `Actor` provenance literal reused for attribution. [2]
- The app that routes `POST /api/actions/{action}` to this and executes the gate write. [3]
- The control-plane gate write path the router calls for a gate-decision verb (slice 6b). [4]
- The compact acknowledgement store used for lifecycle attention dismissals. [5]
- `_dismiss_action_outcome` allows target omission only for gate-open+gateId or actionable-drift. [6]
