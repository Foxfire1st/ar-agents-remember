# mcp/src/agents_remember/models/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

The strict public wire response model for the direct landing operation (L16-R8): one branch
addressed direct landing result with a typed `state` (`landed` / `would-land` / `refused`).

## Code Commentary

### Logic

`DirectLandingResponse` extends `ToolResponse` with `operation: Literal["direct_landing"]`,
`state`, a bounded `summary`, and optional `status`/`detail` (so a fail-closed refusal still
reports its typed reason), plus the commit evidence fields `contractPath`, `codeCommit`,
`memoryContentCommit`, `ledgerCommit`, `dryRun`, and a `memory` facts dict.

### Conventions

The `status`/`detail` pair is present only on refusals; the landed/would-land shapes carry the
commit evidence. Bounds follow the strict-response model convention (summary/detail ≤ 8192).

### Invariants And Boundaries

- The wire shape stays strict: every field is typed; `memory` is an arbitrary fact dict from the
  operation, never a nested response envelope.
- This model only shapes the response; the operation logic lives in
  `worktrees/direct_landing.py`.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The response model shape for the direct landing operation. | `DirectLandingResponse` | mcp/src/agents_remember/models/direct_landing.py:12-30 |
| Registered as the `direct_landing` tool response model. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:146-223 |
| Produced by the worktree operation. | `_direct_landing_preview`; `_direct_landing_apply` | mcp/src/agents_remember/worktrees/direct_landing.py:186-203; mcp/src/agents_remember/worktrees/direct_landing.py:206-283 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L1 Response Contract

The direct-landing response now carries normalized `effectiveInput` on success/preview and typed `invalidFields`, `resolvedPlan`, and `correctedCall` on refusal. This is a shape change only; durable recovery is not implied. Direct landing remains a synchronous, lock-serialized sequence rather than an atomic transaction.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation (L16-R8):
  the strict response envelope carrying landed/would-land/refused states and commit evidence.
  Verified at code commit a9d50e08.
