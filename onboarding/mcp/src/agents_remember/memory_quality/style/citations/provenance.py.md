# mcp/src/agents_remember/memory_quality/style/citations/provenance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/provenance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532` |
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Historical source and exact dependency-version provenance for citation claims. `GitHistory.commit`
accepts only commits reachable from the current repository history or an explicitly retained
prepared-history anchor; `Histories` passes those anchors to the code history while memory history
still comes from the ledger. Source files are read from current bytes for the working-tree side of
the comparison, and dependency checks require exact resolved Python or npm versions.

## Code Commentary

### Logic

Module-level surface:

- `Read` (class, lines 35-37)
- `LockedVersion` (class, lines 41-44)
- `GitHistory` (class, lines 48-102)
- `Histories` (class, lines 106-170)
- `VersionRead` (class, lines 183-186)
- `requirement_candidate_for` (function, lines 189-199)
- `package_candidate_for` (function, lines 202-214)
- `manifest_error` (function, lines 217-221)
- `requirement_versions` (function, lines 214-255)
- `package_lock_versions` (function, lines 258-273)
- `package_from_path` (function, lines 286-290)
- `ecosystem_from_path` (function, lines 293-301) — The one resolved-version namespace capable of proving ``path``'s identity.
- `normalised_package` (function, lines 304-305)
- `_git_error` (function, lines 308-310)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `Read` (lines 35-37). | `Read` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:35-37 |
| Defines the class `LockedVersion` (lines 41-44). | `LockedVersion` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:41-44 |
| Defines the class `GitHistory` (lines 48-102). | `GitHistory` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:48-102 |
| Defines the class `Histories` (lines 106-170). | `Histories` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:106-170 |
| Defines the class `VersionRead` (lines 183-186). | `VersionRead` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:183-186 |
| Defines the function `requirement_candidate_for` (lines 189-199). | `requirement_candidate_for` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:189-199 |
| Defines the function `package_candidate_for` (lines 202-214). | `package_candidate_for` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:202-214 |
| Defines the function `manifest_error` (lines 217-221). | `manifest_error` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:217-221 |
| Defines the function `requirement_versions` (lines 214-255). | `requirement_versions` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:214-255 |
| Defines the function `package_lock_versions` (lines 258-273). | `package_lock_versions` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:258-273 |
| Defines the function `package_from_path` (lines 286-290). | `package_from_path` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:286-290 |
| Defines the function `ecosystem_from_path` (lines 293-301) — The one resolved-version namespace capable of proving ``path``'s identity.. | `ecosystem_from_path` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:293-301 |
| Defines the function `normalised_package` (lines 304-305). | `normalised_package` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:304-305 |
| Defines the function `_git_error` (lines 308-310). | `_git_error` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:308-310 |

## Update History

- 2026-09-10T04:35+02:00 — CCR-L42 final predecessor-history curation: documented reachable current
  or retained prepared-history code anchors, ledger-mapped memory history, and exact dependency
  provenance; re-anchored the current helper ranges. Verification metadata remains closeout-owned.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
