# mcp/src/agents_remember/serving/eve_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/eve_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| lastVerifiedCommitDate | 2026-09-16T13:48:06+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The native eve protocol adapter: AR's existing session contract implemented over eve's durable session
API. `EveSessionAdapter` owns exactly one AR-owned eve application process and one durable eve session
per bridge epoch, and derives readiness, acceptance and terminal state from the protocol rather than
from a pane, a log line or a successful process spawn.

It is one of the registered built-in protocol harnesses and the only one whose native process is an
AR-owned application rather than a `PATH` command. It also implements the optional interrupt
capability (`interrupt`), so it participates in the existing structural interrupt port.

## Code Commentary

### Logic

The module docstring states the three load-bearing properties; the code below enforces them.

**Cursor, not event id, is the resume position.** `_translate` advances `self._cursor` to
`max(cursor, event.index + 1)` for every event — replayed or not — and `_is_replay` drops a duplicate
envelope id while still advancing the cursor past it. Records without an envelope id fall back to a
contiguous high-water mark, because that is the only replay proof a pre-version-20 record supports.
`_is_replay` holds no window of its own: the adapter owns **one** `EveEventDeduplicator` instance
(`eve_protocol.EveEventDeduplicator`, bounded by `EVE_REPLAY_WINDOW`) and delegates, so the documented
component is the one under test and there is no second copy of the bound to drift.

**Acceptance is not completion.** `submit` opens a `_SubmissionEvidence` row before the write, then
classifies the outcome: `accepted` from eve's durable delivery id, `rejected` from a typed refusal
before any write, `unknown` when the transport failed and the write may have landed. The receipt
reports *acceptance* and says so ("turn completion is reported on the stream"). `reconcile` answers
`accepted` / `rejected` / `unresolved` from durable evidence and **never repeats a possibly accepted
write**; `_read_from_cursor` bounds the scan at `_RECONCILE_READ_LIMIT` (4096) and a scan that reaches
the bound reports `unresolved` rather than guessing.

`_proves_delivery` proves acceptance the only way a *reconciled* request can be proved: the durable
record must hold the exact accepted message verbatim past that request's cursor. A lost response never
delivers the request's own delivery id back to the adapter, so the delivery-id comparison is **not**
part of this proof — the branch that tested it was deleted rather than kept as a claim no evidence can
exercise, and `reconcile`'s detail string now states exactly what it checked.

**Ordinary deliveries queue.** `turnPolicy: "queue"` is spelled by the wire module's single
`TURN_POLICY_QUEUE` constant on every create *and* every follow-up, so AR never inherits eve's
cancellation-backed `steer` on either turn shape. `preflight_operation` captures fresh idle protocol
evidence while the authority still owns the queue row, and `_claim_prepared_operation` returns a
`guard()` that re-checks the operation, the transport generation and the activity token immediately
before the write — so a state change between preflight and write fails closed with
`HarnessAdapterBusyError` rather than writing into a changed world.

`interrupt` is turn-addressed to the **observed** turn id: the adapter sends the turn it actually saw
on the stream, never a caller-supplied guess. Guard order is fixed and names both inputs: the caller's
turn identity is checked first (it addresses native work), then the AR operation identity. A repeat
naming the same `(turn, operation)` pair replays the first acknowledgement with **no second native
write**. eve's cancel is cooperative, so the acknowledgement reports `accepted` only and settlement is
reported later by the turn boundary on the stream.

`set_model` and `set_effort` report `unsupported` and name the one path that really changes them — a
rotated runtime — because eve's model and effort are compiled application values. `set_effort` also
validates against `REASONING_EFFORTS` and, when the requested effort was refused, reports the model the
session is actually running as the effective value rather than echoing the refused request.

