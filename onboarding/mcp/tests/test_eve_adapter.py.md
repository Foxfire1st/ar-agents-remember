# mcp/tests/test_eve_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_eve_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `609756111eb3c239d0563d8631bfd564645bc9d1` |
| lastVerifiedCommitDate | 2026-09-16T10:25:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Native-adapter conformance for the eve session protocol: the six acceptance scenarios the requirement
names, each with a dedicated case class driving the **real** `EveSessionAdapter` and its real event
mapper through the same transport seam the production HTTP client implements. Only the eve *process*
is replaced.

## Code Commentary

### Logic

Two private helpers carry the suite: `_Pump` drives a subscription iterator and `_Harness` assembles
an adapter over a `FakeRuntimeFactory`. Ten case classes then hold the contract:

- `EveAdapterHandshakeTests` — start/handshake, protocol version, capabilities, and the finally-path
  that stops a partially started runtime.
- `EveAdapterCapabilityTests` — the advertised catalog's honest shape.
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

### Conventions

- The module inserts `mcp/src` on `sys.path`, matching the sibling-test convention.
- Cases run under `unittest.IsolatedAsyncioTestCase`; `_Pump` starts the subscription as a task so a
  case observes events rather than blocking on the iterator.
- Determinism is deliberate: the clock and the transport are injected, so a case never waits on real
  time or a real socket.

### Invariants And Boundaries

- **The double is a transport, not an adapter.** `FakeEveRuntime` implements `EveRuntimeTransport`, so
  the adapter, mapper, cursor arithmetic, replay guard and operation bookkeeping under test are all
  production code. A test that replaced the adapter instead would prove nothing about this contract.
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

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the scenarios are the requirement's own acceptance list, cited from the task-local packet. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter under test, its limits, id, reasoning vocabulary and event mapper. | `EveSessionAdapter`; `EveAdapterLimits`; `DEFAULT_EVE_ADAPTER_LIMITS`; `EVE_ADAPTER_ID`; `REASONING_EFFORTS` | mcp/src/agents_remember/serving/eve_adapter.py:82-143 |
| The deterministic transport double and its scripted turn builder. | `FakeEveRuntime`; `FakeRuntimeFactory`; `FakeTurn`; `FakeEveSession` | mcp/tests/eve_adapter_test_support.py:27-310 |
| The cancel observation the interrupt cases assert on is the recorded request pair, not fake state. | `FakeEveSession.cancel_requests`; `_current_turn_id` | mcp/tests/eve_adapter_test_support.py:41-60; mcp/tests/eve_adapter_test_support.py:301-316 |
| The AR control-wire and adapter-model types the cases assert against. | `LaunchSpec`; `ControlOperationRef`; `SubmissionReceipt`; `ReconciliationResult`; `InterruptResult`; `AdapterEvent`; `PromptRequest`; `InteractionResponse` | mcp/src/agents_remember/models/conversations/control_wire.py:1-200; mcp/src/agents_remember/serving/harness_control_models.py:1-260 |
| The wire-level cases one layer below this file, which now assert the outgoing request bodies. | `EveCursorTests`; `EveFrameTests`; `EveWireRequestTests` | mcp/tests/test_eve_protocol.py:195-253; mcp/tests/test_eve_protocol.py:140-194; mcp/tests/test_eve_protocol.py:382-526 |
| The live native proof of the same six scenarios. | `_scenario_protocol`; `_scenario_concurrent` | mcp/tests/live_eve_native_fixture.py:534-740; mcp/tests/live_eve_native_fixture.py:892-1010 |

## Cross-Repo References

No external repository boundary is implemented by this test.

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol being conformed to is the pinned published `eve` package's contract. | exact dependency pins | eve_runtime/package.json:14-20 |

## Update History

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): the round strengthened assertions
  rather than adding scenarios, and three of those strengthenings are recorded as contracts.
  `EveAdapterSubmissionTests`' full-protocol case now asserts its own premise, names a duplicated block
  in its failure message, and asserts the ordered assistant sequence (a seeded double-render and a
  seeded dropped block both fail it). `EveAdapterInterruptTests` assert the **request** that reached the
  runtime — via `FakeEveSession.cancel_requests`, which records `(session_id, turn_id)` — so a seeded
  "cancel never contacts the runtime" and a seeded wrong-turn cancel both fail.
  `EveAdapterReconcileTests` assert the detail names the durable-record proof rather than a delivery id.
  The "an assertion must be able to fail" boundary was added to the body, and all three citation tables
  were rewritten into the `Finding | Anchor | Source` shape. Verification metadata moves to the leaf's
  current base `e9300687`, with the governed closeout stamping the real code commit.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a test module added by the
  native eve session-adapter change set. Records the ten case classes mapped to the six named
  scenarios, and the boundary that matters most: the double replaces the transport, so the adapter and
  mapper under test remain production code. Verification metadata is pinned to the leaf's base commit
  `67b21aeb` because the candidate is deliberately uncommitted — the governed closeout stamps the real
  code commit, and no hash or fingerprint was invented here.
