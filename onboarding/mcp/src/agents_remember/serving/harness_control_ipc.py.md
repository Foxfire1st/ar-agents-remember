# mcp/src/agents_remember/serving/harness_control_ipc.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides user-private Unix-domain-socket IPC for one exact-session bridge, with bounded JSON-line
requests and explicit snapshot, live advertise, model/effort set, submit, respond, reconcile,
transcript, and stop actions. Exactly three additive read actions — `evidence`,
`evidence-native-page`, and `submission-provenance` — ride under the unchanged
`ar-harness-control/v1` protocol. Two more additive actions — `interrupt` and `operation-timeline`
— plus the additive optional `assets` key on `submit` carry schema validation, resolve-and-verify
spool confinement, and digest verification at admission. The additive optional `threadId` payload
key on `evidence-native-page` is the multiplexed-thread selector that lets a caller page a
sub-agent thread's native history; absent means the parent/session thread exactly as before.

## Code Commentary

### Logic

Endpoint names hash the complete control identity. Runtime directories are `0700`, sockets `0600`,
and non-socket replacements are refused. Every request validates protocol and identity before
dispatch. `advertise`, `set-model`, and `set-effort` serialize the bridge's normalized capability
and `SetResult` types; submit and reconcile retain full internal receipt evidence. After accepted
dispatch, narrow peer-loss exceptions are contained while the bridge remains the truth owner.

The three evidence actions are read-only and additive. `evidence` pages the bridge's deque-domain buffer
(`afterSequence`, bounded `limit` capped at `MAX_EVIDENCE_PAGE = 500`). `evidence-native-page`
pages harness-native history through the bridge with an opaque `cursor` and a server-bounded limit
(`MAX_NATIVE_EVIDENCE_PAGE = 200`); unsupported adapters fail closed typed. `submission-provenance`
requires `expectedBridgeEpoch` plus 1..64 unique `requestIds` and returns the authority's batch.
Every response in both evidence domains carries `bridgeEpoch`; the 14 pre-existing actions and the
one-request-per-connection model are byte-preserved, and unknown actions still fail typed.

The interrupt/timeline actions follow the same additive posture (the set is now 20 actions). `interrupt` requires
`expectedBridgeEpoch` and forwards the optional `turnId`/`expectedOperationId` guards to the
bridge's epoch-guarded dispatch. `operation-timeline` pages the authority's retained ledger with
`afterSequence`/`limit` bounded by `MAX_OPERATION_TIMELINE_PAGE`. The `assets` key on `submit` is
validated before any bridge dispatch: `_submit_asset_schema` enforces the count limit, MIME
allow-list, per-asset byte limit, sha256 shape, and unique ids; `_confined_asset_path` then builds
the convention path `<endpoint-root>/assets/<requestId>/<assetId>` under the request-independent
resolved assets anchor (never caller-supplied), banning empty/over-255-byte components, dot
segments, and separators in either component, resolving and verifying containment before any
filesystem touch (NUL/invalid paths translate to typed refusals); `_verify_staged_asset` finally
checks existence, size, and sha256 against the staged bytes. Asset bytes never cross the wire —
only verified references ride submit.

The multiplexing extension keeps the same additive posture without adding an action: `_evidence_native_page`
now forwards the optional `threadId` payload key straight to cit:([`thread_id`], mcp/src/agents_remember/serving/harness_control_ipc.py:399-399)
through `_optional_text`. When the key is absent the call is byte-identical to before and reads the
parent/session thread; when present it selects that (sub-agent) multiplexed thread — the codex
app-server serves `thread/read` for every multiplexed thread, and adapters that do not multiplex
simply never see a non-None selector. The action set stays 20 under `ar-harness-control/v1`.

### Conventions

The wire is one bounded JSON object per line. Actions are kebab-case; payload field names are the
normalized camel-case names. The socket transports commands but does not decide acceptance.

### Invariants And Boundaries

- Same-user filesystem permissions are the local endpoint security boundary.
- Exact catalog/session identity is required on every request.
- Dispatch, identity, protocol, request validation, serialization, cancellation, and unrelated
  failures remain authoritative and loud. Only the two concrete peer-disconnect classes are
  contained after accepted dispatch; this is not a broad connection-error or fallback boundary.
- A delayed reply disconnect leaves an ambiguous accepted submission reconcilable through the bridge;
  it does not retry or silently degrade the request.
- Advertise and set address the exact running adapter instance; pre-session discovery does not use
  this socket.
