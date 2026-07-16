# mcp/src/agents_remember/errors.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                    |
| path                   | `mcp/src/agents_remember/errors.py`   |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-07-16T06:15+02:00                |
| lastVerifiedCommitHash | `a1b0aa9143fa777efd8389892e3283ff257ef44d`                    |
| lastVerifiedCommitDate | 2026-07-16T06:37:02+02:00|
| governingOverview      | `../../overview.md`                   |

## Governing Overview

[agents_remember overview](../../overview.md)

## Purpose

Defines the shared typed error family for Agents Remember. In the harness-control slice it
distinguishes contract failures, adapter disconnect ambiguity, Codex protocol failures, and the L4
client-side first-byte boundary used to decide whether a request is safe to retry.

## Code Commentary

### Logic

`AgentsRememberError` remains the package base and a `ValueError`. `HarnessControlClientError`
extends `HarnessControlError` with `may_have_sent`: failures before the Unix socket accepts a byte
remain retryable, while failures after the first accepted byte must be reported as unknown and
reconciled under the same request id. `HarnessAdapterDisconnectedError` carries the equivalent
native-adapter ambiguity plus optional vendor correlation. Codex-specific subclasses preserve
app-server method/code evidence.

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

## Cross-Repo References

No external repository boundary is implemented by the error declarations.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the client-side first-byte
  ambiguity type and its retry-safe versus reconcile-required evidence boundary.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the error-sidecar body for the negotiated protocol
  failure wording change.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: documented the typed Codex app-server
  protocol failure addition. Verification remains pinned until the leaf code commit exists.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator refresh: documented typed control-contract and
  ambiguous-disconnect errors used by the new bridge surfaces.

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
