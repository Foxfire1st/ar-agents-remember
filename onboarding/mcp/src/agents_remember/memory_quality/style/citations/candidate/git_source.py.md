# mcp/src/agents_remember/memory_quality/style/citations/candidate/git_source.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Select citation source files from one exact Git tree and prove the selected files' current bytes before direct resolution or repository indexing.

## Code Commentary

### Logic

`GitSourceCandidate.members` verifies the repository root and tree object, then reads the recursive NUL-delimited Git census. It retains blob paths, excludes non-blob entries such as gitlinks, and refuses absolute, traversal, noncanonical, or duplicate member names.

`_identity` checks the root and each parent with `lstat` and requires a regular physical member. `verify` collects these identities, enforces the shared source-size budget before reading bodies, and hashes changed or unproved members in batches of at most 64 using Git's `hash-object --no-filters`. Each hash must match the selected blob and its metadata identity must remain unchanged after hashing. Cached proofs are reused only while the observed identity matches.

`resolve` proves one member before returning its path.

`state` proves the eligible sorted population, excludes skipped binary suffixes and the memory
subtree, and emits the source-index owner's `TreeState`. Git membership controls this population even
for tracked files inside normally skipped build directories or ignored paths.

**Since 260915-CAPS-L14 the explicit candidate route honours the same register and the same caps the
default walk does.** `state` takes a `CitationIndexCaps` and an `ExclusionRegister`: a member the
register excludes is *reported* on the tree record rather than silently absent, and the surviving
members pass through the shared `apply_source_bounds`, so an oversized member is skipped with its
path and size instead of refusing the tree. **Membership stays Git's answer** — the register and the
caps decide only how much of that population is read. The old `check_source_bounds` call in `verify`
is gone, because a bound that can be satisfied must report rather than raise. This is also the route
that records the `gitignoreAuthority` Git actually exercised, where the default walk would otherwise
carry the register's default `absent`.

### Conventions

Git commands use the kernel runner. `Identity`, `TreeState`, `SourceFile`, `SourceIndexError`, and the source-budget policy come from `source_index_state`; the register and its `excluding_rule` come from `exclusion_register`.

### Invariants And Boundaries

- An existing filesystem file is insufficient: code lookup requires membership in the selected tree and matching unfiltered blob bytes.
- Dirty or missing selected files, unsafe physical paths, unexpected hash populations, and observed changes during hashing refuse acquisition.
- This owner does not lock source files or prevent an external writer from changing them after an observation; index leases and publication remain with their existing owners.
- **An excluded or oversized member is reported, never silently dropped and never a whole-tree refusal.** Membership is Git's decision; the register and the caps only narrow what is read from it.

### Todos

None.

## Evidence

### Repo-Internal References

- Candidate membership comes from the exact Git tree and refuses unsafe census paths. [1]
- Root and parent traversal require real directories and a regular member. [2]
- Batched unfiltered hashing with post-hash identity checks; the shared bound is applied by the caller, not raised here. [3]
- Direct code resolution verifies the exact selected member. [4]
- The candidate population now consumes the register and the caps, reporting what it excludes or skips. [5]
- The register's path-rule decision the candidate population consults. [6]
- The one budget owner, which reports skips instead of raising. [7]
- The register record this route consults, including the authority Git actually exercised. [8]
- The tree record this route emits, carrying the population and its reported skips. [9]
