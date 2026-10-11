# mcp/src/agents_remember/application/review_meaning_effects.py

## Governing Overview

[Owning route](overview.md)

## Purpose

Project the reviewed owner’s recorded meaning judgments from the resolved after-memory index for both subject answers and navigation outlines.

## Code Commentary

History is filtered by exact owner and admitted attempt-file path before grouping by raw record ID. Changed invariant rows, deleted/retire invariant rows and changed family rows become steps; other dispositions do not. Attempt numbers come from the path, not revision, date or row identity. A baseline index is used only to recover raw identity for retired or after-absent UUID selections: their history still comes exclusively from the after side.

Unreadable/legacy after sides, incomplete indexes, unresolved identities and invalid relevant rows produce unavailable, never an absence claim. A readable complete history with no eligible row produces none. Old family rows missing both effect and own revision remain explicit unrecorded steps; half-recorded rows are invalid. Shared owner-level reads produce outline labels and subject steps without deriving a label or a net effect.

## Evidence

- The resolved after index and optional identity-only baseline feed one record projection. [1]
- The same owner-filtered projection supplies outline labels. [2]
- Only admitted dispositions form steps; old and half-recorded family cases remain distinct. [3]
