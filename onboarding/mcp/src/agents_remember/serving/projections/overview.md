# serving/projections/ — Projection File-Surface Readers Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/projections/` |
| onboardingRoute | `mcp/src/agents_remember/serving/projections/overview.md` |
| parentOverview | [`serving/overview.md`](../overview.md) |

## What This Area Is

This area reads producing subsystems' file surfaces and assembles inputs for the workspace projection. It covers providers, enclosure contracts, task documents, engine-process facts, drift snapshots, landing observations, ledger and analytical surfaces. The serving tick combines these inputs with lifecycle logs, reduces them through the observer APIs, and publishes projection files. Observer event mutation remains with its write-side owner; serving may consume the lower observer projection and reducer APIs.

## Hot Path Summary

The named dependency adapter joins the owning ordinary master and its explicitly listed child files; source state feeds the same pure master-order derivation used by publication. Requested-body/corpus readers and newly read named owner/child inputs require the raw task schema before tolerant parsing. Missing/wrong-schema neighbors are not admitted. The earlier defaulted-schema admission gap remains historical diagnosis, not a current source defect; these predicates and scoped dependency-field assertions do not establish universal serialized-body parity or an executed result.

`snapshots.py` supplies provider readers and re-exports the split readers. `projection_inputs.py` refreshes retained inputs by domain; `contract_snapshot.py` builds one immutable enclosure snapshot for each task refresh. `landing_state.py` observes eligible landing arcs in the background. `projection_store.py::project_and_write` connects input reading, reduction and publication. `paths.py` resolves serving's observer store paths locally; the kernel has equivalent path definitions, but this module is not currently a wrapper around them.

## Construction And Data Flow

Incremental refresh carries complete accepted paths through actual task/lifecycle dependency consumers. Incomplete/uncertain samples reconcile fully. Closeout queue reuse separately authenticates each sprint's document, code/memory and source-tip evidence; a workspace-only wake is not a demand for whole-corpus census. Semantically identical projection publication retains its file, and unsuccessful required refresh/publication keeps invalidations owed.


The task-document reader computes whole header-note and review-finding counts before bounded summary selection (six header notes and twenty-five review findings). Summary mode emits no decision bodies and no decisionsCount field; full-body mode retains all decisions and complete reader strings/collections.
Form derives from the model's sprint/master/task rule, not the count of visible sub-task rows. Header,
status, step/sub-step note/outcome and review changes participate in body revision identity. These
read-only projection/display additions preserve the bounded canonical enumeration and explicitly named
on-demand joins below; they create no task, acceptance or scheduling authority.

Full body requests avoid canonical task-corpus enumeration: they read the requested document, graph-named masters for sprint annotations, and the owning master plus its explicitly listed task files for ordinary dependency facts. External direct-grant annotation adds an explicit task-addressed grant census and retained legacy unaddressed fallback, so no zero-directory/constant-I/O promise is made. Summary/series canonical enumeration and ordering remain unchanged.

The serving projector passes its retained input state, provider refresher and landing reader into `project_and_write`. Refresh kinds distinguish full refreshes, named domain changes and heartbeats. Domain retention avoids re-reading every surface for unrelated changes; closeout queues are nevertheless read on every input pass.

Full task refresh constructs contracts, enclosures, task documents and series locally before assigning the retained quartet; failure during that construction preserves the prior quartet. A failed input read leaves _task_refresh_pending set, and a later read, including a heartbeat, forces a full retry. Complete incremental task samples assign contracts and enclosures before reprojecting task documents and subsequently merging series, so failure on that branch need not preserve the entire prior quartet. Contract construction reuses successful parses only while mtime, size and ctime match, removes entries outside the live enumeration, and publishes a read-only mapping.

The earlier runtime reader account of copied inbox/expectation task references is historical: those readers and slots are absent from the current input schema. Current enclosure readers include the lifecycle-operation projection returned by the durable operation reader. That reader prefers the newest active operation when any exist, otherwise the newest available record; it may instead return a journal-read decision or no safely projectable operation. Durable operation state remains the authority. Keeping worker and resume identities private remains standing intent; the complete downstream field exclusion was not established in this bounded review.

Task JSON supplies the task-document and series surfaces. The always-on reader projects every valid canonical document without a task-document count window, while omitting full reader bodies. Its master join table indexes every valid master payload in that set. The on-demand body reader opens the requested document and builds graph annotations for named masters and ordinary dependency facts for the owning master/listed tasks; it does not enumerate the canonical document corpus or use the shared task payload cache.

