# mcp/src/agents_remember/serving/app.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Builds the dashboard's FastAPI app. `_build_serving_runtime` constructs the long-lived collaborators one
app owns, and `create_app` registers every route on an app whose lifespan runs the background loops. The
app has no authentication; the command line binds it to `127.0.0.1` by default.

## Code Commentary

### The runtime (`_build_serving_runtime`)

- The projector is built with the refreshers that the resolved live inputs enable: provider state, landing
  state and the change watcher.
- The terminal host, catalog and paster come from the supplied collaborators or are constructed.
- One serving clock (`replay.now` or the wall clock) is given to the liveness sweeper, the runtime and the
  observer-health publisher.
- The liveness sweeper is wired with the hosted-interaction synchronizer, the turn-state event logger and,
  when supplied, the terminal execution-evidence registrar.
- `_ServingRuntime` receives the build stamp (`process_serving_build()`, resolved once), the notifier
  heartbeat store, the observer-health publisher, the inbox evidence registrar, the projection interval,
  `capsule_launch`, and `review_trees_shutdown` copied from the collaborators. The lifespan reads that
  last field to stop the tree route's child computations when serving ends.
- The provider metrics store is returned beside the runtime.

### The app (`create_app`)

`create_app(config, cadence=..., replay=..., live_inputs=..., collaborators=...)` builds the runtime,
creates the app with `_serving_lifespan`, adds gzip compression at level 6, and registers, in this order:
the projection routes, the action routes, the terminal session and control routes, the files, changeset,
notes and requirements routes, the review routes (`knowledge_review`, `knowledge_review_entries`,
`review_source_content`), the review summary route, the tree view route (`review_trees`), the knowledge
reader route, the harness control routes, and the static mount last.

`OWNED_SERVING_COLLABORATORS` is an empty collaborator record: the app then constructs its own terminal
objects and every port-backed route refuses by name.

### Endpoints named by the module

`GET /api/state` returns the projection once. `GET /api/stream` is the state stream: a snapshot, then
deltas. `GET /api/events` tails the raw observer event log with byte-offset resume.
`POST /api/actions/<action>` is the gate return channel. `POST /api/operator-inbox` records a developer
response for an agent without a hosted session.

### Role Runtime and Scope

create_app invokes collaborators.extra_api_routes when supplied after built-in routes and before mount_static. Thus role launch routes coexist with MIK knowledge-reader/summary/tree routes and cannot be shadowed by the greedy asset mount. The factory adds no second launch route owner.

## Evidence

- The module docstring: the endpoints and the local-first posture. [17]
- The runtime: projector, terminal objects, one serving clock, and the fields copied from the collaborators. [13]
- The shutdown callable is copied from the collaborators onto the runtime. [14]
- The app: lifespan, compression, and the routes in their order with the static mount last. [15]
- The empty collaborator record. [16]

### Runtime Source References

- Frozen implementation of create_app supporting the stated file behavior. [12]
