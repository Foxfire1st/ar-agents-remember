# mcp/src/agents_remember/models/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| This initializer declares the public model export list. | `__all__` | mcp/src/agents_remember/models/__init__.py:90-90 |

## 260731-EFA-L9 Change

The initializer now also re-exports the curated conversation wire-model surface from
`models/conversations/` (R6) — the shared evidence/control-wire contracts, conversation
primitives/identity/cursors/content/capabilities/status/stream/history/operation DTOs, and
telemetry — keeping the package initializer exports-only.

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: recorded the conversation-model export
  additions; the L9 change section above documents them. Verification metadata pinned until
  closeout stamps the L9 code commit.
- 2026-08-04T11:39+02:00 — 260731-EFA-L6 S18-B13 curator: bound the public model-export claim to exact initializer anchors and normalized scoped citation evidence.

- 2026-06-11T06:47+02:00 — No content impact: `DirectCloseoutPreviewResponse`/`DirectCloseoutApplyResponse` left the export surface (import block and `__all__`) with the issue #62 worktree-only closeout; the exports-only contract this sidecar describes is unchanged.
- 2026-06-01T20:45+02:00 — Added `WorktreeAbandonResponse` to the response-model export surface for the `worktree_abandon` tool.
- 2026-05-31T12:50+02:00 — Dropped `CodexExecutionPolicy` from the export surface (removed from the `agents_remember.models.benchmarks` import block and from `__all__`); behaviour-preserving export-surface reduction, no sidecar prose named the removed symbol (1.0.0 review remediation).
- 2026-05-30T22:29+02:00: Added `finalize_payload_tokens` to the token-helper export surface (import and `__all__`) for the S6 token-counter wiring. Verification metadata stays pinned until closeout commits the change.
- 2026-05-28T19:52+02:00: Created for the response-contract package export surface.
