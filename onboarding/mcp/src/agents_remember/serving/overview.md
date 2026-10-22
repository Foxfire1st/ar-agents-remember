# Serving — Dashboard, Hosted Sessions, And Review Boundaries

## Governing Overview
[mcp/overview.md](../../../overview.md)

## Purpose

The serving package composes the local dashboard, projection/event streams and retained file, note, task, requirement, change-set, Knowledge and review readers over configured application ports. Native Paseo integration remains a separate retained subtree; the removed hosted terminal catalogue, harness adapter/control, conversation, notifier and supervisor plane is not this package's current responsibility.

Role launch instructions are generic capsule-or-refused values; compilation and admission remain application-owned. The current source literal PUBLIC_TOOLS has41 names: the 40 after dispatch_agent removal plus the mounted knowledge_write. Declaration, installation content, native receipt identity and observed host execution are separate facts; this overview creates no new CODE grade.

## Hot Path Summary

`app.create_app` builds app-scoped collaborators and registers retained reader/action/grant routes before the static mount. Projection version 2 serves reference-keyed `tasks` (TaskEntry), `taskCounts`, unbound enclosures and retained analytics; state SSE uses task/task.removed/taskCounts rather than lifecycle rows. `/api/task-document` returns separately requested TaskSummary content, not another status authority. The retained action path acknowledges/dismisses attention and the developer grant route calls shared grant authority; gate-decision and operator-inbox routes are absent.

`register_canvas_routes` (MIK-R104, MIK-R105) adds two surfaces after the API routes and before the static mount. The frame route serves one live session's own admitted document and its assets under the policy headers, and the trusted API route serves the panel's saved-first view, the side conversation and the one explicit presenter start. `RefuseCrossOriginWrites` refuses a state-changing browser request that is not from this dashboard's own page — `Sec-Fetch-Site` other than `same-origin`, or, when that header is absent, a foreign or `null` `Origin` — with a named 403 before any route, while a request carrying neither header comes from no browser page and passes; `RefuseForeignHosts` refuses every request, reads included, whose `Host` names another host or port. A frame that navigates itself keeps its sandbox flags and its writes still fail the origin guard.

_app_lifespan compacts the workspace river, primes the projector and starts projection, provider-metrics, leaf-archive recovery, held native-role message delivery and river-compaction tasks. Optional heap/allocator tasks remain opt-in. It does not prime or poll a terminal catalogue or run a hosted-seat notifier. The archive worker drains cancellation before close; held-message sweep failures are contained. Shutdown invokes the injected review-tree owner, cancels and awaits owned background tasks; there is no removed terminal-host shutdown.

The projector retains change-driven invalidation, stable/current publication, subscription delivery and task-input retry ownership. Canonical task status maps to planned/started/aborted/completed; only started tasks receive bound host-agent works/paused/unknown activity and contributing eventAt. Declared lists, documented-subTask master precedence and unambiguous commanded-master relations determine membership independently of worktree bindings. Only an absent subTask master uses list fallback; its present contrary or unresolvable master remains explicit and unbound. Other listed document kinds retain list placement under identity/cycle guards without own-master validation by that path. The same producer reports distinct list/record disagreements once per master rather than dropping contrary facts. Host reads occur at startup and host invalidation, with boot reconciliation and a proved supervisor-exit subscription; ordinary heartbeat/full healing is not host polling. File readers retain their own absence and last-good-data policies. Review/read shims do not turn an unwired adapter into an empty catalogue, body or comparison.

The read-only catalogue and changed-intent summary routes accept an optional recorded comparison number and forward it through their typed ports. Catalogue negative numbers receive 400; summary negative numbers produce the typed unavailable result without inventing counts. The summary cache includes that number in its question key, so different numbered comparisons cannot reuse each other's answer. `RecordedAnswerReuse.answer` also accepts an explicit keep predicate: a freshly produced value rejected by it is returned but never retained, while ordinary input-observation and age/capacity bounds remain with that cache owner. These transport additions select no arbitrary tree and confer no review or acceptance authority.

## Construction And Ownership

Configured McpRuntimeConfig and admitted roots feed the dashboard; untrusted request values do not install arbitrary host roots. Compilation, task authority, canonical knowledge comparison, native role launch and independent acceptance remain with their actual owners. Serving capsule_delivery is an immutable copied value, not a harness-specific carrier/protocol planner.

## Invariants And Boundaries

Snapshots/deltas, raw observer events and separately requested bodies are different transports. Refusal/unavailable and absent/empty are not interchangeable. Retained internal compilation and old stored data do not restore public compile, gate or structural-session operations.

