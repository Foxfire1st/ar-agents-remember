# mcp/src/agents_remember/certification/planning.py

## Governing Overview

[Certification overview](overview.md)

## Purpose

Compiles one validated canonical registry into immutable, candidate-bound per-gate plans and
re-admits external plans only when they exactly equal that authoritative compilation.

## Code Commentary

### Logic

`compile_certification_plan` requires a clean exhaustive registry report and a declared profile,
then compiles every selected gate in order. Each gate carries earlier-gate prerequisites, exact
rail definitions, canonical waves, and its own digest; the enclosing plan binds the registry,
profile, candidate, and full gate catalog. `admit_certification_plan` reconstructs those exact
bytes and rejects any substitution.

### Conventions

Registry compilation, not caller-authored JSON, is plan authority. Rail ordering comes from the
canonical registry and wave ordering comes from the model's deterministic dependency algorithm.

### Invariants And Boundaries

- Invalid registries and unknown profiles fail before plan publication.
- Every gate selected by the profile is compiled; a certifying plan cannot delete a barrier.
- Registry digest, profile identity/kind, candidate identity, rail catalog, waves, and plan digest
  must all match canonical reconstruction.
- Admission has no compatibility or partial-plan fallback.
- This module plans work but does not execute adapters or select repository-specific rail content.

### Todos

Execution consumes admitted plans in a later owner.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation could be checked.

### Repo-Internal References

- Compilation rejects invalid registries and binds every selected gate to the exact candidate. [1]
- External plans are authorized only by byte-equivalent canonical reconstruction. [2]
- Each gate plan includes all earlier profile gates as barriers plus deterministic rails and waves. [3]
- Compiled rails preserve ownership, authority, applicability, evidence, dependency, and artifact contracts. [4]

### Cross-Repo References

The selected profile is supplied by a repository consumer; no repository name or command is
embedded here.

- Planning selects generic profile-applicable declarations from the canonical registry. [5]
