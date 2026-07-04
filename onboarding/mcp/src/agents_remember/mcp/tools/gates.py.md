# mcp/src/agents_remember/mcp/tools/gates.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/src/agents_remember/mcp/tools/gates.py`       |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-07-04T12:32+02:00                      |
| lastVerifiedCommitHash | `7679eb76a4c3137f7a4a5e02e455e7759f9d9c19`         |
| lastVerifiedCommitDate | 2026-07-04T12:58:55+02:00|
| governingOverview      | `overview.md`                                      |

## Purpose

Payload builders for the lifecycle gate control-plane tools. `lifecycle_gate_payload`
is the public agent-facing junction: it opens the durable gate, blocks the
ambient lifecycle with the same ask, and keeps the public tool call blocked until
the gate is decided or a gate-specific inbox response exists. The split
create/wait builders remain lower-level compatibility builders for internal
callers and tests.

## Code Commentary

### Logic

Each builder is **config-rooted** — `_store(config)` builds a
`GateStore(observer_root(config))` (the same root the observer event log uses,
like `context_packet`) — and returns through `_tool_payload`, so a gate action is
itself an attributed tool call. `lifecycle_gate_payload` requires the active
ambient lifecycle, rejects an explicit lifecycle-id mismatch, expires any older
open gate on that lifecycle, creates the durable typed gate, calls
`AmbientLifecycle.block` with `ask.kind`/`prompt`/`options`, then calls the
gate/inbox wait loop with no public timeout and gate-specific inbox matching; it returns
separate `gate`, `lifecycle`, and `wait` objects with the wait result so callers
do not infer one state from another. `gate_create_payload` is now a lower-level compatibility builder: it coerces `kind` to a
`GateKind`, resolves the lifecycle from the explicit argument or the active ambient lifecycle,
expires any existing open gate on that lifecycle, mints a ULID, opens a gate, and appends it; a
lifecycle-less server process fails fast instead of writing a workspace gate by accident.
`gate_decide_payload`
validates the decision against `DECISION_STATES`, folds `current()` to find the
gate (missing → `KeyError`), and appends a decided snapshot; it takes explicit
`decided_by` / `decided_via`. L4 extends it with optional `deciding_role` and
`evidence_refs`: when `decided_via="orchestration"`, the deciding actor is the
active lifecycle/session (or an explicit test override), the resulting snapshot
is checked against the configured `GatePolicy` before append, and owner
self-approval / missing reviewer verdict evidence is rejected server-side.
`gate_create_payload` and `lifecycle_gate_payload` can also attach initial gate
evidence refs. `gate_wait_payload` is a bounded poll (injectable
`sleep` / `monotonic`) that returns when the gate leaves `open` or
`timeout_seconds` elapses (`timedOut`), including any decision attribution/note in the response.
`gate_response_wait_payload` is the dashboard-response helper: a compatibility call polls the folded
gate plus the operator inbox every five seconds for up to five minutes by default, or blocks when
called with `timeout_seconds=None`; it returns when the gate leaves `open`, a matching inbox entry is
pending, or its explicit bounded timeout elapses. `lifecycle_gate_payload` passes
`allow_ungated_entries=False`, so stale lifecycle-scoped inbox entries cannot wake a new gate. The
helper never consumes inbox entries. If a waited gate was physically dismissed/cleared, it returns
`cancelled` so the caller unblocks. Non-enforcement gate decisions that are returned through this wait
are deleted after the payload is built; worktree/closeout/integration/cleanup gate decisions stay
until the consuming tool applies them. `gate_list_payload` returns the folded gate set.
`gate_decide_for_lifecycle` (slice 6b)
is the dashboard's write path: it resolves the lifecycle's newest still-open gate, optionally verifies
an expected `gateId` to reject stale dashboard actions, records an optional decision `note`, and decides
it — the serving layer calls it with `developer` / `dashboard`, reusing the `gate_decide` response
envelope. `cancel` decisions physically delete the gate and any inbox entries tied to it.

### Invariants And Boundaries

