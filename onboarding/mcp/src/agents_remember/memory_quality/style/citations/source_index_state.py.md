# mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T02:22:00+02:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Define citation source identity, shared input bounds, and schema-9 manifest/readiness values used by index acquisition and storage.

## Code Commentary

### Logic

`ReadyGeneration` is the bounded authority for opening one published database generation. Its reader requires the exact schema/state/key set, canonical generation and snapshot SHA-256 values, bounded integer counters, absolute root spellings, and explicit `candidateTree`. The marker is limited to 16 KiB; frozen readers can validate it without loading per-file state.

`candidate_tree` accepts either `None` for filesystem selection or exactly 40 lowercase hexadecimal digits for the selected Git tree. `Manifest` retains this selection alongside the complete directory/file population and content snapshot. `SourceFile` pairs a filesystem identity with its content digest; `TreeState` and `Validation` carry deterministic observations and the stale/metadata-change decision.

`Identity` captures path, device, inode, mode, size, and nanosecond mtime/ctime. `check_source_bounds` is the single input-budget owner: at most 100,000 files, 4 MiB per file, and 64 MiB total. Acquisition and candidate hashing call it on observed metadata before body reads.

### Conventions

Source-index errors and limits are shared through this module. Serialization uses `candidateTree` in JSON, while the Python value is `candidate_tree`. Database metadata has its own representation but must agree with readiness.

### Invariants And Boundaries

- Missing candidate selection or an obsolete schema cannot silently become a current readiness/manifest value.
- Filesystem selection and a selected Git tree remain distinguishable even when their indexed content is equal.
- POSIX identity is an invalidation signal; content hashing and physical-path safety remain responsibilities of the acquiring owner. These dataclasses do not freeze or lock files.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selection is either filesystem mode or one canonical 40-digit Git tree identity. | `candidate_tree` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:24-30 |
| The bounded ready marker validates schema, identity, roots, counters, and candidate selection. | `ReadyGeneration` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:61-152 |
| File metadata retains device/inode/mode/size and nanosecond modification/change times. | `Identity` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:155-201 |
| One metadata-based budget bounds file count, individual file size, and total source bytes. | `check_source_bounds` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:204-221 |
| A source file carries its observed identity and authoritative content digest. | `SourceFile` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:224-242 |
| The full manifest retains file/directory observations and explicit candidate selection. | `Manifest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:253-298 |
| Validation distinguishes content staleness from metadata-only change. | `Validation` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:301-307 |

## Update History

- 2026-09-06T02:22:00+02:00 — L30 recovery source review: Documented schema-9 candidate selection and the shared metadata-first source budget; refreshed identity, readiness, and manifest anchors. Verified against prepared code commit `97e8ed2e1fae21756c3ad995c30613d4fbfcc503`; source review does not claim Gate-5 execution or recovery acceptance.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