**The effort axis is RETIRED from the catalog, and `REASONING_EFFORTS` is not a menu.**
`_capability_snapshot` publishes `supports_effort=False`, `effort_options=()`, `default_effort=None`;
`EffortOption` is no longer imported at all. The reason is measured rather than asserted: the pinned
application reads **no** effort value — there is no `AR_EVE_EFFORT` consumer under `eve_runtime/agent`
— so an effort menu would advertise a control whose every value produces the same run. The selection
is still **reported** (`selected_effort`) because the configuration a session was started under is a
fact, not a menu. `REASONING_EFFORTS` therefore survives as a **launch-validation vocabulary only**:
a settings-owned selection naming an undocumented level is refused at launch instead of being passed
through as if it meant something, while a launch naming a documented level still runs identically.
The distinction to keep straight when reading this module: *validation of a launch* is not
*advertisement of a control*.

`_event_stream` reconnects from the persisted index whenever the reader closes: a closed reader is not
a dead session, and reconnecting is what tells a live-but-parked session apart from a finished one.
`stop` terminates only the process this adapter started and never deletes a durable eve session.
`attach_durable_session` is the restart path: the epoch resumes the session it already proved instead
of creating a replacement.

### Conventions

- `EVE_ADAPTER_ID = "eve-session"` is the adapter id reported at handshake.
- `EveAdapterLimits` bounds retained submissions (256), pending interactions (64) and the cold
  discovery health budget (120 s); all three are validated positive at construction.
- `_evict_submission` drops only the oldest **settled** row and raises when every retained row is
  still pending, so live evidence is never discarded to make room.
- Launch-environment resolution reads the environment **as given**, so `AR_EVE_RUNTIME_ROOT` and
  `AR_EVE_NODE` genuinely select the application root and the interpreter; `_runtime_env` then strips
  both selectors from what the child inherits, so a staged epoch cannot re-resolve itself elsewhere.
- `raw` on snapshots carries `streamCursor` and `observedTurnId`; the handshake raw carries the
  runtime endpoint, root, node executable and a null `sessionId` until one is bound.

### Invariants And Boundaries

- **One epoch, one process, one durable session.** A session identity change inside one epoch raises.
- **A durable id is never replaced.** An unknown or terminal session id is refused; no replacement
  session is created, and an unknown durable id during restart fails rather than silently rebinding.
- **Acceptance is never inferred** from a pane, silence or a successful spawn, and a possibly accepted
  write is never repeated.
- **Eve's `meta.id` is not a cursor.** See the cursor rule above.
- **The replay window has exactly one implementation.** `EveEventDeduplicator` owns the bound; an
  inline second copy in this module is a regression, not a local optimization.
- **The adapter carries a capsule binding; it does not compile or select a capsule.**
  `AR_BINDING_REF` / `AR_CAPSULE_DIGEST` / `AR_WORKSPACE_ROOT` are transported to the runtime, which
  applies them before the first model call. Capsule compilation, selection and worktree admission are
  other leaves' scope.
- **No asset submission.** `submit` refuses an asset-carrying payload rather than dropping the assets.
- **No effort option is advertised.** `_capability_snapshot` must keep `supports_effort=False`,
  `effort_options=()` and `default_effort=None`. Publishing a menu would claim a control the pinned
  runtime does not read; `REASONING_EFFORTS` may not be reused as a catalog source. The one writer that
  may name an effort is a settings-owned launch selection, and it is validated, not advertised.
- **No second orchestration registry.** Session identity and stream cursor are published on the
  existing `AdapterSnapshot` (`vendor_session_id`, `raw["streamCursor"]`), which is the existing
  session-evidence path the terminal catalog already persists.
- This adapter supports one transport: eve's documented HTTP session protocol. There is no terminal
  scraping, no ACP-only launcher and no replacement agent loop.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; eve's published session/streaming documentation is the external authority, mirrored by the wire module and the runtime README. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter implements AR's existing protocol, capability and interrupt ports rather than introducing a new seam. | `LaunchableHarnessProtocolAdapter`; `InterruptCapableAdapter`; `AdapterHandshake`; `SubmissionReceipt`; `ReconciliationResult`; `InterruptResult` | mcp/src/agents_remember/serving/harness_control_adapter.py:26-26; mcp/src/agents_remember/serving/harness_control_adapter.py:34-37; mcp/src/agents_remember/serving/harness_control_models.py:1-260; mcp/src/agents_remember/models/conversations/control_wire.py:1-200 |
