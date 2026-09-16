# mcp/tests/eve_adapter_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/eve_adapter_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| lastVerifiedCommitDate | 2026-09-16T22:28:15+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the modeled ordering is the pinned eve protocol's, mirrored from the production transport. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The seam this double implements is the production transport protocol, which is why the adapter stays under test. | `EveRuntimeTransport`; `EveRuntimeProcess.send_message`; `EveRuntimeProcess.stream` | mcp/src/agents_remember/serving/eve_runtime_client.py:62-89; mcp/src/agents_remember/serving/eve_runtime_client.py:170-238 |
| The cancel request this double records is the one the production client builds, including the target turn. | `cancel_turn_body`; `FakeEveSession.cancel_requests` | mcp/src/agents_remember/serving/eve_runtime_client.py:85-89; mcp/tests/eve_adapter_test_support.py:41-60 |
| Frame decoding is delegated to the production parser, not re-implemented here. | `parse_event_frame` | mcp/src/agents_remember/serving/eve_protocol.py:192-222 |
| The conformance suites that consume this double, one case class per named scenario. | `EveAdapterSubmissionTests`; `EveAdapterReconnectTests`; `EveAdapterReconcileTests`; `EveAdapterInterruptTests`; `EveAdapterIsolationTests` | mcp/tests/test_eve_adapter.py:371-1128 |
| The live native fixture is the non-deterministic counterpart and deliberately does **not** use this double. | `TracingEveRuntime` | mcp/tests/live_eve_native_fixture.py:123-170 |
| The capsule binding this double's launches now carry, built through the capsule seam's own fixture support rather than hand-written environment values. | `fixture_launch_binding`; `fixture_carrier_for`; `binding_env`; `repository_with_commit` | mcp/tests/eve_adapter_test_support.py:336-364; mcp/tests/eve_capsule_test_support.py:565-620 |
| The launch path that verifies the declared carrier before a process exists, which is why a partial binding would be refused before any protocol behaviour is observed. | `verify_capsule_binding` | mcp/src/agents_remember/serving/eve_runtime_launch.py:447-497 |
| The live native fixture is the only artifact that proves the *live runtime* half of the same seam; it drives a real eve process rather than this double. | `TracingEveRuntime`; `_scenario_capsule_binding` | mcp/tests/live_eve_native_fixture.py:123-170; mcp/tests/live_eve_native_fixture.py:1758-1813 |
| The two session-control members this double had to gain, declared by the production protocol. | `compact_session`; `clear_session` | mcp/src/agents_remember/serving/eve_runtime_client.py:62-89 |
| The cases that pin the two members statically and behaviourally, so a member that exists and does nothing also fails. | `EveRuntimeTransportFakeContractTests` | mcp/tests/test_eve_adapter.py |
| The named environment guard, its call sites, and the install it names. | `require_installed_eve_application`; `_started`; `_start_eve`; `_evidence_frames` | mcp/tests/eve_adapter_test_support.py:42-61; mcp/tests/test_eve_adapter.py; mcp/tests/test_eve_product_integration.py; eve_runtime/README.md:25 |

## Cross-Repo References

No external repository boundary is implemented by this support module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: **the double now implements the whole protocol, and
  the launch-dependent cases skip by name** (defect D19, repaired by this leaf). `compact_session` and
  `clear_session` were added because `EveRuntimeTransport` gained them and this fake did not, which made
  `FakeRuntimeFactory` unassignable at the seven rewired call sites and failed the whole-tree pyright
  gate; the fix is on the double, because the protocol is the shipped seam. Each mirrors the real
  route's documented difference — compaction *represents* the history, clear *removes* it while keeping
  the session identity — and the pair is pinned statically (pyright) and behaviourally
  (`EveRuntimeTransportFakeContractTests` in `test_eve_adapter.py`). `require_installed_eve_application`
  gives every case that starts the real runtime a **named** skip when `eve_runtime/node_modules` is
  absent, stating the missing path and the exact install command; coverage of the call sites was proved
  per case in its own process (40 guarded / 59 clean / 0 unguarded), and serial and three consecutive
  `-n=4` runs are now deterministic where the failure had moved between schedules. **Recorded, not
  repaired: D20.** `stage_runtime_root` stages before it checks the install, so a refused call leaves a
  half-staged destination the next call accepts — a production fail-open that is not this leaf's seam;
  that non-determinism is what the guard removes from the *test* side only. Verification metadata moves
  to this leaf's synced base `8997e184`; the candidate is deliberately uncommitted, so the governed
  closeout stamps the real code commit and no hash or fingerprint was invented here.

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: **the double's launches must now carry a real,
  verifiable capsule binding.** `fixture_launch_binding` was added because the launch path is no longer
  a pass-through: `resolve_runtime_spec` verifies the declared carrier, its digest and the admitted
  worktree before a process would exist, so a launch declaring half a binding is refused before any
  protocol behaviour can be observed. The fixture therefore builds a **real** git worktree with a real
  commit and a real carrier through the capsule seam's own support module, and returns the same four
  values a real launch carries; `test_eve_adapter.py`'s `_launch` now spreads that result into the
  launch environment and takes `cwd` from it, replacing the hand-written `AR_WORKSPACE_ROOT` /
  `AR_BINDING_REF` pair that could not have passed the verification. It is `lru_cache(maxsize=1)`
  because the work is real and the binding immutable. This is a genuine coupling worth recording: the
  transport is a double, but the launch path is production. Verification metadata moves to the leaf's
  synced base `23cc7a72`; the candidate is deliberately uncommitted, so the governed closeout stamps
  the real code commit and no hash or fingerprint was invented here.

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): the cancel control became a
  **request record**. `FakeEveSession.cancel_requests` now stores the `(session_id, turn_id)` pair
  rather than merely noting that a cancel occurred, which is what allows the interrupt cases to assert
  the exact turn that reached the runtime; before this round a seeded "cancel never contacts the
  runtime" and a seeded wrong-turn cancel both passed. The boundary "a recorded control must record the
  request, not a boolean" was added, `_current_turn_id` is now named, and all three citation tables were
  rewritten into the `Finding | Anchor | Source` shape. Verification metadata moves to the leaf's
  current base `e9300687`, with the governed closeout stamping the real code commit.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a support module added by the
  native eve session-adapter change set. Records that it is a transport double (not an adapter
  double), the two modeled behaviors that make the cursor assertions meaningful, the
  durable-write-before-response ordering the reconcile cases depend on, and the fact that pytest does
  not collect this filename. Verification metadata is pinned to the leaf's base commit `67b21aeb`
  because the candidate is deliberately uncommitted — the governed closeout stamps the real code
  commit, and no hash or fingerprint was invented here.
