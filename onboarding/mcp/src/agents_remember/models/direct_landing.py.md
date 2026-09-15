# mcp/src/agents_remember/models/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No configured Domain Documentation source applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain-documentation source applies. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Real code/memory SHAs are separate from optional ledgerCache diagnostics. | L20-L54 | [mcp/src/agents_remember/models/direct_landing.py](mcp/src/agents_remember/models/direct_landing.py) |
| The response model shape for the direct landing operation. | L20-L54 | [mcp/src/agents_remember/models/direct_landing.py](mcp/src/agents_remember/models/direct_landing.py) |
| Registered as the `direct_landing` tool response model. | L214-L214 | [mcp/src/agents_remember/models/tools/tool_registry.py](mcp/src/agents_remember/models/tools/tool_registry.py) |
| Produced by the admitted direct-landing coordinator. | L113-L125 | [mcp/src/agents_remember/worktrees/direct_landing.py](mcp/src/agents_remember/worktrees/direct_landing.py) |
| Memory-content execution and same-generation recovery are journaled below the coordinator. | L42-L75; L78-L135 | [mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py](mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py) |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No separate external implementation source applies to this file. | N/A | N/A |

## 260821-CLIVE-L1 Response Contract

The direct-landing response carries normalized `effectiveInput` on success/preview and typed
`invalidFields`, `resolvedPlan`, and `correctedCall` on refusal. L2 adds journal generation and
recovery evidence to that public contract: synchronous invocation and lock serialization remain,
but partial memory-content publication is reconciled and resumed through the canonical root journal.

## 260821-CLIVE-L2 Current Contract

The current source seams include `DirectLandingResponse`. The response vocabulary now describes a journaled direct-landing generation, including effective accepted input and typed recovery/refusal evidence. Synchronous invocation and transient locking do not imply absence of durable recovery.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `DirectLandingResponse` at this ownership boundary. | L20-L54 | [mcp/src/agents_remember/models/direct_landing.py](mcp/src/agents_remember/models/direct_landing.py) |

## 260821-DAGQC-L2 Closed Outcome Vocabulary

The response model closes the top-level outcome plane to exactly `landed`, `would-land`, or
`refused` and declares the projection recovery fields separately. Intermediate journal states
belong inside the lifecycle projection; they are evidence about how the operation is proceeding,
not a fourth direct-landing outcome. The separate `doorGenerationId` recovery field this section
once carried was removed by the closeout-door cut (commit `fad9808e`); a direct landing no longer
carries or reports a door generation.

## Update History

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Distinguished actual output SHAs from optional ledger-cache diagnostics in direct landing responses. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.

- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `DirectLandingResponse` repointed to mcp/src/agents_remember/models/direct_landing.py:20-54. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:147-225. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `direct_landing` repointed to mcp/src/agents_remember/worktrees/direct_landing.py:117-129. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `DirectLandingResponse` repointed to mcp/src/agents_remember/models/direct_landing.py:20-54. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: recorded that `DirectLandingResponse.doorGenerationId` was removed and that the closed-outcome section no longer declares a door recovery field. Verification metadata remains pinned because only the cut-affected claim was reconciled; source documentation only, no acceptance claim.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed closeout input/projection package relocations; direct-landing outcome and nested journal evidence remain unchanged.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: closed direct-landing outcome state and separated nested journal lifecycle evidence from the top-level result. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation (L16-R8):
  the strict response envelope carrying landed/would-land/refused states and commit evidence.
  Verified at code commit a9d50e08.
