# mcp/src/agents_remember/models/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
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
- Top-level `state` is only the closed operation outcome (`landed`, `would-land`, or `refused`).
  Journal lifecycle state and recovery facts remain nested and cannot overwrite it.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The response model shape for the direct landing operation. | `DirectLandingResponse` | mcp/src/agents_remember/models/direct_landing.py:20-55 |
| Registered as the `direct_landing` tool response model. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:148-227 |
| Produced by the admitted direct-landing coordinator. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:132-144 |
| Memory/ledger execution and same-generation recovery are journaled below the coordinator. | `execute_direct_landing`; `execute_or_require_direct_landing_recovery` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:68-105; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:108-165 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L1 Response Contract

The direct-landing response carries normalized `effectiveInput` on success/preview and typed
`invalidFields`, `resolvedPlan`, and `correctedCall` on refusal. L2 adds journal generation and
recovery evidence to that public contract: synchronous invocation and lock serialization remain,
but partial memory/ledger publication is reconciled and resumed through the canonical root journal.

## 260821-CLIVE-L2 Current Contract

The current source seams include `DirectLandingResponse`. The response vocabulary now describes a journaled direct-landing generation, including effective accepted input and typed recovery/refusal evidence. Synchronous invocation and transient locking do not imply absence of durable recovery.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `DirectLandingResponse` at this ownership boundary. | L20-L55 | `mcp/src/agents_remember/models/direct_landing.py` |

## 260821-DAGQC-L2 Closed Outcome Vocabulary

The response model closes the top-level outcome plane to exactly `landed`, `would-land`, or
`refused` and declares the door/projection recovery fields separately. Intermediate journal states
belong inside the lifecycle projection; they are evidence about how the operation is proceeding,
not a fourth direct-landing outcome.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: closed direct-landing outcome state and separated nested journal lifecycle evidence from the top-level result. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation (L16-R8):
  the strict response envelope carrying landed/would-land/refused states and commit evidence.
  Verified at code commit a9d50e08.
