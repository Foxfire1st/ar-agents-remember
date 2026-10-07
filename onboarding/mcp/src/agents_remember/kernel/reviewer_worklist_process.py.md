# mcp/src/agents_remember/kernel/reviewer_worklist_process.py

## Governing Overview

[mcp package overview](../../../overview.md)

## Purpose

Starts, shares, bounds, stops and reaps the child processes that compute the reviewer's leaf-wide worklist,
and validates what a child returns. The module knows nothing about worklists beyond the shape of the answer:
the caller hands it a JSON payload and a build identity, and gets back the validated reply of a child that
ran the package's module `agents_remember.application.reviewer_worklist_child`. It keeps no cache and writes
nothing to disk; request and reply travel through pipes.

## Code Commentary

### Constants

- `MAX_ACTIVE_CHILDREN` is 2: the children that run at the same time.
- `MAX_WAITING_COMPUTATIONS` is 8: the computations that run or wait at the same time. Requests that share a
  computation are not counted.
- `DEADLINE_SECONDS` is 60: the whole request, that is, waiting, start, computation and collecting the
  answer, and also the work before the child when the caller bound the request's arrival.
- `CHILD_DEADLINE_SECONDS` is 65: the child's own alarm, five seconds past the parent's deadline.
- `EXIT_BUILD_MISMATCH` is 75: the exit status of a child that imported another build.
- `OPERATION` is `reviewer-worklist/v1`: the protocol name carried by request and reply.
- `PARENT_PID_ENV` is `AR_WORKLIST_PARENT_PID`: the environment name that tells the child its parent's
  process ID.

### Errors

Every failure is a `WorklistProcessError` with a `code` and a `next_action` that the reviewer's route turns
into a refusal. The base class has the code `candidate_unresolved` and the action "correct the named worklist
process failure, then reopen the review". `WorklistOverloaded` has the code `reviewer_busy` and the action
"the reviewer is computing other worklists; retry". `WorklistBuildMismatch` keeps the base code and asks to
restart the dashboard so that it serves the installed build.

### One request

- `worklist_request(cancellation)` binds the request's cancellation event and its arrival time to the
  calling context. The serving route enters it for every tree request, so the deadline runs from the arrival
  and the work before the child spends part of it.
- `build_identity(stamp)` keeps the fields `version`, `sourceDigest`, `pythonExecutable`, `packageRoot` and
  `commit` of a build stamp. The first four must be present; `commit` may be missing.
- `ReviewerWorklistProcesses.compute(payload, source)` builds the request (`operation`, `source`, `payload`
  and `request`, the SHA-256 of the three as compact sorted JSON), joins or starts the flight for that
  digest, waits for it and returns the validated reply. When a flight was shared, each of its requesters
  gets its own deep copy of the reply.
- `_environment(source)` refuses unless the identity's package root and interpreter are this process's own,
  and raises `WorklistBuildMismatch` when the child module file is missing from the package. The child's
  environment is the parent's plus `PYTHONPATH` set to the directory that holds the package and the parent's
  process ID.
- `_launch` starts `[sys.executable, "-P", "-m", CHILD_MODULE]` with three pipes and `start_new_session=True`.
  There is no shell, no script path and no other module. A failed start is a `WorklistProcessError`.

### Flights: sharing, queue and bound

A flight (`_Flight`) is one computation in progress. `_flights` maps a request digest to its flight from the
moment the flight is created until its thread has reaped the child.

- **Sharing.** A request whose digest has a flight joins it (`_join`) and waits for the same child. A flight
  whose cancel event is set is treated as absent: the new request starts its own flight, and the finishing
  thread of the cancelled one removes only its own registry entry.
- **Bound.** A request that would start a new flight while `_flights` already holds
  `MAX_WAITING_COMPUTATIONS` flights is refused at once with `WorklistOverloaded`. A request that joins an
  existing flight is never refused by this bound.
- **Queue.** Each flight's thread (`_fly`) enters a first-in-first-out queue (`_admit`) and starts its child
  when fewer than `MAX_ACTIVE_CHILDREN` children run and the flight is at the head of the queue. A flight
  that still waits when less than one second of its deadline is left is refused with `WorklistOverloaded`
  instead of being started. The flight's deadline runs from the arrival of the request that created it.
- **Waiting.** `_await` polls the flight every 0.05 seconds. It raises "computation was cancelled" when the
  owner is shutting down or the request's own cancellation event is set, and at the request's deadline it
  raises `WorklistOverloaded` if the flight never got a child and a plain deadline failure otherwise. A
  failed flight raises a new error of the same class for each requester.
