# mcp/src/agents_remember/models/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0` |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`__init__.py` re-exports the public Pydantic response-contract model surface.

## Code Commentary

The package initializer collects base response primitives, domain response
models, token helpers, and the public tool response model registry into one
import surface with an explicit `__all__`.

## Invariants And Boundaries

- Keep this file as exports only; contract behavior belongs in the concrete
  model modules.
- Export additions should follow actual public model additions and registry
  changes.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Concrete response model modules live beside this initializer. | [models overview](overview.md) |

## Update History

- 2026-06-01T20:45+02:00 — Added `WorktreeAbandonResponse` to the response-model export surface for the `worktree_abandon` tool.
- 2026-05-31T12:50+02:00 — Dropped `CodexExecutionPolicy` from the export surface (removed from the `agents_remember.models.benchmarks` import block and from `__all__`); behaviour-preserving export-surface reduction, no sidecar prose named the removed symbol (1.0.0 review remediation).
- 2026-05-30T22:29+02:00: Added `finalize_payload_tokens` to the token-helper export surface (import and `__all__`) for the S6 token-counter wiring. Verification metadata stays pinned until closeout commits the change.
- 2026-05-28T19:52+02:00: Created for the response-contract package export surface.
