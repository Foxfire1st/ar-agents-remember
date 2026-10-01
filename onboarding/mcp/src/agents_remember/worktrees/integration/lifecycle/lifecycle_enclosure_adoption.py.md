# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_adoption.py

## Governing Overview

[lifecycle operation integration overview](overview.md)

## Purpose

Explicit audited adoption of pre-locator readable worktree enclosures.

## Code Commentary

### Logic

The public surface is `AdoptedLifecycleArtifact`, `LifecycleEnclosureAdoptionReceipt`, `LifecycleEnclosureAdoptionPreview`, `preview_lifecycle_enclosure_adoption`, `apply_lifecycle_enclosure_adoption`. Adoption is an explicit audited dry-run/apply path for a readable pre-locator enclosure. It binds exact bytes, publishes one locator/manifest/journal location, and records an idempotent receipt; it is distinct from schema migration and never runs as an implicit fallback.

Since 260831-CCR (commit `99dc249b`) adoption recognizes the legacy missing-intent generation
archive as a first-class owned artifact: `_LEGACY_MISSING_INTENT_ARTIFACT` (line 30) matches
`closeout-operation.legacy-missing-intent-generation-{n}.json` /
`direct-landing-operation.legacy-missing-intent-generation-{n}.json`, and `_is_legacy_artifact`
(line 265) admits it alongside the pre-L25 `_LEGACY_ARTIFACT`. The report/root scans keep using the
one predicate (lines 225-253), so a legacy missing-intent generation preserved by the store is
adopted (moved) with the enclosure instead of being left behind or treated as an unowned artifact.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- Legacy missing-intent generation archives are owned, adopted artifacts; near matches (e.g. a
  `.log` sibling) stay out.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `AdoptedLifecycleArtifact`; `LifecycleEnclosureAdoptionReceipt`; `LifecycleEnclosureAdoptionPreview` as its public seam. [1]
- The missing-intent generation archive recognition predicate. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Successor-WAL Retirement

Enclosure adoption no longer recognizes `.successor-intent` as a legacy artifact. That standalone
WAL is not recoverable authority under the final design; successor publication is proven by the
terminal archive/receipt/locator and exact predecessor transaction instead.

## CCR-R02@v2 Missing-Intent Archive Adoption

The lifecycle store preserves a superseded legacy missing-intent generation as
`*.legacy-missing-intent-generation-{n}.json` before publishing an intent-bound successor
(`lifecycle_operation_store._retire_missing_intent_generation`). This module treats those exact
archives as owned artifacts so enclosure adoption can move them into the canonical lifecycle root
unmodified. Part of the landed L25 candidate `99dc249b`.
