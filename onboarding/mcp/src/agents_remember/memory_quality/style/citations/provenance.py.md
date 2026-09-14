# mcp/src/agents_remember/memory_quality/style/citations/provenance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/provenance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T17:20+02:00 |
| lastVerifiedCommitHash | `270704b86116728a64ada83ee258a0e7726206b4` |
| lastVerifiedCommitDate | 2026-09-14T18:18:08+02:00|
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

- `Read` (class, lines 40-43)
- `LockedVersion` (class, lines 46-50)
- `GitHistory` (class, lines 53-111)
- `Histories` (class, lines 114-184)
- `VersionRead` (class, lines 187-190)
- `requirement_candidate_for` (function, lines 193-203)
- `package_candidate_for` (function, lines 206-218)
- `manifest_error` (function, lines 221-225)
- `requirement_versions` (function, lines 228-269)
- `package_lock_versions` (function, lines 272-287)
- `package_from_path` (function, lines 290-294)
- `ecosystem_from_path` (function, lines 297-305) — The one resolved-version namespace capable of proving ``path``'s identity.
- `normalised_package` (function, lines 308-309)
- `_git_error` (function, lines 312-314)

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
| Defines the class `Read` (lines 40-43). | `Read` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:40-43 |
| Defines the class `LockedVersion` (lines 46-50). | `LockedVersion` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:46-50 |
| Defines the class `GitHistory` (lines 53-111). | `GitHistory` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:53-111 |
| Defines the class `Histories` (lines 114-184). | `Histories` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:114-184 |
| Defines the class `VersionRead` (lines 187-190). | `VersionRead` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:187-190 |
| Defines the function `requirement_candidate_for` (lines 193-203). | `requirement_candidate_for` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:193-203 |
| Defines the function `package_candidate_for` (lines 206-218). | `package_candidate_for` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:206-218 |
| Defines the function `manifest_error` (lines 221-225). | `manifest_error` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:221-225 |
| Defines the function `requirement_versions` (lines 228-269). | `requirement_versions` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:228-269 |
| Defines the function `package_lock_versions` (lines 272-287). | `package_lock_versions` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:272-287 |
| Defines the function `package_from_path` (lines 290-294). | `package_from_path` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:290-294 |
| Defines the function `ecosystem_from_path` (lines 297-305) — The one resolved-version namespace capable of proving ``path``'s identity.. | `ecosystem_from_path` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:297-305 |
| Defines the function `normalised_package` (lines 308-309). | `normalised_package` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:308-309 |
| Defines the function `_git_error` (lines 312-314). | `_git_error` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:312-314 |

## Update History

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): the three `GitHistory` reads (`commit`'s `rev-parse --verify` and `merge-base
  --is-ancestor`, and `file`'s `show`) now hand the runner one
  `GitRunnerOptions(timeout=GIT_METADATA_TIMEOUT_SECONDS)` object instead of a `timeout=` keyword. No
  content impact: this card stated no `run_git` call form, so the reachability, ledger-mapped memory
  history and exact-dependency-version claims above still hold. All fourteen symbol ranges in the
  Logic list and the reference table were re-derived against the current file. Eight rows moved by
  the four-line import growth alone (`VersionRead` 183-186 → 187-190, `requirement_candidate_for`
  189-199 → 193-203, `_git_error` 308-310 → 312-314, and the five others likewise), and six were
  already loose against the file the card cited — `Read` 35-37 → 40-43, `LockedVersion` 41-44 →
  46-50, `GitHistory` 48-102 → 53-111, `Histories` 106-170 → 114-184, `requirement_versions`
  214-255 → 228-269 and `package_lock_versions` 258-273 → 272-287 — so those now name their symbols
  exactly, with `kernel/git_command.py` declaring `GitRunnerOptions` at `:115-128` and `run_git` at
  `:149-213`; verification metadata remains closeout-owned.

- 2026-09-10T04:35+02:00 — CCR-L42 final predecessor-history curation: documented reachable current
  or retained prepared-history code anchors, ledger-mapped memory history, and exact dependency
  provenance; re-anchored the current helper ranges. Verification metadata remains closeout-owned.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