| Registration is through the existing factory owner, which is the seam this leaf deliberately used instead of adding a kernel harness row. | `create_harness_protocol_adapter`; `_LAUNCH_KNOBS`; `_eve_expected_selection` | mcp/src/agents_remember/serving/harness_control_factories.py:35-40; mcp/src/agents_remember/serving/harness_control_factories.py:56-102; mcp/src/agents_remember/serving/harness_control_factories.py:105-130 |
| The wire contract, cursor decoder, transport seam, launch composition and interaction queue are the adapter's own dependencies. | `EveStreamEvent`; `EveNdjsonDecoder`; `EveRuntimeTransport`; `EveRuntimeSpec`; `EveInteractionQueue` | mcp/src/agents_remember/serving/eve_protocol.py:67-269; mcp/src/agents_remember/serving/eve_stream_cursor.py:13-13; mcp/src/agents_remember/serving/eve_stream_cursor.py:18-69; mcp/src/agents_remember/serving/eve_runtime_client.py:91-372; mcp/src/agents_remember/serving/eve_runtime_launch.py:90-372; mcp/src/agents_remember/serving/eve_interactions.py:34-109 |
| Event translation and normalized state are the mapper's, not the adapter's. | `EveEventMapper` | mcp/src/agents_remember/serving/eve_events.py:102-646 |
| The one replay window the adapter delegates to is declared beside the wire contract it serves. | `EveEventDeduplicator`; `EVE_REPLAY_WINDOW` | mcp/src/agents_remember/serving/eve_protocol.py:224-224; mcp/src/agents_remember/serving/eve_protocol.py:234-267 |
| Acceptance on a reconciled request is proved from the durable record holding the exact message. | `_proves_delivery`; `_RECONCILE_READ_LIMIT` | mcp/src/agents_remember/serving/eve_adapter.py:868-868; mcp/src/agents_remember/serving/eve_adapter.py:877-889 |
| The conformance suites drive this real adapter through the transport seam, one class per named scenario. | `EveAdapterHandshakeTests`; `EveAdapterSubmissionTests`; `EveAdapterReconnectTests`; `EveAdapterReconcileTests`; `EveAdapterInterruptTests`; `EveAdapterRestartTests` | mcp/tests/test_eve_adapter.py:271-328; mcp/tests/test_eve_adapter.py:373-603; mcp/tests/test_eve_adapter.py:663-723; mcp/tests/test_eve_adapter.py:726-811; mcp/tests/test_eve_adapter.py:814-907; mcp/tests/test_eve_adapter.py:910-958 |
| The live native fixture proves the same six scenarios against the real runtime over real HTTP. | `_scenario_protocol`; `_scenario_reconnect`; `_scenario_reconcile`; `_scenario_cancel`; `_scenario_restart`; `_scenario_concurrent` | mcp/tests/live_eve_native_fixture.py:572-622; mcp/tests/live_eve_native_fixture.py:625-672; mcp/tests/live_eve_native_fixture.py:675-738; mcp/tests/live_eve_native_fixture.py:774-833; mcp/tests/live_eve_native_fixture.py:849-888; mcp/tests/live_eve_native_fixture.py:1012-1054 |
| The capability snapshot this adapter publishes: the model is real, the effort axis is not, and no effort option is offered. | `_capability_snapshot`; `supports_effort`; `effort_options`; `default_effort` | mcp/src/agents_remember/serving/eve_adapter.py:688-718 |
| The launch-validation vocabulary that survives the retirement, and the setter that validates against it without advertising it. | `REASONING_EFFORTS`; `set_effort` | mcp/src/agents_remember/serving/eve_adapter.py:90-98; mcp/src/agents_remember/serving/eve_adapter.py:301-323 |
| The capability catalog consumes this snapshot, so the retired axis is what the dashboard actually reads. | `HarnessCapabilityCatalog` | mcp/src/agents_remember/serving/harness_capability_catalog.py:84-212 |
| Cases pin the retirement in both directions: the pinned runtime reads no effort value and the catalog agrees, and the effort setter refuses every candidate including its own vocabulary. | `test_the_pinned_runtime_reads_no_effort_value_and_the_catalog_agrees`; `test_the_effort_setter_refuses_every_candidate_including_its_own_vocabulary`; `test_no_advertised_control_lacks_a_runtime_consumer` | mcp/tests/test_eve_product_integration.py:999-1022; mcp/tests/test_eve_product_integration.py:1024-1041; mcp/tests/test_eve_product_integration.py:1043-1067 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| The controlled application is the pinned published `eve` package, unmodified; nothing is forked or vendored. | exact dependency pins; "the runtime is the unmodified published `eve` package" | eve_runtime/package.json:14-20; eve_runtime/README.md:3-8 |

