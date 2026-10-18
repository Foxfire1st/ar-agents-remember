# mcp/src/agents_remember/cli/dashboard_review_summary.py

## Governing Overview

[Area overview](../../../overview.md)

## Purpose

Bind native review-summary dependency observations at dashboard composition, without moving selection authority into serving.

## Code Commentary

The port pairs initial selection observations with dependencies reported by native comparison resolution. Initial inputs include enclosure-directory selection, the recorded contract, that enclosure’s `knowledge-worklist.json`, and applicable repositories/worktrees; absent paths remain observations. Invalid review context follows no invalid path. Resolved inputs include code/memory repositories, comparison records and database content. The callback observes native baseline captures; memoization here is scoped to a read, not global admission. ContentRead tracks database bytes rather than derived-index timestamps. This composition owns dependency wiring, not counts, path authority or an atomic workspace snapshot.

The explicit worklist path is an added initial dependency. Regenerating that native worklist can invalidate summary reuse even while the task selector and contract stay fixed. It is an input observation, not proof the file is present or a new semantic authority.

## Evidence

- Initial selection, contract, worklist-path and applicable repository/worktree observations preserve explicit absence. [1]
- Resolved repository/record/database inputs use content observations for derived-index bytes. [2]
- Config-bound native reading and capture observation remain request-scoped dependency wiring. [3]
