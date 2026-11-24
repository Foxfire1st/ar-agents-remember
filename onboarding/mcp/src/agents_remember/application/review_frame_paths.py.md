# mcp/src/agents_remember/application/review_frame_paths.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

This module defines shared frame-store paths and the task-wide lock resource.

## Code Commentary

The path helpers derive the same lock resource for callers that already have an admitted task area or frame directory.

## Relationships

The frame store owns guarded access. Inventory persistence and physical-byte accounting reuse the store’s file names.

## Evidence

- Shared metadata and task-lock identities are defined once. [1]
