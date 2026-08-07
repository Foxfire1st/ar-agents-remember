# harness_control_client.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_client.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Synchronous exact-session client for the Unix control socket owned by a hosted harness runner. It
is the serving boundary for live advertise, honest model/effort set, correlated whole-message
submission, reconciliation, interaction responses, transcript reads, and stop. It also provides
strictly validated reads for the evidence family: `read_control_evidence`,
`read_control_native_page`, and `read_submission_provenance`. The control-plane surface adds the
epoch-guarded `interrupt_control` write, the paged `read_operation_timeline` read with strict
monotonicity/epoch/coherence validation, additive `assets` on `submit_control_prompt`, and strict
withdrawal-recovery parsing. The evidence `nativeMethod` is deserialized on the frame round trip,
and a control-socket connect failure maps to an honest "already exited" lifecycle note (unlinking
the stale socket on `ECONNREFUSED`) instead of surfacing a raw `[Errno 111]`. The multiplexed
control plane adds the per-thread `thread_id` selector on `read_control_native_page`, parses the
plural `pendingInteractions` on snapshots, and reads the optional evidence `threadId` wire key
back into `EvidenceFrame.thread_id`.

## Code Commentary

### Logic

Every request carries protocol version and exact catalog identity. Capability and set responses are
strictly parsed through the normalized type layer; setter calls use a bound above Claude's native
correlated acceptance window. Submit sends the complete message and caller request id once.

cit:([`_exchange_control`], mcp/src/agents_remember/serving/harness_control_client.py:534-568) distinguishes connect/pre-write failure from any failure after the socket
accepts the first byte. Pre-write failure raises as unavailable (`may_have_sent=False`) and may be
retried by policy. The remainder write is CONDITIONAL: `send` usually accepts the whole request, and
`sendall` is a do-while over its buffer, so calling it with an empty remainder still issued one
zero-length send. Once the server had answered and closed with the request drained, the peer was gone
and that pointless write raised `EPIPE` — turning an exchange the server actually completed into a
`may_have_sent=True` disconnect that forces reconciliation. Only a non-empty remainder is written now
(260727-CHATS-IM-L4). A connect failure routes through
cit:([`_connect_unavailable_detail`], mcp/src/agents_remember/serving/harness_control_client.py:532-552): `ECONNREFUSED` (a stale socket file with nothing
listening — the observed `[Errno 111]` banner) and `ENOENT` (an absent socket) both map to
the honest "the controlled runner already exited (…)" note, and the stale socket is best-effort
`unlink`ed on `ECONNREFUSED` so the next probe reads the absent case cleanly instead of repeating the
refused surprise; a timeout and any other error get their own honest phrasings. On Linux AF_UNIX
`ECONNREFUSED` means no listener, so the unlink cannot orphan a live endpoint. Post-write loss,
malformed response, or mismatched post-dispatch evidence becomes an honest `unknown` receipt or
`SetResult` carrying the original request id/value; it is never resent. The explicit reconcile
operation queries the bridge's retained same-id truth.

The evidence reads validate responses strictly rather than trusting JSON coercion:
`read_control_evidence` enforces monotonic frame sequences, `latestSequence` coherence, and typed
rejection of native-cursor coordinates in the deque domain; `read_control_native_page` rejects
adapter-sequence coordinates in the native domain, enforces native-id uniqueness, and requires
`nextCursor` continuation coherence (an empty page cannot carry a cursor, and the cursor must
continue the last frame) under the dedicated `EVIDENCE_PAGE_TIMEOUT_SECONDS = 35.0` bound (the
`SET_CONTROL_TIMEOUT_SECONDS` precedent, above the 2-second control default);
`read_submission_provenance` enforces exact result count/order, valid sources, and request-id echo.
Every evidence response carries `bridgeEpoch`; a caller-supplied expected epoch that mismatches
raises `HarnessBridgeEpochMismatchError`, so cross-restart continuation fails detectably. The
optional evidence `nativeMethod` is deserialized on the frame round trip (cit:(["def _evidence_page(result: object, *, expected_bridge_epoch"], mcp/src/agents_remember/serving/_harness_control_parsing.py:348-348)):
a present value must be non-empty text or the read fails typed, so the projector receives the
 carried notification method the bridge preserved. The optional evidence `threadId` rides the same
 frame parse (cit:(["def _evidence_page(result: object, *, expected_bridge_epoch"], mcp/src/agents_remember/serving/_harness_control_parsing.py:348-348)): a present value must be non-empty text or the
