# mcp/tests/test_serving_app_background_loops.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_serving_app_background_loops.py`   |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-14T14:03:04+02:00               |
| lastVerifiedCommitHash | `1cb69766bf7e023fb3d7021107da78dc5e53e994`         |
| lastVerifiedCommitDate | 2026-08-14T14:12:59+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural coverage for the dashboard app's **background loops and their lifespan wiring**.
`serving/app.py` runs four always-on background tasks (projection, provider metrics,
supervisor sweep, workspace-river compaction) plus two opt-in ones (the heap diagnostic and
the glibc arena trim). Their steady state is exercised by the rest of the suite simply by
booting the app; what was never exercised is the part that matters operationally.

## The Failure Mode This Suite Exists For

Every loop's `except Exception` arm and the metrics loop's cancellation boundary. **A background task that dies on one bad pass silently
stops sampling / sweeping / compacting for the lifetime of the daemon, and nothing else in
the process notices.** Each retry test proves both halves: the failing pass is logged, **and** the
loop performs the next pass anyway. The cancellation regression separately proves shutdown waits
for an already-entered metrics worker write before propagating cancellation.

## What Each Class Owns

| Class | Loop |
| --- | --- |
| `MetricsLoopTests` | A failed provider sample costs one interval, and cancellation cannot return while an in-flight metrics write still runs. |
| `SupervisorLoopTests` | `orchestration.supervisor.enabled` is re-read **on every pass**, so turning the sweep on takes effect without restarting the daemon. Settings state, not boot state. |
| `MallocTrimLoopTests` | The opt-in arena reclaim: never runs unless `AR_MALLOC_TRIM` is set; the interval is resolved **once at task start** rather than per tick; one trim per tick; failures survivable. |
| `WorkspaceRiverCompactionLoopTests` | The one event river nothing else reclaims — it must keep shrinking, and keep going on error. |
| `OptionalLifespanTaskTests` | The two `if`s in the lifespan that decide whether the opt-in tasks exist at all, plus the cancellation every background task shares on shutdown. `_TaskProbe` is an awaitable stand-in recording entry and cancellation. |

## Method

Fakes stop at the process/platform seam only: `docker ps`
(`sample_provider_containers`), the libc `malloc_trim` symbol, and — where a *failure* has
to be provoked — the one collaborator that raises. `_CatalogOnlyHost` is a `TerminalHost`
duck-type with no PTYs; the runtime is a real `_ServingRuntime` over real stores with an
unrun projector. Loops are driven until a predicate holds and then cancelled the way the
lifespan cancels them; the wait helper fails naming what never happened rather than timing
out anonymously.

## Invariants And Boundaries

- Assert **both** that the failure was logged and that the next pass ran. A test that only
  asserts the log would pass against a loop that then dies.
- The supervisor switch is re-read per pass; do not cache it at task start.
- The trim interval is resolved once per task, deliberately — that asymmetry with the
  supervisor switch is intentional and asserted.
- Opt-in tasks must not exist when their flag is unset, and every background task must be
  cancelled on shutdown.
- Cancelling `_metrics_loop` during `ProviderMetricsStore.record` must leave the task pending until
  that worker returns, then propagate `CancelledError` with the completed sample readable.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The metrics race regression blocks the worker write, cancels the loop, proves it remains pending, then releases and observes the written sample. | `test_cancellation_drains_an_inflight_metrics_write_before_returning` | mcp/tests/test_serving_app_background_loops.py:224-255 |
| The drained worker-thread helper and metrics loop under test. | `_to_thread_drained_on_cancel`; `_metrics_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:60-98 |
| The lifespan cancels and awaits all background tasks. | "def _serving_lifespan(" | mcp/src/agents_remember/serving/_app_lifespan.py:195-243 |
| The same app's failing route arms. | `PasteRouteTests` | mcp/tests/test_serving_app_routes.py:486-540 |
| The opt-in heap diagnostic's own suite. | `HeapDiagLoopTests` | mcp/tests/test_heap_diag.py:103-264 |

## Update History

- 2026-08-14T14:03:04+02:00 — No content impact: R46 replaces the timeout helper's local
  `if`/`AssertionError` branch with `self.assertTrue` using the same five-second wait and failure
  message. The metrics cancellation semantics, forcing sequence, and suite ownership documented
  here are unchanged; verification remains pinned to the last committed source until closeout.

- 2026-08-14T12:31:43+02:00 — R44 curator: recorded the deterministic in-flight metrics-write
  cancellation race and the required post-drain cancellation propagation. Verification remains
  closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 3 citation entries (6 findings); no Tier-3 findings.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new background
  loop / lifespan suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
