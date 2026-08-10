# mcp/tests/test_harness_control_client.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_client.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T15:55+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused retry-safety coverage for the blocking exact-session harness-control client. It pins the
first-byte ambiguity boundary for submit and setter calls so a transport failure can never cause a
blind duplicate native command.

## Code Commentary

### Logic

`HarnessControlWriteCompletionTests` pins the write-completion contract: `_WholeWriteSocket` accepts
the entire request in one `send` and raises `BrokenPipeError` from `sendall`, proving the client
issues no remainder write when nothing remains; a partial-write companion proves a genuine remainder
is still written. Without that contract the zero-length send raised `EPIPE` after the server closed,
which is the intermittent broken pipe that blocked the commit gate (260727-CHATS-IM-L4).

A socket double fails either before its first `send` accepts a byte or after that first byte while
`sendall` completes the request. The tests require `HarnessControlClientError.may_have_sent` to be
false in the first case and true in the second. Post-write submit loss returns an `unknown`
`SubmissionReceipt` with the caller's original request id; an incoherent response carrying another
request id is also reduced to unknown without adopting its vendor correlation. Post-write model-set
loss returns an honest `SetResult(ok=False, acceptance="unknown")` for the requested value. Every
case asserts exactly one client request and therefore no transport retry.

The 260718-CHATS-L5F R6 addition,
`test_refused_control_socket_yields_honest_note_and_unlinks_stale_socket`, pins the control-stop
exit-path repair: a control-socket `connect()` that raises `ECONNREFUSED` (the socket file exists but
nothing is listening — an unclean runner exit) is mapped by `_connect_unavailable_detail` to the
honest "already exited (stale control socket…)" lifecycle note rather than a raw `[Errno 111]`
surprise, and the stale socket is unlinked so the next probe reads the absent (ENOENT) case. On Linux
AF_UNIX, ECONNREFUSED means no listener, so the unlink cannot orphan a live endpoint.

`test_native_page_serializes_thread_id_only_when_set` pins the multiplexed selector at the client
serialization seam: `read_control_native_page` emits the additive `threadId` on the
`evidence-native-page` request only when set, and an unset selector produces the byte-identical
pre-multiplex single-thread request (limit plus optional cursor, nothing else).

### Conventions

The module uses a minimal context-manager socket fake and `unittest.mock` at the Unix-socket
constructor or `request_control` seam. It tests transport classification and public helper behavior
without starting an adapter, server, or terminal process.

### Invariants And Boundaries

- `may_have_sent` becomes true only after the socket accepts at least one request byte.
- A socket that accepts the whole request in one `send` must see NO second write: the fake's
  `sendall` raises unconditionally, so reaching it fails the test. The partial-write companion keeps
  the remainder path honest, since the `_Socket` base returns a one-byte `send`.
- A pre-write failure remains a loud client error; a post-write failure becomes an honest unknown
  outcome with the original request id or requested setter value.
- A mismatched response cannot donate request or vendor correlation evidence to the caller.
- Submit and setter helpers issue one request only; retry/reconciliation is an explicit caller
  operation, never an automatic resend.
- A refused control socket yields the honest lifecycle note (never a raw errno) and unlinks the stale
  socket so the next probe reads ENOENT (260718-CHATS-L5F R6).

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test source is the direct authority for byte-boundary classification; the client implementation
owns the corresponding exact-session request encoding and unknown-result conversion.