read fails typed, and an absent key yields `None` — the parent thread — so the multiplexed demux
key the models serialize reaches the projector verbatim.

Two multiplex seams live here. cit:([`read_control_native_page`], mcp/src/agents_remember/serving/harness_control_client.py:369-401) gained the
additive `thread_id` selector: it rides the payload as `threadId` only when set (cit:([`read_control_native_page`, "threadId"], mcp/src/agents_remember/serving/harness_control_client.py:387-419)), so a
`None` reads the parent/session thread with the exact pre-multiplexing request shape. And `_snapshot` now
parses the plural pending set (cit:(["def _snapshot(raw: Mapping[str, object]) -> AdapterSnapshot:  # pragma: no cover", `pendingInteractions`], mcp/src/agents_remember/serving/_harness_control_parsing.py:637-637; mcp/src/agents_remember/serving/_harness_control_parsing.py:654-654)): the singular `pendingInteraction`
parse was extracted verbatim into the shared strict `_pending_interaction` helper (cit:(["def _pending_interaction(raw: object) -> PendingInteraction:  # pragma: no cover"], mcp/src/agents_remember/serving/_harness_control_parsing.py:617-617) —
same required-text/choices/questions validation), and the additive `pendingInteractions` list maps
each entry through it. The plural key is OPTIONAL — absent on pre-multiplexing bridges it deserializes to the
empty tuple — but a present non-list value fails typed, so a malformed multiplex payload is never
silently truncated to the parent view.

The control-plane helpers hold the same strict posture. `interrupt_control` sends the epoch-guarded write
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
  designed "already exited" note, the stale socket is unlinked best-effort on `ECONNREFUSED`,
  and the failure stays `may_have_sent=False` (retry-safe pre-write).
- A request the socket accepted whole issues NO further write. A completed exchange must never be
  reported as a disconnect, so the client never performs a write it has no bytes for.
- The evidence `nativeMethod` is parsed only when present and must be non-empty text; it is
  carried metadata, never a resend or acceptance signal.
- The evidence `threadId` is parsed only when present and must be non-empty text; absent reads as
  `None` = the parent thread, so the multiplexed demux key crosses the wire verbatim and is never
  invented.
- The snapshot's plural `pendingInteractions` is additive and optional: absent
  means `()` (the pre-multiplexing bridge shape), a present non-list fails typed, and every entry passes the
  same strict `_pending_interaction` validation as the singular parent slot.
- The native-page `thread_id` selector is sent only when set; a `None` selector produces the exact
  pre-multiplexing request payload, so single-thread bridges see no contract change.

### Todos

None known for the exact-session client.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The IPC server and queue retain exact-session truth; durable inbox redelivery consumes the same
unknown/reconcile contract without a second submission.

| Finding | Anchor | Source |
| --- | --- | --- |
| The private server dispatches advertise/set/submit/reconcile against one bridge identity. | `HarnessControlServer` | mcp/src/agents_remember/serving/harness_control_ipc.py:99-412 |
| Request id is the idempotency key and retained reconciliation truth comes back from the authority directly, with no facade in the path since 260731-EFA-L6. | `HarnessSubmissionAuthority` | mcp/src/agents_remember/serving/harness_submission_authority.py:116-1023 |
| Client tests pin pre-first-byte versus post-first-byte ambiguity and unknown setter/submission mapping. | `HarnessControlClientRetrySafetyTests` | mcp/tests/test_harness_control_client.py:149-319 |
| A regression test pins that a refused control socket yields the honest note AND unlinks the stale socket (never a raw errno). | `test_refused_control_socket_yields_honest_note_and_unlinks_stale_socket` | mcp/tests/test_harness_control_client.py:150-180 |
| Real socket and durable-inbox regressions prove lost responses converge by same-id reconciliation without native resend. | `test_outer_socket_lost_receipt_reconciles_retained_known_truth`, `test_durable_inbox_outer_loss_converges_by_reconcile_without_resend` | mcp/tests/test_harness_control_ipc.py:183-222; mcp/tests/test_harness_control_ipc.py:224-294 |
| Contract tests pin the strict page/native-page/provenance validators, cross-domain typed rejection, and epoch-continuity failure exercised through this client. | `EvidenceIpcTests` | mcp/tests/test_harness_control_evidence_ipc.py:48-337 |
| The IPC server answers the two additive actions and verifies staged assets before dispatch, so this client's references and reads stay reference-only and strictly shaped. | `HarnessControlServer` | mcp/src/agents_remember/serving/harness_control_ipc.py:99-412 |
| Contract tests pin the strict interrupt/timeline/recovery validators, the cross-domain cursor rejection, and the epoch-flip typed failure through this client. | `ClientValidationTests` | mcp/tests/test_harness_control_plane_recovery.py:107-207 |

