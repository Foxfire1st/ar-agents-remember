# mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T02:22:00+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Define citation source identity, shared input bounds, and schema-9 manifest/readiness values used by index acquisition and storage.

## Code Commentary

### Logic

`ReadyGeneration` is the bounded authority for opening one published database generation. Its reader requires the exact schema/state/key set, canonical generation and snapshot SHA-256 values, bounded integer counters, absolute root spellings, and explicit `candidateTree`. The marker is limited to 16 KiB; frozen readers can validate it without loading per-file state.

`candidate_tree` accepts either `None` for filesystem selection or exactly 40 lowercase hexadecimal digits for the selected Git tree. `Manifest` retains this selection alongside the complete directory/file population and content snapshot. `SourceFile` pairs a filesystem identity with its content digest; `TreeState` and `Validation` carry deterministic observations and the stale/metadata-change decision.

`Identity` captures path, device, inode, mode, size, and nanosecond mtime/ctime.

**`apply_source_bounds` is the single input-budget owner, and it reports rather than refuses.**
`check_source_bounds` — the old raise-on-exceed owner this card used to describe — **no longer exists
in the module**; the four bounds are module constants and the ruling is the developer's 2026-08-20
decision:

| Constant | Value | Meaning when exceeded |
| --- | --- | --- |
| `MAX_SOURCE_FILE_BYTES` | 4 MiB | the file is **skipped**, with a `SourceSkip` naming its path and size |
| `MAX_SOURCE_BYTES` | 512 MiB | the aggregate, applied to the **post-exclusion, post-skip** set; the overflow is dropped largest-first and reported |
| `MAX_SOURCE_HARD_STOP_BYTES` | 2 GiB | past it no index is built at all — a reported, actionable error naming offenders, not a skip list |
| `MAX_SOURCE_FILES` | 100 000 | refused with the route that fixes it |
| `MAX_DATABASE_BYTES` | 256 MiB | unchanged by the ruling |

`SKIP_REASONS` is the closed vocabulary (`per-file-cap`, `total-cap`, `unreadable`) and
`STATUS_WITHIN_CAPS` / `STATUS_CAPPED` / `STATUS_NOT_EVALUATED` the status vocabulary; the skip list
is bounded by `SKIP_SAMPLE_LIMIT` with an exact `skippedCount` beside it. `SCHEMA_VERSION` is now
**10**: the register keys are part of the manifest, and a v9 manifest is refused and rebuilt rather
than read as "no register".

### Conventions

Source-index errors and limits are shared through this module. Serialization uses `candidateTree` in JSON, while the Python value is `candidate_tree`. Database metadata has its own representation but must agree with readiness.

The register's vocabulary is declared here too, because the record and the filter must agree on their
names: `EXCLUSION_SOURCE_PATH_RULES` / `EXCLUSION_SOURCE_GITIGNORE` / `EXCLUSION_SOURCE_CALLER`, and
`GITIGNORE_AUTHORITY_GIT` / `GITIGNORE_AUTHORITY_REGISTER` / `GITIGNORE_AUTHORITY_ABSENT`.

### Invariants And Boundaries

- Missing candidate selection or an obsolete schema cannot silently become a current readiness/manifest value. **A v9 manifest is refused and rebuilt**, so a rebuilt index cannot silently lose the rules that produced its population.
- Filesystem selection and a selected Git tree remain distinguishable even when their indexed content is equal.
- POSIX identity is an invalidation signal; content hashing and physical-path safety remain responsibilities of the acquiring owner. These dataclasses do not freeze or lock files.
- **A bound that can be satisfied never refuses the tree.** Exceeding a cap produces a reported state with a named file and size; only the hard stop refuses the acquisition, and it does so with offenders and a next step.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selection is either filesystem mode or one canonical 40-digit Git tree identity. | `candidate_tree` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:351-357 |
| The bounded ready marker validates schema, identity, roots, counters, and candidate selection. | `ReadyGeneration` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:389-407 |
| File metadata retains device/inode/mode/size and nanosecond modification/change times. | `Identity` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:483-494 |
| The four bounds, the skip vocabulary, the status vocabulary and the schema version. | `MAX_SOURCE_BYTES`; `MAX_SOURCE_FILE_BYTES`; `MAX_SOURCE_HARD_STOP_BYTES`; `SKIP_REASONS`; `SCHEMA_VERSION` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:18-43 |
| The register's source and authority vocabularies. | `EXCLUSION_SOURCES`; `GITIGNORE_AUTHORITIES` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:45-61 |
| The one input-budget owner, which reports skips instead of raising. | `apply_source_bounds` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:272-324 |
| The cap overrides an operator may supply, with the keys they actually overrode. | `CitationIndexCaps` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:69-81 |
| One exclusion decision, carrying the source that made it. | `ExclusionRule` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:106-110 |
| The register record: its rules, its ignore-file patterns, its authority and its caps. | `ExclusionRegister` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:127-172 |
| One skipped source with its path, size and reason. | `SourceSkip` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:176-181 |
| The bounds report the citation check surfaces. | `SourceBoundsReport` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:201-218 |
| A source file carries its observed identity and authoritative content digest. | `SourceFile` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:532-539 |
| The full manifest retains file/directory observations and explicit candidate selection. | `Manifest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:577-592 |
| Validation distinguishes content staleness from metadata-only change. | `Validation` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:637-642 |

## Update History

- 2026-09-17T12:20+02:00 — 260915-CAPS-L14 curator: **corrected this card against a source that changed under it.** It taught `check_source_bounds` and a **64 MiB** aggregate; that function no longer exists in the module and the ruled aggregate is **512 MiB**, so the card was wrong about both the owner and the number. Replaced that paragraph with the current contract: `apply_source_bounds` as the one budget owner, the five bounds in a table with what each means when exceeded, the closed `SKIP_REASONS` and status vocabularies, the bounded skip list with an exact `skippedCount`, and **`SCHEMA_VERSION` 9 → 10** with a v9 manifest refused and rebuilt rather than read as "no register". Added the register's source/authority vocabularies and rows for `CitationIndexCaps`, `ExclusionRule`, `ExclusionRegister`, `SourceSkip`, `SourceBoundsReport` and `apply_source_bounds`, and **re-derived every remaining range** against the 642-line source (this leaf's diff moved readiness from `:61` to `:389`). Verification metadata is left at `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.

- 2026-09-06T02:22:00+02:00 — L30 recovery source review: Documented schema-9 candidate selection and the shared metadata-first source budget; refreshed identity, readiness, and manifest anchors. Verified against prepared code commit `97e8ed2e1fae21756c3ad995c30613d4fbfcc503`; source review does not claim Gate-5 execution or recovery acceptance.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
