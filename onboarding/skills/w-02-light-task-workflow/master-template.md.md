# skills/w-02-light-task-workflow/master-template.md

## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This template defines a master plus flat light-subtask series when one task no longer fits a
single-page plan. It connects one integration branch and multiple leaf enclosures to the approved
requirement corpus.

## Code Commentary

### Logic

The master carries a filtered table of stable IDs, exact versions, canonical packet links, and
manifestation leaves. Each leaf names exactly one primary revision and may reference adjacent
dependency or preservation constraints. Subtasks close incrementally into the master branch;
the master owns the single release boundary.

The scaffold includes a Requirement Attempt Summary with attempts, rejection history/count,
current state, dominant open failure class, and authoritative leaf-journal links. It is regenerated
from immutable worker/reviewer records and is explicitly non-gating; leaf journals win every
conflict or stale-summary case.

Only formal review-handoff attempts appear in that summary. Internal implementation/test/evidence
runs remain separate protocol events. Leaf records stay lightweight and requirement-specific by
linking content-addressed frozen expanded evidence instead of copying the complete master corpus.

An unrelated later candidate does not reopen an accepted attempt; only the two bounded
invalidation authorities apply.

### Conventions

- Flat numbered files are stable creation identities; the master's list determines execution
  order.
- One master integration branch holds all leaf integrations.
- Each active subtask receives its own enclosure/worktree.
- Decision logs stay append-only.

### Invariants And Boundaries

- Corpus approval precedes both master and leaf creation.
- A master summarizes but never rewrites requirement contracts.
- No leaf may claim closure of multiple independently falsifiable requirements.
- Every revision appears in worker evidence and independent adjudication.
- Requirement version changes invalidate and rebrief only affected work.
- The summary is observation, never requirement, task, lifecycle, closeout, integration, or queue
  authority.

### Todos

None.


## CCR-R12@v5 Light-Task Boundary

A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Full quality, full tests, full memory quality, certification, and review remain explicit operations and are not automatic closeout or integration prerequisites.

## Evidence

### Docs References

No external Domain Documentation source governs this topology template.

### Repo-Internal References

- The master projects requirements to manifestation subtasks. [1]
- Each subtask names one primary revision and adjacent constraints separately. [2]
- Usage rules preserve approval, versioning, and evidence boundaries. [3]
- The master summary exposes attempt state while preserving leaf-journal authority and a non-gating boundary. [4]

### Cross-Repo References

The target repository supplies its integration, check, and release policy; this template supplies
only lifecycle topology.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.
