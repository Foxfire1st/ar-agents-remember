# mcp/src/agents_remember/models/role_capsules/audiences.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pure validation and projection of operation passages addressed to all stage roles or selected roles.

## Current Contract

all mode returns the block unchanged, with no sections-mode marker validation. sections mode scans the complete operation block, validating even excluded passages; nonblank text before a marker, malformed marker-shaped lines, duplicate/unknown recipients or unknown mode refuse with operation-audience-invalid and source path/line. Canonical markers accept all alone or comma-separated admitted role names. Only common/addressed non-marker lines are retained with original line endings; identity/revision stay on the replaced block. It reads no file and rewrites no selected sentence. The compiler separately hashes selected content so differing projections of the same source remain distinct.

## Invariants And Boundaries

This is candidate-source onboarding, not execution, CODE/MEMORY acceptance, serving-build currentness or permission to publish. The owning caller retains transaction, host and role authority.

## Evidence


- Launch copies detail files, substitutes paths, and records frozen revisions. [1]

- Replay validates regular opened files and frozen revisions at deterministic detail names beside the saved handover in its recorded canonical folder, not mutable corpus sources. [2]

- Per-request detail artifacts use exact admitted bytes beside the handover and write-once publication. [3]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [4]
