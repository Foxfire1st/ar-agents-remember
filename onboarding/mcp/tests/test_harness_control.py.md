# mcp/tests/test_harness_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-adapter conformance suite for the protocol-neutral harness control contract, serialized
model/effort setters, reliable whole-message submission, retained reconciliation, terminal surface,
durable-inbox convergence, and the exact-session private IPC boundary.

## Code Commentary

### Logic

The suite drives exact identity and capability handshakes, normalized snapshots/events, immediate
and queued acceptance, blocked/settling/completion states, disconnect ambiguity, reconciliation
without resend, bounded retention, draft custody, and graceful/forced shutdown. IPC scenarios cover
private endpoint permissions, exact identity, malformed requests, and peer loss after accepted
dispatch without losing the preserved vendor correlation.

The deterministic fake adapter also implements the normalized `advertise()` method. It returns an
empty `CapabilitySnapshot`, allowing the shared bridge conformance suite to continue satisfying the
expanded `HarnessProtocolAdapter` boundary without pretending that this generic fake owns a vendor
catalog. Vendor-specific discovery and catalog assertions remain in the Claude, Codex, and Pi test
modules.

The fake implements explicit model/effort methods and records every launch, setter, and prompt
operation. The scenarios prove one shared FIFO control queue from launch through a setter into
the following prompt; cancelling a caller while a setter is executing does not terminate that
queue when the adapter later completes. A truth-table test rejects mismatched requested values,
illegal acceptance tokens, `echo-verified` without an effective value, accepted results marked
not-ok, and unknown/unsupported results that falsely claim an effect. Each rejected result leaves
the runner usable for the next prompt. The unregistered adapter remains explicitly unsupported for
both setters.

**260731-EFA-L8 (round 11): queued acceptance is deterministic by construction.** The fake
adapter gates submissions behind `release_submit` / `release_set` asyncio events, so a prompt
submitted while the setter is still held receives its `queued` receipt BEFORE the release — the
queue state is constructed by ordering, never by timing heuristics. The rewrite removed
receive-before-release races: a held submission is returned only after the test releases it, and
`queued` is asserted while the gate is still closed.

The suite also drives the real local socket and daemon route composition. Duplicate
request ids are idempotency keys: a retained duplicate returns the first receipt, and a duplicate
arriving while the first submit is pending waits for that same result; neither path replaces the
first payload or calls the adapter twice. Reconciliation maps retained immediate/queued receipts to
accepted, rejected to rejected, and unsupported to unsupported without invoking native
reconciliation; only genuinely unknown evidence delegates to the adapter. The registration call
shape is followed: `register_harness_control_routes` now takes one `ConversationRuntime` whose
`ConversationScope(workspace_root=..., coordination_root=...)` is the immutable scope, alongside
the harness registry, catalog, `TerminalHost`, liveness clock/config, a `HarnessCapabilityCatalog`,
and a `LocalOperatorAuthorizationResolver.for_workspace(...)` authorization.

The exact-session IPC cases advertise the normalized snapshot and pass through honest queued and
unsupported setter results; prompts travel through `submit_control_prompt(entry, text,
ControlSubmission(source=..., request_id=..., expected_bridge_epoch=...))`, so source, id, and
epoch are one submission descriptor rather than three loose keywords. A deliberately dropped outer
response proves the caller keeps the same
request id as unknown, then recovers the bridge-retained vendor correlation without resend. The
same loss is driven through `deliver_inbox_entry`, whose call shape is now an
`InboxDeliveryLog(store=..., entry=...)` plus a `sessions=HostedSessionRuntime(catalog=..., host=...)`
and the paster: the durable bus moves from unknown to delivered /
accepted with one adapter call and no paste fallback. The entry it delivers is minted by
`create_operator_inbox_entry` from `InboxMessage`, `InboxRouting`/`InboxAddress`, and `InboxPoster`
parameter objects. A concurrent public duplicate test reaches
the HTTP route, Unix socket, bridge queue, and adapter, proving identical responses and one native
submission end to end.

