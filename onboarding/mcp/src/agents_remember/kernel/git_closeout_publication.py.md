# mcp/src/agents_remember/kernel/git_closeout_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/git_closeout_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[Owning overview](../../../overview.md)

## Purpose

Expected-old publication capability and exact prepared commit proof.

## Code Commentary

### Logic

Publication has a separate sealed capability from private preparation. The binding names the operation, generation, logical branch, expected old commit and exact prepared commit/tree. Raw commit validation recomputes the complete object identity and requires the exact prepared tree; a new prepared commit must have the sole expected-old parent. Observations distinguish old, new and existing states; publication authority, cancellation and journal selection remain caller responsibilities.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870` and remains byte-identical at the recovery code candidate. Its behavior was re-read against that source during memory recovery; the existing metadata owner still owns the pending verification stamp.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `GitCloseoutPublicationError` owns the corresponding behavior described above. | `GitCloseoutPublicationError` | `mcp/src/agents_remember/kernel/git_closeout_publication.py:23-30` |
| `GitCloseoutPublicationBinding` owns the corresponding behavior described above. | `GitCloseoutPublicationBinding` | `mcp/src/agents_remember/kernel/git_closeout_publication.py:34-81` |
| `GitCloseoutPublicationCapability` owns the corresponding behavior described above. | `GitCloseoutPublicationCapability` | `mcp/src/agents_remember/kernel/git_closeout_publication.py:85-94` |
| `GitCloseoutPublicationObservation` owns the corresponding behavior described above. | `GitCloseoutPublicationObservation` | `mcp/src/agents_remember/kernel/git_closeout_publication.py:98-101` |
| `GitCloseoutPublicationResult` owns the corresponding behavior described above. | `GitCloseoutPublicationResult` | `mcp/src/agents_remember/kernel/git_closeout_publication.py:105-108` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
