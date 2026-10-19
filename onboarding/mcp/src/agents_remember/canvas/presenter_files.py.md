# mcp/src/agents_remember/canvas/presenter_files.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Descriptor-anchored presenter reads and scans. The authority directory is opened once and every later component is opened relative to an already held descriptor without following links, so renaming a directory after it was checked cannot redirect a read.

## Code Commentary

- `directory_fd` refuses a symlink at any component, and `open_at` opens one regular child of a held directory with no path re-resolution.
- Writes, creation, unlinking and recursive removal all go through held parents, and `descriptor_path` ties a native path to its held parent for the shared atomic-write and lock owners.
- `scan_files` yields relative path, parent descriptor, name and size while the parent stays open, so enumeration cannot be swapped underneath.

## Evidence

- A directory is opened once and every child is opened relative to a held descriptor. [1]
- Enumeration yields children while their parent descriptor remains held. [2]
