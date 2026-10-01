# mcp/src/agents_remember/kernel/recorded_reads.py

## Governing Overview

[mcp package overview](../../../overview.md)

## Purpose

**Record the files a computation read outside any Git tree, with their exact identities (MIK-R09, L09).** A result
computed from Git trees is a function of their content-addressed IDs, so a caller may reuse it for the same IDs; a
computation that also reads plain files (a task's requirement manifest, coordination settings) can be reused only
while those files are unchanged. The mandatory gate's memo keeps every verdict with the read set this module recorded
and hashes each file again before reuse. The recorder was first written inside `requirement_endpoint.py` (ruling
2026-09-30T15:09:25) and moved to the kernel in the review R1 fix round, so other readers (the onboarding gate's
settings resolution) can record too.

## Code Commentary

### Logic

- **Identities.** `bytes_identity(data)` is `sha256:<hex>`; `file_identity(path)` is the identity of a file now: its
  bytes' SHA-256, `absent` (`ABSENT`) when it does not exist, or `unreadable (<error type>)`.
- **`recorded_reads()`** is a context manager: inside it, a `ContextVar` (`_READS`) holds one `{path: identity}`
  dictionary, yielded to the caller and reset on exit, so recording is per thread and per evaluation.
- **`record_read(path, identity=None)`** does nothing outside a recording block. Inside one, it records the identity
  the reader passes (the bytes it actually read), or the file's identity now. A path recorded twice with different
  identities becomes `CONFLICTING` ("conflicting reads"): the file changed while it was being read, and the caller must
  not reuse the result.

### Conventions

- The readers pass the identity of exactly the bytes they read where they have them (`requirement_endpoint._manifest`),
  and record a linked packet before its owner reads it, so a race can only cause a miss.

### Invariants And Boundaries

- **A reused verdict saw the same outside files.** With the memo's re-hash (`memo._Kept.still_read_the_same`), a file
  that changed since is a miss, and a file read inconsistently makes the verdict unkeepable. Proved by
  `test_every_file_read_is_in_the_read_set_and_a_conflicting_read_is_never_kept` and the approval-state test
  (`test_a_kept_pass_is_recomputed_once_an_endpoint_s_approval_state_changes`).
- Outside a recording block the module has no effect, so every other caller of the readers is unchanged.

### Todos

- None.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: why plain-file reads are recorded, and the three identities. [1]
- The identities. [2]
- The recording block and one read. [3]
- The manifest read records exactly the bytes it read. [4]
- The gate records every evaluation's reads. [5]
- The read set and the conflicting read. [6]

### Cross-Repo References

No meaningful cross-repo references found: the recorded files are plain paths the caller names.

No cross-repo boundary is crossed by this file.