The canonical enumeration lists repository folders, task folders and their direct JSON entries. It excludes archive and enclosure paths and does not descend into notes. Graph-master lookup still lists repository and task directories before selecting the named task folders; its JSON reads follow the graph references rather than all documents. Equality with an earlier recursive glob is not a general promise: the current source explicitly describes excluding historical copies below notes.

Task projection carries explicit execution nature, typed `SubTaskRef.masterRef`, seats, persisted execution graph, derived waves and a render-ready execution graph view. The serving seam resolves graph endpoints, titles and master facts for the primitives-only graph-view builder. Ordinary masters can project a derived waitsFor graph; absent dependency data supplies no Order. Sprints retain their explicitly authored graph contract. Reader-body and graph fields are constructed separately. Body revision includes subtask links, discarded rows, seats, execution nature and graph, so those edits invalidate a fetched body.

Approved requirement packet references and acceptance-obligation questions become readable strings in reader bodies. The revision digest retains their full typed JSON values. Master task and series projections also expose discarded-unstarted rows and counts, including reason, timestamp and proof; discarded rows participate in body revision identity.

The closeout reader strictly validates each sprint payload, captures its current projection source and reads the effective disposable queue. It projects service condition, source classification, fingerprint, problems, and member order and reasons. The source capture supports graph and graph-less modes. The effective store returns invalid-empty for unreadable or mismatched state. Strictly invalid sprint payloads are skipped before source capture, so the invalid-empty promise applies after that admission boundary. Task-history and closeout projection do not rewrite their source authorities.

Landing observation has its own enclosure walk and concurrency limit. Completed arcs without a valid current final receive one permitted finishing attempt per process, including startup, with four terminal admissions per sweep. Successful or failed attempts stay consumed even after later final loss; only a real reopen resets that arc. Abandoned and build-only contracts remain probe-free. Completed contracts serve trusted current finals; missing, corrupt, stale or unsuccessful finals remain explicitly missing rather than entering recurring historical repair. After a successful atomic final-file replacement, the writer evicts the parsed-final cache entry for that exact path, even if mtime is unchanged. Failed writes retain the warning path.

`projection_store.py` reads lifecycle logs and gathers analytical surfaces, passes inputs to the pure workspace reducer, and writes `latest-state.json` and `latest-metrics.json`. Each file is published through the atomic-write primitive separately; these two writes are not one transaction.

## What Belongs Here

| Path | Role |
| --- | --- |
| `paths.py` | Observer store-root resolution using local definitions equivalent to kernel primitives. |
| `contract_snapshot.py` | One immutable member-enclosure snapshot per task-domain refresh. |
| `snapshots.py` | File-surface readers and the public re-export surface. |
| `snapshots_impl/` | Split reader implementations: analytics, runtime/enclosures, task docs, closeout queues and shared helpers. |
| `drift_snapshots.py` | Projection-side drift-snapshot pruning policy. |
| `landing_state.py` | Bounded background landing observation and publication. |
| `projection_inputs.py` | Domain-invalidated retained projection inputs. |
| `projection_store.py` | Log/snapshot reading and per-file atomic projection writes. |

## Structures Found Here

- Reader hub and split implementations, using producing subsystems' parsers where provided and local JSON/projection parsing where required.
- Immutable contract snapshots, live-set parse caching and bounded landing observation.
- Retained input state with full, change and heartbeat refresh kinds.
- Projection publication through `latest-state.json` and `latest-metrics.json`.

## Local Invariants And Boundaries

- Enclosure enumeration excludes notes and archives. Snapshot construction records foreign contracts in `skipped` and excludes them from the mapping and parse cache. Foreign membership is checked against the filesystem-resolved repository tasks folder determined by the enclosure's position. Landing observation applies the same exclusion independently and names it in a warning.
- A projection reader must not erase a durable task document merely because its schema does not know a field. The task reader retries validation after removing exactly the addressed `extra_forbidden` paths, with a fixed pass bound. Genuine invalidity and unaddressable validation locations remain fail-closed. The closeout reader still has a separate strict-validation boundary. Gate projection uses the tolerant store read; the enforcement fold's strict read remains distinct.
- A request-path reader should cost what it names rather than read every document in the corpus. The body reader opens the requested document and graph-named masters; the canonical background pass lists only the three task levels. This adds no task-document index or persistent store. The always-on readers retain their existing shared payload cache; the HTTP body reader does not mutate it.
- Atomic publication prevents a partially written individual projection file from being exposed. It does not promise a jointly atomic state/metrics pair.
- Observer event mutation belongs to the write-side owner. This route is not wholly free of durable housekeeping: input refresh prunes expired lifecycle logs and orphaned drift snapshots, and projection publication prunes attention dismissals. The former inbox-reader compaction account is historical, not a current housekeeping call. These current calls must be distinguished from the standing ownership intent.
- Kernel ownership of shared path conventions remains the stated intent. Serving's local path definitions currently duplicate those conventions; the overview does not endorse that discrepancy as intended architecture.

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Observer write side (ambient, events, store, reducer) | `observer/` |
| Wire contracts and control services | `models/conversations/`, `serving/conversation/` |
| Drift-snapshot path primitives | `kernel/primitives/drift_snapshot.py` |

