# mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Transfers the exact transitional certified candidate into journal-owned integration authority and
pins final-versus-nonfinal organizational scope before sprint-super publication.

## Code Commentary

### Logic

`preview_integration_boundary` captures exact task-source bytes and final/non-final scope before
claim. `prepare_integration_publication_intent` chooses the complete post-claim publication identity
and snapshots the transitional certified candidate into journal input. `transfer_integration_claim`
then consumes or proves that exact candidate under queue serialization and records claim proof in
the journal. Quality certification is reread from the integration operation; later protected-ref
publication and recovery no longer depend on a surviving queue row.

### Invariants And Boundaries

- Every irreversible publication re-verifies the exact candidate, commits, and completion scope.
- The journaled claim snapshot, not the queue row, is retained through Git recovery of torn ref
  state.
- A completed organizational master must carry its durable full-gate certification.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Boundary preview refuses final/non-final task-source drift before protected publication. | `preview_integration_boundary` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:52-101 |
| Dry-run reads the exact final-leaf decision. | `preview_organizational_completion` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:104-109 |
| Publication intent pins the exact organizational scope before claim transfer. | `prepare_integration_publication_intent` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:112-166 |
| Durable quality certification is reread from the integration journal. | `recorded_organizational_quality_certification` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:230-247 |
| Claim transfer records the exact candidate and integration publication intent before protected publication. | `transfer_integration_claim` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:169-227 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `IntegrationBoundaryFacts`, `preview_integration_boundary`, `preview_organizational_completion`. Organizational completion and repair are canonical integration-journal transitions with exact candidate, ref, quality, and cancellation evidence. The queue may schedule a door candidate but does not own failure repair or reopening lifecycle state.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `IntegrationBoundaryFacts`, `preview_integration_boundary`, `preview_organizational_completion` at this ownership boundary. | L45-L49; L52-L101; L104-L109 | `mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for organizational completion queue-to-repository publication.
