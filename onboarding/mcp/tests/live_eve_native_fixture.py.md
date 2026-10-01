# mcp/tests/live_eve_native_fixture.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The live native fixture: **the real eve runtime driven by the real AR eve adapter, with nothing
doubled.** It starts the AR-owned eve application as a child process, points it at a deterministic
local model provider, and drives `EveSessionAdapter` through eve's production HTTP transport — health,
session create, follow-up, structured input response, turn cancel, the durable NDJSON stream, cursor
reconnect, reconciliation and a bridge restart.

It is the leaf's live-proof artifact: the unit suites prove the contract against a transport double,
and this file is what proves it against a real process, real HTTP and a real durable stream. It also
records **every request the adapter actually sent**, which is what turns "the wire carries the queued
policy" and "the cancel names the observed turn" from claims into artifacts.

Not pytest-collected: the filename does not match `test_*.py`. It is a standalone script run
explicitly, which is deliberate — it needs Node 24 and an installed dependency tree, so it must not
join the default suite.

## Code Commentary

### Logic

`LiveFixture` owns the child runtime, the fixture model provider process and the adapter under test;
`TracingEveRuntime` subclasses the production client to record every native event and every request it
sends. `ScenarioResult` carries one scenario's outcome and why. `_free_port` reserves a loopback port
per server, and `_await_turn` bounds the wait for a turn boundary.

Six scenarios, each a `_scenario_*` coroutine:

| Scenario | What it proves |
| --- | --- |
| `_scenario_protocol` | accepted submit → deltas → tool request → tool result → boundary, with the runtime's own file tool writing into the admitted worktree, and the create carrying `turnPolicy: "queue"` |
| `_scenario_reconnect` | a dropped stream reconnects from the persisted cursor with no duplicate transcript and no duplicate terminal notification, and the session stays usable — including that the **follow-up** also carries the queued policy |
| `_scenario_reconcile` | a lost submit response reconciles `accepted` from the durable record holding this exact message past the request's cursor, with exactly one native write, and the artifact records which evidence resolved it |
| `_scenario_cancel` | an exact observed turn is cancelled (`turn.cancelled` → `session.waiting`), the sent cancel body names that turn, and the same live session then accepts the next message |
| `_scenario_restart` | a restarted bridge attaches to the same durable id, and an unknown id is refused rather than replaced |
| `_scenario_concurrent` | two sessions with interleaved events keep separate transcripts, identities and pending sets |

**Two further scenarios were added by the capsule/workspace leaf**, because the capsule binding cannot be
proved by a unit double: it is applied by the shipped TypeScript inside the real runtime.

| Scenario | What it proves |
| --- | --- |
| `_scenario_capsule_binding` (1758) | **five claims read from one launch**, reported as one scenario: an admitted capsule reaches the model; a forged user message cannot move the binding; a missing or edited carrier stops execution; the write scopes are the admitted ones; and compaction/clear/resume leave the trusted block governing |
| `_scenario_capsule_execution` (1680) | the runtime's own file tools execute **inside the admitted worktree** and refuse a path outside every admitted surface |

`_capsule_world` (1172) builds the capsule world through the capsule seam's own support module, so the
fixture consumes the producer instead of re-deriving a carrier. `CapsuleRun` (1191) holds one admitted
capsule, its own model provider and the session the scenario works with.

`_observe_admitted_identity` (1394) is the observation that makes the forging claim falsifiable: it reads
the `<agents-remember-binding>` block out of the **first effective prompt** and records nine
`bindingBlockDeclares*` labels plus `bindingBlockFields`. `_binding_fields` (1358) returns an **ordered
tuple of `(key, value)` pairs, deliberately not a mapping** — a mapping silently collapses a repeated
key, and a block stating two conflicting roles would then be certified as declaring one. The three
declared rules (1420, 1431-1438) require every occurrence of an identity field to carry the admitted
value, so the guard is conflict-sensitive rather than order-sensitive.

`_observe_first_prompts` (1455) reads the provider's own view of the effective prompt, which is why
`eve_fixture_model.py`'s trace gained a `messages` key: the assertion is made against what a model would
actually receive, not against the plan the fixture wrote.

`run_real_provider_probe` / `_run_real_attempt` are a separate bounded probe: one native turn per
hosted provider, recording each provider's own refusal. The script exits non-zero when a scenario's own
assertion fails, and **exits `3` when no hosted provider completed** — a refusal is reported as a
refusal, never as a pass.