## Historical And Verification Limits

Old terminal/session launch-site, provider-specific carrier and first-prompt acceptance claims are withdrawn as current facts. Retained source declarations and static tests are not fresh runtime/test acceptance; the existing bounded producer seals remain literal and separately graded.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/serving/`               |

### Native-source claim qualifications

- A numbered recorded comparison is looked up exactly; code/memory ranges use its recorded sides (converted memory base when present), and the list returns those four tree operands. A comparison combined with mode is refused by _comparison_mode_refusal, with explicit query-presence checks in register_changeset_routes.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/changeset_comparison.py:16-27`; `mcp/src/agents_remember/serving/changeset.py:636-642`.

- **The comparison route's handler over its injected port.**  Anchor: "def api_review_intent("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:661-709`.

- **The entry route's handler: the task context alone, and an unwired process answered with a named refusal rather than an empty list.**  Anchor: "def api_review_intent_entries("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:644-655`.

- **The expansion route's handler and the module-level transport behind it (`260921-ICR-L3`).**  Anchor: "def api_review_intent_source_content("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:657-659`.

- The query parser that admits only those two.  Anchor: "def review_request_from_query("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:294-327`.

- The refusal code a process with no adapter produces.  Anchor: `review_adapter_unavailable`

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- The 404 for a candidate that does not resolve.  Anchor: `status_code`

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- **The registration that must precede the static mount and that takes all three ports.**  Anchor: "def register_review_routes("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:627-709`.

- The review registrar is mounted before static routing and accepts three review transport ports; the summary route is mounted separately.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:627-709`.

- The GET-only route handler over the injected port.  Anchor: "def api_review_intent("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:661-709`.

- **The status mapping the routes inherit from the change-set routes; the signature accepts all three typed results and reads success as `refusal is None`.**  Anchor: "def _status_for("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- **The 400 a selector kind outside the admitted set gets, inside the comparison handler.**  Anchor: "def api_review_intent("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:661-709`.

- Retained transport mapping includes the legacy candidate_dataset_absent code as404; this does not establish a live dataset candidate path.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- **The 200/refusal split the entry handler makes: `entries` serves `200`, anything else goes through `_status_for`.**  Anchor: "def api_review_intent_entries("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:644-655`.

- The registration that must precede the static mount.  Anchor: "def register_review_routes("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:627-709`.

- The shared status mapping accepts three typed transport result classes and treats refusal is None as success.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- **The status mapping widened to the third result type, where the expansion's refusal code reaches `400` through the same fall-through as `comparison_refused`.**  Anchor: `source_content_unresolved`

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`; `mcp/src/agents_remember/models/knowledge/review_refusal.py:15-30`.

- A numbered recorded comparison is looked up exactly; code/memory ranges use its recorded sides (converted memory base when present), and the list returns those four tree operands.

The retained app shares one always-on background ledger across actual worker units, synchronous publication, event tails and startup. Diagnostics expose owner/wake facts with explicit incomplete windows rather than acceptance. Transaction-bound own-write suppression and pending invalidations retain healing for their admitted domains; native host activity is excluded from periodic healing. Raw event SSE reads only the workspace River, with writer/compactor-owned retention and virtual offsets; it is neither a lifecycle catalogue nor task/activity truth. Server-side host-start loading keeps its shared OS lease/progress and cancellation-drained driver without restoring the removed terminal catalogue or notifier plane.

## Landing Interest And Periodic Safety

Landing discovery and new remote-probe admission are conditional on the Projector's actual shared state-stream subscribers, bound by app composition before startup. Per current exact contract identity, semantic-answer age increases the due interval from 30 seconds to 120, 600 and 3600; changed answers/contracts reset it. One-shot state reads and frontend signals create no landing interest. Existing accounting, drained cancellation, sweep-local remote sharing and exact terminal-final/reopen boundaries remain.

This is not a dashboard-wide stop switch. Projection/watch/healing and other owned loops retain obligations within their domains; native host activity has no periodic healing poll. In particular, provider sample/record/degradation/compact remains periodic and independent of page interest or launch-authority absence: leftover labelled stacks must stay observable after revocation/restart or malformed authority. No fleet-retirement witness is inferred from permission to launch. Runtime measurements and installation acceptance remain separate from these source contracts.

## Native Read Reuse And Content Boundaries

`register_changeset_routes` creates one bounded ChangesetCache, shared with the intent-summary route through its typed inputs/read port. Native Git remains the selector/diff owner. Reuse observes repository/configuration/reference/object and, when needed, working-tree generations plus dependencies discovered before consumption. Pending results enter retention only after matching fresh post-read observations; incomplete/changing dependencies and failed native reads do not become reusable successes. Object-absence proofs also invalidate on additions. This is not TTL-based permission to serve stale inputs or a new comparison generation. Successful change-set/summary responses derive weak ETags from their returned bytes and honor If-None-Match; an unwired summary keeps its named 503.

