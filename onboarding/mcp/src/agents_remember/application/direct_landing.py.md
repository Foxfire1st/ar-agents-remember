# mcp/src/agents_remember/application/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[application overview](overview.md)

## Purpose

The application boundary for the direct landing operation (L16-R8): a thin wrapper that runs one
branch-addressed direct landing (policy-gated, atomic) and translates `DirectLandingError` into a
typed refused response envelope. No queue, gate, or lifecycle logic lives here.

## Code Commentary

### Logic

`direct_landing_tool(config, request)` calls `worktrees.direct_landing.direct_landing(config,
request)` and returns its success dict; on `DirectLandingError` it returns
`{ok: False, operation: "direct_landing", state: "refused", status: exc.status, detail: str(exc)}`
so the fail-closed reason reaches the wire in the strict response shape.

### Conventions

The application layer owns error translation; all validation and mutation live in
`worktrees/direct_landing.py`. Re-exports `DirectLandingError`, `DirectLandingRequest`, and
`direct_landing_tool` for the payload builder.

### Invariants And Boundaries

- Refusals always carry a typed `status` and human `detail`; no silent fallback to a success shape.
- This module never commits, never moves refs, and never reads the ledger itself.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application boundary translates operation errors into typed refused responses. | `direct_landing_tool` | mcp/src/agents_remember/application/direct_landing.py:13-27 |
| The operation it wraps. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:74-126 |
| The request model it accepts. | `DirectLandingRequest` | mcp/src/agents_remember/worktrees/direct_landing.py:56-71 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation (L16-R8):
  the error-translating application boundary over the worktree operation. Verified at code
  commit a9d50e08.
