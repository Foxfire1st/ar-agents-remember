# mcp/src/agents_remember/certification/repository_profiles/source_selection/git.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned selection contract.

No configured domain documentation applies.

### Repo-Internal References

- The observer resolves exact Git authority and complete path bytes; the profile entrypoint wraps owner failures. [1]

### Cross-Repo References

No cross-repository implementation boundary is owned by this file.

No cross-repository reference is required.
