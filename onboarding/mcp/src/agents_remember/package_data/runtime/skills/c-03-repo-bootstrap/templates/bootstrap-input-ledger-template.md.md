# bootstrap-input-ledger-template.md

## Purpose

This template defines the source-intake ledger used before bootstrap agents ask for additional sources or proceed into research, including source deltas for existing-memory slice maintenance.

## Code Commentary

### Logic

The template captures target repo, control mode, bootstrap mode, memory root, onboarding root, topology, branch, source inventory gate status, presented source inventory, excluded sources, weak categories, user-added sources, corrections, source deltas, settings path-rule exclude review, cross-repo context, assumptions, hard stops, and operator decision.

### Conventions

The ledger is the durable record of what sources were presented and accepted or rejected. It should be written after the source inventory review, before scout and deeper bootstrap work or automated execution.

### Invariants And Boundaries

The source inventory must be shown before asking for additions, and the ledger should not cite source registries as proof. It is an intake decision artifact, not evidence for durable behavior claims.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The input ledger records run metadata, onboarding root, source inventory gate status, and the presented source inventory with status, planned use, and user decision. [1]
- The template captures excluded sources, weak source categories, additional user sources, corrections, source deltas, settings path-rule exclude review, cross-repo context, assumptions, hard stops, and proceed/no-proceed decision. [2]
- `c-03-repo-bootstrap` skill requires source inventory review to be written to `bootstrap/input-ledger.md` using this template before automated execution starts. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