**A start failure is a blocked artifact, for every failure shape.** `START_FAILURES` covers the
adapter's own `HarnessControlError`, `TimeoutError`, `OSError`, `SubprocessError` and `RuntimeError`, so
an OS-level spawn failure is reported as `status: "blocked"` with the operator-facing reason and
`failureType` naming the exception class — never a raw traceback and never a fabricated scenario
artifact. `AR_EVE_NODE=/nonexistent/ar-eve-node-seed` is the seed that exercises it.

### Conventions

- Run from the repository root:
  `mcp/.venv/bin/python mcp/tests/live_eve_native_fixture.py --report-dir <dir>`; add `--real-model`
  for the hosted-provider probe.
- It writes one JSON artifact per scenario plus a transcript of every native event it observed.
- A run that cannot start reports that as a **blocked scenario with the exact reason** rather than a
  pass, and reports no scenario artifact for scenarios it never reached.
- Requirements are checked before anything starts: Node ≥ 24 (`PATH`, `$HOME/.nvm`, or `AR_EVE_NODE`),
  and an installed `eve_runtime/node_modules`.

### Invariants And Boundaries

- **Nothing here is doubled.** Using a fake transport or a fake adapter would make this file a slower
  copy of `test_eve_adapter.py` and would destroy its only value: independence from the deterministic
  double.
- **A blocked run is not a pass**, and a blocked run must not fabricate the artifacts of the scenarios
  it never ran. Covering every start-failure shape is what keeps that true for an OS-level failure and
  not only for the adapter's own error type.
- **Acceptance on a reconciled request is proved from the durable record, not from a delivery id.** A
  lost response never delivers the request's own id back to the adapter, so the scenario asserts the
  exact-message proof and reports the detail string it obtained.
- **This script is not in the default suite.** It requires Node 24 and an installed dependency tree, so
  it is run explicitly and its artifacts are the evidence, not a pytest exit code.
- The recorded limitations are honest and must stay visible: the hosted-model half is **unrun** in this
  environment for want of a credential (the probe reaches the providers and records their refusals), and
  the shipped reader is line-based and bounded because an unbounded chunked read was measured stalling
  against this server.
- It must not be "fixed" by pointing it at the deterministic stub — that would remove the live proof
  the requirement asks for.
- **The binding guard is conflict-sensitive, not order-sensitive, and that shape is load-bearing.**
  `_binding_fields` returns ordered pairs rather than a mapping precisely so a block stating two
  conflicting identity values is *detected*; a future edit that "simplifies" it back into a dict would
  silently restore the order-dependent hole the leaf's round-3 fix closed.
- **The guard inspects one binding block only.** `_binding_block` returns the **first** block, so a
  second complete block appended after the admitted one is invisible to all nine labels. This is
  recorded as residual assertion-completeness risk, not a live defect: `ar-binding.ts` is the only
  production emitter of the `<agents-remember-binding>` delimiters and emits exactly one block, so the
  shape is currently unreachable from shipped code. It was named as material for the final-verification
  leaf and is **not** a closed finding.

### Todos

The real-model half needs a hosted credential present in the environment; the adapter requires no
change for it.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; the scenario list is the task-local requirement packet's own acceptance list.

### Repo-Internal References

- The adapter under live test, driven through its real production transport. [1]
- The request bodies the scenarios assert against are the production builders, so a policy change breaks the live proof too. [2]
- The deterministic provider this fixture starts as the model backend. [3]
- The deterministic counterpart that proves the same contract without a process, and why both exist. [4]
- None [5]
- Node resolution and the runtime root the fixture relies on are the adapter's own launch module, and the interpreter override it seeds is read as given there. [6]
- The blocked-artifact contract covers every start-failure shape and records the failure class. [7]
- The capsule scenario and the observation that makes the forging claim falsifiable: nine labels read from the first effective prompt's binding block. [8]
- The guard's conflict-sensitivity lives in the parser's return type, so a repeated identity key is visible rather than collapsed. [9]
- The capsule world is built through the capsule seam's own support module, so the fixture consumes the producer instead of re-deriving a carrier. [10]
- The trace gained the provider's own `messages` view, which is what lets the assertion be made against the effective prompt rather than the plan the fixture wrote. [11]
- The shipped TypeScript the capsule scenarios actually observe, since no Python case can see it. [12]
- The unit-level counterpart of the same binding, which asserts the format and the launch-time verification without a process. [13]

### Cross-Repo References

- The runtime under test is the pinned published `eve` package and its Node engine requirement, not a sibling repository. [14]
