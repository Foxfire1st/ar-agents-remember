# mcp/src/agents_remember/memory_quality/style/citations/provenance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/provenance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain source applies. | N/A | N/A |

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Historical memory provenance derives once from reachable attribution and validates the selected commit. | L118-L193; L57-L114 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the class `Read`. | L44-L46 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the class `LockedVersion`. | L50-L53 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the class `GitHistory`. | L57-L114 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the class `Histories`. | L118-L193 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the class `VersionRead`. | L197-L199 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `requirement_candidate_for`. | L202-L212 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `package_candidate_for`. | L215-L227 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `manifest_error`. | L230-L234 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `requirement_versions`. | L237-L278 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `package_lock_versions`. | L281-L296 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `package_from_path`. | L299-L303 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `ecosystem_from_path` — The one resolved-version namespace capable of proving ``path``'s identity.. | L306-L314 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `normalised_package`. | L317-L318 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |
| Defines the function `_git_error`. | L321-L323 | [mcp/src/agents_remember/memory_quality/style/citations/provenance.py](mcp/src/agents_remember/memory_quality/style/citations/provenance.py) |


## Cross-Repo References

No separate cross-repository implementation claim is made.

| Finding | Citations | Source Path |
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
