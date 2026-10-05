# mcp/src/agents_remember/serving/app.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Provides the stable FastAPI composition facade and curated public imports for the serving package.

Composes the FastAPI app, existing route families and final static surface.

## Code Commentary

### Logic

`create_app` builds runtime collaborators, registers route families, installs the lifespan, and
returns the app. Terminal assignment exports now use `TerminalAttachTaskRequest` and
`_attach_task_response`; removed leaf-ref helpers are absent. Detailed routing behavior remains in
the private route modules. Serving runtime composition receives `process_serving_build()`, the same
cached process identity projected by MCP `server_info`.

### Conventions

This facade re-exports tested patch/import seams but does not reimplement their behavior.

### Role Runtime and Scope

create_app invokes collaborators.extra_api_routes when supplied after built-in routes and before mount_static. Thus role launch routes coexist with MIK knowledge-reader/summary/tree routes and cannot be shadowed by the greedy asset mount. The factory adds no second launch route owner.

## 260928-MIK-L29 The Knowledge Reader Route Is Registered After The Tree View Route

Right after the tree view route, `create_app` calls `register_knowledge_reader_route(app,
collaborators.knowledge_reader)` (`serving/knowledge_reader.py`, MIK-R29), still before `mount_static(app)`, so the
greedy static mount never shadows it. A process composed without the port answers `GET /api/knowledge/reader/{view}`
with a named 503; with it, every typed answer is a 200 and `invalid-request` a 400. The route is GET-only and the
existing routes are unchanged (the unconverted comparison served them byte-identically, base against worktree).

- The import and the registration after the tree view route, before the static mount. [1]
- The route it registers. [2]

## 260928-MIK-L25 The Tree View Route Is Registered After The Summary Route

Right after the summary route, `create_app` calls `register_review_trees_route(app, collaborators.review_trees)`
(`serving/review_trees.py`, MIK-R25), still before `mount_static(app)`. A process composed without the port answers
`GET /api/review/trees` with a named 503; with it, `trees`, `not-converted` and `refused` are each a 200.

- The import and the registration after the summary route. [3]

## 260921-ICR-L47 The Changed-Intent Summary Route Is Registered Beside The Reviewer Family

Right after `register_review_routes(...)`, `create_app` calls
`register_review_summary_route(app, collaborators.review_intent_summary)` — the separate module
`serving/review_summary.py`, kept out of `serving/review.py` because that module is past the size rail. It
is still registered before `mount_static(app)`. A process composed without the port answers the route with
a named 503; with it, every typed summary state is a 200 (`ICR-R24@v3`).

- The import and the registration after the reviewer family. [4]

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

### Invariants And Boundaries

- Public serving composition exposes task assignment, not leaf assignment.
- Startup migration is delegated to the lifespan.
- Route behavior stays in owned submodules.
- Dashboard and MCP surfaces must not resolve separate build identities inside one process.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- App creation composes the serving route and lifespan families. [5]
- One serving clock, and the observer-health publisher built on it and on the observer root, so the record's completion stamp and every age computed from it share one source. [6]
- The facade exports structural task-assignment names. [7]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

### Runtime Source References

- Frozen implementation of create_app supporting the stated file behavior. [12]

## 260821-CLIVE Serving Composition

App construction now threads the two task-execution registrars into their owning flows. Terminal
liveness receives `TerminalLivenessActions` containing turn-state observation plus the terminal
registrar; the notifier runtime receives the inbox registrar. Registration is deliberately outside
catalog/inbox deletion decisions and uses task-owned proof, while ordinary injected test seams that
omit registrars remain fail-closed.

## 260831-LOCR-L17 Observer-Health Composition

`_build_serving_runtime` resolves one `serving_clock` (`replay.now or utc_now`) and hands it to the
liveness sweeper, the runtime and the observer-health publisher, so a completion stamp and the age
computed from it cannot come from two clocks — a sim replay substitutes all three together. It also
constructs exactly one `TerminalObserverHealthPublisher(observer_root(config), serving_clock)` and
places it on `_ServingRuntime.observer_health`: that is the object the lifespan PUBLISHES this
serving lifetime's accumulator through, and the same object the read routes resolve the persisted row
through. One construction site therefore means the two halves of the reading cannot be wired to
different roots or different lifetimes. The publisher's store is opened under the same observer root
as every other durable control-plane store; no second endpoint, alias, history log or fallback store
is introduced, and nothing in this composition grants health any catalog, closeout, queue or
task-authoring authority.

## 260915-CAPS-L15 Capsule-Compiler Composition

`_build_serving_runtime` copies `collaborators.capsule_launch` onto
`_ServingRuntime.capsule_launch`. This file composes; it does not construct the compiler and does not
know what it is beyond the port type — the composition root (`cli/dashboard.py::serving_collaborators`)
binds the `application`-rank callable, because `serving` may not import that tier. The consequence is
deliberate: a dashboard app whose collaborator record omits the port still builds, and its launch route
then **refuses** a role-configured launch by name rather than opening a seat with no instructions.

- The one line that places the capsule-compiler port on the serving runtime. [8]
- **The reviewer route family registered with all three collaborator ports, the third one being this leaf's entry-content port.** [9]
- The composition root that binds the real compiler into the collaborator record every `create_app` call uses. [10]
- The gate whose behaviour the port's presence decides. [11]
