# selection.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Validates the already admitted repository-profile source-selection decision before ambient role-chat replications start.

## Code Commentary

### Logic

`admitted_selection` loads the typed decision through `read_rail_source_selection`, requires selector id `ambient-role-dependencies` and the caller's exact mode, then refuses any non-applicable decision. It independently observes the supplied repository, exact Git-tree candidate and diff base through `observe_candidate_source_selection`; the entire observed source selection must equal the retained decision before it is returned.

### Conventions

Dependency prefixes and the not-applicable reason belong to `mcp/certification-profile-v1.json`, not a local script constant. The generic source-selection reader owns decoding/digest validation; the generic Git observer owns changed-path census. This script neither recreates those algorithms nor silently selects a different scope.

### Invariants And Boundaries

- Wrong selector, wrong mode, non-applicable decision or moved candidate/base refuses before replication.
- A valid selection is admission evidence, not proof that an E2E rail executed or passed.
- Changes to dependency scope must update the repository profile and its canonical identities.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Exact admitted selector/mode/applicability and current Git observation are required. [1]
- Repository profile owns dependency prefixes and stable ambient selector identity. [2]

### Cross-Repo References

No cross-repository source governs this validator; the explicit repository argument is observed locally.
