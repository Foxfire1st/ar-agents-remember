# mcp/tests/test_harness_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Reusable deterministic fake adapters and private IPC server seams for harness-control checks.

## Code Commentary

### Logic

The fake records launches, submissions, setters, responses and reconciliation requests. It advertises an intentionally empty capability snapshot, can emit snapshots/events, and settles an answered multiplexed interaction from the pending tuple. Completion events carry the original submission operation.

Blocking submit and setter adapters use explicit asyncio events to hold and release work. The observed server exposes connection completion through a finally-set event. The dropped-response server dispatches the first actual submit, closes its socket before returning the receipt, and delegates subsequent connections normally. Fixed identity, launch and catalog builders keep exact-session inputs consistent.

### Invariants And Boundaries

This retained module defines support objects and builders; it contains no collected test functions. Its former family-wide coverage narrative is historical. Helper availability is not evidence that a removed scenario still runs.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fake supplies cached state, recording and deterministic events. | "class _FakeAdapter" | mcp/tests/test_harness_control.py:52-229 |
| Explicit submission hold/release and injected error. | "class _BlockingSubmitAdapter" | mcp/tests/test_harness_control.py:232-246 |
| Explicit setter hold/release returns queued acceptance. | "class _BlockingSetAdapter" | mcp/tests/test_harness_control.py:249-267 |
| Connection completion is observable even when dispatch fails. | "class _ObservedHarnessControlServer" | mcp/tests/test_harness_control.py:270-285 |
| A real first dispatch loses only its outer response. | "class _DropFirstSubmitResponseServer" | mcp/tests/test_harness_control.py:288-309 |
| The catalog builder derives identity fields from the supplied control identity. | "def _catalog_entry(" | mcp/tests/test_harness_control.py:338-351 |

## Docs References

No external documentation is needed for these source-owned helper facts.

## Cross-Repo References

No separate cross-repository authority is established by this helper module.

## Update History

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

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
