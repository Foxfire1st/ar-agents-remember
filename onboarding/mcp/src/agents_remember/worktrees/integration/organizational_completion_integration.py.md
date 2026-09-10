# mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4` |
| lastVerifiedCommitDate | 2026-09-10T09:57:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Transfers the exact claimed door and completed source journal into integration authority and pins
final-versus-nonfinal organizational scope before sprint-super publication.

## Code Commentary

### Logic

`preview_integration_boundary` captures exact task-source bytes and final/non-final scope before
claim. Publication intent binds sprint/candidate, exact claimed door, source kind/generation/
fingerprint/key, source-journal digest, and commits. `source_operation_matches` proves the completed
active retained source plus its exact door; closeout also proves the finalized contract digest.
Protected-ref publication and recovery never consume or depend on a projection row.

### Invariants And Boundaries

- Every irreversible publication re-verifies the exact candidate, commits, and completion scope.
- The journaled claim snapshot, not the queue row, is retained through Git recovery of torn ref
  state.
- A completed organizational master must carry its durable full-gate certification.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Boundary preview refuses final/non-final task-source drift before protected publication. | `preview_integration_boundary` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:52-101 |
| Dry-run reads the exact final-leaf decision. | `preview_organizational_completion` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:80-83 |
| Publication intent pins the exact organizational scope before claim transfer. | `prepare_integration_publication_intent` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:86-133 |
| Publication source identity is re-proved from the integration journal: a completed, active, retained source whose proven door equals the contract, with the finalized closeout contract digest required for a closeout operation. | `source_operation_matches`; `source_journal_sha256` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:189-211; mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:212-218 |
| Claim transfer records the exact candidate and integration publication intent before protected publication. | `transfer_integration_claim` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:136-186 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## CCR-R12@v5 Current Publication Boundary

Integration publication intent binds the prepared code and external-memory pair, source refs, and
organizational completion evidence needed for atomic publication. It does not require or create a
full-quality certification record for the normal route. The publication operation preserves source
movement refusal and authority checks, then records the resulting pair.

## 260821-CLIVE-L2 Current Contract

The current source seams include `IntegrationBoundaryFacts`, `preview_integration_boundary`, `preview_organizational_completion`. Organizational completion and repair are canonical integration-journal transitions with exact candidate, ref, quality, and cancellation evidence. The queue may schedule a door candidate but does not own failure repair or reopening lifecycle state.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `IntegrationBoundaryFacts`, `preview_integration_boundary`, `preview_organizational_completion` at this ownership boundary. | `IntegrationBoundaryFacts`; `preview_integration_boundary`; `preview_organizational_completion` | mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:35-42; mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:43-79; mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:80-85 |

## 260821-CLIVE Source-Journal Transfer

Integration intent transfers the exact claimed door and source journal, re-proves current task
topology, and binds the source journal digest plus exact source identity. `source_operation_matches`
requires a completed active retained source whose proven door equals the contract; closeout also
requires the finalized contract digest. Projection rows are never consumed, and admitted commits
must remain exact.

## Update History
- 2026-09-10T09:50+02:00 — CCR-R12@v5 transaction-only curation against code commit `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`: re-read the journal re-read row: `recorded_organizational_quality_certification` no longer exists, so the row now cites the current `source_operation_matches` / `source_journal_sha256` publication-source proof. Verification metadata remains closeout-owned.

- 2026-09-10T07:41:10+00:00: Generated citation repair: `preview_organizational_completion` repointed to mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:80-83. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `prepare_integration_publication_intent` repointed to mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:86-133. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `transfer_integration_claim` repointed to mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py:136-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout recovery-projection package relocation; door/source-journal transfer and queue-independent completion are unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented exact door/source-journal transfer and removal of queue consumption. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion_integration.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for organizational completion queue-to-repository publication.
