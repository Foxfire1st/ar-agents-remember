# mcp/tests/test_conversation_control_queue.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Queue projection, withdrawal, and recovery contract tests (R2/R3/R7) over the real composition up to
the harness edge (bridge + IPC + real authority + the L2E control-plane reads), with the structural
fake adapter as the only double. Covers complete never-bodies queue truth, cockpit-only withdrawal,
the queued→dispatching race, the bounded 900 s recovery lease, and lease expiry.

## Code Commentary

### Logic

cit:([`QueueProjectionTests`], mcp/tests/test_conversation_control_queue.py:51-208): complete multi-source truth (`3 queued · 1 yours(cockpit) · 1 terminal
· 1 durable`), sequences ordered, no body anywhere in the JSON; only queued cockpit rows carry the
withdrawal ref/redacted preview/digest; legacy cockpit rows report empty held content honestly;
setter operations are not queue rows (while the timeline still enumerates them); semantic monotonic
revisions. cit:([`WithdrawalRecoveryTests`], mcp/tests/test_conversation_control_queue.py:211-619): atomic `cockpit_only` withdrawal; the queued→dispatching
race with exactly one winner (`already-dispatching` 409, refs captured while queued); replay returns
the same outcome/revision + recovery; opaque pending discovery then authenticated fetch/ack/disposed
replay; lost withdraw response → journal-of-last-resort recovery; legacy-row recovery from the
substrate payload; the reference forgery battery; and `test_recovery_lease_expiry_disposes_content`
cit:([`test_recovery_lease_expiry_disposes_content`], mcp/tests/test_conversation_control_queue.py:505-558) which builds its own separate advancing frozen clock (09:00:00Z → 09:16:01Z) and asserts
`pending.items == ()` / `recovery_state == "expired"` after the advance.

Every withdrawal-authority call is addressed through a `ControlRequest(service=…, authorization=…,
ar_session_id=…, expected_bridge_epoch=…)` parameter object (`withdraw`, `withdraw_status`,
`pending_recoveries`, `fetch_recovery`, `acknowledge_recovery`); the legacy substrate writes go
through `submit_control_prompt(entry, text, ControlSubmission(source=…, request_id=…,
expected_bridge_epoch=…))`; and the forgery battery mints its refs with
`mint_ref(secret, "withdrawal-ref", RefBinding(operator, session, epoch), RefTarget(identity=…))`,
so a forged session or epoch is a different `RefBinding` rather than a different keyword.

### Conventions

The happy-path recovery tests read `harness.service` (the `NOW`-anchored instance) so a fresh lease
stays recoverable at any wall-clock time; the one genuine expiry test proves expiry only by advancing
its own frozen clock — never by real time passing — and keeps every original assertion (exact body,
post-ack not-found, disposed replay, on-disk spool deletion).

### Invariants And Boundaries

- Privacy is byte-checked over the full JSON: no non-cockpit body, no cockpit block on non-authorized
  rows, no recovery text in status/reconcile/pending.
- Exactly one winner for the withdraw/dispatch race; refs never outlive their row.
- Expiry is proven by advancing a frozen clock, not by real time; no happy-path assertion is weakened
  by the `NOW`-anchoring.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; the queue/withdrawal contract is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The suite exercises the queue projection and the withdrawal/recovery authority over the shared
topology.

- The source-aware queue projection under test. [1]
- The withdrawal + bounded recovery authority (900 s lease, `sweep_recoveries` expiry sweep at L651) and the `ControlRequest` it is addressed by. [2]
- The shared fake-topology harness with the `NOW`-anchored service. [3]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
