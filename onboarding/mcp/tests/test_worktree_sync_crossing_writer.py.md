# mcp/tests/test_worktree_sync_crossing_writer.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Checks exact selected content, review credit and writer provenance through supported crossing sync.

## Evidence

- A record combining both sides carries product provenance. [1]
- The selected side receives credit for its own exact content. [2]
- Standing follows the selected bytes when the input order changes. [3]

- An unconverted leaf syncing against state-converted main keeps main's converted bytes on unchanged records while retaining the leaf's own edited record and writer. [4]
