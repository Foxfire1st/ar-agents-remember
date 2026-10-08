# mcp/tests/eve_adapter_test_support.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The deterministic eve runtime double for the native-adapter conformance suites. It is a **transport
double, not an adapter double**: it implements the same `EveRuntimeTransport` seam the real HTTP
client does, so every test drives the actual adapter, event mapper, cursor arithmetic and event
translation. Only the eve process and its socket are replaced.

Not pytest-collected: the filename does not match `test_*.py`, so pytest does not import it as a test
module. It is a support module imported by `test_eve_adapter.py` (and is asserted to be a stable
contract by the worker's promotion record, validated through that suite rather than by direct
collection).

## Code Commentary

### Logic

`FakeEveSession` holds one durable session's record plus the controls a test can observe: cancelled
turns, input responses, accepted messages and their delivery ids. **`cancel_requests` records the
request as the pair `(session_id, turn_id)`**, which is what lets a case assert that the cancel that
reached the runtime named the *right* turn — a control that recorded only "a cancel happened" cannot
distinguish a wrong-turn cancel from a correct one, and an earlier revision of this double was exactly
that. `emit` appends one event with the deterministic envelope id the fixture would mint for it.

`FakeEveRuntime` implements the transport seam. Two behaviors are **deliberately modeled rather than
simplified**, because they are what make the cursor and reconnect assertions meaningful:

- the stream is served from a durable per-session record addressed by an absolute index;
- every read ends when the record's current tail is reached, exactly like a bounded catch-up read, so
  a test must reconnect to see more.

Test controls: `turn_events` appends one complete, well-formed eve turn in the documented order
(`turn.started` → deltas → completions → actions → results → requests → `turn.completed` → boundary);
`complete_requested_input` appends the `input.resolved` batch eve writes once a response is accepted;
`last_event_index` and `truncate_record` arm a "lost response" by dropping the durable tail past an
index; the injectable error attributes (`create_error`, `send_error`, `response_error`,
`cancel_error`, `stream_refusals`, `cancel_status`) let a case choose the failure under test.

`_next_delivery` models the ordering that makes reconciliation possible: **eve writes the durable
acceptance marker as part of accepting the message, not as part of the caller's response**, and stamps
the envelope with the delivery id. `send_message` therefore performs the durable write *before*
honoring `send_error`, which is exactly the ambiguous case reconciliation must answer from evidence.

`FakeRuntimeFactory` hands out one runtime per launch and records every spec it was asked for, so a
case can assert what the adapter resolved. `_current_turn_id` exposes the turn a session currently has
open, so a case can state the expected cancel target independently of the adapter's own bookkeeping.

**`compact_session` (206) and `clear_session` (223) complete the protocol the double stands in for.**
`EveRuntimeTransport` gained both when eve's session-control routes landed; the double did not, so it
was no longer assignable to `RuntimeFactory` at the seven call sites that were rewired, and the
whole-tree pyright gate failed on the tree (defect D19). They are implemented **on the double** rather
than narrowed at the injection point, because the protocol is the shipped seam and a double that cannot
stand in for it is the thing that is wrong. Each records the call on the runtime and mirrors the real
route's documented difference: `compact_session` **represents** the history (a summary appended to
`FakeEveSession.compactions`, `session.compacted` emitted, `{ok, sessionId, summary}` returned) while
`clear_session` **removes** it (messages and delivery ids dropped, `session.cleared` emitted,
`{ok, sessionId, removed}` returned) and both keep the session identity. Both refuse an unknown session
through the double's own `_require_session` and both take injectable errors (`compact_error`,
`clear_error`) like every other route here. The static half is re-checked by the whole-tree pyright
gate; the behavioural half is pinned by `EveRuntimeTransportFakeContractTests` in `test_eve_adapter.py`,
so a member that exists and does nothing now fails too.

