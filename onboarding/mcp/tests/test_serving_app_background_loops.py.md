# mcp/tests/test_serving_app_background_loops.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_serving_app_background_loops.py`   |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`         |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural coverage for the dashboard app's **background loops and their lifespan wiring**.
`serving/app.py` runs four always-on background tasks (projection, provider metrics,
agent-notifier sweep, workspace-river compaction) plus two opt-in ones (the heap diagnostic and
the glibc arena trim). Their steady state is exercised by the rest of the suite simply by
booting the app; what was never exercised is the part that matters operationally.

## The Failure Mode This Suite Exists For

Every loop's `except Exception` arm. **A background task that dies on one bad pass silently
stops sampling / sweeping / compacting for the lifetime of the daemon, and nothing else in
the process notices.** Each test proves both halves: the failing pass is logged, **and** the
loop performs the next pass anyway.

## What Each Class Owns

| Class | Loop |
| --- | --- |
| `MetricsLoopTests` | A failed provider sample must cost one interval, not the rest of the daemon's life. |
| `SupervisorLoopTests` | `orchestration.agent-notifier.enabled` is re-read **on every pass**, so turning the sweep on takes effect without restarting the daemon. Settings state, not boot state. |
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The loops and the lifespan under test. | "def _serving_lifespan(" | mcp/src/agents_remember/serving/_app_lifespan.py:168-168 |
| The same app's failing route arms. | `PasteRouteTests` | mcp/tests/test_serving_app_routes.py:427-481 |
| The opt-in heap diagnostic's own suite. | `HeapDiagLoopTests` | mcp/tests/test_heap_diag.py:103-264 |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 3 citation entries (6 findings); no Tier-3 findings.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new background
  loop / lifespan suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