- **Attribution honesty → enforced.** The server registers `gate_decide` with
  `decided_by="model"` / `decided_via="cli"`, so the agent cannot claim a
  developer decision; the dashboard serving layer calls `gate_decide_for_lifecycle`
  with `developer` / `dashboard` (slice 6b). Enforcement now consumes that
  distinction — `worktree_closeout_apply` binds on a developer-attributed
  approval or on a policy-valid orchestration approval (`controlplane/enforcement.py`);
  a model self-decision is non-binding, and a lifecycle cannot approve its own
  gate through orchestration.
- Config-rooted: the store root resolves through `observer.observer_root`, so
  gates live beside the event log; the durable logic stays in `controlplane/`.
- One lifecycle has at most one open gate via `lifecycle_gate_payload` or the retained
  lower-level `gate_create_payload`; superseded gates become
  `expired`, so the dashboard attention queue does not accumulate obsolete approvals. New gates are
  lifecycle-bound by default through the active ambient lifecycle, so agents do not have to pass a
  lifecycle id for normal gate creation.
- `lifecycle_gate_payload` is the only public agent choreography for creating a
  lifecycle gate and waiting on the developer response. `gate_wait_payload` and
  `gate_response_wait_payload` stay as lower-level compatibility wait builders;
  the lifecycle skill must not teach them as the next step after
  `lifecycle_gate`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The gate entity and decision helpers. | [controlplane/records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The gate delegation policy checked before orchestration decisions append. | [controlplane/gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |
| The append-only store these builders mutate. | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| The external-chat inbox store this polls in `gate_response_wait_payload`. | [controlplane/operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| The choke point every gate payload returns through. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| Gate response models. | [models/gates.py](agents-remember/mcp/src/agents_remember/models/gates.py) |

## Update History

- 2026-07-04T12:32+02:00 — 260703-L4: `gate_decide_payload` now handles
  `decidedVia="orchestration"` with a deciding role, active lifecycle/session
  attribution, policy validation, no owner self-approval, and append-only
  evidence refs; create/lifecycle gate payloads accept initial evidence refs.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-06-26T18:43+02:00 — Regression fix: `lifecycle_gate_payload` now uses the
  wait helper with no public timeout and gate-specific inbox matching, so stale
  lifecycle-scoped inbox entries cannot make a newly raised gate return
  immediately while still open.
- 2026-06-26T17:05+02:00 — Regression fix: `lifecycle_gate_payload` now performs
  the bounded gate/inbox wait internally after blocking the lifecycle, so the
  public junction no longer returns immediately with only initialized wait
  metadata.
- 2026-06-26T14:16+02:00 — Task 25: added `lifecycle_gate_payload` as the unified public gate junction and classified `gate_create_payload`, `gate_wait_payload`, and `gate_response_wait_payload` as lower-level compatibility builders, not live agent choreography.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `gate_create_payload` now binds omitted lifecycle ids to the active ambient lifecycle and rejects lifecycle-less creation instead of producing future workspace-shaped lifecycle gates.
- 2026-06-25T13:10+02:00 — Task 23/24: `gate_response_wait` now defaults to a 5-minute/5-second wait, deleted gates unblock as `cancelled`, `cancel` deletes gate/inbox records, and non-enforcement decisions returned through the wait are compacted after pickup.
- 2026-06-25T07:17+02:00 — Task 19: `gate_create_payload` now expires any previous open lifecycle gate, `gate_decide_for_lifecycle` can reject stale expected gate ids and persist decision notes, `gate_wait_payload` returns decision metadata, and new `gate_response_wait_payload` waits for either gate state changes or matching operator-inbox entries. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: added `gate_decide_for_lifecycle` (the dashboard write-path — resolves the lifecycle's newest open gate and decides it `developer`/`dashboard`, reusing the `gate_decide` envelope). The four registered `gate_*` tools are unchanged. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the `gate_create` / `gate_decide` / `gate_wait` / `gate_list` payload builders. Verification metadata pinned until closeout stamps the 6a code commit.