| Finding | Anchor | Source |
| --- | --- | --- |
| The pre-accept socket case keeps `may_have_sent` false before any byte is accepted. | "test_may_have_sent_is_false_until_socket_accepts_a_byte"; `send_error` | mcp/tests/test_harness_control_client.py:182-191 |
| The post-accept socket case records `may_have_sent` true after the first byte is accepted. | "test_may_have_sent_is_true_after_socket_accepts_a_byte"; `sendall_error` | mcp/tests/test_harness_control_client.py:193-202 |
| Post-write submit loss and a mismatched receipt both remain unknown under the original request id with one request call. | `test_post_write_submit_failure_returns_unknown_with_same_request_id`; `test_mismatched_receipt_stays_unknown_and_is_not_resent`; "response timed out"; "different-request" | mcp/tests/test_harness_control_client.py:204-215; mcp/tests/test_harness_control_client.py:262-282 |
| A post-write setter failure returns unknown for the requested model and is not retried. | `test_post_write_set_failure_returns_unknown_without_retry`; "response reset" | mcp/tests/test_harness_control_client.py:284-294 |
| The blocking client preserves whole UTF-8 JSON text, records the first accepted byte, and reports the exact failure stage. | `request_control`; `_encode_control_request`; `_exchange_control` | mcp/src/agents_remember/serving/harness_control_client.py:479-491; mcp/src/agents_remember/serving/harness_control_client.py:494-508; mcp/src/agents_remember/serving/harness_control_client.py:534-568 |
| Submit and set helpers convert only post-write uncertainty into normalized unknown evidence while pre-write failures stay loud. | `submit_control_prompt`; `_set_control_value`; "def _unknown_set_result(value: str"; "def _submission_receipt(" | mcp/src/agents_remember/serving/_harness_control_parsing.py:114-114; mcp/src/agents_remember/serving/harness_control_claude.py:679-679; mcp/src/agents_remember/serving/harness_control_client.py:216-254; mcp/src/agents_remember/serving/harness_control_client.py:584-610 |
| `_connect_unavailable_detail` maps a refused control socket to the honest exit note and unlinks the stale socket (R6). | `_connect_unavailable_detail` | mcp/src/agents_remember/serving/harness_control_client.py:520-540 |

## Cross-Repo References

No sibling repository is needed to prove this local Unix-socket retry-safety boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

Client regressions now cover the submit-specific delayed-echo timeout and retain the control client's bounded request semantics for other calls.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260731-EFA-L2 Delta — `SubmissionStatusLookupTests`

A new class covering the submission-status lookup decoder, all of it refusal-shaped:

- a found lookup carries its status **verbatim**; a not-found lookup needs no evidence;
- a non-object payload is refused;
- **a lookup answering for another request id is refused rather than re-keyed** — silently
  adopting a foreign id is how one request's outcome gets attributed to another;
- an unknown outcome, missing evidence, a non-boolean `withdrawable`, and a found lookup with
  no usable lifecycle state are each refused rather than defaulted.

## Update History

- 2026-08-04T15:32:44+02:00 — 260731-EFA-L6 S18-B08 curator: rebound post-write submit, mismatched-receipt, and setter claims to complete focused-test function extents containing their calls and assertions; the scoped fixer/check remain green.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-30T15:55+02:00 — 260727-CHATS-IM-L4: recorded `HarnessControlWriteCompletionTests`, which
  pins that a fully accepted request issues no remainder write while a partial one still does.
- 2026-07-26T18:30+02:00 — 260718-CHATS-L7 curator: recorded the client serialization test for the
  multiplexed selector (`test_native_page_serializes_thread_id_only_when_set`) — `threadId` is
  emitted on the `evidence-native-page` request only when set, so the unset request stays the
  byte-identical pre-multiplex single-thread shape. One Logic paragraph added; verification
  metadata stays pinned (uncommitted); closeout re-stamps the candidate commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R6 exit-path test
  (`test_refused_control_socket_yields_honest_note_and_unlinks_stale_socket`) — a refused control
  socket maps to the honest "already exited (stale control socket…)" note and unlinks the stale
  socket so the next probe reads ENOENT, never a raw `[Errno 111]`. Verification metadata stays
  pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the one-to-one sidecar for first-byte
  ambiguity, original-correlation preservation, incoherent-response handling, honest unknown setter
  evidence, and the no-automatic-retry invariant. The source is new and uncommitted, so verification
  hash and date remain empty until closeout.
