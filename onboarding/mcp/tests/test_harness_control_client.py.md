# mcp/tests/test_harness_control_client.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_client.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused retry-safety coverage for the blocking exact-session harness-control client. It pins the
first-byte ambiguity boundary for submit and setter calls so a transport failure can never cause a
blind duplicate native command.

## Code Commentary

### Logic

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

### Conventions

The module uses a minimal context-manager socket fake and `unittest.mock` at the Unix-socket
constructor or `request_control` seam. It tests transport classification and public helper behavior
without starting an adapter, server, or terminal process.

### Invariants And Boundaries

- `may_have_sent` becomes true only after the socket accepts at least one request byte.
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test source is the direct authority for byte-boundary classification; the client implementation
owns the corresponding exact-session request encoding and unknown-result conversion.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Socket failures before and after the first accepted byte produce false and true `may_have_sent` respectively. | L30-L81 | [test_harness_control_client.py](agents-remember/mcp/tests/test_harness_control_client.py) |
| Post-write submit loss and a mismatched receipt both remain unknown under the original request id with one request call. | L83-L118 | [test_harness_control_client.py](agents-remember/mcp/tests/test_harness_control_client.py) |
| A post-write setter failure returns unknown for the requested model and is not retried. | L120-L130 | [test_harness_control_client.py](agents-remember/mcp/tests/test_harness_control_client.py) |
| The blocking client preserves whole UTF-8 JSON text, records the first accepted byte, and reports the exact failure stage. | L205-L263 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| Submit and set helpers convert only post-write uncertainty into normalized unknown evidence while pre-write failures stay loud. | L99-L136; L282-L317 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| `_connect_unavailable_detail` maps a refused control socket to the honest exit note and unlinks the stale socket (R6). | — | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |

## Cross-Repo References

No sibling repository is needed to prove this local Unix-socket retry-safety boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R6 exit-path test
  (`test_refused_control_socket_yields_honest_note_and_unlinks_stale_socket`) — a refused control
  socket maps to the honest "already exited (stale control socket…)" note and unlinks the stale
  socket so the next probe reads ENOENT, never a raw `[Errno 111]`. Verification metadata stays
  pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the one-to-one sidecar for first-byte
  ambiguity, original-correlation preservation, incoherent-response handling, honest unknown setter
  evidence, and the no-automatic-retry invariant. The source is new and uncommitted, so verification
  hash and date remain empty until closeout.