**`require_installed_eve_application` (42) is a named environment guard, not a retry and not a
silent skip.** A case that starts the real runtime stages a per-epoch application directory whose
`node_modules` is a link to `eve_runtime/node_modules`, which is a machine-local install
(`eve_runtime/README.md:25`) absent in every checkout on this machine: without it the launch refuses
by design, so such a case **cannot run here** rather than failing. The guard skips by name, stating the
missing path (`EVE_APPLICATION_ROOT`, 35), that the case starts the real runtime, and the exact
one-command install (`EVE_INSTALL_COMMAND`, 38), so a fresh checkout reports `skipped` with a reason
and a provisioned run still executes the cases. Nothing here installs the runtime: a suite whose
verdict depends on which machine ran it is the defect the guard exists to remove.

`fixture_launch_binding` (336) is the one piece of production-shaped state this double needs. The
transport is a double, but **the launch path is the real one**: `resolve_runtime_spec` now verifies the
declared carrier, its digest and the admitted worktree before a process would exist, so a launch that
declared half a binding would be refused before any protocol behaviour could be observed. It therefore
builds a real git worktree with a real commit and a real carrier through the capsule seam's own support
module, and returns the same four values a real launch carries. It is `lru_cache(maxsize=1)` because the
work is real and the binding is immutable; `test_eve_adapter.py`'s `_launch` spreads its result into the
launch environment and takes `cwd` from it, so the fixture cannot drift from what the launch path
verifies.

**`RecordedModelRequest` (440) and `serve_recording_provider` (467) are the provider boundary this
module now supplies.** `260915-CAPS-L17` needed to read the **request body a direct provider received**
— that body *is* the value the effort axis is measured by — and the product's deterministic fixture
model cannot serve: it answers a scripted plan and traces a **normalized projection** of the request,
and a projection is exactly what must not be trusted when the body is the field under test. So this is
a real recording HTTP server (a direct OpenAI-compatible endpoint) that keeps each body verbatim,
exposing it both as `body` and through `reasoning_effort` (which collapses "absent" to `None` for
readable assertions, so a case that must distinguish *not sent* from *sent as null* asks
`"reasoning_effort" in body` directly) and `top_level_keys()`.

`drop_reasoning_effort` is the **instrument's** way to model a boundary that loses the value: the key
is removed from the request the provider *receives*, in `do_POST` **before** the body is recorded and
before it answers, so the recorded bytes and the answer describe a request that never carried it. That
placement is the point — substituting the absence inside an assertion would prove nothing about the
boundary, which is defect `L17-5`'s lesson and the reason the flag lives here rather than in a case.

`staged_runtime_root` (580) assembles the one application root that keeps the bytes under test the
checkout's own: `agent` is a **symlink to the authored directory** (so a case compiles what the
repository ships, recorded edits and all, rather than a reduced application written for the case),
`node_modules` links to the machine-local install the production stager requires, and the three
lockfile/tsconfig files are copied. Nothing is installed and nothing is copied into the worktree.

### Conventions

- The record is decoded through the production frame parser (`parse_event_frame`), so a fixture that
  emits a malformed frame fails the same way a real server response would.
- `FakeTurn` declares a scripted turn as data (deltas, message, reasoning, actions, results, requests,
  boundary) rather than as a sequence of emit calls per case.
- `_boundary_data` supplies the documented payload for `session.waiting` and `session.failed`.

### Invariants And Boundaries

- **This file must not become an adapter double.** Its value is that the adapter and mapper stay
  production code under test; replacing them here would make every case in `test_eve_adapter.py`
  vacuous.
- **A recorded control must record the request, not a boolean.** The cancel observation carries the
  session and turn ids, because a guard that only proves "something was called" cannot fail when the
  adapter cancels the wrong turn.
- The durable-write-before-response ordering in `send_message` is load-bearing for the reconcile
  cases. Reordering it would silently make "lost response" tests pass for the wrong reason.
- The per-read tail bound is intentional: removing it would let a case observe events it never
  reconnected for, defeating the cursor assertions.
