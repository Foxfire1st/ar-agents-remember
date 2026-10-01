# mcp/src/agents_remember/models/direct_landing.py

## Governing Overview

[models overview](overview.md)

## Purpose

The strict public wire response model for the direct landing operation (L16-R8): one branch
addressed direct landing result with a typed `state` (`landed` / `would-land` / `refused`).

## Code Commentary

### Logic

`codeCommit` and `memoryContentCommit` are the real output identities. `ledgerCache` is
optional diagnostic data from refreshing the downstream projection; it is not a commit reference
or evidence required to make a landing successful. The retired `ledgerCommit` field is absent.

`DirectLandingResponse` extends `ToolResponse` with `operation: Literal["direct_landing"]`,
`state`, a bounded `summary`, and optional `status`/`detail` (so a fail-closed refusal still
reports its typed reason), plus the commit evidence fields `contractPath`, `codeCommit`,
`memoryContentCommit`, `dryRun`, and a `memory` facts dict, plus optional `ledgerCache` diagnostics.

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

## Evidence

### Docs References

No configured Domain Documentation source applies.

No configured external domain-documentation source applies.

### Repo-Internal References

- Real code/memory SHAs are separate from optional ledgerCache diagnostics. [1]
- The response model shape for the direct landing operation. [2]
- Registered as the `direct_landing` tool response model. [3]
- Produced by the admitted direct-landing coordinator. [4]
- Memory-content execution and same-generation recovery are journaled below the coordinator. [5]
- None [6]
- None [7]
- None [8]

### Cross-Repo References

No meaningful cross-repository reference applies.

No separate external implementation source applies to this file.

## 260821-CLIVE-L1 Response Contract

The direct-landing response carries normalized `effectiveInput` on success/preview and typed
`invalidFields`, `resolvedPlan`, and `correctedCall` on refusal. L2 adds journal generation and
recovery evidence to that public contract: synchronous invocation and lock serialization remain,
but partial memory-content publication is reconciled and resumed through the canonical root journal.

## 260821-CLIVE-L2 Current Contract

The current source seams include `DirectLandingResponse`. The response vocabulary now describes a journaled direct-landing generation, including effective accepted input and typed recovery/refusal evidence. Synchronous invocation and transient locking do not imply absence of durable recovery.

### Reconciled Source Evidence

- The current module exposes `DirectLandingResponse` at this ownership boundary. [9]

## 260821-DAGQC-L2 Closed Outcome Vocabulary

The response model closes the top-level outcome plane to exactly `landed`, `would-land`, or
`refused` and declares the projection recovery fields separately. Intermediate journal states
belong inside the lifecycle projection; they are evidence about how the operation is proceeding,
not a fourth direct-landing outcome. The separate `doorGenerationId` recovery field this section
once carried was removed by the closeout-door cut (commit `fad9808e`); a direct landing no longer
carries or reports a door generation.
