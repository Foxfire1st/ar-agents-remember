# mcp/src/agents_remember/memory_quality/style/citations/candidate/git_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/candidate/git_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T02:22:00+02:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Select citation source files from one exact Git tree and prove the selected files' current bytes before direct resolution or repository indexing.

## Code Commentary

### Logic

`GitSourceCandidate.members` verifies the repository root and tree object, then reads the recursive NUL-delimited Git census. It retains blob paths, excludes non-blob entries such as gitlinks, and refuses absolute, traversal, noncanonical, or duplicate member names.

`_identity` checks the root and each parent with `lstat` and requires a regular physical member. `verify` collects these identities, enforces the shared source-size budget before reading bodies, and hashes changed or unproved members in batches of at most 64 using Git's `hash-object --no-filters`. Each hash must match the selected blob and its metadata identity must remain unchanged after hashing. Cached proofs are reused only while the observed identity matches.

`resolve` proves one member before returning its path. `state` proves the eligible sorted population, excludes skipped binary suffixes and the memory subtree, and emits the source-index owner's `TreeState`. Git membership controls this population even for tracked files inside normally skipped build directories or ignored paths.

### Conventions

Git commands use the kernel runner. `Identity`, `TreeState`, `SourceFile`, `SourceIndexError`, and source-budget policy come from `source_index_state`.

### Invariants And Boundaries

- An existing filesystem file is insufficient: code lookup requires membership in the selected tree and matching unfiltered blob bytes.
- Dirty or missing selected files, unsafe physical paths, unexpected hash populations, and observed changes during hashing refuse acquisition.
- This owner does not lock source files or prevent an external writer from changing them after an observation; index leases and publication remain with their existing owners.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate membership comes from the exact Git tree and refuses unsafe census paths. | `members` | mcp/src/agents_remember/memory_quality/style/citations/candidate/git_source.py:34-60 |
| Root and parent traversal require real directories and a regular member. | `_identity` | mcp/src/agents_remember/memory_quality/style/citations/candidate/git_source.py:62-82 |
| Metadata bounds precede batched unfiltered hashing and post-hash identity checks. | `verify` | mcp/src/agents_remember/memory_quality/style/citations/candidate/git_source.py:84-107 |
| Direct code resolution verifies the exact selected member. | `resolve` | mcp/src/agents_remember/memory_quality/style/citations/candidate/git_source.py:109-113 |
| Git-selected source population preserves tracked build/ignored files and excludes memory and skipped suffixes. | `state` | mcp/src/agents_remember/memory_quality/style/citations/candidate/git_source.py:115-136 |

## Update History

- 2026-09-06T02:22:00+02:00 — L30 recovery source review: Created onboarding for exact Git membership, physical-path checks, bounded unfiltered hashing, and candidate source selection. Verified against prepared code commit `97e8ed2e1fae21756c3ad995c30613d4fbfcc503`; source review does not claim Gate-5 execution or recovery acceptance.
