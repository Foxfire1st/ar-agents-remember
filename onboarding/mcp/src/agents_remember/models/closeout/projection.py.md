# mcp/src/agents_remember/models/closeout/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Define the strict public models for disposable closeout projections and task-publication effects.

## Code Commentary

### Logic

The models represent bounded source problems, schedulable members, exactly two projection service conditions, invalidation/rebuild results, and per-scope task-document projection effects.

### Invariants And Boundaries

- Projection service condition is only valid-built or invalid-empty.
- A valid-built empty membership is terminal-empty; no third durable state is invented.
- Claimed lifecycle, commit, certification, and integration evidence are not projection fields.
- All collections and text are bounded and unknown fields are refused.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Projection problems, members, and queue state use strict bounded models. | `ProjectionSourceProblem`; `CloseoutProjectionMember`; `CloseoutQueueState` | mcp/src/agents_remember/models/closeout/projection.py:23-90 |
| Invalidation, rebuild, and task-document effects are explicit typed results. | `ProjectionInvalidationResult`; `ProjectionRebuildResult`; `TaskDocProjectionEffect` | mcp/src/agents_remember/models/closeout/projection.py:91-142 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