Full task bodies have a separate app-scoped LRU of at most 1,024 entries/16 MiB, distinct from the background task-payload parse cache and native change-set/summary reuse. Captured filesystem inputs revalidate before body reuse; serialized TaskSummary bytes define its content revision. Unreadable/changing generations are served uncached and cannot justify a 304. State GET/SSE retain their separate projection-instance dump memo and servingBuild tail. None of these caches changes task stage, host activity, recorded operands, permission or acceptance.

## Open Review Memory Invalidations

The existing state SSE route accepts optional reviewRepo/reviewMaster/reviewLeaf. No selector keeps
ordinary stream behavior; any supplied selector forms the complete identity tuple for canonical
single-segment/root admission through the injected port. Collaborators and app runtime carry that
port. Request strings do not select arbitrary memory roots or alter the projector state schema.

The connection owns native nonrecursive directory handles, excluding symlink directories and named
generated/temporary subtrees. Startup and relevant directory events reconcile registrations; this is
not idle timer filesystem polling. A separate ready future precedes the size-one coalescing change
queue, and nonce/counter revisions are invalidations, not Git trees or acceptance observations.
Handled admission/watch errors publish review.memory.error with recovery; ordinary event delivery
retains its own stream path. Closing the connection drains queued async reads and joins the native
worker rather than abandoning its handles. No measured total shutdown bound is claimed.

A missing comparison number is not a dataset-mode discriminator: enabled live leaf-wide tree reads
can start without one, while focused card-entry reads require one. The transport retains some legacy
refusal spellings for status mapping; that does not reinstate removed candidate producers.


## Current Behavior

the change-set routes now run on a dedicated `_BoundedReads` scheduler: eight workers plus eight pending jobs, an explicit 503 over the cap, a queued job withdrawn on disconnect and a running job releasing its slot only at its physical end; the route returns 499 and the runner's one `_wait_process` kills the Git child and its group. Freshness is Git's own: id-keyed commit pairs are served with no observation, working views run `git status --porcelain=v2 -z` and have no cache where a plain read costs no more, and the object store is a `count-objects -v` census; the object/worktree walks are removed. The cache's result/repository/per-read maps are capacity-bounded, an abandoned read admits nothing, and the id-keyed accepted gap is named in the cache module. The intent-summary route keeps its 200/503/304 idiom and shares the same cache.

**L184.** The serving tick reads usage reports at a new stamped end, writes the one limit file whole under an exclusive lock, pauses a limited recipient's drain before any host read, and reaches the bridge through the port the composition root binds.

## Evidence


- Master validation in placement applies only to documented subTasks; other listed kinds retain list placement under existing identity/cycle guards, not a kind-rejection or own-master-validation rule. [137]


- The query, the port and the GET handler with its three answer classes. [3]
- The collaborator port and the registration before the static mount. [4]
- LaunchCapsuleMode has only capsule/refused and no resolver or legacy carrier policy. [9]

- Internal compile_launch_capsule admits task/free-agent seats through retained compiler ownership and returns a generic delivery/refusal. [13]

- The shared naming primitive appends the same physical lock suffix. [21]
- Every-directory filtering retains lock suffix exclusion. [22]

- **The comparison route's handler over its injected port.**  Anchor: "def api_review_intent(" [29]




- **The expansion route's handler and the module-level transport behind it (`260921-ICR-L3`).**  Anchor: "def api_review_intent_source_content(" [31]

- **The unwired-entry body: `unavailable` with the "not served rather than served empty" reason and next action — and, since `260921-ICR-L3`, its sibling for the expansion route.** [32]
- **The entry route constant, and the comment recording why it is a second path rather than a second adapter.** [33]
- The two admitted selector kinds, refused rather than mapped. [34] [46]

- The query parser that admits only those two.  Anchor: "def review_request_from_query(" [35]


- The query parser that admits only those two.  Anchor: "def review_request_from_query(" [47]

- **The status mapping the routes inherit from the change-set routes: success is `refusal is None`, and the four candidate codes — including `subject_unresolved` — answer `404`.** [36]
- The refusal code a process with no adapter produces. [37] [49]
- The 400 a selector kind outside the admitted set gets. [38]
- The 404 for a candidate that does not resolve. [39]

- **The registration that must precede the static mount and that takes all three ports.**  Anchor: "def register_review_routes(" [40]

