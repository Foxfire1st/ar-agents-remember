# mcp/src/agents_remember/serving/actions.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/serving/actions.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-08-02T01:05+02:00                       |
| lastVerifiedCommitHash | `28a66feae742bf02fe4b647388b220f921cc7007`   |
| lastVerifiedCommitDate | 2026-08-15T03:44:49+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The precomputed availability + node shapes validated against. | `ActionAvailability`, `WorkspaceProjection` | mcp/src/agents_remember/observer/projection.py:49-62; mcp/src/agents_remember/observer/projection.py:1026-1045 |
| The `Actor` provenance literal reused for attribution. | `Actor` | mcp/src/agents_remember/observer/events.py:31-31 |
| The app that routes `POST /api/actions/{action}` to this and executes the gate write. | "def _action_response(runtime: _ServingRuntime", "def _register_action_routes(app: FastAPI" | mcp/src/agents_remember/serving/_app_routes.py:308-308; mcp/src/agents_remember/serving/_app_routes.py:388-388 |
| The control-plane gate write path the router calls for a gate-decision verb (slice 6b). | `record_gate_decision`, `record_lifecycle_gate_decision` | mcp/src/agents_remember/controlplane/gate_decisions.py:83-128; mcp/src/agents_remember/controlplane/gate_decisions.py:131-156 |
| The compact acknowledgement store used for lifecycle attention dismissals. | `AttentionDismissalStore`, `dismiss` | mcp/src/agents_remember/controlplane/attention_dismissals.py:45-135 |
| `_dismiss_action_outcome` allows target omission only for gate-open+gateId or actionable-drift. | `_dismiss_action_outcome` | mcp/src/agents_remember/serving/actions.py:170-219 |

## Update History

- 2026-08-03T02:32:19+02:00 — Curator W3-B02 repaired 4 Repo-Internal citation rows, resolving 8 manifest findings with exact evaluator, router, gate-service, projection, and acknowledgement-store anchors; verification metadata was preserved.
- 2026-08-02T01:05+02:00 — No content impact: repaired this document's `Repo-Internal References` table shape. Rows carrying a citation cell were rendering short: the header declared two columns while those rows held three, and GFM TRUNCATES the extra cell, so the citation was in the source but invisible in the rendered table (`memory_quality/style/document_shape/tables.py`, `table_row_cell_count_mismatch`). Widened the header and its delimiter row to `| Finding | Citations | Source Path |` — the shape 1,941 rows in this tree already use — and padded the two-cell rows with `n/a`, which is this tree's own no-citation value (489 uses; zero empty citation cells exist). No finding text and no citation was changed by the widening. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: `evaluate_action` now takes one `ActionEvaluationContext`
  built by the caller instead of six keywords; recorded that context as the named request-context
  concept and recorded that `app.py` deleted its two duplicate shape guards because this module is
  the single place those shapes are refused. Verification metadata stays pinned until closeout.
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
