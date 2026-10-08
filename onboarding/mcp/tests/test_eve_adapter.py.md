# mcp/tests/test_eve_adapter.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Native-adapter conformance for the eve session protocol: the six acceptance scenarios the requirement
names, each with a dedicated case class driving the **real** `EveSessionAdapter` and its real event
mapper through the same transport seam the production HTTP client implements. Only the eve *process*
is replaced.

## Code Commentary

### Logic

Two imported helpers from `eve_adapter_event_test_support.py` carry the suite: `_Pump` drives a subscription iterator and `_Harness` assembles
an adapter over a `FakeRuntimeFactory`. Ten case classes then hold the contract:

- `EveAdapterHandshakeTests` — start/handshake, protocol version, capabilities, and the finally-path
  that stops a partially started runtime.
- `EveAdapterCapabilityTests` — the advertised catalog's honest shape, and the launch/live split. The
  reported case is `test_advertise_reports_the_launch_selection_and_the_backed_effort_menu` (346): the
  catalog publishes the model the runtime compiles, **reports** the launch's effort as configuration
  (`selected_effort == "high"`), and offers the effort axis itself —
  `tuple(option.key for option in model.effort_options) == REASONING_EFFORTS`, `supports_effort` true,
  `default_effort == PROVIDER_DEFAULT_EFFORT`, every option `launch_settable` and **not**
  `session_settable`, and `config_options` carries exactly `["model", "effort"]` with the effort
  option's `current_value` the selection. The pinned application reads `AR_EVE_EFFORT` through eve's
  own `defineAgent({ reasoning })`, so the menu is a control the runtime honours rather than one whose
  every value produces the same run. Its sibling
  `test_the_effort_axis_is_launch_settable_and_never_live_settable` (376) pins the other half against
  the started runtime: `set_effort` refuses **every** candidate — including the ones this catalog
  advertises — with `acceptance == "unsupported"` and the requested value echoed as
  `requested_value`, while `effective_value` stays the model the session is actually running and
  `selected_effort` stays `"high"`. Neither side is read from the catalog's own menu.
- `EveAdapterSubmissionTests` — the full protocol fixture distinguishing acceptance from completion;
  an input request becoming a pending interaction and a response targeting it; free-text responses
  using the `text` field with unknown ids refused; preflight refusing while an input request is
  pending. The full-protocol case **asserts its own premise** (the scripted deltas reconstruct the
  finalized block), asserts that no assistant text appears twice — naming the duplicate in the failure
  message — and asserts the whole ordered assistant sequence.
- `EveAdapterQueuePolicyTests` — a follow-up is queued and does **not** cancel the active turn.
- `EveAdapterReconnectTests` — a dropped stream reconnects from the persisted cursor with no duplicate
  transcript and no duplicate completion.
- `EveAdapterReconcileTests` — a lost submit response reconciles `accepted`/`rejected`/`unresolved`
  from durable evidence without an automatic second write, and the detail names the durable-record
  proof rather than a delivery id.
- `EveAdapterInterruptTests` — cancel targets the exact observed turn **as a request**: the cases
  assert what reached the runtime, not the double's bookkeeping, including that a refused guard sends
  nothing at all and that a replay sends exactly one request. The same live session then accepts
  another message.
- `EveAdapterRestartTests` — a restarted bridge attaches to the existing durable session, and an
  unknown id is refused rather than replaced.
- `EveAdapterSessionCompletionTests` — session retirement is distinguished from a turn boundary.
- `EveAdapterIsolationTests` — two concurrent sessions with interleaved events keep separate
  transcripts, identities and pending sets.
- `EveRuntimeTransportFakeContractTests` (1142) — the double really implements the protocol it stands
  in for. `compact_session` and `clear_session` arrived on `EveRuntimeTransport` when eve's
  session-control routes landed and the double did not gain them, so every case handing it to
  `EveSessionAdapter` was a type error only pyright could see (D19). The typed
  `transport: EveRuntimeTransport = FakeEveRuntime()` assignment is the static half, re-checked by the
  whole-tree pyright gate; the behavioural half is what a type checker cannot see, because a member
  that exists and does nothing is a double that lies about the runtime it replaces — compaction must
  keep the history and record a summary, clear must drop it and keep the session identity, and both
  must refuse an unknown session.