## Cross-Repo References

No external repository boundary is implemented by the local Unix-socket client.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Submission Authority Delta

The exact-session client now reads authority/status/withdraw and sends epoch-bound submit/reconcile.
Its byte classifier distinguishes no-byte, first-byte-possible, and decoded typed errors; parser
logic preserves the normalized lifecycle alphabet while stripping private raw evidence. A post-write
transport loss is returned as ambiguous, never reclassified into retry safety.

## Submit Echo Timeout Delta

The control client applies the longer submit timeout only to the healthy submit-echo path and retains bounded control request handling. This prevents a normal delayed echo from being prematurely labelled unknown without widening unrelated calls.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Multiplexed Control Plane Delta

The client now speaks the multiplexed control plane: `read_control_native_page` carries the additive `threadId` selector (parent thread when absent), and `_snapshot` parses the plural `pendingInteractions` through the extracted strict `_pending_interaction` helper — optional/absent-tolerant for pre-multiplexing bridges, typed-fatal on a malformed list. The singular `pendingInteraction` parse is byte-identical to before, now shared.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260727-CHATS-IM-L2 Opaque Cursor And Typed History Delta

The client reconstructs `NativeHistoryLimitExceeded` with exact byte evidence and
`NativeHistoryUnavailable` with its stable code from private control responses (cit:(["def _decode_control_response(response: bytes) -> object:  # pragma: no cover"], mcp/src/agents_remember/serving/_harness_control_parsing.py:63-63)).
Native-page `nextCursor` is now treated as an opaque adapter continuation rather than required to
equal the final frame's native id (cit:(["def _native_evidence_page(  # pragma: no cover", "def _native_evidence_frames(  # pragma: no cover"], mcp/src/agents_remember/serving/_harness_control_parsing.py:399-399; mcp/src/agents_remember/serving/_harness_control_parsing.py:421-421)). Page shape, duplicate-id checks, epoch validation,
and non-empty-page continuation rules remain strict.

## 260731-EFA-L2 Current Delta

**`ControlSubmission`** (`source`, `request_id`, `submitted_at`, `expected_bridge_epoch`, `assets`)
is now the second argument of `submit_control_prompt(text, submission)`: **everything about one
submission except its text** — who sent it, as what, against which epoch. The request id makes the
submission idempotent, the source decides which authority owns it, the epoch is the bridge
generation it is valid against, and the assets are the bytes it references. A request id replayed
with a different source or epoch is a *different* submission, and the wire payload
(`_submit_payload`) is built from all of them at once.

Two parsing guards were made structural rather than repeated:

- `_submission_lookup(raw_lookup, *, expected_id)` — one lookup out of a status batch, verified
  against the id asked for **at that position**. The id/order mismatch, invalid outcome, non-boolean
  `withdrawable` and missing-state refusals all still raise `HarnessControlError`; they now live in
  one place instead of inline in the batch loop.
- `_submission_state(value)` is now overloaded and **raises** for anything outside the seven
  lifecycle states. `optional=True` is the only way to get `None` back, and it means the field was
  absent. Because `None` never survives a required call, callers no longer re-check for it — the
  removed `"operation timeline item requires lifecycle state"` raise was that duplicate check, not a
  relaxation: a timeline item with a missing or bogus state still fails loudly, one call earlier.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: now a facade over `_harness_control_parsing.py` for the raw-response parsers; patch targets (`request_control`/`socket.socket`) keep working and the surface is pinned. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 8 repository-internal reference rows for the IPC server, submission authority, client retry tests, socket/reconciliation regressions, evidence validators, and control-plane validation tests; scoped citation verification follows.

