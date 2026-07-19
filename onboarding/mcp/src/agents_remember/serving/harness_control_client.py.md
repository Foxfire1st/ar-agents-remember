# harness_control_client.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_client.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04` |
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Synchronous exact-session client for the Unix control socket owned by a hosted harness runner. It
is the serving boundary for live advertise, honest model/effort set, correlated whole-message
submission, reconciliation, interaction responses, transcript reads, and stop. 260718-CHATS-L0E
adds strictly validated reads for the evidence family: `read_control_evidence`,
`read_control_native_page`, and `read_submission_provenance`.

## Code Commentary

### Logic

Every request carries protocol version and exact catalog identity. Capability and set responses are
strictly parsed through the normalized type layer; setter calls use a bound above Claude's native
correlated acceptance window. Submit sends the complete message and caller request id once.

`_exchange_control` distinguishes connect/pre-write failure from any failure after the socket accepts
the first byte. Pre-write failure raises as unavailable and may be retried by policy. Post-write
loss, malformed response, or mismatched post-dispatch evidence becomes an honest `unknown` receipt
or `SetResult` carrying the original request id/value; it is never resent. The explicit reconcile
operation queries the bridge's retained same-id truth.

The L0E evidence reads validate responses strictly rather than trusting JSON coercion:
`read_control_evidence` enforces monotonic frame sequences, `latestSequence` coherence, and typed
rejection of native-cursor coordinates in the deque domain; `read_control_native_page` rejects
adapter-sequence coordinates in the native domain, enforces native-id uniqueness, and requires
`nextCursor` continuation coherence (an empty page cannot carry a cursor, and the cursor must
continue the last frame) under the dedicated `EVIDENCE_PAGE_TIMEOUT_SECONDS = 35.0` bound (the
`SET_CONTROL_TIMEOUT_SECONDS` precedent, above the 2-second control default);
`read_submission_provenance` enforces exact result count/order, valid sources, and request-id echo.
Every evidence response carries `bridgeEpoch`; a caller-supplied expected epoch that mismatches
raises `HarnessBridgeEpochMismatchError`, so cross-restart continuation fails detectably.

### Conventions

The client is blocking because its FastAPI and MCP callers are synchronous. It validates the
long-lived subprocess peer rather than trusting JSON coercion. The 35-second set timeout is a
protocol bound, not an invented acceptance result.

### Invariants And Boundaries

- The catalog row's exact identity and endpoint are authoritative on every request.
- A request is safe to retry only when no byte was accepted; after first-byte acceptance it remains
  unknown until same-id reconciliation.
- No capability mutation or prompt falls back to terminal/composer input.
- Setter responses must echo the requested value or are downgraded to unknown.
- Vendor raw detail remains internal; public route shaping belongs to the API/model serializers.
- Evidence reads reject cross-domain coordinates typed before any I/O: native cursors never enter
  the deque domain and adapter sequences never enter the native domain.
- Evidence page/native page/provenance responses must be internally coherent (monotonicity,
  uniqueness, continuation, exact counts) or the read fails with a typed client error.

### Todos

None known for the L4 exact-session client.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The IPC server and queue retain exact-session truth; durable inbox redelivery consumes the same
unknown/reconcile contract without a second submission.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The private server dispatches advertise/set/submit/reconcile against one bridge identity. | L127-L227 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The queue treats request id as an idempotency key and returns retained reconciliation truth. | L114-L145; L378-L411 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |
| Client tests pin pre-first-byte versus post-first-byte ambiguity and unknown setter/submission mapping. | L61-L145 | [test_harness_control_client.py](agents-remember/mcp/tests/test_harness_control_client.py) |
| Real socket and durable-inbox regressions prove lost responses converge by same-id reconciliation without native resend. | L1036-L1153 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Contract tests pin the strict page/native-page/provenance validators, cross-domain typed rejection, and epoch-continuity failure exercised through this client. | L463-L1309 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |

## Cross-Repo References

No external repository boundary is implemented by the local Unix-socket client.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

The exact-session client now reads authority/status/withdraw and sends epoch-bound submit/reconcile.
Its byte classifier distinguishes no-byte, first-byte-possible, and decoded typed errors; parser
logic preserves the normalized lifecycle alphabet while stripping private raw evidence. A post-write
transport loss is returned as ambiguous, never reclassified into retry safety.

## Update History

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the three validated evidence reads,
  the 35-second native-page timeout precedent, cross-domain typed coordinate rejection,
  continuation/native-id coherence checks, exact provenance count/order validation, and
  epoch-continuity `HarnessBridgeEpochMismatchError`. Verification metadata stays pinned until
  closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented generation-bound lifecycle calls, first-byte
  classification, typed-error decoding, privacy parsing, and no-resend ambiguity.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented live advertise/set, strict
  normalized parsing, whole-message submit, first-byte retry safety, and same-id ambiguity closure.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented identity-bound protocol requests,
  correlated acceptance/reconciliation, interaction responses, and no raw-terminal fallback.
