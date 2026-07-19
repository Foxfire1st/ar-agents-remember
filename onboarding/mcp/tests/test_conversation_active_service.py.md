# mcp/tests/test_conversation_active_service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Projector-engine and store tests for 260718-CHATS-L1 (R2/R4): hydration, ordering, idempotence,
provenance resolution, rehydration, and the review-fix gap mechanics — driven through a scripted
in-memory bridge seam, plus the review-F1 tool-convergence proofs through the real mappers and
store.

## Code Commentary

### Logic

A `_ScriptedBridge` (L65-L218) plays scripted evidence/native/transcript/provenance/snapshot
answers through the projector's injected reader seams. `CodexEngineTests` (L221-L335): hydration
from native pages plus the live window with stable identity and ordinals; live polling appends
in order; idempotent re-feeds mint no duplicates; provenance resolves through the batch;
ephemeral-thread native refusal stays honestly partial; rehydration reproduces the identical
projection with a new generation. `ClaudeEngineTests` (L336-L441): the echo zipper merges
submission echoes and frames in exact turn order (echo first, result in a later poll, multiple
turns) with no duplicate or inverted items. `PiEngineTests` (L442-L487): eager native
continuation anchors live items to durable-entry identity and live tool upserts converge.
`StoreTests` (L488-L508): identical upsert replays are no-ops. `ToolConvergenceTests`
(L509-L692, review finding F1): claude `tool_use` → `tool_result`, pi live start → update →
end (including the result-less update as a true no-op), and pi entry call → `toolResult` all
converge to items carrying BOTH input and output blocks with completed phase; codex full-item
re-maps are byte-identical under the block union. `OverflowGapTests` (L693-L740, review finding
F2): with a clamped undrained subscriber queue the consumer receives exactly one
`retention-overflow` gap (requiresRepage + closeAfterEvent) then the close sentinel, and the
retention sequence set is contiguous with no hole. `ZipperEvictionGapTests` (L741-L820, review
finding F3): an advancing eviction floor raises `ZipperEvidenceEvicted` for the echo-zipper
projector (mapped to one ordering-fault gap), does NOT gap the codex projector (totals clear
honestly), and a fresh claude projector rehydrates from the remaining window without raising.

### Conventions

Engine tests run on `IsolatedAsyncioTestCase` with injected reader callables — no socket, no
real IPC; the scripted bridge records calls so channel discipline (page sizes, cursors, epoch
parameters) is asserted too.

### Invariants And Boundaries

- Ordering assertions cover both sequence monotonicity and item-level turn order.
- Gap assertions always require exactly one typed gap with the exact reason and the close
  sentinel — never silent loss.
- Rehydration must reproduce items, revisions, and ordinals identically.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries; the engine contract is
repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The projector engine under test: hydration, poll channels, zipper, retention, gap mechanics. | L134-L791 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| The store under test: idempotent apply, block union, delta buffering. | L101-L319 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| The evidence/native/provenance page products the scripted bridge mimics. | L320-L380 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the engine/store
  suite — hydration/ordering/idempotence/provenance/rehydration plus the F1/F2/F3 fix pins (19
  tests). Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
