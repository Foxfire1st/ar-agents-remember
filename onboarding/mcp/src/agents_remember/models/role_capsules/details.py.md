# mcp/src/agents_remember/models/role_capsules/details.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pure manifest step-detail parsing and compilation of named placeholders to exact admitted source bytes.

## Current Contract

parse_detail_declarations accepts a references object and processes only mapping rows with step_detail exactly true. It requires nonblank string source/step and a nonempty list of string roles; other reference metadata stays ordinary. compile_detail_references finds {{detail:path}} placeholders in selected blocks, deduplicating by first appearance. Each named path must be declared for the role and present in admitted by_path or detail-reference-missing refuses with remedy. Output freezes source path, source revision, exact admitted bytes and step without injecting the body into instructions. This pure helper neither enforces word budgets nor writes/replays workspace files; declaration role membership beyond string shape is not an extra validation claim.

## Invariants And Boundaries

This is candidate-source onboarding, not execution, CODE/MEMORY acceptance, serving-build currentness or permission to publish. The owning caller retains transaction, host and role authority.

## Evidence


- Launch copies detail files, substitutes paths, and records frozen revisions. [1]
- Replay validates regular opened files, content revisions and original canonical report binding, not mutable corpus sources. [2]
- Per-request detail artifacts use exact admitted bytes beside the handover and write-once publication. [3]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [4]
