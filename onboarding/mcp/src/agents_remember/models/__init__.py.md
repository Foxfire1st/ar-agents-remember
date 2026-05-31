# mcp/src/agents_remember/models/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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

- 2026-05-31T12:50+02:00 — Dropped `CodexExecutionPolicy` from the export surface (removed from the `agents_remember.models.benchmarks` import block and from `__all__`); behaviour-preserving export-surface reduction, no sidecar prose named the removed symbol (1.0.0 review remediation).
- 2026-05-30T22:29+02:00: Added `finalize_payload_tokens` to the token-helper export surface (import and `__all__`) for the S6 token-counter wiring. Verification metadata stays pinned until closeout commits the change.
- 2026-05-28T19:52+02:00: Created for the response-contract package export surface.
