# mcp/src/agents_remember/serving/harness_control_ipc.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_ipc.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

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
now forwards the optional `threadId` payload key straight to cit:([`thread_id`], mcp/src/agents_remember/serving/harness_control_ipc.py:395-395)
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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The bridge supplies ordered native truth and the blocking client applies first-byte retry safety.
The `threadId` selector lands on the bridge's additive `native_page(thread_id=...)`
parameter, whose `None` default keeps the parent-thread read byte-identical.

| Finding | Anchor | Source |
| --- | --- | --- |
| The bridge exposes live advertise and ordered setter operations only while running. | `submissions` | mcp/src/agents_remember/serving/harness_control_bridge.py:323-332 |
| The bridge's `native_page` accepts the additive `thread_id` selector (`None` = parent thread) and forwards it to multiplexing adapters. | `native_page` | mcp/src/agents_remember/serving/harness_control_bridge.py:226-271 |
| The blocking client validates exact identity and distinguishes pre-write from post-write loss. | "before any request bytes were accepted" | mcp/src/agents_remember/serving/harness_control_client.py:587-587 |
| IPC tests pin capability actions, setters, same-id submit retention, response loss, and reconciliation. | `test_exact_session_ipc_advertises_and_returns_set_acceptance` | mcp/tests/test_harness_control_ipc.py:148-181 |
| Evidence contract tests pin the three additive actions over a real socket: pages, continuation, cross-domain typed rejection, epoch mismatch, and provenance. | `test_evidence_action_round_trip_with_epoch_and_paging` | mcp/tests/test_harness_control_evidence_ipc.py:57-89 |
| The channel bounds and the `InterruptResult`/`OperationTimeline` DTOs these actions serialize. | `MAX_OPERATION_TIMELINE_PAGE` | mcp/src/agents_remember/serving/harness_control_models.py:113-113 |
| The bridge's epoch-guarded interrupt dispatch and timeline delegation behind the two additive actions. | "interrupt adapter must not mint the bridge epoch" | mcp/src/agents_remember/serving/harness_control_bridge.py:299-299 |
| Contract tests pin the asset schema/traversal/verification batteries, the two actions end-to-end over a real socket, and the typed confinement refusals. | `test_digest_and_size_verification` | mcp/tests/test_harness_control_plane_channels.py:167-216 |

## Cross-Repo References

No external repository boundary is implemented by the local exact-session socket.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

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
typed fields before reconstructing either error cit:(["control request failed"], mcp/src/agents_remember/serving/harness_control_ipc.py:605-605). This makes the selected-child
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

## Update History

- 2026-08-02T21:28:06+02:00 — 260731-EFA-L6 curator W2-B10: repaired 19 citation findings (8 reference rows and 3 prose pointers); scoped recheck clean.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the `test_harness_control.py` citation.
  The stamped `L988-L1285` sits inside `HarnessControlConformanceTests`, not the IPC suite; the
  IPC tests are `HarnessControlIpcTests` (opens L1355). The five behaviours the row names are
  L1423-L1670 — `test_exact_session_ipc_advertises_and_returns_set_acceptance` (capability read +
  both setters and their accept/unsupported acceptances),
  `test_outer_socket_lost_receipt_reconciles_retained_known_truth` and
  `test_durable_inbox_outer_loss_converges_by_reconcile_without_resend` (response loss +
  reconciliation), and `test_public_duplicate_returns_retained_result_with_one_adapter_call`
  (same-id retention, exactly one adapter submission) — plus L1844-L1898,
  `test_peer_timeout_after_submit_preserves_reconciliation_result`. Both ranges read back; claim
  unchanged.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `_CONTROL_ACTIONS` handler table (one unknown-action refusal) and `StagedAssetClaim` as the pre-verification wire claim.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented typed history
  unavailable/limit serialization and strict byte-evidence reconstruction across the private
  control IPC. Verification metadata remains pinned while uncommitted.

- 2026-07-26T15:37 — 260718-CHATS-L7 curator: documented the additive optional `threadId` payload
  key on `evidence-native-page` (`_evidence_native_page`, cit:([`thread_id`], mcp/src/agents_remember/serving/harness_control_ipc.py:395-395)) — the multiplexed-thread
  selector forwarded to `bridge.native_page`; absent = parent/session thread byte-identical to
  before, no new action, protocol unchanged. Added the additive/absent-means-parent invariant and
  refreshed the bridge (advertise L413-L425, native_page L209-L246, interrupt/timeline L264-L328),
  client (L186-L326; L475-L585), and models (L113-L122; L403-L443) citation ranges against the
  current sources. Verification metadata stays pinned: the L7 change is uncommitted, so no commit
  hash can attest it.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the two additive actions
  (`interrupt`, `operation-timeline`) and the additive `assets` submit key — schema validation,
  resolve-and-verify confinement under the request-independent assets anchor with the lexical
  separator/dot-segment ban and NUL translation, and admission-time size/sha256 verification —
  with the action set now 20 under the unchanged v1 protocol. Verification metadata stays pinned
  until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the three additive read actions
  (`evidence`, `evidence-native-page`, `submission-provenance`), their bounds and epoch scoping,
  and the byte-preserved 14-action/protocol baseline. Verification metadata stays pinned until
  closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented lifecycle IPC actions, epoch/source validation,
  cockpit privacy, bounded batches, and typed error preservation.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented exact-session advertise and set
  actions, normalized serialization, and retained private receipt evidence for ambiguity closure.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: documented narrow post-dispatch peer-disconnect
  containment during reply and close lifecycle, with delayed-reply reconciliation preserved.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for private exact-identity
  IPC, permissions, bounded messages, and explicit control operations.