- **The entry port type: the task context in, one typed entry result out — and, since `260921-ICR-L3`, the expansion port beside it.** [41]
- **The unwired-entry body: `unavailable` with the "not served rather than served empty" reason and next action.** [42]
- Review route registration precedes the static mount and accepts knowledge-review, entry-list and source-content ports. [43]
- **The entry port type: the task context in, one typed entry result out.** [44]

- The GET-only route handler over the injected port.  Anchor: "def api_review_intent(" [45]


- **The status mapping the routes inherit from the change-set routes; the signature accepts all three typed results and reads success as `refusal is None`.**  Anchor: "def _status_for(" [48]


- **The 400 a selector kind outside the admitted set gets, inside the comparison handler.**  Anchor: "def api_review_intent(" [50]



- **The 200/refusal split the entry handler makes: `entries` serves `200`, anything else goes through `_status_for`.**  Anchor: "def api_review_intent_entries(" [52]


- The registration that must precede the static mount.  Anchor: "def register_review_routes(" [53]

- The status mapper accepts the three review result types; success is refusal absence, with distinct unavailable and missing-subject/candidate refusals. [54]
- **The new owner: which exact Git objects a committed range binds, the three absence kinds, and the one absence that may degrade to empty.** [55]
- **The caller that owns the degradation policy and (260921-ICR-L25) carries the code half's named absence instead of raising it: the two sides resolve independently, and only an unrecorded memory half empties.** [56]
- **The doc-reader entry point that publishes the unrecorded state in the body.** [57]
- **The new owner: which exact commits a master net binds, the deterministic digest, same-call currentness, and the named refusal for a missing endpoint.** [59]
- **The thin delegating entry and the pinned file view, with the shared master 400/404 mapping.** [60]
- **The served vocabulary: the generation identity, the net's `generation` + `currentness` + `scope`, and the `committed`/`working` leaf-row state.** [61]
- **The nine cases that measure this route's half of the change, through real contracts, repos and routes.** [62]
- **The parser's two admitted shapes, and the refusals it keeps: a half-named selector and an unadmitted kind still return `None`.** [63]
- **The route's optional query parameters and the `400` body that now names the "omit both" option and reports whichever parameter was supplied.** [64]
- The status mapping and the serializer, unchanged by that leaf (the mapping serves a third result type since `260921-ICR-L3`). [65]
- **The composition the task-context answer reaches, which is where the complete inventory is measured.** [66]
- **The third route constant, GET-only, with the comment recording why it is a third path rather than a payload field: the inventory is the whole task's change set and a payload carrying every file's text would be a document dump.** [68]
- **The expansion's whole selector as one value: the task context, the entry path, and both camel-case tree ids, which travel together because any one alone selects nothing.** [69]
- **The parse that refuses a blank component rather than defaulting it — a defaulted tree id would make the server choose a generation.** [70]
- **The one-line route registration, and the module-level transport behind it: the unwired `503`, the incomplete-generation `400`, and the same two exception shapes the comparison handler uses.** [71]
- **The expansion route's own unwired answer: "not served rather than served as an empty file".** [72]

- **The third port type and the third collaborator field, with the reason it is a port rather than a payload field.** [73]

- **The status mapping widened to the third result type, where the expansion's refusal code reaches `400` through the same fall-through as `comparison_refused`.** [74]
- The `400` body for a query that did not name the generation whole, and the exact expected set it names. [75]

- **The composition root's third review port, whose docstring names the two facts the route rests on: the caller's generation rather than the server's choice, and no working tree or `HEAD` as a source of bytes.**  Anchor: `read_review_source_content` [77]

- **The application owner behind the port: the admitted paths (a changed path of a measured change set, or unchanged context a recorded realization of the same comparison links — decided by the admission owner), both bound trees read by object id, and the per-side states.** [78]
- **The cases that drive the new route through the real composition: an incomplete query refused by the transport, an unwired process refused by name, and an unmeasured generation that still confines the path to a measured change set.** [79]
- **The one mapping and the one body builder: the `400`/`404` idiom cannot differ between the two adapters.** [80]
- **The two actions the bodies gained, and where they are named.** [81]
- The expansion read's whole transport, whose docstring now states the shared mapping. [82]
- The published surface, unchanged: the three route constants, the three ports and the two parsers. [83]
- Current imported source owns this scoped route boundary. [84] [85] [86] [87] [88]
- The collaborator that stops the route's child computations. [89]
- The runtime receives the shutdown callable from the collaborators. [90]
- Serving shutdown calls it on a worker thread before the background tasks are cancelled. [91]

