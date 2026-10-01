# onboarding-wave-template.md

## Purpose

This template defines route-overview and file-onboarding wave manifests.

## Code Commentary

### Logic

The wave manifest records wave metadata, goal, included cards, excluded/deferred paths, evidence requirements, worker instructions, assignments, done criteria, and developer review questions.

### Conventions

Waves are small, bounded units. Workers read assigned cards first, read only listed evidence, keep planning notes out of durable onboarding, preserve strict one-to-one file mapping, and return changed paths plus unresolved questions.

### Invariants And Boundaries

The wave manifest coordinates workers; it is not durable source behavior documentation. Every included target needs onboarding output or an explicit blocker plus curator review.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The onboarding wave template records wave metadata, cards, deferred targets, evidence needs, worker instructions, assignments, done criteria, and review questions. [1]
- `c-03-repo-bootstrap` Phase 4H writes onboarding wave manifests. [2]
- The onboarding-file worker instructions are governed by the c-05 skill routing section. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
