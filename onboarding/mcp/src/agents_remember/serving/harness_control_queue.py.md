# mcp/src/agents_remember/serving/harness_control_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides the legacy `HarnessControlQueue` surface as a thin lifecycle/runner facade over
`HarnessSubmissionAuthority`. FEUI-L5 removes its former independent command queue, prompt ledger,
and execution-order authority so one bridge has exactly one prompt/setter timeline.
260718-CHATS-L0E adds one additive read-only provenance delegation through the same facade;
260718-CHATS-L2E adds the matching read-only `operation_timeline` delegation.

## Code Commentary

### Logic

Construction creates one `HarnessSubmissionAuthority` with the configured timeline and duplicate-
ledger bounds. Submit, response, model/effort set, status, reconcile, resolve-operation, and withdraw
methods delegate to that authority. The facade retains bridge start/stop and adapter lifecycle
compatibility, but it neither admits its own prompt FIFO nor stores a competing receipt ledger.
Authority events and exact operation references flow through the bridge to the same underlying
instance. L0E adds `provenance(expected_bridge_epoch, request_ids)`, a read-only delegation shaped
on the status delegation that is the sole bridge→authority path for the submission-provenance
batch; the facade holds the authority privately and admits no bypass. L2E adds
`operation_timeline(expected_bridge_epoch, *, after_sequence, limit, byte_budget)`, the same
provenance-shaped read-only delegation for the paged never-bodies ledger enumeration — the sole
bridge→authority path for the timeline read, defaulting to `MAX_OPERATION_TIMELINE_PAGE` and the
shared `EVIDENCE_PAGE_BYTE_BUDGET`.

### Conventions

The historical class name is retained for call-site compatibility. “Queue” now names the facade,
not an additional actor. Ordering, idempotency, withdrawal linearization, safe-retry classification,
and retention all live in `harness_submission_authority.py`.

### Invariants And Boundaries

- One authority instance owns the epoch-bound prompt/setter timeline.
- This facade cannot enqueue work behind the authority or release its active operation.
- Response bypass and status/withdrawal responsiveness are authority behavior, not a second queue.
- Stop delegates through the authority/adapter lifecycle and leaves no stranded facade futures.
- The `operation_timeline` delegation is read-only like `provenance`: it holds no facade state,
  mutates nothing, and remains the sole bridge→authority path for the timeline read.

### Todos

The compatibility class can be renamed only in a separately scoped API migration; it must not regain
independent queue semantics.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The normalized data module supplies the exact vocabulary; the bridge exposes the ordered methods.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The capability contract declares the five acceptance values and serialization rejects any other token. | L13-L23; L152-L159; L216-L225 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |
| The bridge exposes setters only while running and delegates both to this queue. | L422-L428 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The blocking client preserves post-write ambiguity under the same caller request id. | L179-L252; L253-L325 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| Queue and IPC tests prove pending and retained duplicates invoke the adapter once and known receipts reconcile locally. | L983-L1087; L1458-L1497; L1571-L1669 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| The bridge delegates the epoch-checked paged operation-timeline read through this facade's sole authority path. | L154-L169; L320-L334 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py); [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| Contract tests pin the timeline enumeration over this delegation: all sources and kinds, paged union, eviction floor, budget edge, and epoch flip. | L773-L1010 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |

## Cross-Repo References

No external repository boundary is implemented by the queue.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Current authority lives in `HarnessSubmissionAuthority`; this class is only the bridge-compatible
facade and lifecycle wrapper. Earlier history describing an independent command runner remains
historical and must not be read as current architecture.

## 260731-EFA-L2 Current Delta

The queue facade now constructs and forwards the two concepts declared in
[harness_submission_authority.py](harness_submission_authority.py.md) instead of six loose
arguments: it takes a **`BridgeSnapshotPort`** (`clock`, `snapshot`, `set_snapshot`, `publish` — how
a bridge sub-component reads, replaces, publishes and timestamps the ONE snapshot) and builds a
**`SubmissionLimits`** (`timeline=queue_limit`, `ledger=submission_limit`) for the authority it
wraps. The facade's own behaviour and the wrapped authority's bounds are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 line citations. The two-target
  operation-timeline row cited L163-L179; L270-L284 — the second overran this 227-line facade
  because it belongs to the second link; both were repointed to the current definitions,
  `harness_control_queue.py::operation_timeline` at L154-L169 and
  `harness_control_bridge.py::operation_timeline` at L320-L334 (same link order). The
  `mcp/tests/test_harness_control.py` row now cites the exact tests instead of L673-L751;
  L1155-L1232: the queue-level block L983-L1087
  (`test_duplicate_request_id_returns_retained_result_without_resubmission`,
  `test_dispatching_duplicate_returns_unknown_without_resubmission`,
  `test_known_receipts_reconcile_without_native_reconciliation`) plus the IPC-level
  `test_outer_socket_lost_receipt_reconciles_retained_known_truth` (L1458-L1497) and
  `test_public_duplicate_returns_retained_result_with_one_adapter_call` (L1571-L1669).
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `BridgeSnapshotPort` / `SubmissionLimits` pass-through to the submission authority.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the additive read-only
  `operation_timeline` delegation — the same provenance-shaped epoch-checked facade path for the
  paged never-bodies ledger enumeration, with no independent facade state. Verification metadata
  stays pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the additive read-only
  `provenance` delegation — epoch-checked, the sole bridge→authority path for the
  submission-provenance batch, with no independent facade state. Verification metadata stays
  pinned until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: rewrote current purpose/logic/invariants for the thin facade
  and removed the obsolete second-queue/ledger authority claim.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented request-id idempotency for
  pending and retained duplicates, first-payload authority, one adapter call, and local
  reconciliation of retained known truth.
- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented shared setter ordering,
  fail-closed five-value validation, effective-value rules, accepted-set snapshot refresh, and
  cancellation-safe future completion.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for ordered command
  execution, stranded-await failure handling, and bounded unsupported receipt retention.
