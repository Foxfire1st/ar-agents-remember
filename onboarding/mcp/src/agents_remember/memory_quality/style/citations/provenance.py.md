# mcp/src/agents_remember/memory_quality/style/citations/provenance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/provenance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Historical source and exact dependency-version provenance for citation claims.

## Code Commentary

### Logic

Module-level surface:

- `Read` (class, lines 35-37)
- `LockedVersion` (class, lines 41-44)
- `GitHistory` (class, lines 48-102)
- `Histories` (class, lines 106-170)
- `VersionRead` (class, lines 174-176)
- `requirement_candidate_for` (function, lines 179-189)
- `package_candidate_for` (function, lines 192-204)
- `manifest_error` (function, lines 207-211)
- `requirement_versions` (function, lines 214-255)
- `package_lock_versions` (function, lines 258-273)
- `package_from_path` (function, lines 276-280)
- `ecosystem_from_path` (function, lines 283-291) — The one resolved-version namespace capable of proving ``path``'s identity.
- `normalised_package` (function, lines 294-295)
- `_git_error` (function, lines 298-300)

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
| Defines the class `VersionRead` (lines 174-176). | `VersionRead` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:174-176 |
| Defines the function `requirement_candidate_for` (lines 179-189). | `requirement_candidate_for` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:179-189 |
| Defines the function `package_candidate_for` (lines 192-204). | `package_candidate_for` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:192-204 |
| Defines the function `manifest_error` (lines 207-211). | `manifest_error` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:207-211 |
| Defines the function `requirement_versions` (lines 214-255). | `requirement_versions` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:214-255 |
| Defines the function `package_lock_versions` (lines 258-273). | `package_lock_versions` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:258-273 |
| Defines the function `package_from_path` (lines 276-280). | `package_from_path` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:276-280 |
| Defines the function `ecosystem_from_path` (lines 283-291) — The one resolved-version namespace capable of proving ``path``'s identity.. | `ecosystem_from_path` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:283-291 |
| Defines the function `normalised_package` (lines 294-295). | `normalised_package` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:294-295 |
| Defines the function `_git_error` (lines 298-300). | `_git_error` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:298-300 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
