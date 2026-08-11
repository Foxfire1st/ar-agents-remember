# mcp/src/agents_remember/tasks/document_refs.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/document_refs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Resolves canonical sprint/master/leaf document references and their containment from the actual task
files. This is the topology authority behind structural seat qualification and replaces leaf-key
parsing as an identity model.

## Code Commentary

### Logic

`TaskDocumentTopology` indexes real task documents, normalizes repository-qualified references,
checks level and containment, and walks leaf→master→sprint without synthesizing anchors. Typed
`TaskDocumentRefError` failures distinguish malformed, missing, mismatched, and ambiguous topology.

### Conventions

Canonical paths are coordination-root-relative and remain tied to the actual task document.

### Invariants And Boundaries

- Task files, not session ancestry, define containment.
- Every resolved reference names one real document at one verified level.
- Ambiguity and scope loss fail closed.
- This module does not inspect terminal liveness or choose occupants.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Task document topology is centralized in one typed resolver. | `TaskDocumentTopology` | mcp/src/agents_remember/tasks/document_refs.py:26-252 |
| Structural seats consume this topology to qualify parent and child relations. | `StructuralSeatResolver` | mcp/src/agents_remember/serving/structural_seats.py:22-160 |

## Cross-Repo References

The task documents live in the configured coordination root, but the resolver contract is implemented
inside agents-remember and has no sibling-repository code dependency.


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created as the real-document topology authority; absorbs canonical validation formerly described by `serving/leaf_ref_validation.py`.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: predecessor leaf-reference card was verified against the then-current worktree; stale moved-path references were repaired.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 curator: predecessor card rebound two onboarding citations to code authorities.
- 2026-08-02T16:55+02:00 — 260731-EFA-L6 curator: predecessor card repaired three repo-internal citation rows.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: predecessor leaf validation added bounded legacy role-suffix detection and canonical leaf-plus-role refusal guidance.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: predecessor card was created for terminal leaf-key normalization at serving and MCP write boundaries.
