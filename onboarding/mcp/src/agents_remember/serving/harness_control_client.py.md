# harness_control_client.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_client.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T06:15+02:00 |
| lastVerifiedCommitHash | `a1b0aa9143fa777efd8389892e3283ff257ef44d` |
| lastVerifiedCommitDate | 2026-07-16T06:37:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Synchronous exact-session client for the Unix control socket owned by a hosted harness runner. It
is the serving boundary for live advertise, honest model/effort set, correlated whole-message
submission, reconciliation, interaction responses, transcript reads, and stop.

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

## Cross-Repo References

No external repository boundary is implemented by the local Unix-socket client.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented live advertise/set, strict
  normalized parsing, whole-message submit, first-byte retry safety, and same-id ambiguity closure.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented identity-bound protocol requests,
  correlated acceptance/reconciliation, interaction responses, and no raw-terminal fallback.