- Endpoint transport is replaceable behind the protocol contract.
- Evidence actions cross only this user-private socket: payloads carry native frames (including
  user text) and never reach `snapshot.raw` or any public projection.
- Deque-sequence and native-cursor coordinate domains stay disjoint at the wire boundary; both
  evidence reads and the provenance batch are epoch-scoped.
- Asset bytes never cross the socket: only schema-validated references ride `submit`, the spool
  path is constructed by convention under the request-independent resolved
  `<endpoint-root>/assets` anchor, containment is verified before any filesystem touch, and
  size/sha256 are re-checked against the staged bytes at admission.
- The interrupt write and timeline read cross only this user-private socket, epoch-guarded; the
  timeline never carries bodies, and the recovery body crosses only inside the already
  `cockpit_only` withdrawal response.
- The 18 pre-existing actions stay byte-preserved; the two additive actions and the optional `assets`
  key keep the protocol at `ar-harness-control/v1` and unknown actions still fail typed.
- The `threadId` key on `evidence-native-page` is additive and optional: absent means the
  parent/session thread exactly as before (pre-multiplexing clients are byte-compatible), the IPC layer
  performs no thread-id validation of its own (the adapter's `thread/read` echo check stays the
  authority), and the action count and protocol version are unchanged.

### Todos

None known for the private IPC action set.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The bridge supplies ordered native truth and the blocking client applies first-byte retry safety.
The `threadId` selector lands on the bridge's additive `native_page(thread_id=...)`
parameter, whose `None` default keeps the parent-thread read byte-identical.

- The bridge exposes live advertise and ordered setter operations only while running. [1]
- The bridge's `native_page` accepts the additive `thread_id` selector (`None` = parent thread) and forwards it to multiplexing adapters. [2]
- The blocking client validates exact identity and distinguishes pre-write from post-write loss. [3]


| The channel bounds and the `InterruptResult`/`OperationTimeline` DTOs these actions serialize. | `MAX_OPERATION_TIMELINE_PAGE` | mcp/src/agents_remember/serving/harness_control_models.py:63-63 |
| The bridge's epoch-guarded interrupt dispatch and timeline delegation behind the two additive actions. | "interrupt adapter must not mint the bridge epoch" | mcp/src/agents_remember/serving/harness_control_bridge.py:303-303 |


### Cross-Repo References

No external repository boundary is implemented by the local exact-session socket.

No meaningful cross-repo references found.

## Submission Authority Delta

IPC dispatch now carries epoch/source through submit and exposes reconcile, resolve-operation,
authority, bounded status, and withdraw actions. Cockpit-only disclosure is enforced before raw-free
serialization; request ids and operation refs are validated structurally. Typed busy/conflict/epoch
errors retain their meaning across the private socket boundary.

## Bounded Message Ceiling Delta

The private control IPC accepts the raised bounded message ceiling needed for native interaction payloads while preserving its line-oriented timeout and framing contract. The ceiling is an explicit transport limit, not an unbounded read.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260727-CHATS-IM-L2 Typed History IPC Delta

The private IPC preserves child-history semantics in both directions.
`NativeHistoryLimitExceeded` serializes status, stable code, actual bytes, and limit bytes;
`NativeHistoryUnavailable` serializes status and code. The inverse decoder requires the same
typed fields before reconstructing either error cit:(["control request failed"], mcp/src/agents_remember/serving/harness_control_ipc.py:609-609). This makes the selected-child
boundary recoverable across Unix IPC without converting it into an undifferentiated
`HarnessControlError`.

## 260731-EFA-L2 Current Delta

The two `if action == …` dispatch chains were replaced by one `_CONTROL_ACTIONS` handler table
mapping each action name to a bound coroutine (`_handshake`, `_advertise`, `_set_model`,
`_set_effort`, `_submit`, `_submission_authority`, `_submission_status`, `_withdraw`, `_reconcile`,
`_transcript`, `_evidence`, …). An unknown action still raises `HarnessControlError(f"unknown
control action: {action}")` — that is now one refusal instead of two (the separate "unknown
capability action" message is gone because capability actions are ordinary table entries). Every
action's payload validation and response shape is unchanged.

**`StagedAssetClaim`** (`asset_id`, `mime_type`, `byte_size`, `sha256`) names what the wire CLAIMS
about one staged asset, **before the spooled file is read**. Every field is a claim to be verified
against the file on disk: the id locates it, and the mime type, byte size and digest are what must
match. Verifying one field against another asset's claim is exactly the substitution the digest
check exists to catch, so the claim travels as one value.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
