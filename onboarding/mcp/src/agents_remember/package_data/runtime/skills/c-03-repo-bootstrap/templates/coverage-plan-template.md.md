# coverage-plan-template.md

## Purpose

This template defines the coverage-planning artifact that turns scout and area research into prioritized route, file, evidence, and slice cleanup work.

## Code Commentary

### Logic

The coverage plan records strategy, area coverage goals, route classifications, file classifications, evidence pack needs, deferred routes/files, slice cleanup decisions, developer review questions, and decisions.

### Conventions

Coverage planning happens before governing route maps and waves. It should classify work by risk and value, and in existing-memory slice maintenance it should decide whether stale route memory is refreshed, moved, removed, retired, or preserved.

### Invariants And Boundaries

The plan is scheduling and prioritization input. It should not become durable file behavior documentation or promote low-confidence findings into fact.

### Todos

Fill verification metadata after the source file is committed.

## Evidence

### Repo-Internal References

- The coverage plan template captures strategy, area goals, route classification, file classification, and evidence pack queues. [1]
- The template records deferred routes/files, slice cleanup decisions, developer review questions, and decisions for later waves. [2]
