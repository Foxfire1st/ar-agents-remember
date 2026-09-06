# mcp/src/agents_remember/certification/repository_profiles/source_selection/git.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/source_selection/git.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:50:20+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Source applicability overview](overview.md)

## Purpose

Observes an exact complete Git path delta for repository-declared source applicability.

## Code Commentary

### Logic

`observe_candidate_source_selection` requires a Git-tree candidate and the actual repository root, resolves the diff base to a commit and tree, verifies the candidate object is a tree, and runs a NUL-delimited recursive `diff-tree --no-renames` through the canonical Git command owner. The complete sorted changed-path tuple binds base commit, base tree and candidate tree in a validated digest-bearing record. Rename detection is disabled so both old and new paths remain represented.

The command wrapper refuses failed observations or output above its 16 MiB bound. Nonempty path output must end with NUL. `observe_profile_source_selection` does no observation when no selected rail declares it; otherwise owner failures become a typed `CertificationProfileError` finding.

### Conventions

Route observations through the canonical Git command owner and retain exact base and candidate identities.

### Invariants And Boundaries

- Observation reads exact tree objects rather than substituting current worktree paths.
- An observation failure refuses selection; it does not widen scope or manufacture an empty census.
- The canonical model rejects duplicate, noncanonical or excessive path populations.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-owned selection contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The observer resolves exact Git authority and complete path bytes; the profile entrypoint wraps owner failures. | `observe_candidate_source_selection`; `observe_profile_source_selection` | mcp/src/agents_remember/certification/repository_profiles/source_selection/git.py:37-104 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T14:50:20+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented selection ownership, refusal behavior and execution limits. Source verification does not claim test execution or CCR acceptance.
