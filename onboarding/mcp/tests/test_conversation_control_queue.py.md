# mcp/tests/test_conversation_control_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured; the queue/withdrawal contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite exercises the queue projection and the withdrawal/recovery authority over the shared
topology.

| Finding | Anchor | Source |
| --- | --- | --- |
| The source-aware queue projection under test. | "async def operation_queue" | mcp/src/agents_remember/serving/conversation/control/queue_projection.py:51-51 |
| The withdrawal + bounded recovery authority (900 s lease, `sweep_recoveries` expiry sweep at L651) and the `ControlRequest` it is addressed by. | "def sweep_recoveries" | mcp/src/agents_remember/serving/conversation/control/withdrawals.py:658-658 |
| The shared fake-topology harness with the `NOW`-anchored service. | `NOW` | mcp/tests/_control_plane.py:79-79 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 5 citation finding(s); scoped recheck clean.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: the withdrawal authority, the harness
  control client, and the ref minter all moved their loose arguments into parameter objects, so
  this suite now calls `withdrawals.*` through `ControlRequest`, `submit_control_prompt` through
  `ControlSubmission`, and `mint_ref` through `RefBinding` + `RefTarget`. Added a Logic paragraph
  naming those call shapes (the forgery battery in particular now varies a `RefBinding`, not a
  keyword) and re-anchored the line references the same commit moved: `QueueProjectionTests` is
  L51 (was L47), `WithdrawalRecoveryTests` is L211 (was L202),
  `test_recovery_lease_expiry_disposes_content` is L505 (was L465), `queue_projection.py` is
  L47-L152, `withdrawals.py` is L121-L706, and the `NOW`-anchored `ControlHarness` is L436-L520.
  No test was added, removed, or renamed and the privacy, one-winner, and frozen-clock-expiry
  assertions are untouched.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the queue/withdrawal/
  recovery suite — complete never-bodies truth, cockpit-only withdrawal race, opaque discovery +
  authenticated fetch/ack, journal-of-last-resort recovery, forgery battery, and the untouched
  frozen-clock expiry proof. Verification is blank because the new source file is uncommitted;
  closeout owns its first source stamp.
