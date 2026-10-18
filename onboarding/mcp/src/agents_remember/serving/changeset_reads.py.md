# mcp/src/agents_remember/serving/changeset_reads.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Wrap existing native Git/content reads with exact-input retention for change-set routes, without adding a diff or endpoint parser.

## Code Commentary

Working changed-file reads bind the repository’s working generation and observe applicable .gitattributes paths before native computation. Selected HEAD/branch reads track their literal reference; counters are retained by the exact measured value tuples.

A failed command is not retained as a reusable result. A missing committed file is retained only after native ls-tree proves absence in a readable tree, not merely because show failed. Working text binds the requested path. Every wrapper computes normally when no app-owned cache read context exists; the common cache, not these helpers, owns bounds and stable-observation admission.


## Current Behavior

the read wiring now follows rule 5 and the f0607391/b84bf836 repair. A pair of immutable object ids is served from `cached_read(("changed-files", root, base, head), (), ...)` with no observation at all (`:49-57`); a working view has no cache and runs the native `git_changes.changed_files_with_counts(..., observe=observe)` every time (`:73-81`, R1-06); a ref-keyed or mixed range keeps `_range_inputs` (`:84-104`). `commit_text_or_none` on an id uses `_revision_inputs` = `()` (`:143-152`); `read_git` whose arguments name ids uses `CommitPresence` inputs (`:155-165`); the fixed-read wrapper uses `Retention(keep=...)`. This supersedes the earlier sentence that every working read binds a cached working generation: a working read now has no generation to bind. The exact counter tuple cache remains.

## Evidence

- Working diff counters use the native reader and register attribute inputs. [1]
- A missing text result needs successful native absence proof before retention. [2]
- Only successful fixed native command results are retained. [3]