- 2026-08-02T01:42+02:00 — 260731-EFA-L6 deleted-source cleanup. `serving/harness_control_queue.py` was deleted outright by the L6 class-split work (a pure forwarding facade), and its mirrored sidecar was removed with it. **Curator's judgement, stated rather than assumed: the card had no subject left.** Every invariant it carried was either the facade's own NON-behavior ("cannot enqueue work behind the authority", "holds no facade state, mutates nothing") or was explicitly attributed to `harness_submission_authority.py`, so nothing moved with the deletion and no knowledge needed rehoming — which is also why no replacement card was manufactured. Present-tense claims that `HarnessControlQueue` "is a facade" were corrected here to say it no longer exists; dated history entries naming it are preserved verbatim. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations. `_exchange_control`
  cited the single line L530 (now inside `_connect_unavailable_detail`); the function with its
  pre-write / post-write split and the conditional remainder write is L534-L568. The evidence
  `nativeMethod` parse cited L871-L875 → L891-L895 (the `raw_frame.get("nativeMethod")` read plus
  its non-empty-text refusal). `read_control_native_page`'s additive selector cited L391-L392, which
  is the `cursor` branch; the `threadId` payload key is set at L393-L394.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The two
  lost-response regressions now read at cit:([`test_outer_socket_lost_receipt_reconciles_retained_known_truth`, `test_durable_inbox_outer_loss_converges_by_reconcile_without_resend`], mcp/tests/test_harness_control_ipc.py:183-222; mcp/tests/test_harness_control_ipc.py:224-294), both in
  `HarnessControlIpcTests` and both asserting `adapter.reconciliation_requests == []`. The prior
  range landed in the fake-adapter bridge tests.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `ControlSubmission`, the `_submission_lookup` extraction, and the overloaded `_submission_state` that now refuses non-members itself (the removed timeline re-check was a duplicate, not a relaxation).
- 2026-07-30T15:55+02:00 — 260727-CHATS-IM-L4: recorded the conditional remainder write in
  `_exchange_control`. An empty remainder still issued a zero-length send, which raised `EPIPE` after
  the server answered and closed, reporting a completed exchange as a `may_have_sent` disconnect; it
  surfaced as an intermittent broken pipe that blocked the commit gate under full-suite load.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: recorded typed native-history error
  reconstruction and the opaque continuation contract, including removal of the obsolete
  `nextCursor == last nativeId` assumption. Verification metadata stays pinned while uncommitted.

- 2026-07-27T00:02+02:00 — 260718-CHATS-L7R curator: recorded the evidence `threadId` parse — the
  `_evidence_page` frame loop reads the optional wire key into `EvidenceFrame.thread_id`
  (present-must-be-non-empty-text, L868-L870; assigned onto the frame at L878), so the multiplexed
  demux key now survives the IPC round trip to the projector; absent yields `None` = the parent
  thread, keeping the pre-multiplex read shape. Verification metadata stays pinned — the change is
  uncommitted.
- 2026-07-26T15:34 — 260718-CHATS-L7 curator: documented the additive `thread_id` selector on
  `read_control_native_page` (present-only `threadId` payload key) and the plural
  `pendingInteractions` snapshot parse (extracted `_pending_interaction` helper, absent-tolerant,
  non-list typed failure); refreshed the R6/R1 citation line ranges (L507-L528, L530, L863-L874)
  for the L7-shifted source. Verification metadata stays pinned to the pre-commit source history
  until closeout (the L7 change is uncommitted).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R1 — documented the evidence `nativeMethod`
  deserialization on the frame round trip (present-must-be-non-empty-text, cit:(["def _evidence_page(result: object, *, expected_bridge_epoch"], mcp/src/agents_remember/serving/_harness_control_parsing.py:348-348)). R6 —
  documented `_connect_unavailable_detail` (cit:([`_connect_unavailable_detail`], mcp/src/agents_remember/serving/harness_control_client.py:532-552)): `ECONNREFUSED`/`ENOENT` map to the honest
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