## Update History
- 2026-09-16T11:41:11+00:00: Generated citation repair: `EveAdapterHandshakeTests`; `EveAdapterSubmissionTests`; `EveAdapterReconnectTests`; `EveAdapterReconcileTests`; `EveAdapterInterruptTests`; `EveAdapterRestartTests` repointed to mcp/tests/test_eve_adapter.py:271-328; mcp/tests/test_eve_adapter.py:373-603; mcp/tests/test_eve_adapter.py:663-723; mcp/tests/test_eve_adapter.py:726-811; mcp/tests/test_eve_adapter.py:814-907; mcp/tests/test_eve_adapter.py:910-958. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **the effort axis is retired from the catalog.**
  `_capability_snapshot` now publishes `supports_effort=False`, `effort_options=()` and
  `default_effort=None`, and `EffortOption` is no longer imported. Recorded the measured reason (the
  pinned application reads no effort value, so a menu would advertise a control whose every value
  produces the same run) and the distinction a reader must keep straight: `REASONING_EFFORTS` survives
  as a **launch-validation vocabulary only** — a settings-owned selection naming an undocumented level
  is refused at launch — and is *not* a catalog source; `selected_effort` is still reported because the
  configuration a session started under is a fact rather than a menu. Body updated on Logic and
  Invariants, and three reference rows added for the snapshot, the surviving vocabulary and the cases
  that pin both directions. Verification metadata moves to the leaf's synced base `ff97072c`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit and no
  hash or fingerprint was invented here.

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): re-read this card against the A2
  revision of the same uncommitted candidate and updated four contracts. (1) `_proves_delivery` /
  `reconcile`: the delivery-id branch was **deleted** because a lost response never delivers the
  request's own id, so acceptance is proved only by the durable record holding the exact accepted
  message, and the detail string now says exactly that. (2) Launch-environment resolution reads the
  environment as given, so `AR_EVE_RUNTIME_ROOT` / `AR_EVE_NODE` are live selectors rather than
  documented-but-inert names, while `_runtime_env` still strips both from the child. (3) `_is_replay`
  holds no window: the adapter delegates to the single `EveEventDeduplicator`, and a second inline
  copy is now stated as a regression. (4) `interrupt` is pinned to the **observed** turn id. Citation
  tables were rewritten into the `Finding | Anchor | Source` shape. Verification metadata moves to the
  leaf's current base `e9300687`; the candidate is still deliberately uncommitted, so the governed
  closeout stamps the real code commit and no hash or fingerprint was invented here.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a file added by the native
  eve session-adapter change set. Records the native session contract, the acceptance-versus-completion
  separation, the never-repeat-a-possibly-accepted-write rule, the turn-addressed interrupt with
  replay-once, the honest `unsupported` setters, and the explicit boundaries (no capsule compilation,
  no second registry, no asset submission, no replacement session). Verification metadata is pinned to
  the leaf's base commit `67b21aeb` because the candidate is deliberately uncommitted — the governed
  closeout stamps the real code commit, and no hash or fingerprint was invented here.
