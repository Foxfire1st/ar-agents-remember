# mcp/src/agents_remember/worktrees/outside_scratch.py

## Governing Overview

[overview](overview.md)

## Purpose

This module owns the one scratch root an enclosure generation is given when its work cannot live under the enclosure's own `scratch/`: a sandbox has to leave the marker ancestry of the projects home, and a tool may refuse a long path. It derives that root's identity from the enclosure instead of a name, plants a marker inside the root that proves who owns it, and deletes the root when a retained record says its generation has ended. Nothing here is chosen by hand, so no deletion depends on somebody remembering it.

## Code Commentary

### Logic

- `generation_id` hashes `OUTSIDE_SCRATCH_SCHEMA`, the repository, the resolved contract path and the predecessor generation with sha256, and `root_path` names the root `ar-` plus the first twelve hex characters of that digest; `require_socket_budget` refuses a root whose `SANDBOX_SOCKET_SUFFIX` path, formatted with `LONGEST_UID`, would reach `SOCKET_PATH_LIMIT` of 108 bytes.
- `record_for` computes the whole record without touching the disk, and `marker_text` writes `schema`, `repository`, `coordinationRoot`, `contractPath`, `generation` and `path` as sorted JSON with a trailing newline, so `marker_sha256` is a function of identity alone and a recreated root reproduces the digest the enclosure already records.
- `with_root_record` reuses what publication wrote rather than recomputing it: the manifest's `outsideScratch` entry first, then the contract's `outside_scratch_root`, `outside_scratch_generation` and `outside_scratch_marker_sha256`. A retry of one generation therefore cannot found a second root, and only `new_generation=True` folds in a predecessor and replaces the record.
- `ensure_root` validates the parent first through `_parent_problem` — not a symlink, a directory, owned by `os.getuid()`, mode exactly `MANAGED_MODE` 0o700 — then the socket budget, then `require_confinement`, and refuses a root that is itself a symlink.
- A root whose marker digest equals `_identity(record)` answers `{"state": "present"}`; a tree carrying a complete marker of another generation is refused with `carries the marker of generation ...` and left byte for byte as it stands; only a tree with no readable marker is removed and rebuilt, answering `{"state": "recreated"}`.
- `_build_root` stages the work as `.partial-<generation[:12]>-<pid>`, chmods it 0700, writes the marker, then `os.rename`s it into place, so the final name never exists without its marker and an interrupted publication leaves a `.partial-` directory the sweep can reclaim.
- `remove_root` reports instead of raising: `symlink`, `parent-unusable`, `is-the-parent` and `outside-the-managed-parent` for a target that is not a real child of the managed parent; `already-absent` when the root is gone, including a `FileNotFoundError` from a racing remover; then `_marker_problem` with `marker-missing-or-unreadable`, `marker-names-another-path`, `marker-names-another-generation`, `marker-names-another-enclosure` or `marker-differs-from-the-record` before any bytes are deleted.
- `scan_roots` walks names in lexical order strictly above an `after` cursor, takes `MAX_ROOTS` (512) per pass, keeps `.partial-` staging names in the walk, and reports `complete` with an empty cursor when it reaches the end.
- `reconcile` applies `_removal_problem` before either ordinary-root deletion or interrupted-publication cleanup. An ordinary root must also pass `_marker_refusal` and `ended(marker)`; a real `.partial-` directory with a dictionary marker is interrupted staging work, whose marker names its final path, so the ordinary-marker checks do not apply. A refused managed parent leaves both the entries and the reconcile cursor untouched; a valid parent retains the bounded paging and completed-cursor retirement behavior.

## Invariants And Boundaries

- One root per generation: the path is `ar-` plus twelve hex characters of a digest over repository, contract path and predecessor generation, so a successor never reuses its predecessor's root.
- A name is never ownership: the marker inside the tree must name the same path, generation, enclosure and digest the record carries before removal.
- The parent and every root are mode 0700 and owned by the current uid; a symlinked, foreign or group-readable parent refuses allocation and removal alike as `parent-unusable`.
- Only a real directory directly under `OUTSIDE_SCRATCH_PARENT` is removed; a linked root is reported as `symlink` and never followed.
- An enclosure published before this change records no root: `recorded_root` returns `None`, `removal_entry_for` returns `{}`, `ensure_recorded_root` returns `None` and `terminal_blocker` answers `(None, [])`.

## Evidence

- `mcp/tests/test_outside_scratch_root.py`: the generation case derives the identity, asserts the twelve-character name and proves a successor generation gets a different root; the ageing case deletes the tree and proves `ensure_root` recreates an empty root with the identical marker digest, then answers `present` on a second call.
- The sweep cases prove `reconcile` deletes one finished root while reporting `generation-not-ended`, `marker-missing-or-unreadable`, `marker-names-another-path` and `symlink` for the others, and that a `.partial-` staging directory left by an interrupted publication is removed.
- The refusal cases prove a socket path at or over `SOCKET_PATH_LIMIT`, a parent at 0755, a symlinked parent, a foreign marker and a tree of another generation each refuse with its own reason while the tree stays intact, and that a dry run answers `would_remove` without deleting.
