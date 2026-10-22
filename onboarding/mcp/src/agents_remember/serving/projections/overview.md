# serving/projections/ — Projection File-Surface Readers Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/projections/` |
| onboardingRoute | `mcp/src/agents_remember/serving/projections/overview.md` |
| parentOverview | [`serving/overview.md`](../overview.md) |

## What This Area Is

This area reads file surfaces published by producing subsystems and assembles native task, enclosure, provider, engine, drift, landing, ledger and analytical inputs for the workspace projection. `read_task_sources` supplies canonical summaries plus declared parent/child facts; the observer task-entry producer joins them with worktree contracts and bound native host-agent activity. Served tasks/counts replace parallel lifecycle/document/series projections. The workspace River is a separate diagnostic/event transport, not an input folded into task state.

## Hot Path Summary

Native task sources feed one server TaskEntry producer: authored status owns stage, and only started tasks carry bound host activity/eventAt. Declared lists, preserved record-master facts and unambiguous commanded-master relations own membership independently of worktrees. For documented subTasks, a genuinely absent master permits list fallback; a present contrary or unresolvable master does not. Other listed kinds retain identity/cycle-guarded list placement without kind rejection or own-master validation by that path. Structured disagreements expose the contrary list/record facts without authoring a repair. Host intake runs at startup/invalidation, not periodic healing. Full task bodies are separate TaskSummary content with an app-scoped dependency-validated cache.

The named dependency adapter joins the owning ordinary master and its explicitly listed child files; source state feeds the same pure master-order derivation used by publication. Requested-body/corpus readers and newly read named owner/child inputs require the raw task schema before tolerant parsing. Missing/wrong-schema neighbors are not admitted. The earlier defaulted-schema admission gap remains historical diagnosis, not a current source defect; these predicates and scoped dependency-field assertions do not establish universal serialized-body parity or an executed result.

`snapshots.py` supplies provider readers and re-exports the split readers. `projection_inputs.py` refreshes retained inputs by domain; `contract_snapshot.py` builds one immutable enclosure snapshot for each task refresh. `landing_state.py` observes eligible landing arcs in the background. `projection_store.py::project_and_write` connects input reading, reduction and publication. `paths.py` resolves serving's observer store paths locally; the kernel has equivalent path definitions, but this module is not currently a wrapper around them.

## Construction And Data Flow

Incremental refresh carries complete accepted paths through task dependency consumers; incomplete/uncertain samples reconcile affected domains fully. Host activity is a distinct invalidation domain excluded from ordinary full/healing refreshes after initial intake. Closeout queue reuse separately authenticates each sprint document, code/memory and source-tip evidence; a workspace-only wake is not a whole-corpus census request. Semantically identical projection publication retains its files, and unsuccessful required refresh/publication keeps invalidations owed.


The task-document reader computes whole header-note and review-finding counts before bounded summary selection (six header notes and twenty-five review findings). Summary mode emits no decision bodies and no decisionsCount field; full-body mode retains all decisions and complete reader strings/collections.
Form derives from the model's sprint/master/task rule, not the count of visible sub-task rows. Header,
status, step/sub-step note/outcome and review changes participate in body revision identity. These
read-only projection/display additions preserve the bounded canonical enumeration and explicitly named
on-demand joins below; they create no task, acceptance or scheduling authority.

Full body requests avoid canonical task-corpus enumeration: they read the requested document, graph-named master documents and the child files explicitly declared by those masters for sprint annotations, plus the owning ordinary master/listed tasks for dependency facts. External direct-grant annotation adds an explicit task-addressed grant census and legacy unaddressed fallback, so no zero-directory/constant-I/O promise is made. These content dependencies are captured for a separate body cache; canonical background task-source enumeration remains distinct.

The serving projector passes its retained input state, provider refresher and landing reader into `project_and_write`. Refresh kinds distinguish full refreshes, named domain changes and heartbeats. Domain retention avoids re-reading every surface for unrelated changes; closeout queues are nevertheless read on every input pass.

Full task refresh constructs contracts, enclosures and canonical task sources locally before assigning the retained trio; failure during construction preserves that trio. A failed input read leaves `_task_refresh_pending` set; a later pass forces a full healing-domain retry while preserving explicitly owed domains. Complete incremental samples assign contracts/enclosures before replacing the reprojected document closure, so that branch is not whole-trio rollback atomic. Closure replacement drops newly invalid sources rather than retaining stale summaries. Contract construction still reuses successful parses only while mtime, size and ctime match, removes departed entries and publishes a read-only mapping.

The earlier runtime reader account of copied inbox/expectation task references is historical: those readers and slots are absent from the current input schema. Current enclosure readers include the lifecycle-operation projection returned by the durable operation reader. That reader prefers the newest active operation when any exist, otherwise the newest available record; it may instead return a journal-read decision or no safely projectable operation. Durable operation state remains the authority. Keeping worker and resume identities private remains standing intent; the complete downstream field exclusion was not established in this bounded review.

