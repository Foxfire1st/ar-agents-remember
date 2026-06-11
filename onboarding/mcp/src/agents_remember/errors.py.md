# mcp/src/agents_remember/errors.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                    |
| path                   | `mcp/src/agents_remember/errors.py`   |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-05-31T12:30+02:00                |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                    |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../overview.md`                   |

## Purpose

`errors.py` defines the typed error family for Agents Remember. It gives the
package a single coherent error contract so domain failures can be raised and
caught by type instead of as bare `ValueError` / `RuntimeError`. New code should
raise and catch the typed members of this family.

## Code Commentary

### Logic

The module declares two classes and no runtime behavior. `AgentsRememberError`
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

## Update History

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
