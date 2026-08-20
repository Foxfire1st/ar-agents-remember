# serving/projections/ — Projection File-Surface Readers Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/projections/` |
| onboardingRoute | `mcp/src/agents_remember/serving/projections/overview.md` |
| parentOverview | [`serving/overview.md`](../overview.md) |
| lastUpdated            | 2026-08-20T05:04+02:00 |
| lastVerifiedCommitHash | `8071a64497ed88f8f423e853dc9440532fd573af` |
| lastVerifiedCommitDate | 2026-08-20T02:19:58+02:00|

## What This Area Is

### 260731-EFA-L23 Route Delta

L23 makes the runtime enclosure reader attach the latest durable lifecycle-operation projection. The projection exposes task-addressed progress and report evidence while keeping worker/process resume identities private.

The projection file-surface readers moved by 260731-EFA-L9 from `observer/` into the serving
tree (layering cleanup: the serving projection tick owns these readers, and observer stays the
write side of the observable-lifecycle substrate). The route reads provider state, enclosure
contracts, drift snapshots, task documents, engine-room facts, and the landing/ledger surfaces,
and drives the atomic projection write.

## Hot Path Summary

`snapshots.py` is the file-surface reader hub (`read_providers`, `read_enclosures`,
engine-process facts); `projection_store.py::project_and_write` ties reading, reduction, and the
atomic write together; `projection_inputs.py` retains bounded domain inputs; `landing_state.py`
owns bounded background landing observation; `contract_snapshot.py` caches one immutable
enclosure snapshot per tick. `paths.py` resolves the observer store roots (shared with the
observer write side through `kernel/primitives/observer_paths.py`).

## What Belongs Here

| Path | Role |
| --- | --- |
| `paths.py` | Observer store-root resolution (thin wrapper over kernel primitives). |
| `contract_snapshot.py` | One immutable leaf-enclosure contract snapshot per tick. |
| `snapshots.py` | File-surface readers (providers, enclosures, analytical surfaces). |
| `snapshots_impl/` | Split reader implementations: analytics, runtime/enclosures, task docs, shared helpers. |
| `drift_snapshots.py` | Projection-side drift-snapshot pruning policy. |
| `landing_state.py` | Bounded background landing observation and publication. |
| `projection_inputs.py` | Domain-invalidated bounded projection inputs. |
| `projection_store.py` | Log/snapshot reading and atomic projection writes. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Observer write side (ambient, events, store, reducer) | `observer/` |
| Wire contracts and control services | `models/conversations/`, `serving/conversation/` |
| Drift-snapshot path primitives | `kernel/primitives/drift_snapshot.py` |

## Structures Found Here

- File-surface reader hub and split reader implementations.
- Immutable contract-snapshot cache and bounded landing observation.
- Projection input state with domain refresh kinds.
- Atomic projection store with `latest-state.json`/`latest-metrics.json`.

## Operating Model

1. The serving projection tick enumerates which domain changed (`projection_inputs.py`).
2. Readers (`snapshots.py`, `snapshots_impl/`) read the producing subsystems' own parsers and project
   inbox entry/subject/owner and expectation task references as canonical `TaskDocumentRef` values;
   they do not synthesize an agent-visible leaf-address field. The task-document reader likewise
   copies explicit master nature and sprint graph, derives waves from that validated graph, and
   includes those cells in body-revision identity so topology changes invalidate the projection.
3. `project_and_write` ties reading, pure reduction, and the atomic write together.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `snapshots.py` | reader hub | All named-state surfaces feed the projection. | covered |
| `projection_store.py` | I/O edge | Atomic publication and lifecycle-log reads. | covered |
| `contract_snapshot.py` | cache | One contract parse per tick, reused by three readers. | covered |
| `landing_state.py` | background observer | Bounded landing facts without blocking the tick. | covered |

## Local Invariants And Traps

