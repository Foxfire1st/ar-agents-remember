# mcp/src/agents_remember/serving/app.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Builds the dashboard's FastAPI app. `_build_serving_runtime` constructs the long-lived collaborators one
app owns, and `create_app` registers every route on an app whose lifespan runs the background loops. The
app has no authentication; the command line binds it to `127.0.0.1` by default.

## Current Runtime Composition

The app constructs one landing refresher with its shared background ledger, passes that exact instance to the Projector and binds its interest predicate to `Projector.has_subscribers` before any background loop starts. Only actual state-stream subscribers express landing interest; one-shot state reads and frontend signals do not. The live/sim input choice still controls whether the refresher exists. Provider safety sampling is a separate periodic lifespan owner and is not gated by page interest or launch authority.

Composition builds the projector with provider/landing/watch refreshers, the optional host reconciliation collaborator, runtime clock/build/shutdown port and metrics store. It registers projection/action, files, changeset, notes, requirements, review/summary/tree/knowledge and optional injected routes, then static assets. One changeset cache returned by route registration is shared with review summary. No terminal host, liveness sweeper, notifier, operator-inbox or harness-control registrar is constructed.

## Code Commentary

`_build_serving_runtime` supplies `host_activity_reconcile` to `ProjectionRefreshers`; host intake remains event-driven and boot-reconciled rather than a periodic census. The existing landing refresher, actual-subscriber interest, shared background ledger and review-child shutdown remain their owners’ contracts. Provider safety sampling is independent of page interest.

`create_app` installs lifespan and gzip, registers built-in routes and optional `extra_api_routes` before static delivery. Empty collaborator capabilities refuse their own routes, not the entire app or an invented empty result. `/api/state` serves the projection; `/api/stream` sends task/key entity and taskCounts deltas; `/api/events` uses the raw workspace River’s virtual cursor. Ordinary action acknowledgement is not mutation or a gate decision. Runtime/build identity is shared within the process.

## Evidence


### Runtime Source References


### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The route it registers. [19]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260928-MIK-L29 The Knowledge Reader Route Is Registered After The Tree View Route

Right after the tree view route, `create_app` calls `register_knowledge_reader_route(app,
collaborators.knowledge_reader)` (`serving/knowledge_reader.py`, MIK-R29), still before `mount_static(app)`, so the
greedy static mount never shadows it. A process composed without the port answers `GET /api/knowledge/reader/{view}`
with a named 503; with it, every typed answer is a 200 and `invalid-request` a 400. The route is GET-only and the
existing routes are unchanged (the unconverted comparison served them byte-identically, base against worktree).


## 260928-MIK-L25 The Tree View Route Is Registered After The Summary Route

Right after the summary route, `create_app` calls `register_review_trees_route(app, collaborators.review_trees)`
(`serving/review_trees.py`, MIK-R25), still before `mount_static(app)`. A process composed without the port answers
`GET /api/review/trees` with a named 503; with it, `trees`, `not-converted` and `refused` are each a 200.


## 260921-ICR-L47 The Changed-Intent Summary Route Is Registered Beside The Reviewer Family

Right after `register_review_routes(...)`, `create_app` calls
`register_review_summary_route(app, collaborators.review_intent_summary)` — the separate module
`serving/review_summary.py`, kept out of `serving/review.py` because that module is past the size rail. It
is still registered before `mount_static(app)`. A process composed without the port answers the route with
a named 503; with it, every typed summary state is a 200 (`ICR-R24@v3`).


## 260921-ICR-L3 Reviewer Route Registration Carries All Three Ports

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

The call was one line and is now five; the fifth argument is the new one. It is the single line in this
module where the surface's *three* routes and one composition root are visible together, and it is the
only change this leaf makes here: the call still joins the other route-family registrations
(`register_files_routes`, `register_changeset_routes`, `register_notes_routes`,
`register_requirements_routes`) and is still made **before** `mount_static(app)`, so the static mount's
greedy catch-all cannot shadow any reviewer route. Every argument is a collaborator port — the route
family composes no adapter of its own — so a process that omits one refuses **that** route by name
rather than serving an empty surface, and the third port's absence is the entry-content route's own
named refusal, not an empty file.

## 260915-KS-L45 Reviewer Route Registration Carries Both Ports

**The count in this section is superseded: the call now carries three ports since 260921-ICR-L3** (see
the section above). The ordering constraint, the no-adapter rule and the one-composition-root reading it
records are still exactly right, so the entry is retained rather than rewritten.

`create_app` registers the reviewer route family with **both** collaborator ports:

```python
register_review_routes(
    app, config, collaborators.knowledge_review, collaborators.knowledge_review_entries
)
```

It joins the other route-family registrations (`register_files_routes`, `register_changeset_routes`,
`register_notes_routes`, `register_requirements_routes`) and is called **before**
`mount_static(app)`, so the static mount's greedy catch-all cannot shadow either reviewer route — the
same ordering constraint every route family in this function obeys. Both arguments are collaborator
ports: the route family composes no adapter of its own, and a process that supplies only one of them
refuses the *other* route by name rather than serving an empty surface. This registration call is the
one place where the fact that the surface has two routes and one composition root is visible.

## 260915-KS-L22 Reviewer Route Registration

`create_app` first registered the reviewer route family in the L22 increment, with the comparison port
alone. The section above supersedes it by passing the entry port beside it; the ordering reason and
the no-adapter rule this entry recorded are unchanged. It reads: the route family
(`register_files_routes`, `register_changeset_routes`, `register_notes_routes`,
`register_requirements_routes` and this one) is registered **before** `mount_static(app)` so the
static mount's greedy catch-all cannot shadow it, the port is the collaborator's rather than an
adapter composed here, and a process that supplies no `knowledge_review` collaborator is refused by
name rather than served an empty surface.

## 260831-CCR-L23 Requirements Route Registration

`create_app` now calls `register_requirements_routes(app, config)` right
after `register_notes_routes`, mounting the read-only task-local
`/api/requirements/{list,read}` surface before the greedy static mount. Route
handlers live in `serving/requirements.py`; composition here is one registration
call plus the import.

- Frozen implementation of create_app supporting the stated file behavior. [12]

- The current _build_serving_runtime copies the collaborators' review_trees_shutdown callable onto the runtime; this retained shutdown boundary also has a current owner, separate from the historical constructor accounts. [14]

- The app: lifespan, compression, and the routes in their order with the static mount last. [15]
- The empty collaborator record. [16]
- The module docstring: the endpoints and the local-first posture. [17]
- The import and the registration after the tree view route, before the static mount.  Anchor: `register_knowledge_reader_route` [18]
- The import and the registration after the summary route.  Anchor: `register_review_trees_route` [20]
- The import and the registration after the reviewer family.  Anchor: `register_review_summary_route` [21]
- App creation composes the serving route and lifespan families. [22]
- **The reviewer route family registered with all three collaborator ports, the third one being this leaf's entry-content port.**  Anchor: `register_review_routes` [26]

- Current construction shares one landing instance, binds actual subscriber interest before startup and supplies the shared ledger. [29]
- Retained route registration and optional collaborator routes precede static delivery; removed terminal/notifier collaborators are absent. [30]
