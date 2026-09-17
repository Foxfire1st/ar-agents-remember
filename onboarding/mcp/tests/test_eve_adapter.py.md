# mcp/tests/test_eve_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_eve_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:43+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l17-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
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
- Determinism is deliberate: the clock and the transport are injected, so a case never waits on real
  time or a real socket.

### Invariants And Boundaries

- **The double is a transport, not an adapter.** `FakeEveRuntime` implements `EveRuntimeTransport`, so
  the adapter, mapper, cursor arithmetic, replay guard and operation bookkeeping under test are all
  production code. A test that replaced the adapter instead would prove nothing about this contract.
- **No case may assert an advertised effort option.** The catalog offers none, and the capability case
  asserts the *absence* in three fields plus the `config_options` shape; a case that reinstates an
  effort-menu expectation is asserting a withdrawn claim.
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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the scenarios are the requirement's own acceptance list, cited from the task-local packet. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter under test, its limits, id, reasoning vocabulary and event mapper. | `EveSessionAdapter`; `EveAdapterLimits`; `DEFAULT_EVE_ADAPTER_LIMITS`; `EVE_ADAPTER_ID`; `REASONING_EFFORTS` | mcp/src/agents_remember/serving/eve_adapter.py:82-82; mcp/src/agents_remember/serving/eve_adapter.py:100-110; mcp/src/agents_remember/serving/eve_adapter.py:127-132; mcp/src/agents_remember/serving/eve_adapter.py:135-135; mcp/src/agents_remember/serving/eve_adapter.py:155-936 |
| The deterministic transport double and its scripted turn builder. | `FakeEveRuntime`; `FakeRuntimeFactory`; `FakeTurn`; `FakeEveSession` | mcp/tests/eve_adapter_test_support.py:26-37; mcp/tests/eve_adapter_test_support.py:40-77; mcp/tests/eve_adapter_test_support.py:80-286; mcp/tests/eve_adapter_test_support.py:289-298 |
| The cancel observation the interrupt cases assert on is the recorded request pair, not fake state. | `FakeEveSession.cancel_requests`; `_current_turn_id` | mcp/tests/eve_adapter_test_support.py:41-60; mcp/tests/eve_adapter_test_support.py:301-308 |
| The AR control-wire and adapter-model types the cases assert against. | `LaunchSpec`; `ControlOperationRef`; `SubmissionReceipt`; `ReconciliationResult`; `InterruptResult`; `AdapterEvent`; `PromptRequest`; `InteractionResponse` | mcp/src/agents_remember/models/conversations/control_wire.py:1-200; mcp/src/agents_remember/serving/harness_control_models.py:20-20; mcp/src/agents_remember/serving/harness_control_models.py:105-105; mcp/src/agents_remember/serving/harness_control_models.py:127-127; mcp/src/agents_remember/serving/harness_control_models.py:177-177 |
| The wire-level cases one layer below this file, which now assert the outgoing request bodies. | `EveCursorTests`; `EveFrameTests`; `EveWireRequestTests` | mcp/tests/test_eve_protocol.py:195-232; mcp/tests/test_eve_protocol.py:140-192; mcp/tests/test_eve_protocol.py:382-522 |
| The live native proof of the same six scenarios. | `_scenario_protocol`; `_scenario_concurrent` | mcp/tests/live_eve_native_fixture.py:572-622; mcp/tests/live_eve_native_fixture.py:892-1010 |
| The advertised catalog publishes a backed effort menu, and this suite's capability pair asserts the menu and the launch-only rule against the started runtime. | `EveAdapterCapabilityTests`; `test_advertise_reports_the_launch_selection_and_the_backed_effort_menu`; `test_the_effort_axis_is_launch_settable_and_never_live_settable`; `_capability_snapshot` | mcp/tests/test_eve_adapter.py:343-421; mcp/tests/test_eve_adapter.py:346-374; mcp/tests/test_eve_adapter.py:376-421; mcp/src/agents_remember/serving/eve_adapter.py:699-748 |
| The other half of the split: the launched application really applies the level, read at the provider boundary by the module that starts it per level. | `EveEffortConsumerTests` | mcp/tests/test_eve_effort_runtime.py:175-214 |

## Cross-Repo References

