# serving/projections/ — Projection File-Surface Readers Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/projections/` |
| onboardingRoute | `mcp/src/agents_remember/serving/projections/overview.md` |
| parentOverview | [`serving/overview.md`](../overview.md) |

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
   The always-on readers enumerate the canonical task corpus through one bounded walk
   (`snapshots_impl/_common.py::_iter_task_json`, three listed levels). The on-demand single-document
   body read (`/api/task-document`) never enumerates it.
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
- **A projection reader must not delete durable truth over one unknown field.** These readers consume
  documents written by other, independently versioned processes, so an unknown key is a version skew,
  not corruption: the reader tolerates it (260913-LCA-L10, `snapshots_impl/_task_documents.py`), while
  every genuine invalidity still withholds the document. The strict end of that split stays with
  authoring and with the enforcement folds, exactly as `snapshots_impl/_runtime.py:121-123` states it.
- Projection writes are atomic; readers never observe half-written state.
- **A request-path reader must cost what it names, not what the corpus holds.** The projector's pass
  and the HTTP body read run in one process and compete for one GIL, so a corpus-sized read on either
  side slows the other (260921-ICR-L42: review R1 attributed almost all of the browser's 3.865 s leaf read to
  three concurrent whole-corpus enumerations). The body read opens only the requested document and the masters its
  sprint graph names. The always-on enumeration lists only `tasks/<repository>/<task>/` and returns
  exactly the list the earlier recursive glob did. Neither adds an index, persistent cache or store.
- Readers may consume observer projection/reducer APIs; observer event mutation remains
  with its write-side owner. Layering permits serving to consume lower observer APIs.

## Evidence

### Repo-Internal References

- The observer store-root conventions are kernel-owned. [1]
- The projection tick consumes these readers. [2]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.

### Docs References

No Domain Documentation source is configured.

No configured domain documentation was available.

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


## 260815-DAG-L12 Route Impact

The task-documents snapshot reader (`snapshots_impl/_task_documents.py`) now projects the render-ready `executionGraphView` on sprint documents (L12-R4): `_master_docs_by_ref` indexes every valid master payload in the projected set for the summary reader — no bound evicts a document, so all of them are indexed (260916-TDPU; it formerly indexed only the bounded payload window); the on-demand body read, since 260921-ICR-L42, builds the same table from only the masters its graph names — `_execution_graph_view` walks the persisted graph (waves, endpoints, titles, facts) and feeds the primitives-only builder, and `_task_doc_node` splits into the reader-body and execution-graph field groups. Docs without a graph project `None`.


## 260815-DAG Master Full-Gate Repair Route Impact

`snapshots_impl/_closeout_queue.py` and `_runtime.py` import paths updated to the moved `worktrees/queue/*` / `models/queue/*`.

## 260821-CLIVE Closeout And Task-History Projection

`snapshots_impl/_closeout_queue.py` captures the exact current projection source for every
orchestrating sprint, including valid graph-less atomic-sequential sprints, then reads the effective
disposable projection. It surfaces service condition, source classification/fingerprint/problems,
and waiting-generation member order/reasons. Invalid, unreadable, missing, or stale bytes become
invalid-empty rather than disappearing or serving stale candidates.

`snapshots_impl/_task_documents.py` adds typed discarded-unstarted rows and counts to master task
and series projections. The audited proof/reason/timestamp remain task history and participate in
body revision identity. Neither projection mutates its source authority.

## CCR Typed Requirement Projection

The task reader now renders approved requirement packet references and acceptance-obligation
questions as readable strings, while its body-revision digest retains the full typed JSON
values. This preserves wire compatibility without losing semantic edit invalidation.

## 2026-08-26 Atomic Task Refresh And Retry

`ProjectionInputState._refresh_tasks` builds contracts, enclosures, task documents, and series into
locals before publishing the new task-domain snapshot. It sets `_task_refresh_pending` before the
read begins, preserves the previous snapshot if a reader raises, and clears the flag only after all
four values publish together. A heartbeat therefore retries an interrupted task refresh without
waiting for a second task mutation. This is part of the route's bounded-retention and atomic
publication contract, not a cache optimization.

## 260913-LCA-L10 Tolerant Read Edge (Route Impact)

`snapshots_impl/_task_documents.py` stopped deleting a durable task document over a field this reader's
schema does not know. All five read-edge call sites now route through one `_projected_document`, which
validates strictly and then, only for pydantic's `extra_forbidden`, drops exactly the addressed keys and
validates again; every other failure still withholds the document. The route-level consequence is the
one this overview now carries as an invariant: the projection edge reads tolerantly because it renders,
and the strict read remains with authoring and the enforcement folds.

Why it mattered at route level: a completed leaf whose JSON carried a step-level `note` from a newer
build vanished from `analytics.taskDocuments`, so the dashboard's sub-task index rendered that row as
dead text while unstarted rows stayed live — a version skew that presented as a status filter. Nothing
about the summary window caused it: `TASK_DOCUMENT_SUMMARY_LIMIT = 250` was measured irrelevant to that
defect, and that change set touched no dashboard file. (That limit no longer exists — 260916-TDPU
removed the task-document summary bound, so the route now projects every canonical document; see the
2026-09-16 entry below. 260916-TDPU's only dashboard edits are comments recording this removal, in
`detail-panel/model.ts` and `detail-panel/masterSeries.test.tsx`.)

Two things stay out of scope deliberately, recorded on the reader's card rather than repaired here: a
sixth same-class drop site at `snapshots_impl/_closeout_queue.py:33-36`, and the residual unprunable-loc
gap (a loc pydantic augments, such as the legacy `ref`), which stays fail-closed.

## 260921-ICR-L42 Bounded Task-Document Reads (Route Impact)

The change spans two files of this route with one purpose. `snapshots_impl/_task_documents.py`'s body
read stopped building its master join table from the whole corpus. It now reads the requested
document and, for a sprint only, the masters its graph names (`_graph_master_docs`, through
`_common._canonical_task_json_candidates`). `snapshots_impl/_common.py::_iter_task_json` stopped
recursively globbing every JSON under `tasks/`. It now walks only the three canonical levels, for the
same result. The route-level consequence is that both costs follow what is named, while the served
projection is byte-identical. That was checked on 561 live canonical bodies and 15 probe paths,
including every 404 case.

The projector's own pass (`projection_inputs.py` → `read_closeout_queues`, and on task refresh
`read_task_documents` and `read_series_documents`) uses the same enumeration, so it also becomes
cheaper. Its cache discipline is unchanged. The body read no longer touches the shared
`TaskDocumentPayloadCache`, so HTTP threads no longer mutate it alongside the projector thread. The
installed-build confirmation (concurrent master+leaf reads, projector CPU) belongs to leaf L50. The
notes-listing request belongs to leaf L55 and the eager review catalogue to leaf L47; both are separate
costs this route change does not claim.

- The body read and its graph-only join table. [3]
- The bounded canonical enumeration every always-on reader uses. [4]
