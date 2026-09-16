# mcp/tests/eve_adapter_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/eve_adapter_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T20:42+02:00 |
| lastVerifiedCommitHash | `8997e184efe67e853a60780912ef5ac21844a323` |
| lastVerifiedCommitDate | 2026-09-16T20:51:44+02:00|
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

## Cross-Repo References

No external repository boundary is implemented by this support module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
