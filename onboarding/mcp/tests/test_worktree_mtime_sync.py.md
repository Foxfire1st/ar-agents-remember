# test_worktree_mtime_sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_mtime_sync.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`                |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_worktree_mtime_sync.py` verifies the memory-worktree mtime-sync step that
enables GrepAI clone reuse. `git checkout` stamps fresh mtimes on all files;
GrepAI's watcher skips unchanged files by `ModTime`, so a freshly-checked-out
memory worktree appears fully modified and triggers a full re-embed — defeating
the DB clone. `_sync_worktree_memory_mtimes` mirrors source-repo mtimes onto the
worktree so the watcher reuses the existing index.

## Code Commentary

### Logic

Fixtures build a source (`memory-repos/ar-x`) and target (`worktrees/x/memory-x`)
directory pair. Two files exist in both (`memory.md`, `onboarding/overview.md`),
stamped OLD in source and NEW in target. One file exists only in target
(`only-in-target.md`, stamped NEW). A `.git/HEAD` file exists in target (must
be skipped).

`MtimeSyncTests`:

- `test_syncs_matching_files_to_source_mtime`: after sync, both matching files
  have mtime ≈ OLD; `filesSynced=2`, `filesMissingInSource=1`.
- `test_target_only_file_is_left_untouched`: `only-in-target.md` mtime stays NEW.
- `test_git_dir_is_skipped`: `.git/HEAD` mtime stays NEW and is not counted.
- `test_dry_run_changes_nothing`: `dry_run=True` → `state="skipped"`, `memory.md`
  mtime still NEW.

### Conventions

Uses `os.utime` to set synthetic past/future mtimes. No Git, Docker, or network
access; pure filesystem operations via `tempfile.TemporaryDirectory`.

### Invariants And Boundaries

The tests protect: only matching files (present in both source and target)
have their mtime overwritten; `.git` subtrees are excluded; target-only files
are untouched; dry-run is a no-op; `filesMissingInSource` counts target files
absent from source without failing the sync.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_sync_worktree_memory_mtimes` lives in the worktree start module. | `_sync_worktree_memory_mtimes` | mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:79-118 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces worktree-memory mtime synchronization used for safe provider index reuse.

### Current Invariants

- Only byte-identical files inherit source mtimes.
- Missing, divergent, or differently typed paths keep their own evidence and are not masked.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma alignment only; the documented mtime-sync behavior is unchanged.

- 2026-06-01T00:00+02:00 — Created onboarding for the new mtime-sync tests.
