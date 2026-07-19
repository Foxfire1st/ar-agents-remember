# mcp/src/agents_remember/serving/harness_control_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04` |
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines protocol-neutral value objects and JSON projections for one hosted harness control session:
exact identity, handshake, normalized state, prompt and interaction requests, receipts,
reconciliation, transcript entries, and shutdown mode. L4 adds deliberately raw-free serializers
for the daemon's public submit and reconciliation responses. 260718-CHATS-L0E adds the additive,
read-only native evidence family: deque-domain and native-domain evidence pages, submission
provenance, the reserved `arEvidence` raw key, byte-bounded clip/window helpers, and the structural
`NativePageReader` protocol.

## Code Commentary

### Logic

The normalized snapshot keeps control (`starting`, `ready`, `disconnected`, `failed`,
`unsupported`), activity, and acceptance orthogonal while retaining raw vendor detail internally.
Request ids, correlation ids, timestamps, and exact AR/session identity remain explicit.
`receipt_json` and `reconciliation_json` preserve full internal evidence for private IPC and durable
diagnostics. `public_receipt_json` and `public_reconciliation_json` expose only normalized fields and
intentionally omit `raw` from the daemon consumer contract.

The L0E evidence family is purely additive. `AR_EVIDENCE_KEY` (`"arEvidence"`) is the single reserved
`AdapterEvent.raw` key under which mappers place one full native payload; every pre-existing raw key
keeps its exact shape. `EvidenceFrame`/`EvidencePage` carry the deque coordinate domain (adapter
event sequence, `latestSequence`, `evictedBeforeSequence`, `truncated`, `bridgeEpoch`);
`NativeEvidenceFrame`/`NativeEvidencePage` carry the native domain with typed identity
(`nativeId`/`nativeParentId`/`nativeType`) and an opaque `nextCursor`; `SubmissionProvenance{,Batch}`
carry request-id source/state/timestamps/vendor-correlation with an epoch stamp. The two coordinate
domains are disjoint and never mixed. `clip_evidence_payload` bounds one serialized payload to a byte
budget with a visible `…[truncated]` marker envelope; `window_native_evidence_page` + `_native_window_start`
window a full native read into a bounded page whose cursor names the last native id of the previous
page, clipping a single oversized frame so every page makes progress. The runtime-checkable
`NativePageReader` structural protocol lets concrete adapters opt into native paging without editing
`HarnessProtocolAdapter`.

### Conventions

Internal serializers preserve additive vendor evidence; public serializers are separate named
functions rather than an exclusion flag so callers cannot accidentally leak the private mapping.
Wire names are camel-case.

### Invariants And Boundaries

- Models carry protocol state; tmux pane text and terminal logs are diagnostic, not authoritative.
- Additive raw event detail is retained without guessing semantics for unknown event kinds.
- Disconnect-after-possible-send remains unknown and must be reconciled, never blindly resent.
- Public receipt/reconciliation responses retain normalized correlation and detail but never `raw`.
- The evidence family is additive and read-only: no existing DTO or serializer changes shape or
  semantics, and unknown native shapes cross as unknown-vendor evidence with raw preserved and
  semantics never guessed.
- Evidence frames are evidence, not authority; deep history stays with the native read APIs.
- Deque-sequence and native-cursor coordinates are disjoint domains; `bridgeEpoch` rides every
  evidence response so a mid-paging bridge restart fails detectably.

### Todos

None known for the L4 public serialization boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The API consumes only the public projections, while private IPC keeps full internal serializers. The
L0E evidence DTOs are consumed by the bridge buffer, the three additive IPC actions, and the
validated client reads.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The daemon submit and reconcile routes select the public raw-free serializers. | L173-L210 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| Private IPC still serializes full receipts and reconciliation evidence for exact-session peers. | L180-L227 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Public route tests seed sensitive-looking raw mappings and prove they do not cross the boundary. | L166-L219 | [test_serving_harness_control_api.py](agents-remember/mcp/tests/test_serving_harness_control_api.py) |
| The bridge diverts `arEvidence` payloads into its bounded deque and stamps the epoch on every evidence page. | L85-L88; L168-L232; L440-L471 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The three additive IPC actions serialize these evidence/provenance DTOs onto the private socket. | L198-L203; L286-L313 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Contract tests pin the evidence round-trips, bounds, no-leak guarantee, continuation, and provenance matrix over these DTOs. | L268-L1460 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |

## Cross-Repo References

No external repository boundary is implemented by these local protocol models.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

The normalized model now carries bridge epoch on prompts, receipts, and reconciliation; defines full
operation references, authority/status/batch/withdraw/event records; and separates private internal
serialization from raw-free public lifecycle projection. The public alphabet is intentionally
smaller than vendor evidence and sufficient for monotonic cockpit rendering.

## Update History

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the additive native evidence
  family — the reserved `arEvidence` raw key, deque-domain `EvidenceFrame`/`EvidencePage`,
  native-domain `NativeEvidenceFrame`/`NativeEvidencePage` with typed identity and opaque
  continuation, `SubmissionProvenance{,Batch}`, the structural `NativePageReader` protocol, and the
  byte-bounded clip/window helpers. Verification metadata stays pinned to the last committed source
  until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: added generation-bound submit records, full operation refs,
  normalized status/withdraw DTOs, and explicit public/private serialization boundaries.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the explicit public receipt and
  reconciliation serializers that preserve normalized evidence while omitting adapter-private raw.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the normalized
  control models, identity/correlation state, raw vendor detail, and R11 draft ownership.