Multiplexed sub-agent approval authority cases (R6) round out the suite.
cit:([`test_subagent_pending_interaction_responds_without_parent_operation`], mcp/tests/test_harness_control_conformance_1.py:437-491) proves an agent
entry riding the plural `pending_interactions` tuple owns no parent operation, so the
active-operation guard must not strand it: the response routes to the adapter with no operation
attached, the answered entry settles out of the plural tuple, and an unknown interaction id is
still refused (`HarnessInteractionNotPendingError`) without reaching the adapter. The fake
adapter's `respond` now settles the answered multiplexed entry out of `pending_interactions` too.
cit:([`test_parent_thread_tuple_entry_gets_the_operation_guard`], mcp/tests/test_harness_control_conformance_1.py:493-551) pins the entry-thread
parent rule: a concurrent PARENT pending riding the plural tuple (the adapter's per-thread
pending map makes that normal traffic) gets the active-operation guard exactly like the singular
slot — answering it operation-free is refused — while the agent tuple entry still answers without
one. cit:([`test_multiplexed_pending_interactions_serialize_through_every_surface`], mcp/tests/test_harness_control_conformance_1.py:553-612) round-trips the
plural pending tuple through every wire: `snapshot_json` carries both the singular
`pendingInteraction` (back-compat) and the additive `pendingInteractions`; the control client
parses the additive field back and defaults a pre-multiplexing bridge (key absent) to the empty tuple; the
catalog projection and `TerminalCatalogEntry` JSON round-trip carry
`controlPendingInteractions`; and an empty multiplex never writes the additive key.

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase`, fixed timestamps and identities, bounded fake
queues, and deterministic adapter events. Bounds are set through one `BridgeLimits` object —
`HarnessControlBridge(identity, adapter, limits=BridgeLimits(queue=..., submission=...,
subscriber_queue=..., transcript=...))` — so the subscriber-coalescing, eviction, unsupported-ledger,
and transcript-reclamation cases each clamp exactly the dimension they probe. The terminal host is
constructed as `TerminalHost(TerminalHostSeams(tmux_probe=...))`. Assertions favor whole protocol
outcomes and loud error messages over transport timing heuristics.

### Invariants And Boundaries

- The fake adapter proves the common protocol contract without registering a production driver.
- Its empty capability advertisement is a structural test double only; it must not be interpreted
  as a static default catalog or capability-discovery fallback.
- Launch, model/effort setters, and prompts share one ordered command queue; setter completion or
  caller cancellation cannot bypass or poison later work.
- `echo-verified` requires `ok` plus an effective value; `immediate` and `queued` cannot claim one;
  `unknown` and `unsupported` cannot claim acceptance or effect; no sixth acceptance token is valid.
- An adapter without registered native setter support returns `unsupported`, never a simulated set.
- Tests assert bounded-time loud failure rather than allowing stranded awaits.
- Accepted-dispatch IPC peer loss contains only the documented broken-pipe/reset paths; identity,
  protocol, validation, dispatch, and unrelated failures remain loud.
- Ambiguous sends remain reconcilable and are never blindly retried; draft-preservation tests keep
  surface ownership and whole-message ordering explicit.
- A caller request id identifies one authoritative payload and one retained result. Pending and
  completed duplicates cannot replace the text or create a second adapter call.
- Known receipt reconciliation is local and correlation-preserving; adapter reconciliation is
  reserved for a bridge-retained `unknown` outcome.
- Exact-session advertise and setters travel through the private identity-checked endpoint, and
  durable-bus recovery must converge without invoking terminal paste.
- Multiplexed sub-agent approvals answer through the authority without a parent operation; the
  singular parent pending slot stays back-compatible, the plural tuple is additive on every wire,
  and an empty multiplex never serializes the additive key (R6). Parent-ness follows the entry's
  own thread: a concurrent parent pending riding the tuple gets the active-operation guard exactly
  like the singular slot.

### Todos

None.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test module directly proves the fake-adapter bridge contract; the adapter protocol defines the
advertisement and setter methods it now satisfies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fake adapter implements startup, snapshots, an intentionally empty normalized advertisement, prompt submission, reconciliation observation, and explicit setter results. | `_FakeAdapter` | mcp/tests/test_harness_control.py:113-287 |
| Shared ordering and cancellation coverage proves launch, setter, and following prompt execute in one FIFO queue that survives a cancelled waiter. | `test_capability_setters_share_launch_set_prompt_queue_order`; `test_cancelled_setter_late_completion_does_not_kill_command_queue` | mcp/tests/test_harness_control_conformance_1.py:65-90; mcp/tests/test_harness_control_conformance_1.py:92-123 |
| The invalid-result matrix rejects dishonest evidence and arbitrary acceptance strings without poisoning the runner; unregistered adapters remain explicitly unsupported. | `test_bad_set_result_installs_resolvable_unknown_barrier_without_poisoning`; `test_unregistered_adapter_setters_remain_explicitly_unsupported` | mcp/tests/test_harness_control_conformance_1.py:125-166; mcp/tests/test_harness_control_conformance_1.py:168-173 |
| Pending and retained duplicate ids return the first result and preserve the first payload with one adapter submission; known receipts reconcile locally without a native reconcile call. | `test_duplicate_request_id_returns_retained_result_without_resubmission`; `test_dispatching_duplicate_returns_unknown_without_resubmission`; `test_known_receipts_reconcile_without_native_reconciliation` | mcp/tests/test_harness_control_conformance_2.py:68-100; mcp/tests/test_harness_control_conformance_2.py:102-134; mcp/tests/test_harness_control_conformance_2.py:136-174 |
| Exact-session IPC advertises and returns honest queued/unsupported setter acceptance through the blocking client. | `test_exact_session_ipc_advertises_and_returns_set_acceptance` | mcp/tests/test_harness_control_ipc.py:148-181 |
| Outer response loss returns unknown, then retained reconciliation restores accepted state and vendor correlation with one adapter call. | `test_outer_socket_lost_receipt_reconciles_retained_known_truth` | mcp/tests/test_harness_control_ipc.py:183-222 |
| Durable-inbox redelivery converges from unknown to delivered/accepted through reconcile, makes one adapter submission, and never invokes paste. | `test_durable_inbox_outer_loss_converges_by_reconcile_without_resend` | mcp/tests/test_harness_control_ipc.py:224-294 |
| The public concurrent duplicate case crosses HTTP and real Unix-socket IPC, returns identical correlated responses, and invokes the adapter once. | `test_public_duplicate_returns_retained_result_with_one_adapter_call` | mcp/tests/test_harness_control_ipc.py:296-394 |
| Private endpoint permission, identity, peer-loss, and malformed-request cases preserve exact-session ownership and loud failure. | `test_peer_timeout_after_submit_preserves_reconciliation_result`; `test_private_endpoint_exact_identity_and_submission`; `test_malformed_ipc_request_is_rejected_without_control_fallback` | mcp/tests/test_harness_control_ipc.py:678-733; mcp/tests/test_harness_control_ipc.py:735-771; mcp/tests/test_harness_control_ipc.py:773-793 |
| `HarnessProtocolAdapter` requires cached advertisement and model/effort setters alongside startup, snapshot, submit, reconciliation, and shutdown. | `HarnessProtocolAdapter` | mcp/src/agents_remember/serving/harness_control_adapter.py:32-59 |
| The submission authority behind the queue treats request ids as idempotency keys, refuses a second source/payload under the same id, and converts known receipts into reconciliation truth before considering the native port. | `_pre_admission_receipt_locked`; `reconcile` | mcp/src/agents_remember/serving/harness_submission_authority.py:217-243; mcp/src/agents_remember/serving/harness_submission_authority.py:358-404 |
| Exact-identity IPC dispatches advertise and setters separately from submit/reconcile while retaining private internal serializers. | `HarnessControlServer`; `_dispatch`; `_advertise`; `_set_model`; `_set_effort`; `_submit`; `_reconcile` | mcp/src/agents_remember/serving/harness_control_ipc.py:99-412 |

## Cross-Repo References

No sibling repository is required to prove this protocol-neutral test suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Submission Authority Delta

The common control suite now treats one `HarnessSubmissionAuthority` as the prompt/setter timeline.
It covers ordered terminal outcomes, unknown-setter barriers, no-resend idempotency/reconciliation,
bounded ambiguity, private status/withdraw, IPC and outer-response loss, durable-source interaction,
and duplicate raw-free projection. Earlier second-runner queue semantics are historical only.

## Structured Interaction Surface Delta

Harness-control coverage now includes the expanded structured interaction/control surface while preserving exact epoch, request, and transport failure boundaries.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-08-11T19:58+02:00 — No content impact: removed an explicit `leaf_key=None` from the local
  catalog fixture after that retired model field disappeared; native harness control behavior and
  evidence assertions documented by this card are unchanged.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: restructured under 1,200 lines (357): the shared fake-adapter helpers stay here and the conformance family moved to `test_harness_control_conformance_1.py` / `_2.py`; L8's deterministic receipt-before-release rewrite is applied verbatim in the family. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T20:09+02:00 — 260731-EFA-L8 curator (bounded delta 2): recorded the round-11
  deterministic rewrite — the fake adapter gates submissions behind `release_submit` /
  `release_set` events, so a prompt submitted while the setter is held receives its `queued`
  receipt by construction (receipt before release), removing receive-before-release timing races.
  Verification metadata stays pinned until closeout stamps the code commit.
- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 11 citation rows across the fake adapter, conformance cases, submission authority, and private IPC implementation; scoped citation fixing regenerated the source ranges.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation whose subject
  had moved out of the cited file. `harness_control_queue.py` is now a 227-line facade — its own
  docstring says the ordering truth lives in `HarnessSubmissionAuthority` — so `L114-L145;
  L378-L411` pointed at plain delegation (`submit` L84-L85, `reconcile` L90-L96). Repointed the
  link and both ranges to `harness_submission_authority.py`: `_pre_admission_receipt_locked`
  L254-L281, where a repeat request id returns the first receipt but a different source or payload
  digest under that id raises `HarnessRequestConflictError`; and `reconcile` L399-L417, where
  `_known_reconciliation` answers from the retained record and returns before
  `self._adapter.reconcile(...)` is ever awaited. Read both ranges back, and sharpened the claim's
  "retains one payload/result" to the conflict behaviour the code actually implements.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: rewrote the call-shape claims this card had gone
  stale on and re-anchored every self-citation. Route registration no longer takes a
  `coordination_root` keyword: `register_harness_control_routes` now receives one
  `ConversationRuntime` carrying `ConversationScope(workspace_root, coordination_root)`, the harness
  registry, catalog, host, liveness clock/config, a `HarnessCapabilityCatalog`, and a
  `LocalOperatorAuthorizationResolver.for_workspace(...)`, so the Logic paragraph was rewritten to
  match. Bridge bounds now travel as `limits=BridgeLimits(queue=..., submission=...,
  subscriber_queue=..., transcript=...)`, the terminal host as
  `TerminalHost(TerminalHostSeams(tmux_probe=...))`, prompts as `submit_control_prompt(entry, text,
  ControlSubmission(...))`, and durable delivery as `deliver_inbox_entry(InboxDeliveryLog(store,
  entry), sessions=HostedSessionRuntime(catalog, host), paster=...)` with the entry minted from the
  `InboxMessage`/`InboxRouting`/`InboxAddress`/`InboxPoster` objects; Conventions and the IPC
  paragraph now name all of them. Corrected the nine Repo-Internal citations and the three R6
  in-prose ranges against the current file (`_FakeAdapter` L112-L284, FIFO ordering L440-L494,
  invalid-result matrix L495-L544, duplicate/reconcile L983-L1088, IPC advertise L1423-L1457, outer
  loss L1458-L1498, durable inbox L1499-L1570, public duplicate L1571-L1670, private endpoint
  L1844-L1959, and R6 at L768-L823, L824-L883, L884-L944). No test was added, removed, or renamed
  and no protocol, queue, or reconciliation behavior changed. Verification metadata stays pinned;
  closeout re-stamps the candidate commit.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the entry-thread parent-guard pin
  cit:([`test_parent_thread_tuple_entry_gets_the_operation_guard`], mcp/tests/test_harness_control_conformance_1.py:493-551): a concurrent parent
  pending riding the plural tuple gets the active-operation guard like the singular slot while an
  agent entry answers operation-free. Re-anchored the serialization round-trip (L808-L866 →
  L868-L928) and extended the R6 invariant. Verification metadata stays pinned (uncommitted);
  closeout re-stamps the candidate commit.

- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: recorded the multiplexed sub-agent approval
  authority cases (R6) — respond-without-parent-operation with unknown-id refusal, and the plural
  `pending_interactions` serialization round-trips across snapshot/client/catalog surfaces with
  the additive-key-never-empty invariant. Verification metadata stays pinned (uncommitted);
  closeout re-stamps the candidate commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the one-line call-shape follow —
  the IPC daemon route composition passes the new required `coordination_root` keyword. No
  protocol, queue, or reconciliation behavior changed. Verification metadata remains pinned until
  closeout stamps the candidate commit.

- 2026-07-17T21:39+02:00 — FEUI-L5: rewrote the common matrix around the sole authority,
  idempotency, withdrawal, response loss, bounded retention, and privacy.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented exact-session advertise/set
  acceptance, pending and retained request-id idempotency, known-receipt reconciliation, outer
  response-loss recovery, durable-bus convergence without resend or paste, and the public
  duplicate/one-adapter-call path. Body verified against the uncommitted L4 candidate; verification
  metadata remains pinned to the latest committed source revision until closeout.
- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented one launch/set/prompt FIFO,
  cancellation-safe late completion, the complete SetResult truth matrix including arbitrary
  acceptance rejection, and explicit unsupported fallback setters. Verification metadata remains
  pinned until closeout stamps the L3 code commit.
- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented the fake adapter's intentionally
  empty normalized advertisement and its boundary from vendor catalog discovery; corrected the
  governing overview backlink while preserving existing verification metadata.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: documented delayed-reply peer-disconnect
  regression and bridge reconciliation result with narrow error containment.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for fake-adapter
  conformance, R11 draft preservation, ambiguous-send recovery, bounds, and shutdown coverage.