The boundary table is retained as existing route metadata. In current source, drift path resolution imports kernel observer-path primitives, while this route also implements snapshot-file removal locally; the table alone does not establish exclusive implementation ownership.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `snapshots.py` | reader hub | All named-state surfaces feed the projection. | covered |
| `projection_store.py` | I/O edge | Atomic publication and lifecycle-log reads. | covered |
| `contract_snapshot.py` | cache | Stat-identity parse reuse and one shared snapshot on task refresh. | covered |
| `landing_state.py` | background observer | Bounded landing facts without blocking the tick. | covered |

## How To Use This Area

When changing a projection reader, read this overview and the owning reader's sidecar, preserve the input/refresh discipline in `projection_inputs.py`, and verify the change through the applicable projection, observer and structural checks. This is guidance for future work, not a report of checks executed for this proposal.

## Metadata And Verification Limits

The coverage labels below are preserved onboarding metadata, not current lifecycle, acceptance or test-execution promises. This review establishes no task status or lifecycle acceptance authority.

Historical route-move attribution, dashboard-edit attribution, the reported 3.865-second contention diagnosis, the 561-body/15-probe equivalence check, the former 250-document limit's measured irrelevance, and installed-build confirmation assignments cannot be established from these current source owners alone. They are historical claims awaiting parent adjudication, not executed evidence here. No cross-repository implementation was examined; the former blanket absence claim is not established by this bounded account.

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

## Interested Landing Observation

The serving app binds the landing refresher to actual Projector state-stream subscribers. It admits no discovery without interest, rechecks after awaited discovery and at semaphore admission, and leaves unbound explicit refresh callers unchanged. LandingProbeSchedule stores only current eligible exact identities; semantic-answer/contract changes and clock regression reset the epoch, with 30/120/600/3600-second due intervals at unchanged ages 120/600/3600 seconds. Observation-age noise is not a changed answer; a fact's own at and row order are semantic. Due eligibility is not a total event-to-publication latency guarantee.

The schedule advances after actual publication, not a skipped probe. Existing bounded terminal admission, one finishing attempt per arc, truthful final validation and copy-on-write publication remain. The previous fixed open cadence is deliberately replaced only for serving-bound calls; provider safety and projection healing are separate owners. landing_cadence.py is the transient policy owner, not durable landing state or a frontend interest channel.

## Evidence


- The observer store-root conventions are kernel-owned. [1]
- The bounded canonical enumeration every always-on reader uses. [4]

- Serving locally defines equivalent observer paths rather than importing the kernel definitions. [5]

- The projection tick consumes these readers. [2]
- The body read and its graph-only join table. [3]

- Full task-domain construction preserves prior values on failure; complete incremental dependency updates are not quartet-rollback atomic. Both retry pending refreshes. [6]

- Contract parsing uses stat identity, rejects foreign contracts and prunes departed entries. [7]
- Task projection tolerates addressed unknown keys, projects graph and typed reader fields, and hashes full semantic values. [8]

- Current enclosure readers project lifecycle operations with the durable operation reader's tolerant boundary. Earlier inbox/expectation-copying and inbox-compaction accounts are historical, absent from current runtime readers and input slots. [9]

- Closeout projection has strict sprint admission and an invalid-empty effective-state boundary. [10]
- Landing observation excludes historical repair and evicts the exact parsed-final entry after successful publication. [11]
- Projection files publish separately; the route also invokes durable housekeeping. [12]
- Direct serving callers pass retained tick state and request one task-document body. [13]

- Actual bound page interest gates discovery and admission; skipped work does not advance publication or terminal attempts. [14]
- Transient due state retains current identities and uses semantic-answer age rather than observation noise. [15]
