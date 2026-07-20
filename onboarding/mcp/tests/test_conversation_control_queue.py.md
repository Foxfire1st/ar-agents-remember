# mcp/tests/test_conversation_control_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
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

`QueueProjectionTests` (L47): complete multi-source truth (`3 queued · 1 yours(cockpit) · 1 terminal
· 1 durable`), sequences ordered, no body anywhere in the JSON; only queued cockpit rows carry the
withdrawal ref/redacted preview/digest; legacy cockpit rows report empty held content honestly;
setter operations are not queue rows (while the timeline still enumerates them); semantic monotonic
revisions. `WithdrawalRecoveryTests` (L202): atomic `cockpit_only` withdrawal; the queued→dispatching
race with exactly one winner (`already-dispatching` 409, refs captured while queued); replay returns
the same outcome/revision + recovery; opaque pending discovery then authenticated fetch/ack/disposed
replay; lost withdraw response → journal-of-last-resort recovery; legacy-row recovery from the
substrate payload; the reference forgery battery; and `test_recovery_lease_expiry_disposes_content`
(L465) which builds its own separate advancing frozen clock (09:00:00Z → 09:16:01Z) and asserts
`pending.items == ()` / `recovery_state == "expired"` after the advance.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite exercises the queue projection and the withdrawal/recovery authority over the shared
topology.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The source-aware queue projection under test. | L40-L144 | [control/queue_projection.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/queue_projection.py) |
| The withdrawal + bounded recovery authority (900 s lease, expiry sweep). | L117-L699 | [control/withdrawals.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/withdrawals.py) |
| The shared fake-topology harness with the `NOW`-anchored service. | L408-L520 | [_control_plane.py](agents-remember/mcp/tests/_control_plane.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the queue/withdrawal/
  recovery suite — complete never-bodies truth, cockpit-only withdrawal race, opaque discovery +
  authenticated fetch/ack, journal-of-last-resort recovery, forgery battery, and the untouched
  frozen-clock expiry proof. Verification is blank because the new source file is uncommitted;
  closeout owns its first source stamp.