Task JSON supplies canonical TaskDocumentSource values, not separate served task-document and series lists. The always-on reader projects every valid canonical document without a count window, omitting full reader bodies. Its graph join table indexes every valid document, including segmented-master children: an available child document supplies its own stage, with declared-row fallback only when absent. On-demand reading avoids the canonical document corpus and background shared payload cache, but the separate app body cache can retain prepared TaskSummary content after every captured input revalidates.

The canonical enumeration lists repository folders, task folders and their direct JSON entries. It excludes archive and enclosure paths and does not descend into notes. Graph-master lookup still lists repository and task directories before selecting the named task folders; its JSON reads follow the graph references rather than all documents. Equality with an earlier recursive glob is not a general promise: the current source explicitly describes excluding historical copies below notes.

Task content carries explicit execution nature, typed SubTaskRef.masterRef, seats, persisted execution graph, derived waves and a render-ready graph view. Serving resolves graph endpoints, titles and each named document’s own stage for the primitives-only builder; it does not infer a master’s stage from its children. Ordinary masters can expose a derived waitsFor graph; absent dependency data supplies no Order. Sprints retain their authored graph contract. Reader-body and graph fields remain separate; body revision includes subtask links, discarded rows, seats, execution nature and graph. TaskEntry separately resolves stage/activity and parent/children/counts, so cached content is not another task-status projection.

Approved requirement packet references and acceptance-obligation questions become readable strings in reader bodies; the revision digest retains their full typed JSON values. Master summary/body content retains discarded-unstarted rows and counts, with reason, timestamp and proof; discarded rows participate in revision identity. These content facts do not restore a separate series projection.

The closeout reader strictly validates each sprint payload, captures its current projection source and reads the effective disposable queue. It projects service condition, source classification, fingerprint, problems, and member order and reasons. The source capture supports graph and graph-less modes. The effective store returns invalid-empty for unreadable or mismatched state. Strictly invalid sprint payloads are skipped before source capture, so the invalid-empty promise applies after that admission boundary. Task-history and closeout projection do not rewrite their source authorities.

Landing observation has its own enclosure walk and concurrency limit. Completed arcs without a valid current final receive one permitted finishing attempt per process, including startup, with four terminal admissions per sweep. Successful or failed attempts stay consumed even after later final loss; only a real reopen resets that arc. Abandoned and build-only contracts remain probe-free. Completed contracts serve trusted current finals; missing, corrupt, stale or unsuccessful finals remain explicitly missing rather than entering recurring historical repair. After a successful atomic final-file replacement, the writer evicts the parsed-final cache entry for that exact path, even if mtime is unchanged. Failed writes retain the warning path.

`projection_store.py` passes retained task sources, host activity and structural/analytical inputs to the pure workspace reducer; it reads no lifecycle logs or workspace River. Stable-content equality suppresses unchanged file publication. When required, latest-state.json and latest-metrics.json publish through separate atomic writes, not a jointly atomic transaction. Task summaries are under TaskEntry; the body-payload warning measures their retained previews, not an analytics.taskDocuments corpus.

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
| `projection_store.py` | Native input reduction and stable-change-gated, per-file atomic projection writes. |

## Structures Found Here

- Reader hub and split implementations, using producing subsystems' parsers where provided and local JSON/projection parsing where required.
- Immutable contract snapshots, live-set parse caching and bounded landing observation.
- Retained input state with full, change and heartbeat refresh kinds.
- Projection publication through `latest-state.json` and `latest-metrics.json`.

## Local Invariants And Boundaries

- Enclosure enumeration excludes notes and archives. Snapshot construction records foreign contracts in `skipped` and excludes them from the mapping and parse cache. Foreign membership is checked against the filesystem-resolved repository tasks folder determined by the enclosure's position. Landing observation applies the same exclusion independently and names it in a warning.
- A projection reader must not erase a durable task document merely because its schema does not know a field. The task reader retries validation after removing exactly the addressed `extra_forbidden` paths, with a fixed pass bound. Genuine invalidity and unaddressable validation locations remain fail-closed. The closeout reader still has a separate strict-validation boundary. Gate projection uses the tolerant store read; the enforcement fold's strict read remains distinct.
- A request-path reader should cost what it names rather than read every document. The body reader opens requested, graph-named master/child and ordinary dependency inputs; the canonical background pass lists the three task levels. No persistent task index is added. Background shared payload parsing remains distinct from the app-scoped TaskSummary body LRU, whose captured inputs must still be current before reuse or 304.
- Atomic publication prevents a partially written individual projection file from being exposed. It does not promise a jointly atomic state/metrics pair.
- Workspace River mutation/retention belongs to its writer/compactor, not these projection readers. Durable housekeeping remains: drift refresh prunes orphaned snapshots and workspace refresh reconciles occurrence-bound attention dismissals from domain observations. A dismissal refresh write failure retains last read acknowledgements without blocking projection; incomplete observations must not erase valid visible occurrences. Lifecycle-log pruning and inbox compaction are historical, absent from this input path.
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
| `projection_store.py` | I/O edge | Native task/host inputs and per-file atomic publication. | covered |
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

