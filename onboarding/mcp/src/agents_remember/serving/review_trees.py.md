# mcp/src/agents_remember/serving/review_trees.py

## Governing Overview

[serving route overview](overview.md)

## Purpose

The HTTP transport of the reviewer's tree view, `GET /api/review/trees`. It checks the query, calls the
port that the composition root wires, and serializes the typed result once. It holds no review logic. It
also owns how the blocking port is run: on the route's own threads, with the request's cancellation and
arrival time bound to the call.

## Code Commentary

### The question

- The task context is `repo`, `master` and `leaf`, never a path. `comparison=<n>` names a recorded
  comparison and `history=recorded` the leaf's latest record.
- At most one focused question is allowed: `invariants=<id,id,...>` for the entries of those invariants,
  `lane=files` for the unexplained-changes lane, or `file=<path>` for one changed path's classification.
  Without one, the answer is the leaf-wide view.
- `ReviewTreesSelection.problem()` refuses a history other than `recorded`, a negative comparison number,
  more than `MAX_ENTRY_INVARIANTS` (500) names, a name longer than `MAX_INVARIANT_KEY_LENGTH` (64), a lane
  other than `files`, an empty file path or one longer than `MAX_FILE_PATH_LENGTH` (4096), and more than
  one focused question. A refused selection answers 400 with `status: invalid-request`.
- `ReviewTreesQuery` is the value handed to the port; `focused` is true when it asks one focused question.

### The answers

Every typed answer of the port is a 200 with the result dumped by alias and without `None` values:
`trees`, `not-converted` and `refused` (with the owner's refusal in the body). A process composed without
the port answers 503 with `status: unavailable`.

### Running the port

- `register_review_trees_route(app, port)` creates one `ThreadPoolExecutor` of `REVIEW_READ_THREADS` (16)
  threads named `review-trees` for the route, and shuts it down without waiting when the app object is
  collected. The handler is a coroutine; the blocking port never runs on the event loop and never on the
  loop's shared default executor, so background work that fills the default executor cannot delay a tree
  read. A read that waits for a worklist child holds one of the 16 threads for that time; reads beyond 16
  wait for a free thread.
- `_request_result` creates a cancellation event, enters `worklist_request(cancellation)` to bind the
  event and the arrival time, copies that context, and runs the port inside the copy on the executor. The
  worklist's 60 second deadline therefore runs from the request's arrival.
- While the port runs, the coroutine checks every 0.1 seconds whether the client has disconnected and
  sets the event when it has. When the coroutine itself is cancelled, it sets the event, waits for the
  worker to finish, and raises the cancellation again. A reviewer worklist computation that no request
  needs any more is thereby stopped and its child reaped before the request ends.
- Every tree request passes through this path, focused or leaf-wide; only the leaf-wide view of a live
  comparison starts a worklist computation.

## Evidence

- The module docstring: transport only, the query's meaning and the status codes. [8]
- The route path, the bounds of a selection and the size of the route's thread pool. [9]
- The query handed to the port. [10]
- The selection and the reasons it is refused. [11]
- The port runs on the route's executor inside the request's context; disconnect and cancellation set the event. [12]
- The route: own executor, 503 without a port, 400 for a refused selection, one serialized result. [13]
- The request context that binds cancellation and arrival. [14]
- A tree read answers in under a second while the default executor is full. [15]
- A client disconnect and a shutdown each stop the child and its Git process through the real route. [16]
- The deadline runs from the request's arrival, so work before the child spends it. [17]
- The route serves the port and refuses when it is not wired. [18]
