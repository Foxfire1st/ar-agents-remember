# mcp/src/agents_remember/mcp/tools/gates.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/src/agents_remember/mcp/tools/gates.py`       |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-01T13:20+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`         |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                      |

## Purpose

Payload builders for the lifecycle gate control-plane tools. `lifecycle_gate_payload`
is the public agent-facing junction: it opens the durable gate, blocks the
ambient lifecycle with the same ask, and keeps the public tool call blocked until
the gate is decided or a gate-specific inbox response exists. The split
create/wait builders remain lower-level compatibility builders for internal
callers and tests.

## Code Commentary

### Parameter Objects And Current Signatures (260731-EFA-L2)

This module gained three local frozen dataclasses and four shared values, and every builder's
keyword list collapsed onto them:

| Type | Carries |
| --- | --- |
| `GateRaise(kind, anchor, request, ask)` | One `lifecycle_gate` raise: which gate to open (`GateAnchor`, `GateRequest` — the same pieces the record layer stores) and the structured `ask` put to the developer. |
| `GateWait(block, timeout_seconds, poll_seconds, sleep, monotonic)` | How a caller waits. `block=False` is raise-and-continue; `timeout_seconds=None` waits indefinitely; `sleep`/`monotonic` are injected so tests drive the loop deterministically. |
| `InboxWatch(agent_id, allow_ungated_entries)` | Which operator-inbox entries end a wait alongside a decision on the gate itself. |

Shared values: `BLOCKING_GATE_WAIT` (`timeout_seconds=None` — block until decided),
`SHORT_GATE_WAIT` (30 s at 1 s — the low-level poll), `DEFAULT_GATE_WAIT` (5 s poll up to 5 minutes
— the compatibility window), `ANY_INBOX_ENTRY` (any pending entry ends the wait).

```python
gate_create_payload(config, *, kind, anchor=None, request=None)
lifecycle_gate_payload(config, raised: GateRaise, *, wait: GateWait = BLOCKING_GATE_WAIT)
gate_decide_payload(config, *, gate_id, lifecycle_id, verdict: GateVerdict, evidence_refs=None)
gate_decide_for_lifecycle(config, *, lifecycle_id, verdict: GateVerdict, expected_gate_id=None,
                          evidence_refs=None)
gate_wait_payload(config, *, gate_id, lifecycle_id, wait: GateWait = SHORT_GATE_WAIT)
gate_response_wait_payload(config, *, gate_id, lifecycle_id, inbox: InboxWatch = ANY_INBOX_ENTRY,
                           wait: GateWait = DEFAULT_GATE_WAIT)
gate_list_payload(config, *, lifecycle_id)
```

Attribution now travels as one `GateVerdict(decision, by, via, note, deciding_role)` instead of
separate `decided_by` / `decided_via` / `note` / `deciding_role` arguments — the registration layer
and the dashboard serving layer each construct their own, which is what keeps model/cli and
developer/dashboard attribution from being mixed by a stray keyword.

`lifecycle_gate_payload` was also decomposed into named helpers — `_gating_lifecycle` (only a
running, matching lifecycle may gate), `_validated_ask` (type-checks the free-form ask mapping),
`_require_raise_and_continue_allowed`, `_raised_gate_payload` — and `gate_decide_payload` into
`_gate_to_decide`, `_require_undelegated_cli_decision`, `_meet_verdict_by_expectation`. The
behaviour described below is unchanged; it is now spread across those helpers rather than inlined.

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
Since 260707-HFX2-L1 (R2): `gate_create_payload` and `lifecycle_gate_payload` both call
`_write_verdict_by_row(config, gate)` right after appending the newly opened gate, in the SAME
call — writing a durable `verdict-by` expectation row (`controlplane/expectation_rows.py`) keyed to
the gate's own id, with its SLA read from `orchestration.expectations.defaults` (falling back to
`DEFAULT_EXPECTATION_SLA_SECONDS` when the config carries no coordination root). `gate_decide_payload`
validates the decision against `DECISION_STATES`, folds `current()` to find the
gate (missing → `KeyError`), and appends a decided snapshot; it takes explicit
`decided_by` / `decided_via`. Since 260707-HFX2-L1 it also looks up that gate's pending `verdict-by`
row (`ExpectationRowStore.find_by_source`) and marks it `met` on ANY terminal decision
(approve/reject/cancel) — the expectation is fulfilled by the decision itself, not by a separate
step. L4 extends it with optional `deciding_role` and
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
pending, or its explicit bounded timeout elapses. `lifecycle_gate_payload` passes an `InboxWatch` with
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

### Current gate-decision boundary

The shared control-plane decision service cit:([`record_gate_decision`], mcp/src/agents_remember/controlplane/gate_decisions.py:83-128)
owns decision recording and any associated gate-log reclamation. This tool module builds the gate,
wait, list, and response payloads; it does not own a private `_reclaim_gate_log` path. The serving
adapter records its dashboard decision through `_recorded_gate_decision`, while `GateStore` remains
the append-only persistence boundary.

Read and wait builders remain pure reads apart from the explicit decision operation. A decision that
has already been appended must not be lost because payload construction or a later reclamation pass
fails; the shared decision service owns that failure boundary.

### Invariants And Boundaries