The schedule advances after actual publication, not a skipped probe. Existing bounded terminal admission, one finishing attempt per arc, truthful final validation and copy-on-write publication remain. The previous fixed open cadence is deliberately replaced only for serving-bound calls; provider safety and non-host projection healing are separate owners. Native host activity is event/invalidation-driven, not a landing or healing poll. landing_cadence.py is the transient policy owner, not durable landing state or a frontend interest channel.

## Native Host Intake And Task Membership

`host_activity.py` admits only complete publications for a bridge-reconciled plugin boot while its proved supervisor subscription is armed. Native agent IDs join to canonical role-agent task bindings; unusable observations remain unknown and unbound agents are ignored/counted, not synthetic activity. `host_supervisor.py` proves the process before/after pidfd acquisition and invalidates the existing pacer on exit; shutdown closes the subscription. Startup and host-domain invalidations drive intake, not recurring healing polls.

The task-entry producer maps planning/inProgress/abandoned/Completed to planned/started/aborted/completed. Only started tasks obtain works/paused/unknown and eventAt: in-turn or permission contributors mean works, a known complete observation without workers means paused, and unknown host means unknown. eventAt is the latest contributing native event, not a projection/feed timestamp. Real child documents own stage; declared-row-only children retain row stage. An authored subTask's own master takes precedence, while a genuinely absent master permits adoption by its listing master. A documented subTask's present unresolvable master is preserved, reported and not adopted. Distinct subTask list/record disagreements are emitted once per declaring master, including subTasks absent from every list. Declared rows and unambiguous commanded-master relations form deterministic acyclic membership with one parent per child. Exact repository/task-root/leaf bindings attach worktrees; unmatched enclosures stay visible separately and never create membership or task stage.

The body cache records link/target and consumed task/graph/order/grant input identities, including selection directories. It serializes TaskSummary content, hashes its bytes and retains only current generations within entry/byte limits. Native change-set/summary caching has separate repository/object/configuration dependencies. Neither cache owns TaskEntry state or River retention.

**L184.** The host-activity input records the reconciliation it applied, so an older answer can no longer certify a boot.

## Evidence



- Master validation in placement applies only to documented subTasks; other listed kinds retain list placement under existing identity/cycle guards, not a kind-rejection or own-master-validation rule. [22]


- The observer store-root conventions are kernel-owned. [1]
- The bounded canonical enumeration every always-on reader uses. [4]

- Serving locally defines equivalent observer paths rather than importing the kernel definitions. [5]

- The projection tick consumes these readers. [2]
- The on-demand body reader validates the requested canonical task document, joins only graph-named masters and their declared children through _graph_master_docs, and also obtains ordinary order/dependency fields through read_order_fields, which reads the owning master and its explicitly listed children. It avoids enumeration of the canonical task corpus; the body join is not graph-only. [3]

- Full task-domain construction stages contracts, enclosures and task_sources in locals and assigns the retained trio only after construction succeeds. Complete incremental dependency refresh is not whole-trio rollback atomic: contracts/enclosures are assigned before affected document closure projection can fail. Any failed read leaves _task_refresh_pending set; a later read forces full healing-domain reconciliation and clears the flag only after success. These guarantees are about the retained trio, not rollback of every cache or aged slot. [6]

- Contract parsing uses stat identity, rejects foreign contracts and prunes departed entries. [7]
- Task projection tolerates addressed unknown keys, projects graph and typed reader fields, and hashes full semantic values. [8]

- Current enclosure readers project lifecycle operations with the durable operation reader's tolerant boundary. Earlier inbox/expectation-copying and inbox-compaction accounts are historical, absent from current runtime readers and input slots. [9]

- Closeout projection has strict sprint admission and an invalid-empty effective-state boundary. [10]
- Landing observation excludes historical repair and evicts the exact parsed-final entry after successful publication. [11]
- Projection files publish separately; the route also invokes durable housekeeping. [12]
- Direct serving callers pass retained tick state and request one task-document body. [13]

- Actual bound page interest gates discovery and admission; skipped work does not advance publication or terminal attempts. [14]
- Transient due state retains current identities and uses semantic-answer age rather than observation noise. [15]

- Canonical task sources retain declared children, the resolved record master and its original literal for one downstream producer, preserving absent versus unresolvable input. [16]
- Full task refresh prepares contracts, enclosures and sources before assigning the retained trio. [17]
- Incremental task reprojection replaces the whole affected closure and drops newly unreadable/invalid sources. [18]
- Startup and explicit host-domain invalidations trigger host intake; ordinary full healing excludes that domain. [19]
- Requested bodies read only their named graph masters/declared children rather than enumerating the canonical corpus. [20]
- Body generation tracks link/target identities and rejects unreadable or changing captured inputs. [21]
