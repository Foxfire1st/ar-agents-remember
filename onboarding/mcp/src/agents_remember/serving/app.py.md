# mcp/src/agents_remember/serving/app.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Build the dashboard FastAPI application and the long-lived runtime it owns. App construction is distinct from CLI socket binding and from the individual route/lifespan owners. No authentication middleware is installed by this default composition; this is not a public/multi-user security boundary.

## Code Commentary

Typed409 refusal routes are registered before canvas routes, so first-match routing refuses old authoring while retained reads keep their owners; explainer routes are wired only through explicit collaborators.

`_build_serving_runtime` resolves live-input capabilities, creates one shared background ledger, optionally creates the landing refresher, and passes those collaborators to the Projector. When landing exists it binds interest to the actual Projector subscriber predicate before returning the runtime. The runtime carries the supplied clock, build stamp, cadence, child shutdown and the review_memory_root collaborator. Provider metrics storage is returned separately for the delegated lifespan owner.

`review_memory_root=collaborators.review_memory_root` supplies the runtime review-memory-root resolver. `usage_read=collaborators.usage_read` wires the runtime to the composition root's host-usage reader, so the serving tick's limit write reads the host's usage report through that reader rather than importing the bridge or adding a lifetime poll. The consumer is the projection route’s `api_stream`: it composes ordinary projection events with `multiplex_review_memory`, the optional review identity tuple and that root port. Identity/root admission and watch behavior belong to that consumer and its multiplexer, not to app construction; forwarding the port does not certify every supplied query or create a second worklist read.

`create_app` supplies the runtime/metrics lifespan, installs gzip and registers projection/action, files, changeset, notes, requirements, reviewer, summary, tree and knowledge-reader routes. The changeset cache returned by its registration is passed to the summary route. The optional extra-route callback runs before static mounting; static delivery is last. Missing-port refusals, action mutation rules and stream framing are route-owner contracts, not new decisions in this function.

 This current local composition account is not a new served-process, browser, background-loop or CODE/MEMORY acceptance measurement.


**L184 — NEW-LIMIT-FROM-REPORT-ONLY.** The app is the composition root, so the collaborators' wiring is realized here.

## Evidence

No domain documentation source is configured. Current repository source establishes these local claims.

- One runtime composition shares its ledger/landing interest and forwards actual supplied collaborators.
- The runtime receives review_memory_root beside the retained child-shutdown port.


- Lifespan/gzip, shared changeset cache, built-in and optional routes precede the static mount. [33]

- The stream consumer forwards the optional review identity and runtime root port into the multiplexer.

## Additional current composition details



### mcp/src/agents_remember/serving/app.py

#### Governing Overview

[Serving overview](overview.md)

#### Purpose

Builds the dashboard's FastAPI app. `_build_serving_runtime` constructs the long-lived collaborators one
app owns, and `create_app` registers every route on an app whose lifespan runs the background loops. The
app has no authentication; the command line binds it to `127.0.0.1` by default.

#### Current Runtime Composition

The app constructs one landing refresher with its shared background ledger, passes that exact instance to the Projector and binds its interest predicate to `Projector.has_subscribers` before any background loop starts. Only actual state-stream subscribers express landing interest; one-shot state reads and frontend signals do not. The live/sim input choice still controls whether the refresher exists. Provider safety sampling is a separate periodic lifespan owner and is not gated by page interest or launch authority.

Composition builds the projector with provider/landing/watch refreshers, the optional host reconciliation collaborator, runtime clock/build/shutdown port and metrics store. It registers projection/action, files, changeset, notes, requirements, review/summary/tree/knowledge and optional injected routes, then static assets. One changeset cache returned by route registration is shared with review summary. No terminal host, liveness sweeper, notifier, operator-inbox or harness-control registrar is constructed.

#### Code Commentary

`_build_serving_runtime` supplies `host_activity_reconcile` to `ProjectionRefreshers`; host intake remains event-driven and boot-reconciled rather than a periodic census. The existing landing refresher, actual-subscriber interest, shared background ledger and review-child shutdown remain their owners’ contracts. Provider safety sampling is independent of page interest.

`create_app` installs lifespan and gzip, registers built-in routes and optional `extra_api_routes` before static delivery. Empty collaborator capabilities refuse their own routes, not the entire app or an invented empty result. `/api/state` serves the projection; `/api/stream` sends task/key entity and taskCounts deltas; `/api/events` uses the raw workspace River’s virtual cursor. Ordinary action acknowledgement is not mutation or a gate decision. Runtime/build identity is shared within the process.

#### Evidence


##### Runtime Source References


##### Docs References

No Domain Documentation source is configured.

##### Repo-Internal References

- The route it registers.

##### Cross-Repo References

No cross-repository implementation dependency governs this file.

#### The Knowledge Reader Route Is Registered After The Tree View Route

