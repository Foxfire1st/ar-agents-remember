# mcp/src/agents_remember/memory_quality/style/citations/provenance.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Historical source and exact dependency-version provenance for citation claims. `GitHistory.commit`
accepts only commits reachable from the current repository history or an explicitly retained
prepared-history anchor; `Histories` passes those anchors to the code history while memory history
comes from reachable memory commit attribution. Source files are read from current bytes for the working-tree side of
the comparison, and dependency checks require exact resolved Python or npm versions.

## Code Commentary

### Logic

`Histories.memory_mappings` derives reachable code-to-memory pairs once per history
observation from memory commit trailers. `memory_commit(code_commit)` resolves an attributed
memory commit and still proves its reachability. No cache-file read supplies historical
provenance; absent or malformed `memory.md` is irrelevant, while unavailable Git attribution or
a missing real attribution remains an explicit provenance error.

Module-level surface:

- `Read` (class)
- `LockedVersion` (class)
- `GitHistory` (class)
- `Histories` (class)
- `VersionRead` (class)
- `requirement_candidate_for` (function)
- `package_candidate_for` (function)
- `manifest_error` (function)
- `requirement_versions` (function)
- `package_lock_versions` (function)
- `package_from_path` (function)
- `ecosystem_from_path` (function) — The one resolved-version namespace capable of proving ``path``'s identity.
- `normalised_package` (function)
- `_git_error` (function)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Historical memory provenance derives once from reachable attribution and validates the selected commit. [1]
- Defines the class `Read`. [2]
- Defines the class `LockedVersion`. [3]
- Defines the class `GitHistory`. [4]
- Defines the class `Histories`. [5]
- Defines the class `VersionRead`. [6]
- Defines the function `requirement_candidate_for`. [7]
- Defines the function `package_candidate_for`. [8]
- Defines the function `manifest_error`. [9]
- Defines the function `requirement_versions`. [10]
- Defines the function `package_lock_versions`. [11]
- Defines the function `package_from_path`. [12]
- Defines the function `ecosystem_from_path` — The one resolved-version namespace capable of proving ``path``'s identity.. [13]
- Defines the function `normalised_package`. [14]
- Defines the function `_git_error`. [15]


### Cross-Repo References

No separate cross-repository implementation claim is made.

No external implementation source applies.
