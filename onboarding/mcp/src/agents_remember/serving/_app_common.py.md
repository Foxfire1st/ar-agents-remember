# mcp/src/agents_remember/serving/_app_common.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Shared pieces of the dashboard app that its route modules and its lifespan use: the collaborator record a
composition root fills (`ServingCollaborators`), the runtime bundle one app is built around
(`_ServingRuntime`), the request bodies of the terminal and operator-inbox routes, the event sequence of
the state stream, and the bridge between a terminal and a WebSocket.

## Code Commentary

### Collaborators and runtime

- `ServingCollaborators` is the one value a caller of `create_app` may supply. Every field is optional.
  For the terminal host, catalog, paster and the harness capability catalog, `None` makes the app
  construct the real object. For a port, `None` means the process cannot answer that route, and the route
  refuses by name instead of serving an empty answer.
- Its fields: `terminal_host`, `terminal_catalog`, `terminal_paster`, `harness_capability_catalog`; the two
  execution-evidence registrars `register_terminal_execution_evidence` and
  `register_inbox_execution_evidence`; the reviewer ports `knowledge_review`, `knowledge_review_entries`,
  `review_source_content`, `review_intent_summary` and `review_trees`; `review_trees_shutdown`;
  `knowledge_reader`; and `capsule_launch`.
- `review_trees_shutdown` is a callable without arguments that stops and reaps the tree route's transient
  child computations. The composition root that owns those computations supplies it, and the lifespan
  calls it when serving ends.
- The serving package ranks below the application package and may not import it. The ports are how
  application callables reach the routes.
- `_ServingRuntime` holds what one running app shares between its routes and its background loops: the
  configuration, the projector, the terminal host, catalog and paster, the liveness clock, configuration
  and sweeper, the build stamp, the notifier heartbeat store, the observer-health publisher, the inbox
  evidence registrar, the projection interval, `capsule_launch` and `review_trees_shutdown`.
  `observer_root` is the root of the durable control-plane stores.
- `LiveProjectionInputs` says which live inputs an app drives (provider state, landing state, change
  watching); an unset toggle is resolved against the replay seam, and a replay with a feeder turns it off.

### State stream

- `_ProjectionBodyCache` keeps the dumped body of the projection instance that is published, so every
  request and subscriber within one projector tick shares one dump.
- `_if_none_match_matches` is the weak comparison of an `If-None-Match` header with the projection
  revision.
- `stream_events` yields the server-sent events of one subscription: a `snapshot` with the full
  projection, then deltas. The snapshot carries the serving build, the notifier heartbeat and, when a
  record exists, the terminal observer health.

### Terminals and inbox

- `TerminalOpenRequest`, `TerminalAttachTaskRequest`, `TerminalRetireRequest`,
  `TerminalLandedCleanupRequest`, `TerminalRenameRequest` and `TerminalPasteRequest` are the bodies of the
  terminal routes. A terminal is opened by kind and harness ID; no command line travels on the wire.
- `OperatorInboxPostRequest` is the body of `POST /api/operator-inbox`.
- `_bridge_terminal` pumps between a terminal's file descriptor and a WebSocket until the child exits or
  the client disconnects. `_apply_terminal_input` accepts a `stdin` write or a `resize` and ignores every
  other frame. `_looks_like_image` checks the leading bytes of an uploaded image.

### Role Runtime and Scope

ServingCollaborators adds optional extra_api_routes callable owned by the composition root, registered before final static mount. This permits CLI/application adapters above serving to install launch routes while retaining the existing capsule/knowledge/reviewer collaborator ports and layer boundary.

## Evidence

- The collaborator record and its optional fields. [21]
- The shutdown callable of the tree route's child computations on the collaborator record. [13]
- The runtime bundle the routes and the loops share. [14]
- The live inputs and their resolution against the replay seam. [15]
- One dump of the projection per published instance. [16]
- The event sequence of one subscription. [17]
- The body that opens a terminal by kind and harness ID. [18]
- The pump between a terminal and a WebSocket. [19]
- The lifespan calls the shutdown callable when serving ends. [20]

### Runtime Source References

- Frozen implementation of ServingCollaborators supporting the stated file behavior. [12]
