# harness_control_client.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_client.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Synchronous exact-session client for the Unix control socket owned by a hosted harness runner. It
is the serving boundary for live advertise, honest model/effort set, correlated whole-message
submission, reconciliation, interaction responses, transcript reads, and stop. 260718-CHATS-L0E
adds strictly validated reads for the evidence family: `read_control_evidence`,
`read_control_native_page`, and `read_submission_provenance`. 260718-CHATS-L2E adds the
epoch-guarded `interrupt_control` write, the paged `read_operation_timeline` read with strict
monotonicity/epoch/coherence validation, additive `assets` on `submit_control_prompt`, and strict
withdrawal-recovery parsing. 260718-CHATS-L5F deserializes the R1 evidence `nativeMethod` on the
frame round trip, and R6 maps a control-socket connect failure to an honest "already exited"
lifecycle note (unlinking the stale socket on `ECONNREFUSED`) instead of surfacing a raw
`[Errno 111]`.

## Code Commentary

### Logic

Every request carries protocol version and exact catalog identity. Capability and set responses are
strictly parsed through the normalized type layer; setter calls use a bound above Claude's native
correlated acceptance window. Submit sends the complete message and caller request id once.

`_exchange_control` (L509) distinguishes connect/pre-write failure from any failure after the socket
accepts the first byte. Pre-write failure raises as unavailable (`may_have_sent=False`) and may be
retried by policy. 260718-CHATS-L5F R6 routes that connect failure through
`_connect_unavailable_detail` (L486-L506): `ECONNREFUSED` (a stale socket file with nothing
listening — the developer's image1 `[Errno 111]` banner) and `ENOENT` (an absent socket) both map to
the honest "the controlled runner already exited (…)" note, and the stale socket is best-effort
`unlink`ed on `ECONNREFUSED` so the next probe reads the absent case cleanly instead of repeating the
refused surprise; a timeout and any other error get their own honest phrasings. On Linux AF_UNIX
`ECONNREFUSED` means no listener, so the unlink cannot orphan a live endpoint. Post-write loss,
malformed response, or mismatched post-dispatch evidence becomes an honest `unknown` receipt or
`SetResult` carrying the original request id/value; it is never resent. The explicit reconcile
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
raises `HarnessBridgeEpochMismatchError`, so cross-restart continuation fails detectably. 260718-
CHATS-L5F R1 deserializes the optional evidence `nativeMethod` on the frame round trip (L840-L851):
a present value must be non-empty text or the read fails typed, so the projector receives the
carried notification method the bridge preserved.

The L2E helpers hold the same strict posture. `interrupt_control` sends the epoch-guarded write
under the setter-class timeout and validates the acknowledgement enum, epoch continuity
(`_evidence_bridge_epoch`), and the `ControlOperationRef` round-trip. `read_operation_timeline`
rejects opaque string cursors typed before I/O, then validates shape, kind/source enums, positive
strictly increasing sequences, `evictedBeforeSequence ≤ latestSequence`, boolean `truncated` (an
empty page can never be truncated), `latestSequence ≥ last item`, and epoch continuity across
pages. `_withdrawal_recovery`/`_asset_reference` parse the additive recovery payload strictly when
present. `submit_control_prompt`'s additive `assets` argument is shape-checked by `_submit_payload`
(a sequence of objects, never a string) while asset-free payloads keep their exact previous key
order.

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
- Timeline pages must additionally be coherent across the read: strictly increasing sequences,
  floor ≤ high-water, non-truncated empty pages, `latestSequence` covering the last item, and one
  continuous epoch; opaque cursor coordinates are rejected typed before any I/O.
- The interrupt acknowledgement is validated (enum, epoch continuity, operation round-trip) and is
  never treated as settlement.
- Asset-free submit payloads keep their exact previous key order; `assets` rides only as a
  sequence of objects.
- A control-socket connect failure never leaks a raw errno: `ECONNREFUSED`/`ENOENT` map to the
  designed "already exited" note (R6), the stale socket is unlinked best-effort on `ECONNREFUSED`,
  and the failure stays `may_have_sent=False` (retry-safe pre-write).
- The evidence `nativeMethod` (R1) is parsed only when present and must be non-empty text; it is
  carried metadata, never a resend or acceptance signal.

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
| The private server dispatches advertise/set/submit/reconcile against one bridge identity. | L150-L250 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The queue facade treats request id as an idempotency key and returns retained reconciliation truth through the authority. | L93-L197 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |
| Client tests pin pre-first-byte versus post-first-byte ambiguity and unknown setter/submission mapping. | L61-L145 | [test_harness_control_client.py](agents-remember/mcp/tests/test_harness_control_client.py) |
| The R6 test pins that a refused control socket yields the honest note AND unlinks the stale socket (never a raw errno). | L61-L92 | [test_harness_control_client.py](agents-remember/mcp/tests/test_harness_control_client.py) |
| Real socket and durable-inbox regressions prove lost responses converge by same-id reconciliation without native resend. | L1036-L1153 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Contract tests pin the strict page/native-page/provenance validators, cross-domain typed rejection, and epoch-continuity failure exercised through this client. | L463-L1309 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |
| The IPC server answers the two additive actions and verifies staged assets before dispatch, so this client's references and reads stay reference-only and strictly shaped. | L212-L215; L252-L325 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Contract tests pin the strict interrupt/timeline/recovery validators, the cross-domain cursor rejection, and the epoch-flip typed failure through this client. | L1475-L1575; L918-L959 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |

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

## 260718-CHATS-L5I Current Delta

The control client applies the longer submit timeout only to the healthy submit-echo path and retains bounded control request handling. This prevents a normal delayed echo from being prematurely labelled unknown without widening unrelated calls.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R1 — documented the evidence `nativeMethod`
  deserialization on the frame round trip (present-must-be-non-empty-text, L840-L851). R6 —
  documented `_connect_unavailable_detail` (L486-L506): `ECONNREFUSED`/`ENOENT` map to the honest
  "already exited" note, the stale socket is unlinked on `ECONNREFUSED`, and no raw errno leaks
  (pre-write `may_have_sent=False`); added both invariants and the R6 regression citation.
  Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented `interrupt_control`, the paged
  `read_operation_timeline` (monotonicity, floor-vs-high-water, truncated/latest coherence,
  cross-page epoch continuity, cross-domain cursor rejection), additive `assets` on
  `submit_control_prompt` with byte-stable asset-free payloads, and the strict
  recovery/asset-reference validators. Verification metadata stays pinned until closeout stamps
  the candidate commit.
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
