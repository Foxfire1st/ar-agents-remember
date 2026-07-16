# mcp/tests/test_harness_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T06:15+02:00 |
| lastVerifiedCommitHash | `a1b0aa9143fa777efd8389892e3283ff257ef44d` |
| lastVerifiedCommitDate | 2026-07-16T06:37:02+02:00|
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

ACPUI-L1 adds the normalized `advertise()` method to the deterministic fake adapter. It returns an
empty `CapabilitySnapshot`, allowing the shared bridge conformance suite to continue satisfying the
expanded `HarnessProtocolAdapter` boundary without pretending that this generic fake owns a vendor
catalog. Vendor-specific discovery and catalog assertions remain in the Claude, Codex, and Pi test
modules.

ACPUI-L3 gives the fake explicit model/effort methods and records every launch, setter, and prompt
operation. The new scenarios prove one shared FIFO control queue from launch through a setter into
the following prompt; cancelling a caller while a setter is executing does not terminate that
queue when the adapter later completes. A truth-table test rejects mismatched requested values,
illegal acceptance tokens, `echo-verified` without an effective value, accepted results marked
not-ok, and unknown/unsupported results that falsely claim an effect. Each rejected result leaves
the runner usable for the next prompt. The unregistered adapter remains explicitly unsupported for
both setters.

ACPUI-L4 extends the suite through the real local socket and daemon route composition. Duplicate
request ids are idempotency keys: a retained duplicate returns the first receipt, and a duplicate
arriving while the first submit is pending waits for that same result; neither path replaces the
first payload or calls the adapter twice. Reconciliation maps retained immediate/queued receipts to
accepted, rejected to rejected, and unsupported to unsupported without invoking native
reconciliation; only genuinely unknown evidence delegates to the adapter.

The exact-session IPC cases advertise the normalized snapshot and pass through honest queued and
unsupported setter results. A deliberately dropped outer response proves the caller keeps the same
request id as unknown, then recovers the bridge-retained vendor correlation without resend. The
same loss is driven through `deliver_inbox_entry`: the durable bus moves from unknown to delivered /
accepted with one adapter call and no paste fallback. A concurrent public duplicate test reaches
the HTTP route, Unix socket, bridge queue, and adapter, proving identical responses and one native
submission end to end.

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase`, fixed timestamps and identities, bounded fake
queues, and deterministic adapter events. Assertions favor whole protocol outcomes and loud error
messages over transport timing heuristics.

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

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test module directly proves the fake-adapter bridge contract; the adapter protocol defines the
advertisement and setter methods it now satisfies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The fake adapter implements startup, snapshots, an intentionally empty normalized advertisement, prompt submission, reconciliation observation, and explicit setter results. | L77-L209 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Shared ordering and cancellation coverage proves launch, setter, and following prompt execute in one FIFO queue that survives a cancelled waiter. | L319-L394 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| The invalid-result matrix rejects dishonest evidence and arbitrary acceptance strings without poisoning the runner; unregistered adapters remain explicitly unsupported. | L396-L435 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Pending and retained duplicate ids return the first result and preserve the first payload with one adapter submission; known receipts reconcile locally without a native reconcile call. | L673-L748 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Exact-session IPC advertises and returns honest queued/unsupported setter acceptance through the blocking client. | L1000-L1034 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Outer response loss returns unknown, then retained reconciliation restores accepted state and vendor correlation with one adapter call. | L1036-L1076 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Durable-inbox redelivery converges from unknown to delivered/accepted through reconcile, makes one adapter submission, and never invokes paste. | L1078-L1153 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| The public concurrent duplicate case crosses HTTP and real Unix-socket IPC, returns identical correlated responses, and invokes the adapter once. | L1155-L1239 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Private endpoint permission, identity, peer-loss, and malformed-request cases preserve exact-session ownership and loud failure. | L1241-L1354 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| `HarnessProtocolAdapter` requires cached advertisement and model/effort setters alongside startup, snapshot, submit, reconciliation, and shutdown. | L31-L53 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The shared queue treats request ids as idempotency keys, retains one payload/result, and converts known receipts into reconciliation truth before considering the native port. | L114-L145; L378-L411 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |
| Exact-identity IPC dispatches advertise and setters separately from submit/reconcile while retaining private internal serializers. | L127-L192 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |

## Cross-Repo References

No sibling repository is required to prove this protocol-neutral test suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
