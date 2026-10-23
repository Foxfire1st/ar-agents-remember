# mcp/tests/test_native_refresh_wiring.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins that the native stores are watched through bounded real roots, that each store write wakes only its own
domain, and that a pass hands the reader exactly the domains that moved.

## Code Commentary

The wiring cases build a coordination tree with stores, archives, temp and a checkout, and check that the native
stores appear as bounded watch roots while the archive and worktree trees are never watched, that each native
store write maps to its own domain, that a withdrawal receipt reaches the held reader on both receipt shapes,
and that the existing own-write lock, temp and mtime filters still drop non-inputs.

The pass cases then pin what the reader is allowed to do: a pass hands it exactly the native domains that moved,
`None` meaning everything and an empty set meaning nothing; a pass builds the canonical task list once and the
rows reuse it; and a heartbeat retains every native fact while only its own domain is reread once the stores are
gone.

The poll cases are the requirement's own: a notice write and a held-queue write wake their domains without a
poll, and the recursive lane never watches the archive or worktree trees.

## Evidence boundary

Source-level pytest cases at the reviewed freeze — a real coordination tree, real config and a counting reader —
not a live-page witness and no measurement: MIK-R200 evidence item 6 is unrun and carried to L36, item 7 unrun.
