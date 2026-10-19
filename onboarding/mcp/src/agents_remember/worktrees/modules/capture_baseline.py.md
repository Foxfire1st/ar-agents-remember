# mcp/src/agents_remember/worktrees/modules/capture_baseline.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Hold a request-local proof of equal physical snapshots spanning a private-index capture. Reuse requires the same tree and current index/file snapshot, plus current HEAD when the caller supplied a head binding. Memory review supplies the bracketed memory HEAD; the future-code helper omits this optional binding and checks its route identity separately. Unreadable or changed bound operands force re-derivation.

## Code Commentary

The request-local memo scope may also carry an on_capture observer. Nested scopes inherit the current observer unless explicitly replaced; both observer and any newly-created memo dictionary reset in finally. An accepted unchanged before/after capture notifies that observer with the repository path so cache dependencies include the actual capture owner. This adds observation, not longer-lived reuse or stronger physical atomicity.

Hold a request-local proof of equal physical snapshots spanning a private-index capture. Reuse requires the same tree and current index/file snapshot, plus current HEAD when the caller supplied a head binding. Memory review supplies the bracketed memory HEAD; the future-code helper omits this optional binding and checks its route identity separately. Unreadable or changed bound operands force re-derivation.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- Hold a request-local proof of equal physical snapshots spanning a private-index capture. Reuse requires the same tree and current index/file snapshot, plus current HEAD when the caller supplied a head binding. Memory review supplies the bracketed memory HEAD; the future-code helper omits this optional binding and checks its route identity separately. Unreadable or changed bound operands force re-derivation. [1]

## Current source evidence


- Capture dependency observation is request-local and restored on every scope exit. [2]

## 260928-MIK-L177 The Proof Reads The Capture's Own Census, Never The Worktree

This section supersedes the "equal physical snapshots" account above, which described a before/after
entry walk. The proof no longer walks a worktree, so it never enters `node_modules` or `.venv`.

`note_capture_baseline` now keeps the capture's **own** census — the private index's every entry, with
Git's recorded mode, size, mtime and ctime — instead of a directory walk, and
`capture_baseline_unchanged` re-checks three things: the worktree's own index file still carries the
stamp the capture bracketed, every captured path still carries the stat the capture recorded, and
Git's native status still supplies the same HEAD and the same eligible untracked names. The status is
the one read that could descend into ignored paths, so it is asked for exactly that answer and the
ignored paths are never enumerated.

A doubt is anything the census cannot answer: a staged, renamed, unmerged or trust-flagged input, a
partial or unreadable index, an unreadable status, an added or removed eligible path, or a changed
HEAD the caller bound. Any doubt re-derives; the proof never trusts. `memo_capture_baselines` keeps
its request-local scope and its `on_capture` observer, which receives the **repository root** the
capture was taken in (not the index): `changeset_cache.observe_repository_capture` uses that path as a
repository root and drops the request's object-store census for the layout a capture has just written,
so the next object read re-censuses instead of trusting one taken before the capture. The private
index is a scratch file inside the capture's temporary directory and is never handed to the observer.