- **Leaving.** `_leave` counts the requester out. When the last requester leaves an unfinished flight, the
  flight's cancel event is set, and `compute` waits up to five seconds for the flight to finish, so the
  request does not return before the child is reaped. A requester that leaves while others wait does not
  stop the child.

### Collecting and validating the reply

- `_collect` writes the request to the child and drains both pipes with `communicate` in slices of at most
  0.1 seconds, so a reply or an error stream larger than a pipe buffer cannot block the child. It stops when
  the owner shuts down, the flight is cancelled or the flight's deadline has passed. Exit status 75 raises
  `WorklistBuildMismatch`; any other non-zero status raises with the first 1,000 characters of the error
  stream. The size of a reply is not capped.
- `_reply` decodes the JSON and refuses a literal `NaN` or `Infinity` and a number that overflows to
  infinity. The reply must have exactly the keys `operation`, `request`, `source`, `module`, `pid`,
  `document`, `reads`, `computation` and `error`. The operation and the request digest must equal the
  request's. The source identity and the module path must equal the parent's own, otherwise the failure is a
  `WorklistBuildMismatch`. The process ID must be an integer other than the parent's, and `_fly` also
  requires it to be the ID of the process it started. `computation` must be two finite monotonic times in
  order and not in the future. Every row of `reads` must pass
  `agents_remember.kernel.recorded_reads.valid_observation`.
- `_validate_document` accepts an `error` only as a non-empty string with no document. A document must be a
  `knowledge-worklist/v1` object in state `complete` or `incomplete` with a `pairing` object and with
  `items` and `incomplete` as lists of objects. A `complete` document with no recorded read is refused.
- After the reply, and after every failure, `_fly` stops the child's process group (`_stop`: `SIGTERM`,
  half a second, then `SIGKILL`), closes the pipes, removes the process from the active set and wakes the
  queue.

### Lifetime of a child

- The child is the leader of its own session and process group, so `_stop` and the child's own handlers
  reach its Git children with one signal to the group.
- `shutdown()` marks the owner as stopped, wakes every waiter and stops every active child. Requests that
  arrive afterwards are refused.
- `arm_child_lifetime()` is called by the child before it reads its request. It routes `SIGTERM` and
  `SIGALRM` to `_kill_group`, arms a real-time alarm of `CHILD_DEADLINE_SECONDS`, and on Linux asks the
  kernel for `SIGTERM` when the parent dies (`prctl(PR_SET_PDEATHSIG)`); a failed `prctl` raises. On another
  platform a thread polls the parent's process ID once a second. If the parent recorded in the environment
  is not the child's parent any more when the function runs, the child ends at once.
- `_kill_group` sends `SIGKILL` to the child's whole group when the child leads its group, which ends the
  child as well. A child that leads no group, such as one started by hand from a shell, exits alone with
  status 1.

## Evidence

- The limits: two children, eight computations, sixty seconds, and the child's own deadline. [1]
- The base failure with its code and action. [2]
- The overload failure with its own code and action. [3]
- The build-mismatch failure asks for a dashboard restart. [4]
- The request context binds cancellation and arrival. [5]
- The build identity and its four required fields. [6]
- The child's environment: the parent's own package root and interpreter, or a refusal. [7]
- Stopping a child signals its whole process group. [8]
- The reply's protocol, identity, process, time and read checks. [9]
- The checks of the returned document and error. [10]
- One request: digest, join, wait, leave, and a copy for a sharer. [11]
- Joining: a cancelled flight is absent, and the bound applies only to a new flight. [12]
- Leaving: the last requester of an unfinished flight cancels it. [13]
- Waiting: cancellation, the request's deadline and the flight's error. [14]
- One thread per flight admits, runs, validates and always reaps. [15]
- The first-in-first-out wait for one of the two child slots. [16]
- The one command line of a child, in its own session. [17]
- Draining the pipes in slices, the deadline, and the exit statuses. [18]
- Shutdown stops every active child. [19]
- The deadline is overload while waiting and a failure once a child ran. [20]
- The child ends its whole group, or itself alone when it leads none. [21]
- The child's handlers, alarm, parent-death signal and parent check. [22]
- Four identical requests get one child; three other computations get one each, and at most two children run at once. [23]
- A ninth computation is refused while nine more requests share one of the eight. [24]
- Overload is raised at once past the bound and at the deadline for a flight without a child. [25]
- A leaving requester does not stop a shared child; the last one reaps it before returning. [26]
- A request that arrives while a cancelled flight is reaped starts its own computation. [27]
- A killed parent takes the child and its Git process with it. [28]
- The child's own alarm ends it and its Git process. [29]
- Malformed, truncated, misidentified and non-finite replies are refused and nothing is kept. [30]