No external repository boundary is implemented by this test.

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol being conformed to is the pinned published `eve` package's contract. | exact dependency pins | eve_runtime/package.json:14-20 |
| The complete, verifiable launch binding the suite's launches now carry, built from a real worktree, commit and carrier rather than hand-written environment values. | `fixture_launch_binding` | mcp/tests/eve_adapter_test_support.py:407-436 |
| The launch-time verification that makes a partial binding unlaunchable, which is why the suite could not keep its fabricated cwd and two-variable environment. | `verify_capsule_binding` | mcp/src/agents_remember/serving/eve_runtime_launch.py:447-497 |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `fixture_launch_binding` repointed to mcp/tests/eve_adapter_test_support.py:407-436. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T10:32+02:00 — 260915-CAPS-L17 curator: **the capability case was rewritten again, so the
  body was corrected in place.** L8 had rewritten it to assert an *absence*
  (`…_and_no_unbacked_effort_menu`: `effort_options == ()`, `supports_effort` false,
  `default_effort` `None`, `config_options == ["model"]`, `REASONING_EFFORTS` not imported). This
  leaf's candidate gives the pinned application a real `AR_EVE_EFFORT` consumer, so that case was
  **replaced** by `test_advertise_reports_the_launch_selection_and_the_backed_effort_menu` (346),
  which asserts the axis is offered and that every option is launch-settable and not session-settable —
  and a second case was added,
  `test_the_effort_axis_is_launch_settable_and_never_live_settable` (376), pinning the launch/live
  split against the started runtime rather than from the menu. Recorded both in the case-class bullet,
  corrected the capability reference row (which still said the suite asserts the absence), anchored it
  at the candidate's real ranges and re-anchored the adapter row to the candidate's line numbers
  (`EVE_ADAPTER_ID` 82, `REASONING_EFFORTS` 100-110, `DEFAULT_EVE_ADAPTER_LIMITS` 135, the class
  155-936). **Checker result (post-sync, verbatim).** The refusal this entry first recorded was
  resolved by the leaf's `worktree_sync`: the pair is now `leaf-candidate` /
  `acceptanceEligible:true` on code base `d8ed8c21`, and the contract-scoped
  `memory_quality_check` ran against this worktree. Headline: `ok:false`,
  `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0
  unonboarded). This card's own contribution: one `onboarding_drift_drifted` finding and one
  `claim_reopen` error at `:139`. The latter is the **D11 uncommitted-candidate signature** as
  this master records it: the checker resolves citations against the code base commit, the
  anchored constructs (`EveSessionAdapter`, `REASONING_EFFORTS`) were changed by this leaf, and
  a generated citation repair from 2026-09-16 had already rewritten the row's ranges
  mechanically. This pass **re-anchored that row by hand** to the candidate's real boundaries
  rather than accepting the projection, and deliberately did **not** advance the verification
  stamp — stamping an uncommitted tree is forbidden, and the closing evidence is the
  post-closeout state of the same ranges. Verification metadata moves to the synced base
  `d8ed8c21`; the candidate is deliberately uncommitted, so the governed closeout stamps the
  real code commit and no hash or fingerprint was invented here.

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: **the suite gained a protocol pin and a named
  environment guard** (defect D19, repaired by this leaf). `EveRuntimeTransportFakeContractTests` (new,
  three cases) pins that the deterministic double implements `compact_session` and `clear_session`,
  which `EveRuntimeTransport` gained without the double following: the static half is a typed
  assignment the whole-tree pyright gate re-checks, the behavioural half covers what a type checker
  cannot see. The same change calls `require_installed_eve_application` at the `_started` funnel and at
  the three cases that start the launch directly, so the launch-dependent cases skip **by name** with
  the missing path and the exact install command instead of failing as a product defect; coverage of
  the reaches was proved per case in its own process, and the failure set that moved between schedules
  (the D20 staging fail-open) is now deterministic. Verification metadata moves to this leaf's synced
  base `8997e184`; the candidate is deliberately uncommitted, so the governed closeout stamps the real
  code commit and no hash or fingerprint was invented here.

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: **the suite's launches now carry a complete,
  verifiable capsule binding.** `_launch` previously hand-wrote `AR_WORKSPACE_ROOT` and
  `AR_BINDING_REF` with a fabricated `/tmp/ar-eve-workspace` cwd. That shape is no longer launchable:
  `resolve_runtime_spec` now verifies the declared carrier, its digest and the admitted git worktree
  before a process would exist, so a partial binding is refused before any protocol behaviour can be
  observed. `_launch` therefore takes `cwd` and its environment from
  `eve_adapter_test_support.fixture_launch_binding()`, which builds a real worktree, a real commit and a
  real carrier. This is a fixture-input correction rather than a behaviour change and the six
  acceptance-scenario classes are untouched — it is recorded because it is the coupling the unit suite
  now has to production launch admission, and because a future edit reintroducing a hand-written binding
  would fail at launch instead of in an assertion. Verification metadata moves to the leaf's synced base
  `23cc7a72`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.
- 2026-09-16T11:43:25+00:00: Generated citation repair: `EveSessionAdapter`; `EveAdapterLimits`; `DEFAULT_EVE_ADAPTER_LIMITS`; `EVE_ADAPTER_ID`; `REASONING_EFFORTS` repointed to mcp/src/agents_remember/serving/eve_adapter.py:144-865; mcp/src/agents_remember/serving/eve_adapter.py:115-121; mcp/src/agents_remember/serving/eve_adapter.py:124-124; mcp/src/agents_remember/serving/eve_adapter.py:81-81; mcp/src/agents_remember/serving/eve_adapter.py:90-98. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: the capability case was **rewritten to assert an
  absence**. `test_advertise_reports_the_launch_selection_and_the_documented_efforts` asserted that
  every `REASONING_EFFORTS` member appeared as a `launch_settable`/`session_settable` option — i.e. it
  pinned the unbacked effort menu. It is now
  `test_advertise_reports_the_launch_selection_and_no_unbacked_effort_menu`, asserting the catalog
  offers no effort option (`effort_options == ()`, `supports_effort` false, `default_effort` `None`)
  while still reporting `selected_effort` as configuration and carrying `config_options == ["model"]`;
  `REASONING_EFFORTS` is no longer imported here. Body updated on Logic and Invariants (a case that
  reinstates an effort-menu expectation would be asserting a withdrawn claim), and a reference row
  added. Verification metadata moves to the leaf's synced base `ff97072c`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.

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
