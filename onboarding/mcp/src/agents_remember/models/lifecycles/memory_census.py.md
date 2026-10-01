# mcp/src/agents_remember/models/lifecycles/memory_census.py

## Governing Overview

[Lifecycle models overview](overview.md)

## Purpose

Defines the strict identities, rows, blockers, and result model for the governed-memory structural census. These models validate exact Git-relative artifact paths and keep the census explicitly noncertifying.

## Code Commentary

### Logic

`require_git_relative_path` rejects empty, escaped, NUL-containing, backslash, drive-prefixed, or non-UTF-8 paths. `GovernedArtifactIdentity` distinguishes file, inline, route, and entity artifacts; `MemoryCensusRow` records expected presence and source reasons; `MemoryCensusResult` enforces unique UTF-8 ordered rows.

### Invariants And Boundaries

- Extra model fields are forbidden and records are frozen.
- Entity rows require `entities.md` plus a nonempty subidentity; whole-document artifacts cannot carry one.
- Absence is legal only for a pre-existing artifact and remains a disposition input, not acceptance.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

- The strict census vocabulary is repository-owned. [1]

### Repo-Internal References

- Exact relative path spelling is validated without normalization. [2]
- Artifact identity and entity subidentity rules are enforced together. [3]
- Presence, source reasons, and structural ordering are validated in the census result models. [4]

### Cross-Repo References

None; the model is local to the governed-memory census.
