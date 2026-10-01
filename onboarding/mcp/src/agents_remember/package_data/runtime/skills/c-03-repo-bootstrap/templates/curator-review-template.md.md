# curator-review-template.md

## Purpose

This template defines the review artifact used after route-overview or file-onboarding waves.

## Code Commentary

### Logic

The curator review records wave status, files reviewed, compliance checks, reference health issues, bucket corrections, required fixes, developer questions, and next-wave recommendation.

### Conventions

Curator reviews are quality gates. They verify route-local placement, strict one-to-one file onboarding, backlinks, reference buckets, source evidence, no absolute paths, append-only history, and low-confidence handling.

### Invariants And Boundaries

Automated bootstrap mode may skip pauses, but it must not skip curator review artifacts. A curator review may require fixes before a wave is treated as complete.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The curator template records wave metadata, reviewed files, and a compliance checklist for placement, references, links, history, low-confidence claims, and state updates. [1]
- The template captures reference-health issues, bucket corrections, required fixes, developer questions, and next-wave recommendations. [2]
- `c-03-repo-bootstrap` skill Phase 4I requires a curator review after each overview or onboarding wave. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
