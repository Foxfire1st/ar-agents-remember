# mcp/src/agents_remember/errors.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                    |
| path                   | `mcp/src/agents_remember/errors.py`   |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-07-14T12:00+02:00                |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661`                    |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00|
| governingOverview      | `../../overview.md`                   |

## Purpose

`errors.py` defines the typed error family for Agents Remember. It gives the
package a single coherent error contract so domain failures can be raised and
caught by type instead of as bare `ValueError` / `RuntimeError`. New code should
raise and catch the typed members of this family.

## Code Commentary

### Logic

The module declares the shared domain error family. `AgentsRememberError`
is the base class for every domain error and subclasses the builtin
`ValueError`. `AuthorityError` subclasses `AgentsRememberError` and marks a path
or repo argument that violated the MCP authority settings — for example a caller
naming a repo that settings do not allow, or passing a path that escapes the
coordinator root. Centralizing this lets every controller report the same
boundary violation the same way.

### Invariants And Boundaries

- `AgentsRememberError` must keep subclassing `ValueError` so existing
  `except ValueError` handlers and the FastMCP error surface keep working
  unchanged. Do not reparent it to `Exception` or `RuntimeError`.
- Every domain error in the package should subclass `AgentsRememberError` (or a
  member of the family) rather than raising bare `ValueError` / `RuntimeError`,
  so the public surface stays one coherent contract.
- This module holds only error-type declarations. It carries no logic, no
  imports of package internals, and must stay dependency-free so any module can
  import it without creating import cycles.

### Conventions

Each class documents its meaning in a docstring rather than carrying behavior.
Subclasses name a specific failure category (e.g. `AuthorityError` for the F11
authority boundary) and inherit from the nearest appropriate family member.

### 260713-PHA-L1 control bridge errors

`HarnessControlError` is the typed contract/identity/bridge failure used by the protocol, queue,
IPC, and terminal surface. `HarnessAdapterDisconnectedError` preserves whether a prompt may have
been sent and an optional vendor correlation id, so callers can reconcile without blind resend.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Control seam using the typed errors. | [harness_control_bridge.py](serving/harness_control_bridge.py) |
| Adapter disconnect semantics. | [harness_control_adapter.py](serving/harness_control_adapter.py) |

## Update History
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator refresh: documented typed control-contract and
  ambiguous-disconnect errors used by the new bridge surfaces.

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
