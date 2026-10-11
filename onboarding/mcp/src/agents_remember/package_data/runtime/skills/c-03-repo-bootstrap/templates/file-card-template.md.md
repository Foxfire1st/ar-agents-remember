# file-card-template.md

## Purpose

This template defines the file-card work order that constrains a future file-level onboarding worker.

## Code Commentary

### Logic

The file card records source/onboarding targets, classification, context, inputs, bounded reads, explanations, traps and done criteria. The required output is a converted card: source-path title, relative Governing Overview link, prose sections and temporary citation-table evidence, passed through the fixer to numbered evidence and a sidecar. No metadata stamps, Update History, manually authored JSON or number selection belong to that output.

### Conventions

File cards are created before assigning file-level onboarding work except for tiny repositories. They keep file workers scoped and prevent broad rediscovery.

### Invariants And Boundaries

A file card does not replace `c-05-create-or-update-onboarding-files` skill. It prepares bounded instructions for `c-05-create-or-update-onboarding-files` skill file-level onboarding and must keep task planning out of durable onboarding.

### Todos

No file-local follow-up; reference anchors carry currentness.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The bounded work order requires converted title/link/prose and temporary citation tables, then fixer-authored evidence and sidecars. [1]
- `c-03-repo-bootstrap` skill Phase 4G writes file cards for priority source files and requires them before file-level onboarding unless the repo is tiny. [2]
- `c-03-repo-bootstrap` skill Phase 4H says each file worker receives one file card and follows `c-05-create-or-update-onboarding-files` skill for file-level onboarding. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
