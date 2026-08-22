# mcp/src/agents_remember/application/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application overview](overview.md)

## Purpose

The application boundary for the direct landing operation: a thin wrapper that runs one
branch-addressed, policy-gated, lock-serialized landing sequence and translates
`DirectLandingError` or `CloseoutInputError` into a typed refused response envelope. No queue,
gate, lifecycle journal, or recovery logic lives here.

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

## 260821-CLIVE-L1 Input Boundary

This wrapper now returns the full typed refusal payload—status/detail plus `invalidFields`, `resolvedPlan`, and `correctedCall`—and passes successful `effectiveInput` through unchanged. It remains only an error-translation boundary. The wrapped operation is policy-gated and lock-serialized, but it is **not atomic**: memory content and ledger are sequential Git commits with neither rollback nor durable crash recovery. Input validation precedes the landing lock and Git; L2-R11/L5-R15 own the memory-before-ledger durability gap.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation (L16-R8):
  the error-translating application boundary over the worktree operation. Verified at code
  commit a9d50e08.
