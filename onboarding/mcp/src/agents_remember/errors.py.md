# mcp/src/agents_remember/errors.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                    |
| path                   | `mcp/src/agents_remember/errors.py`   |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`                    |
| lastVerifiedCommitDate | 2026-07-30T13:59:13+02:00|
| governingOverview      | `../../overview.md`                   |

## Governing Overview

[agents_remember overview](../../overview.md)

## Purpose

Defines the shared typed error family for Agents Remember. It distinguishes route-index census
failures from authority failures while retaining the harness-control contract, adapter disconnect,
Codex protocol, and client-side first-byte ambiguity families. 260718-CHATS-L0 adds the
conversation-composition family: `ConversationCompositionError` marks a violated app-scoped
conversation runtime composition contract, kept distinct from `AuthorityError`, which remains the
type for identity/authorization refusals such as the conversation resolver's loopback ruling.

## Code Commentary

### Logic

`AgentsRememberError` remains the package base and a `ValueError`. `HarnessControlClientError`
extends `HarnessControlError` with `may_have_sent`: failures before the Unix socket accepts a byte
remain retryable, while failures after the first accepted byte must be reported as unknown and
reconciled under the same request id. `HarnessAdapterDisconnectedError` carries the equivalent
native-adapter ambiguity plus optional vendor correlation. Codex-specific subclasses preserve
app-server method/code evidence. `RouteIndexCensusError` identifies a validated-root census failure
without conflating it with `AuthorityError`, which remains the type for a root mismatch or missing
write authority. `ConversationCompositionError` identifies a conversation runtime composition bug —
retrieval before installation, a second install, a foreign object on the reserved state key, or
construction missing a required authority — that must fail at startup or request entry, never
silently at first use.

### Conventions

Classes name one failure category and inherit from the nearest family member. Ambiguity evidence is
an explicit constructor argument, not inferred later from exception text.

### Invariants And Boundaries

- `AgentsRememberError` must keep subclassing `ValueError` so existing
  `except ValueError` handlers and the FastMCP error surface keep working
  unchanged. Do not reparent it to `Exception` or `RuntimeError`.
- Every domain error in the package should subclass `AgentsRememberError` (or a
  member of the family) rather than raising bare `ValueError` / `RuntimeError`,
  so the public surface stays one coherent contract.
- This module holds only error-type declarations and small evidence constructors. It imports no
  package internals and stays safe at the bottom of the dependency graph.
- `CodexAppServerError` identifies malformed, incompatible, or boundedness failures at the pinned
  Codex app-server protocol boundary; disconnect errors preserve possible-send state for reconcile.
- `may_have_sent=True` is never permission to retry; it is evidence that the same request id must be
  reconciled.
- Route-index root/official-settings refusal remains `AuthorityError`; Git record, command, or path
  classification failure after authority is established remains `RouteIndexCensusError` with the
  original cause attached.
- Conversation composition failures (missing/duplicate/foreign/missing-member runtime binding)
  remain `ConversationCompositionError`; identity and cross-principal refusals in the same route
  remain `AuthorityError` — the two families are never interchangeable.

### Todos

None known for the L4 error boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The blocking client uses the new stage evidence; the bridge/queue keep the native ambiguity type.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The socket exchange flips `may_have_sent` only after a successful first write and maps post-write response failures accordingly. | L237-L280 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The ordered queue converts native disconnect evidence into rejected or unknown receipts without blind resend. | L340-L365 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |
| The route-index census raises the dedicated type after root validation and preserves timeout/OS/path-classification causes. | L1-L226 | [route_index_census.py](agents-remember/mcp/src/agents_remember/kernel/route_index_census.py) |
| The conversation runtime raises `ConversationCompositionError` for missing/duplicate/foreign/missing-member bindings; the resolver raises `AuthorityError` for identity refusals. | L73-L101 | [runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |

## Cross-Repo References

No external repository boundary is implemented by the error declarations.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

The shared error family now distinguishes certified native busy/pre-dispatch failure, immutable
request-id conflict, and bridge-epoch mismatch. These types preserve the first-byte boundary: only a
certified pre-dispatch condition may advertise retry safety; possible-write failures remain unknown.

## 260718-CHATS-L5I Current Delta

`HarnessInteractionNotPendingError` gives direct interaction-response callers a typed refusal when no pending interaction is available. It prevents a normal stale or already-settled response from being reported as an undifferentiated control failure.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260727-CHATS-IM-L2 Native-History Error Delta

`NativeHistoryUnavailable` identifies one child/history read that can fail without invalidating
the shared adapter; its stable `code` carries the exact local reason. The
`NativeHistoryLimitExceeded` subtype adds `actual_bytes` and `limit_bytes` and fixes its code to
`materialization-limit` (L124-L144). These types distinguish child-local acquisition/resource
outcomes from malformed shared protocol and bridge-fatal transport failure.

## Update History

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented typed native-history
  unavailability and bounded-materialization byte evidence as child-local outcomes distinct from
  shared transport/protocol failure. Verification metadata remains pinned while uncommitted.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented `ConversationCompositionError` as
  the typed conversation runtime composition failure, distinct from the identity/authorization
  `AuthorityError` family. Verification metadata remains pinned until closeout stamps the
  candidate commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: documented `RouteIndexCensusError` as the typed
  post-authority census failure, distinct from root and official-settings `AuthorityError`.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented typed busy certificate, id-conflict, and epoch-
  mismatch errors used by the reliable submit boundary.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the client-side first-byte
  ambiguity type and its retry-safe versus reconcile-required evidence boundary.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the error-sidecar body for the negotiated protocol
  failure wording change.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: documented the typed Codex app-server
  protocol failure addition. Verification remains pinned until the leaf code commit exists.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator refresh: documented typed control-contract and
  ambiguous-disconnect errors used by the new bridge surfaces.

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