- The composition root composes one worklist process owner. [92]

- It supplies that owner's shutdown to the app. [93]
- The tree port passes the process owner to the application. [94]
- A live read reuses the record of the same trees, and pins before it writes a new record. [95]

- A busy default executor cannot delay a tree read. [97]
- A disconnect, the deadline, shutdown and a queued request each end with the children reaped. [98]
- Current imported source owns this scoped route boundary.   [86] [87] [88]
- The bounds of a selection and the size of the route's thread pool. [100]
- The value handed to the port, and whether it asks a focused question. [101]
- The one selection value and its refusals. [102]
- The port runs on the route's executor with cancellation and arrival bound; a disconnect and a cancellation set the event. [103]
- The route: its own executor, the unwired 503, the selection's 400 and the typed 200. [104]
- The start-only supervision the dashboard composes. [105]
- The install host part. [106]
- The host acquisition. [107]
- A numbered recorded comparison is looked up exactly; code/memory ranges use its recorded sides (converted memory base when present), and the list returns those four tree operands. [108] [109]
- App registers three intent handlers plus separate summary, tree and reader ports before static delivery. [110]
- Startup ordering, native held-message sweep registration, worklist-first shutdown, and awaited background teardown are explicit.  Anchor: `_serving_lifespan`, `_held_delivery_loop`, `_to_thread_owned` (delegating to accounted cancellation-drained offload) [111]
- Leaf-archive recovery alone uses the retained completion-relative background loop; no terminal-observation prime/poll remains. [112]

- Live pacing adds post-completion rest, so interval/heartbeat alone is not a total freshness bound.  Anchor: projection_completed; _next_deadline [113]


- Missing wheel exits degraded; watch establishment, retry and native-watch options are explicit.  Anchor: run; _watch_once [114]

- Tick cancellation drains filesystem work; state commits before subscriber notification. [115]
- Source content admits attributed unchanged context only with measured requested inventory. [120]
- Leaf range returns empty for missing repository before endpoint-owner admission. [121]
- Host ensure is start-only, with observation, lock, and outcome receipt. [128]
- A numbered recorded comparison is looked up exactly; code/memory ranges use its recorded sides (converted memory base when present), and the list returns those four tree operands. [109]

- **The cases that measure this route's half of the change: the recorded range bound and unmoved by a later commit, the state answered instead of a `HEAD` read with the route's own `200`, and the one-half degradation.** [58]
- **The case that admits exactly the two reviewable selector kinds and refuses every other spelling, and the case that drives the same route with no selector parameters at all.** [67]
- The registration call in the app factory, which passes all three collaborator ports and still precedes the greedy static mount.  Anchor: `register_review_routes` [76]
- Current imported source owns this scoped route boundary. [84]
- Current imported source owns this scoped route boundary. [85]

- Shared app composition binds real landing interest before startup. [129]
- Landing interest gates actual discovery and probe admission, while due policy retains exact identities. [130]
- Provider safety remains an independent periodic sequence. [131]

- Complete reconciled host input joins role-agent task identities only while its supervisor observation is armed. [132]
- Native cache values reuse only complete matching input generations; additional consumed inputs must have pre-read observations. [133]
- Pending cache results are retained only when fresh post-read input observations match their captured generation. [134]
- Full TaskSummary preparation has separate bounded retention and generation checks, not a second task-status producer. [135]
- Task-body 304 requires a still-current captured generation and matching content revision. [136]

- The transport still maps the literal legacy candidate_dataset_absent refusal code to404; a status mapping does not establish a currently produced dataset candidate path. [51]
- An enabled live leaf-wide tree read may start without a comparison number; focused card-entry reads require one. Absence of a number does not imply a dataset review. [96]
- The injected canonical memory-root port is carried from collaborators into the shared serving runtime, not resolved from arbitrary client roots. [138]
- The existing state stream opts into review-memory invalidations only through supplied review identity; no-selector streams retain their ordinary event path. [139]
- The connection-owned watcher filters generated/temporary paths, separates ready from coalesced changes, emits invalidation revisions rather than tree identities and drains its worker/merge ownership on closure. [140]

- The catalogue handler admits optional comparison, refuses negative values and forwards all four port arguments. [141]
- The summary handler forwards optional comparison and names a negative number as unavailable. [142]
- Summary ports and cache keys include exact optional comparison identity. [143]
- The summary reader keys retention by the numbered question and current age window. [144]
- The native recorded-answer cache returns predicate-rejected values without retaining them. [145]
- The catalogue handler forwards task context and its optional recorded comparison number; an unwired process still returns a named refusal rather than an empty list. [30]
