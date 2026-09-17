# mcp/src/agents_remember/memory_quality/style/citations/provenance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/provenance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../overview.md` |

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

## Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source applies. | N/A | N/A |

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Historical memory provenance derives once from reachable attribution and validates the selected commit. | n/a | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the class `Read`. | `Read` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:43-46 |
| Defines the class `LockedVersion`. | `LockedVersion` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:49-53 |
| Defines the class `GitHistory`. | `GitHistory` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:56-114 |
| Defines the class `Histories`. | `Histories` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:117-193 |
| Defines the class `VersionRead`. | `VersionRead` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:196-199 |
| Defines the function `requirement_candidate_for`. | `requirement_candidate_for` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:202-212 |
| Defines the function `package_candidate_for`. | `package_candidate_for` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:215-227 |
| Defines the function `manifest_error`. | `manifest_error` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:230-234 |
| Defines the function `requirement_versions`. | `requirement_versions` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:237-278 |
| Defines the function `package_lock_versions`. | `package_lock_versions` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:281-296 |
| Defines the function `package_from_path`. | `package_from_path` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:299-303 |
| Defines the function `ecosystem_from_path` — The one resolved-version namespace capable of proving ``path``'s identity.. | n/a | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `normalised_package`. | `normalised_package` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:317-318 |
| Defines the function `_git_error`. | `_git_error` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:321-323 |


## Cross-Repo References

No separate cross-repository implementation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external implementation source applies. | N/A | N/A |

## Update History

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Replaced cache-file mapping reads with once-per-observation Git attribution for historical citation provenance. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


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
