# mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py

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

## Evidence

### Repo-Internal References

- Selection is either filesystem mode or one canonical 40-digit Git tree identity. [1]
- The bounded ready marker validates schema, identity, roots, counters, and candidate selection. [2]
- File metadata retains device/inode/mode/size and nanosecond modification/change times. [3]
- The four bounds, the skip vocabulary, the status vocabulary and the schema version. [4]
- The register's source and authority vocabularies. [5]
- The one input-budget owner, which reports skips instead of raising. [6]
- The cap overrides an operator may supply, with the keys they actually overrode. [7]
- One exclusion decision, carrying the source that made it. [8]
- The register record: its rules, its ignore-file patterns, its authority and its caps. [9]
- One skipped source with its path, size and reason. [10]
- The bounds report the citation check surfaces. [11]
- A source file carries its observed identity and authoritative content digest. [12]
- The full manifest retains file/directory observations and explicit candidate selection. [13]
- Validation distinguishes content staleness from metadata-only change. [14]