After the review tree-related registrations, `create_app` calls `register_knowledge_reader_route(app,
collaborators.knowledge_reader)` (`serving/knowledge_reader.py`, MIK-R29) and registers the knowledge bytes route, still before `mount_static(app)`, so the
greedy static mount never shadows either route. A process composed without the port answers `GET /api/knowledge/reader/{view}`
with a named 503; with it, every typed answer is a 200 and `invalid-request` a 400. The route is GET-only.


#### The Tree View Route Is Registered After The Summary Route

Right after the summary route, `create_app` calls `register_review_trees_route(app, collaborators.review_trees)`
(`serving/review_trees.py`, MIK-R25), still before `mount_static(app)`. A process composed without the port answers
`GET /api/review/trees` with a named 503; with it, `trees`, `not-converted` and `refused` are each a 200.


#### The Changed-Intent Summary Route Is Registered Beside The Reviewer Family

Right after `register_review_routes(...)`, `create_app` calls
`register_review_summary_route(app, collaborators.review_intent_summary)` — the separate module
`serving/review_summary.py`, kept out of `serving/review.py` because that module is past the size rail. It
is still registered before `mount_static(app)`. A process composed without the port answers the route with
a named 503; with it, every typed summary state is a 200 (`ICR-R24@v3`).


#### Reviewer registration carries three ports

`create_app` registers the reviewer route family with **three** collaborator ports:

```python
register_review_routes(
    app,
    config,
    collaborators.knowledge_review,
    collaborators.knowledge_review_entries,
    collaborators.review_source_content,
)
```

The call passes `app`, `config` and three collaborator ports. The call joins the other route-family registrations
(`register_files_routes`, `register_changeset_routes`, `register_notes_routes`,
`register_requirements_routes`) and is made **before** `mount_static(app)`, so the static mount's
greedy catch-all cannot shadow any reviewer route. Every argument is a collaborator port — the route
family composes no adapter of its own — so a process that omits one refuses **that** route by name
rather than serving an empty surface, and the third port's absence is the entry-content route's own
named refusal, not an empty file.

#### Reviewer port capabilities

The call carries three collaborator ports. The ordering constraint, the no-adapter rule and the one-composition-root reading remain unchanged.

`create_app` registers the reviewer route family with three collaborator ports:



It joins the other route-family registrations (`register_files_routes`, `register_changeset_routes`,
`register_notes_routes`, `register_requirements_routes`) and is called **before**
`mount_static(app)`, so the static mount's greedy catch-all cannot shadow any reviewer route — the
same ordering constraint every route family in this function obeys. All three arguments are collaborator ports: the route family composes no adapter of its own, and an omitted port refuses its own route by name rather than serving an empty surface. This registration call is the
one place where the fact that the surface has three routes and one composition root is visible.

#### Reviewer registration ordering

 The ordering reason and
the no-adapter rule remain unchanged. The route family
(`register_files_routes`, `register_changeset_routes`, `register_notes_routes`,
`register_requirements_routes` and this one) is registered **before** `mount_static(app)` so the
static mount's greedy catch-all cannot shadow it, the port is the collaborator's rather than an
adapter composed here, and a process that supplies no `knowledge_review` collaborator is refused by
name rather than served an empty surface.

#### Requirements route registration

`create_app` now calls `register_requirements_routes(app, config)` right
after `register_notes_routes`, mounting the read-only task-local
`/api/requirements/{list,read}` surface before the greedy static mount. Route
handlers live in `serving/requirements.py`; composition here is one registration
call plus the import.

- The implementation of `create_app` composes the serving route families.

- The current `_build_serving_runtime` copies the collaborators' `review_trees_shutdown` callable onto the runtime.

- The app: lifespan, compression, and the routes in their order with the static mount last.
- The empty collaborator record.
- The module docstring: the endpoints and the local-first posture.
- The import and the registration after the tree view route, before the static mount.  Anchor: `register_knowledge_reader_route`
- The import and the registration after the summary route.  Anchor: `register_review_trees_route`
- The import and the registration after the reviewer family.  Anchor: `register_review_summary_route`
- App creation composes the serving route and lifespan families.
- **The reviewer route family is registered with all three collaborator ports, including the entry-content port.** Anchor: `register_review_routes`

- Current construction shares one landing instance, binds actual subscriber interest before startup and supplies the shared ledger.
- Retained route registration and optional collaborator routes precede static delivery; removed terminal/notifier collaborators are absent.



- `create_app` registers the canvas host and the presenter surface through `register_canvas_routes` after the API routes and before the static mount, then installs `RefuseCrossOriginWrites` and `RefuseForeignHosts`, so both surfaces sit behind the origin and host guards. \[35] [35]




- Typed409 refusal routes are registered before canvas routes, so first-match routing refuses old authoring while retained reads keep their owners; explainer routes are wired only through explicit collaborators. Anchor: `refuse_replaced_canvas_authoring` [36]