- **Attribution honesty → enforced.** `mcp/registration/gates.py` builds
  `GateVerdict(by="model", via="cli")` for a plain `gate_decide`, so the agent cannot claim a
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
- **Gate-log reclamation belongs to the shared decision service.** Keep it off read paths, timers, and
  projection ticks; `record_gate_decision` is the owner-activity boundary for decision recording and
  reclamation.
- **The ownership contract remains a durable-store concern.** `GATE_OWNERSHIP` and
  `is_compaction_owner()` stay in the durable-store layer; this payload module does not claim a direct
  dashboard reclamation path.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The gate entity and decision helpers. | `GateRecord`; `GateAnchor`; `GateRequest`; `GateVerdict`; `decide_gate` | mcp/src/agents_remember/controlplane/records.py:84-116; mcp/src/agents_remember/controlplane/records.py:128-136; mcp/src/agents_remember/controlplane/records.py:139-146; mcp/src/agents_remember/controlplane/records.py:149-163; mcp/src/agents_remember/controlplane/records.py:191-216 |
| The gate delegation policy checked before orchestration decisions append (policy in kernel primitives since L9). | "def record_gate_decision("; "class GatePolicy:" | mcp/src/agents_remember/controlplane/gate_decisions.py:83-128; mcp/src/agents_remember/kernel/primitives/gate_policy.py:54-54 |
| The append-only store these builders mutate. | `append` | mcp/src/agents_remember/controlplane/store.py:121-127 |
| The external-chat inbox store this polls in `gate_response_wait_payload`. | `gate_response_wait_payload` | mcp/src/agents_remember/mcp/tools/gates.py:131-148 |
| The choke point every gate payload returns through. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |
| Gate wait response model. | `GateWaitResponse` | mcp/src/agents_remember/models/gates.py:47-55 |
| The durable-store gate ownership constant. | `GATE_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:138-150 |
| The compaction-owner predicate. | `is_compaction_owner` | mcp/src/agents_remember/controlplane/durable_store.py:123-132 |
| The durable-store contract string. | "DURABLE_STORE_CONTRACT = \"ar-durable-store/1.0\"" | mcp/src/agents_remember/controlplane/durable_store.py:42-52 |
| The serving adapter that records dashboard gate decisions through the shared decision service. | "def _recorded_gate_decision("; "def record_gate_decision(" | mcp/src/agents_remember/controlplane/gate_decisions.py:85-85; mcp/src/agents_remember/serving/_app_routes.py:195-195 |
| The projection reader that no longer rewrites gate logs (`read_gates` → `GateStore.projected_current`). | "def read_gates(coordination_root: Path" | mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:103-103 |

As of cycle 5 the seam channel is operable: lifecycle_gate accepts wait=false (raise-and-continue — returns the gateId in a model-conformant raised payload instead of blocking); gate_decide resolves a bare gate_id across lifecycles via GateStore.find when no lifecycle_id is given, REFUSES cli-attributed non-cancel decisions on kinds the active policy delegates (fail-loud: pass deciding_role or leave it to the developer), and cancel deletes by the gate's own lifecycleId. Cycle 6 hardens the raise path: wait=false is now reserved for SEAM kinds (`SEAM_GATE_KINDS`) that the active policy also delegates — a delegated non-seam kind like plan-approval blocks again — and the check runs BEFORE the expire-sweep and append (validate-then-mutate), so a refused raise persists no orphan open gate and expires no sibling. `gate_list_payload` is now ambient-defaulting: with no explicit lifecycle_id it lists the ACTIVE lifecycle's gates (a raiser polls its own gate without handling lifecycle ids) and falls back to the workspace log only when no lifecycle is active. Cycle 7 closes the addressless-raise hole (AR4-1): a wait=false raise additionally requires a non-empty `enclosure` — the master task name the integrate guard matches the gate by — and refuses inside the same validate-then-mutate block ("a master-handover-approval raise-and-continue requires enclosure=<master task name>"), because an addressless seam gate could only ever fail open at the enforcement rung.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T12:41:53+00:00 — 260731-EFA-L6 S18-B09 curator: split the ownership constant, compaction-owner predicate, and durable-store contract to their distinct frozen-source owners; the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-01T13:20+02:00 — 260731-EFA-L5 curator: this historical ownership note is superseded. Current
  gate decision recording and reclamation are attributed to the shared `controlplane/gate_decisions.py`
  service, while this module documents the payload boundary.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: added `GateRaise` / `GateWait` / `InboxWatch` plus the
  four shared wait values, and collapsed every builder's keyword list onto them — including
  `GateVerdict` replacing the separate `decided_by`/`decided_via`/`note`/`deciding_role` arguments
  on both decide paths. `lifecycle_gate_payload` and `gate_decide_payload` were decomposed into
  named helpers; the gate semantics, attribution rules and refusal ordering are unchanged.
  Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `gate_create_payload`/`lifecycle_gate_payload` now atomically write an R2 `verdict-by` expectation row alongside the opened gate; `gate_decide_payload` marks that row `met` on any terminal decision (approve/reject/cancel). Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: wait=false additionally requires a non-empty `enclosure` (the integrate guard's address, AR4-1a) — refused before the expire-sweep/append, so a mis-called raise still mutates nothing. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: wait=false restricted to delegated seam kinds and validated before mutating (AR3-2/AR3-5); gate_list defaults to the ambient lifecycle (AR3-3). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): wait=false raise, cross-lifecycle decide-by-id, cli refusal on delegated kinds. Verification metadata pinned until closeout stamps the L8 commit.
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
