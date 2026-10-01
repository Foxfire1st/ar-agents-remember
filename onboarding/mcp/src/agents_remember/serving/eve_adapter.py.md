# mcp/src/agents_remember/serving/eve_adapter.py

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

**The effort axis is PUBLISHED as a launch control, because a runtime consumer exists.**
`_capability_snapshot` publishes `supports_effort=True`, an `effort_options` tuple built from
`REASONING_EFFORTS`, and `default_effort=PROVIDER_DEFAULT_EFFORT`; `EffortOption` is imported again.
The reason is measured rather than asserted: the pinned application **consumes** `AR_EVE_EFFORT`
through eve's own agent definition (`eve_runtime/agent/agent.ts` reads the variable and applies it via
`defineAgent({ reasoning })`), and the request body a direct provider receives carries the configured
level — read at the provider boundary by `mcp/tests/test_eve_effort_runtime.py`, not inferred from
documentation. The menu is therefore neither manufactured nor a second catalogue: it **is** the
accepted vocabulary, the same tuple the launch gate validates against, so a published level is one a
launch can select. Every option is `launch_settable=True` and `session_settable=False`.

`REASONING_EFFORTS` is now `PROVIDER_DEFAULT_EFFORT, none, minimal, low, medium, high, xhigh` — eve's
own union, mirrored from the installed `AgentReasoningDefinition`
(`NonNullable<CallSettings["reasoning"]>`), with the AR sentinel as its first member.
`PROVIDER_DEFAULT_EFFORT` is the sentinel's one declaration: it means *no explicit reasoning*, and the
authored application answers it by **omitting** the property rather than forwarding the token. The
vocabulary is confronted against the installed declaration by a drift case and against a recorded
union constant on a host with no install, so the launch gate and the menu cannot drift from the runtime
that has to honour a level.

`default_effort` and `selected_effort` remain **different facts and are not folded together**: the
default is the level a launch that names none runs at, while `selected_effort` is the configuration
this runtime was started under — a fact about the run rather than a menu. Keeping the axis out of
`set_effort` is the launch/live split, **not** a retraction of the axis.

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
- **Every published effort option is backed by the runtime, and the axis stays launch-only.**
  `_capability_snapshot` publishes `supports_effort=True`, `effort_options` = `REASONING_EFFORTS` and
  `default_effort=PROVIDER_DEFAULT_EFFORT`, and every option is `launch_settable=True` /
  `session_settable=False`. This is the same generic rule in its positive form — a published axis must
  name its runtime consumer — so the axis may be advertised **only while** the authored application
  reads `AR_EVE_EFFORT` and applies it through `defineAgent({ reasoning })`; removing that consumer
  means withdrawing the axis again, not leaving the menu up. The menu may not become a second
  catalogue: it is `REASONING_EFFORTS` itself, the tuple the launch gate validates against. And the
  published axis stays a **launch** value: in-session `set_effort` reports `unsupported` for every
  candidate, including the ones this catalogue advertises, because eve compiles the level into the
  running application and a change means a new runtime launch.
- **No second orchestration registry.** Session identity and stream cursor are published on the
  existing `AdapterSnapshot` (`vendor_session_id`, `raw["streamCursor"]`), which is the existing
  session-evidence path the terminal catalog already persists.
- This adapter supports one transport: eve's documented HTTP session protocol. There is no terminal
  scraping, no ACP-only launcher and no replacement agent loop.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; eve's published session/streaming documentation is the external authority, mirrored by the wire module and the runtime README.

### Repo-Internal References

- The adapter implements AR's existing protocol, capability and interrupt ports rather than introducing a new seam. [1]
- Registration is through the existing factory owner, which is the seam this leaf deliberately used instead of adding a kernel harness row. [2]
- The wire contract, cursor decoder, transport seam, launch composition and interaction queue are the adapter's own dependencies. [3]
- Event translation and normalized state are the mapper's, not the adapter's. [4]
- The one replay window the adapter delegates to is declared beside the wire contract it serves. [5]
- Acceptance on a reconciled request is proved from the durable record holding the exact message. [6]
- The conformance suites drive this real adapter through the transport seam, one class per named scenario. [7]
- The live native fixture proves the same six scenarios against the real runtime over real HTTP. [8]
- The capability snapshot this adapter publishes: both axes are real, and the effort menu is the accepted vocabulary with its default. [9]
- The AR sentinel, the accepted reasoning vocabulary mirrored from eve's own union, and the setter that validates against it without echoing it back. [10]
- The capability catalog consumes this snapshot, so the published axis is what the dashboard actually reads. [11]
- The authored consumer that makes the axis real: the application reads the effort input and applies it through eve's own agent definition, omitting the property for the sentinel. [12]
- The launch input the consumer reads, and the two places the selection is carried into the child environment rather than re-derived. [13]
- Cases pin the published axis in both directions: the pinned runtime consumes the effort input and the catalog publishes the axis the client would read, and the setter refuses every candidate including its own vocabulary. [14]

### Cross-Repo References

- The controlled application is the pinned published `eve` package, unmodified; nothing is forked or vendored. [15]
