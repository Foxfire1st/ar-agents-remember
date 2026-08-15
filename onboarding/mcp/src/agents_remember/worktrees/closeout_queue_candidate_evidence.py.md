# mcp/src/agents_remember/worktrees/closeout_queue_candidate_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_queue_candidate_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T12:53+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Builds and rechecks exact code, memory, ledger, route-review, source-lineage, and atomic-series
landing evidence for a queue candidate.

## Code Commentary

### Logic

The module hashes the full canonical route-review record and every referenced file, verifies the
transitive and immediate source bases, resolves the ledger edge and candidate trees, derives a
one-way lifecycle-owner fingerprint, and proves an atomic series' finalized commits actually
landed on the super code and memory source refs. Atomic proof is split into focused code ancestry,
memory ancestry/ledger, master identity, approved finalization, and content-movement predicates.
The same owner compares the complete current route-review fact and returns a precise
malformed-versus-stale blocker to queue projection.

### Conventions

Evidence paths are task-relative and byte-digested. Commit and ancestry questions use the canonical
Git/worktree and ledger helpers rather than new parsing logic.

### Invariants And Boundaries

- Same-count or same-summary route-review replacement still invalidates the candidate.
- External memory must map the exact code base through the ledger.
- Atomic release cannot be fabricated with unchanged base commits or a status-only task edit.
- Atomic finalization must carry explicit approved human review as well as commit approval.
- Raw lifecycle operation keys are reduced to one-way fingerprints before persistence.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Route review binds the full record plus every verdict/evidence file digest. | `route_review_fact` | mcp/src/agents_remember/worktrees/closeout_queue_candidate_evidence.py:22-43 |
| Route-review comparison preserves malformed-record detail and distinguishes it from a stale exact fact. | `route_review_blockers` | mcp/src/agents_remember/worktrees/closeout_queue_candidate_evidence.py:48-67 |
| Source bases are revalidated against transitive and immediate source lineage. | `require_source_bases_current` | mcp/src/agents_remember/worktrees/closeout_queue_candidate_evidence.py:46-71 |
| External memory resolves the exact code-base ledger edge. | `ledger_mapping` | mcp/src/agents_remember/worktrees/closeout_queue_candidate_evidence.py:94-109 |
| Atomic completion proves the finalized series commits and ledger edge landed on current source refs. | `require_atomic_master_landed` | mcp/src/agents_remember/worktrees/closeout_queue_candidate_evidence.py:121-191 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: decomposed the atomic landing proof into
  focused exact predicates and required approved human review; public success and each false
  predicate are directly forced.
- 2026-08-15T11:43+02:00 — No content impact: accepted Ruff's single-line formatting of the
  route-review comparison signature; its inputs, return type, and implementation are unchanged.
- 2026-08-15T11:25+02:00 — L3 static-gate repair: moved exact route-review comparison beside the
  fact builder, reducing queue orchestration complexity without changing blocker vocabulary.
- 2026-08-15T09:10+02:00 — Created for L3's exact candidate-evidence and atomic-landing proof; verification remains closeout-owned.