- Readers reuse the producing subsystem's own parser rather than re-parsing.
- Projection writes are atomic; readers never observe half-written state.
- Do not import the observer write side from here (layering: observer is below serving).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The observer store-root conventions are kernel-owned. | `observer_logs_root` | mcp/src/agents_remember/kernel/primitives/observer_paths.py:34-34 |
| The projection tick consumes these readers. | `project_and_write` | mcp/src/agents_remember/serving/projections/projection_store.py:214-214 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `paths.py` | [`paths.py.md`](paths.py.md) | covered | Path resolution. |
| `contract_snapshot.py` | [`contract_snapshot.py.md`](contract_snapshot.py.md) | covered | Enclosure snapshot cache. |
| `drift_snapshots.py` | [`drift_snapshots.py.md`](drift_snapshots.py.md) | covered | Snapshot pruning. |
| `landing_state.py` | [`landing_state.py.md`](landing_state.py.md) | covered | Landing observation. |
| `projection_inputs.py` | [`projection_inputs.py.md`](projection_inputs.py.md) | covered | Bounded inputs. |
| `projection_store.py` | [`projection_store.py.md`](projection_store.py.md) | covered | Atomic projection I/O. |
| `snapshots.py` | [`snapshots.py.md`](snapshots.py.md) | covered | Reader hub. |
| `snapshots_impl/_analytics.py` | [`snapshots_impl/_analytics.py.md`](snapshots_impl/_analytics.py.md) | covered | Analytical readers. |
| `snapshots_impl/_common.py` | [`snapshots_impl/_common.py.md`](snapshots_impl/_common.py.md) | covered | Shared helpers. |
| `snapshots_impl/_runtime.py` | [`snapshots_impl/_runtime.py.md`](snapshots_impl/_runtime.py.md) | covered | Runtime/enclosure readers. |
| `snapshots_impl/_task_documents.py` | [`snapshots_impl/_task_documents.py.md`](snapshots_impl/_task_documents.py.md) | covered | Task-document readers. |

## Child Overviews

None.

## How To Use This Area

When changing a projection reader:

1. Read this overview and the owning reader's sidecar.
2. Keep the domain input/refresh discipline in `projection_inputs.py`.
3. Prove the change through the projection/observer suites and the structural-coverage suite.

## L23 Final Candidate Route Disposition

The projection route attaches the newest validated lifecycle operation to its owning enclosure and
serves bounded phase, timing, command, report, and recovery guidance. Durable store state remains
authority; projection never exposes worker or resume identity.

## 260815-DAG-L14 Projection Route

`snapshots_impl/_task_documents.py` passes `SubTaskRef.masterRef` through and projects
`doc.seats` as `TaskSeatNode`; the body revision covers sprint structure.

## Update History

- 2026-08-20T05:04+02:00 — 260815-DAG-L14 route impact: `_task_documents.py` projects
  `masterRef` + `seats` and covers them in the body revision. Verified at code commit 8071a644.


- 2026-08-18T13:00+02:00 — No route impact: 260815-DAG-L8 added the closeout-queue projection surface; route purpose unchanged.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: the task-document snapshot slice hydrates
  master nature and sprint graph, derives waves from the validated graph, and incorporates both into
  body-revision identity.

- 2026-08-14T06:25+02:00 — L23 final candidate review: runtime snapshots attach the newest
  validated lifecycle operation and preserve bounded task-addressed phase/report evidence without
  worker or recovery identifiers. Verification remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator route review: L23 makes the runtime enclosure reader attach the latest durable lifecycle-operation projection. The projection exposes task-addressed progress and report evidence while keeping worker/process resume identities private. Verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: updated the route body for canonical
  task-document references in inbox and expectation snapshots; private occupant coordinates remain
  internal runtime evidence.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created the route overview for the
  observer→serving projection-reader move; observer overview retains the write-side governance.
  Verification metadata pinned until closeout stamps the L9 code commit.