- The unknown-session refusal message here mirrors the production client's session-not-active refusal,
  so a case can assert that no replacement session is created.
- **A member the protocol declares and this double does not implement is a defect in the double, not a
  narrowing opportunity at the call site.** That is D19's lesson: the protocol is the shipped seam, the
  fake that cannot stand in for it is what is wrong, and a type-level failure was the only trace until
  whole-tree pyright ran.
- **A boundary that loses a value must lose it in the instrument, not in the assertion.** When the
  field under test is a request body, the recorded bytes are the evidence: `drop_reasoning_effort`
  removes the key from the request the provider *receives*, before recording and before answering.
  Replacing this with an assertion-side substitution (or with a case that simply asserts what the
  fixture model reports) would make the falsifiability seed vacuous.
- **The bytes measured must be the repository's own.** `staged_runtime_root` links `agent` to the
  authored tree rather than copying or reducing it, so a case that measures the launched application
  measures what this repository ships. A copied or hand-written application root would let a
  measurement pass against something the repository does not contain.
- **An environment-dependent case skips by name, never silently and never by retry.** The guard states
  the missing path and the exact install command; a bare skip would let a fresh checkout claim coverage
  it never ran, and a bare failure reads as a product defect instead of a missing machine-local install.
  The guard does **not** repair the launch path it works around: `stage_runtime_root` copies the
  application surface into the destination *before* it checks for the install, so a first refusing call
  leaves a half-staged destination that a second call accepts — a fail-open in production, recorded as
  **D20** and routed to the wiring leaf that owns `serving/eve_runtime_launch.py`. **The staging order
  is reported, not fixed**, and this guard only makes the test side honest in the meantime.

### Todos

None known.

## Resource And Opportunity Ownership

`FakeEveRuntime.stream_passes` records a stream pass only after the durable tail has been consumed;
subscriber assertions can wait for a completed producer opportunity rather than elapsed silence.

`IsolatedEveRuntimeProcess` is a test-only owner for the observed bind/close race. It retries only an
actual EADDRINUSE/address-in-use failure, first stops the failed child, then selects another private
port within one shared hang-guard window. Other startup errors propagate after cleanup; cancellation
and unexpected failures force-stop the owned child/client/stderr reader before propagation and never
trigger a port retry. This does not change the product transport or relax its errors.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; the modeled ordering is the pinned eve protocol's, mirrored from the production transport.

### Repo-Internal References

- The seam this double implements is the production transport protocol, which is why the adapter stays under test. [1]
- The cancel request this double records is the one the production client builds, including the target turn. [2]
- Frame decoding is delegated to the production parser, not re-implemented here. [3]
- The conformance suites that consume this double, one case class per named scenario. [4]
- The live native fixture is the non-deterministic counterpart and deliberately does **not** use this double. [5]
- The capsule binding this double's launches now carry, built through the capsule seam's own fixture support rather than hand-written environment values. [6]
- The launch path that verifies the declared carrier before a process exists, which is why a partial binding would be refused before any protocol behaviour is observed. [7]
- The live native fixture is the only artifact that proves the *live runtime* half of the same seam; it drives a real eve process rather than this double. [8]
- None [9]
- The cases that pin the two members statically and behaviourally, so a member that exists and does nothing also fails. [10]
- The named environment guard, its call sites, and the install it names. The two suites were cited as **bare paths** until this pass, so the three anchors could not resolve; they now carry the real ranges. [11]
- The recording provider boundary this module gained: the raw request body kept verbatim, and the instrument's own drop that models a boundary losing the value. [12]
- The application root the bytes under test come from, and the machine-local install it links to. [13]
- The cases that consume the recording boundary and the staged root, one application root and one process per level. [14]

- A completed stream pass records its exact session and consumed tail. [15]
- Collision-only retries and failed/cancelled-start cleanup share one test-owned resource owner. [16]

### Cross-Repo References

No external repository boundary is implemented by this support module.

No meaningful cross-repo references found.
