# file-card-template.md

## Purpose

This template defines the file-card work order that constrains a future file-level onboarding worker.

## Code Commentary

### Logic

The file card records source and onboarding targets, classification, governing context, why the file matters, what the worker must explain, required inputs, allowed and disallowed reads, required onboarding sections, reference expectations, traps, open questions, and done criteria.

### Conventions

File cards are created before assigning file-level onboarding work except for tiny repositories. They keep file workers scoped and prevent broad rediscovery.

### Invariants And Boundaries

A file card does not replace `c-05-create-or-update-onboarding-files` skill. It prepares bounded instructions for `c-05-create-or-update-onboarding-files` skill file-level onboarding and must keep task planning out of durable onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The file card template records classification, governing context, worker inputs, allowed/disallowed reads, required sections, reference expectations, traps, questions, and done criteria. [1]
- `c-03-repo-bootstrap` skill Phase 4G writes file cards for priority source files and requires them before file-level onboarding unless the repo is tiny. [2]
- `c-03-repo-bootstrap` skill Phase 4H says each file worker receives one file card and follows `c-05-create-or-update-onboarding-files` skill for file-level onboarding. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