- **Every case that starts the real launch calls `require_installed_eve_application` first** — one
  reach in the `_started` funnel (262) that 30 cases pass through, plus three cases that build the
  adapter and call `start`/`discover` directly (302, 315, 328). The transport is a double, but `start`
  is the real launch path and it stages the application; without the machine-local install the case
  **cannot run on this machine**, so it skips by name and states the missing path and the exact install
  command rather than failing as if the product were broken.

### Conventions

- The module inserts `mcp/src` on `sys.path`, matching the sibling-test convention.
- Cases run under `unittest.IsolatedAsyncioTestCase`; `_Pump` starts the subscription as a task so a
  case observes events rather than blocking on the iterator.
- The transport is injected and the event boundaries are observable. Shared real-time guards bound a hung fixture; no elapsed-speed assertion or short quiet window proves an event's absence. These cases use no real transport socket.

### Invariants And Boundaries

- **The double is a transport, not an adapter.** `FakeEveRuntime` implements `EveRuntimeTransport`, so
  the adapter, mapper, cursor arithmetic, replay guard and operation bookkeeping under test are all
  production code. A test that replaced the adapter instead would prove nothing about this contract.
- **The advertised effort menu is launch-only.** Capability cases assert the backed launch menu and its selected value; every live `set_effort` request remains unsupported and cannot change that selection.
- **An assertion must be able to fail.** A guard whose premise is never established (the deltas really
  reconstruct the block) or whose observation is the double's own bookkeeping (a cancel the fake
  records but never sends) is not evidence; both shapes were sealed findings against an earlier
  revision of this file.
- Each case asserts **both directions**: the behavior that must happen and the failure it would
  otherwise hide (a double-rendered block, a replayed durable event, a queued delivery cancelling
  active work, an acknowledgement without native terminal evidence, a repeated possibly-accepted
  write, or cross-session state mutation).
- These cases never start an eve process and never touch the network. The live native proof is
  `live_eve_native_fixture.py`'s scope, and neither substitutes for the other.
- A pending input request refuses further ordinary delivery until it is answered; that is asserted
  here rather than left to the adapter's own documentation.
- **A protocol member the double lacks is a failure of the double, and only a type checker will say
  so** until a case calls it. The contract class above exists because pyright's seven errors were the
  only trace of the gap; a member that exists but does nothing is caught by the behavioural half.
- **A machine-local dependency is named, not retried and not silently skipped.** The guard states what
  is missing and how to install it, so a fresh checkout reports `skipped` with a reason and a
  provisioned run executes the cases; nothing here installs the runtime, because a suite whose verdict
  depends on which machine ran it is the defect the guard removes.

### Todos

None known.

The event fixtures live in [eve_adapter_event_test_support.py](eve_adapter_event_test_support.py.md). Quiet-stream assertions call `_Harness.read_completed_pass` to witness exhaustion of the exact durable session/cursor pass before asserting no duplicate transcript or completion event.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; the scenarios are the requirement's own acceptance list, cited from the task-local packet.

### Repo-Internal References

- The adapter under test, its limits, id, reasoning vocabulary and event mapper. [1]
- The deterministic transport double and its scripted turn builder. [2]
- The cancel observation the interrupt cases assert on is the recorded request pair, not fake state. [3]
- The AR control-wire and adapter-model types the cases assert against. [4]
- The wire-level cases one layer below this file, which now assert the outgoing request bodies. [5]
- The live native proof of the same six scenarios. [6]
- The advertised catalog publishes a backed effort menu, and this suite's capability pair asserts the menu and the launch-only rule against the started runtime. [7]
- The other half of the split: the launched application really applies the level, read at the provider boundary by the module that starts it per level. [8]

### Cross-Repo References

No external repository boundary is implemented by this test.

- The protocol being conformed to is the pinned published `eve` package's contract. [9]
- The complete, verifiable launch binding the suite's launches now carry, built from a real worktree, commit and carrier rather than hand-written environment values. [10]
- The launch-time verification that makes a partial binding unlaunchable, which is why the suite could not keep its fabricated cwd and two-variable environment. [11]

- The event fixture owns the completed durable-record-pass witness. [12]
