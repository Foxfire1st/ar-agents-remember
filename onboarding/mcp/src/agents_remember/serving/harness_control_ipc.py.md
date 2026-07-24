# mcp/src/agents_remember/serving/harness_control_ipc.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_ipc.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides user-private Unix-domain-socket IPC for one exact-session bridge, with bounded JSON-line
requests and explicit snapshot, live advertise, model/effort set, submit, respond, reconcile,
transcript, and stop actions. 260718-CHATS-L0E adds exactly three additive read actions —
`evidence`, `evidence-native-page`, and `submission-provenance` — under the unchanged
`ar-harness-control/v1` protocol. 260718-CHATS-L2E adds two more additive actions — `interrupt`
and `operation-timeline` — plus the additive optional `assets` key on `submit` with schema
validation, resolve-and-verify spool confinement, and digest verification at admission.

## Code Commentary

### Logic

Endpoint names hash the complete control identity. Runtime directories are `0700`, sockets `0600`,
and non-socket replacements are refused. Every request validates protocol and identity before
dispatch. `advertise`, `set-model`, and `set-effort` serialize the bridge's normalized capability
and `SetResult` types; submit and reconcile retain full internal receipt evidence. After accepted
dispatch, narrow peer-loss exceptions are contained while the bridge remains the truth owner.

The three L0E actions are read-only and additive. `evidence` pages the bridge's deque-domain buffer
(`afterSequence`, bounded `limit` capped at `MAX_EVIDENCE_PAGE = 500`). `evidence-native-page`
pages harness-native history through the bridge with an opaque `cursor` and a server-bounded limit
(`MAX_NATIVE_EVIDENCE_PAGE = 200`); unsupported adapters fail closed typed. `submission-provenance`
requires `expectedBridgeEpoch` plus 1..64 unique `requestIds` and returns the authority's batch.
Every response in both evidence domains carries `bridgeEpoch`; the 14 pre-existing actions and the
one-request-per-connection model are byte-preserved, and unknown actions still fail typed.

The L2E actions follow the same additive posture (the set is now 20 actions). `interrupt` requires
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
- The 18 pre-L2E actions stay byte-preserved; the two additive actions and the optional `assets`
  key keep the protocol at `ar-harness-control/v1` and unknown actions still fail typed.

### Todos

None known for the L4 private IPC action set.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The bridge supplies ordered native truth and the blocking client applies first-byte retry safety.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The bridge exposes live advertise and ordered setter operations only while running. | L390-L401 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The blocking client validates exact identity and distinguishes pre-write from post-write loss. | L179-L325; L452-L560 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| IPC tests pin capability actions, setters, same-id submit retention, response loss, and reconciliation. | L988-L1285 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Evidence contract tests pin the three additive actions over a real socket: pages, continuation, cross-domain typed rejection, epoch mismatch, and provenance. | L463-L791 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |
| The channel bounds and the `InterruptResult`/`OperationTimeline` DTOs these actions serialize. | L75-L88; L332-L366 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The bridge's epoch-guarded interrupt dispatch and timeline delegation behind the two additive actions. | L241-L290 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| Contract tests pin the asset schema/traversal/verification batteries, the two actions end-to-end over a real socket, and the typed confinement refusals. | L1025-L1268; L864-L959 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |

## Cross-Repo References

No external repository boundary is implemented by the local exact-session socket.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

IPC dispatch now carries epoch/source through submit and exposes reconcile, resolve-operation,
authority, bounded status, and withdraw actions. Cockpit-only disclosure is enforced before raw-free
serialization; request ids and operation refs are validated structurally. Typed busy/conflict/epoch
errors retain their meaning across the private socket boundary.

## 260718-CHATS-L5I Current Delta

The private control IPC accepts the raised bounded message ceiling needed for native interaction payloads while preserving its line-oriented timeout and framing contract. The ceiling is an explicit transport limit, not an unbounded read.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

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
