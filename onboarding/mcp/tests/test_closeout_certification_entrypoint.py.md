# mcp/tests/test_closeout_certification_entrypoint.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Provides production-shaped fixtures for public closeout certification admission and actual isolated worker execution. Only process launch, Dagger subprocess, and continuation seams are injected; profile admission, publication, terminal selection, and operation runtime remain production owners.

## Code Commentary

### Logic

`_fixture` builds a configured queue/contract and declares a changed candidate. `_review_and_declare` writes the leaf task and declares the route. `_executor` prepares an isolated sandbox, runs the admitted profile, publishes reports, and returns real quality evidence while preserving failure/interruption controls.

### Invariants And Boundaries

- Fixture helpers do not claim that a local host run is certifying evidence.
- Published manifests and terminal records come through production owners.
- Failure and interruption paths stop later gates without fabricating downstream certificates.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

- This suite exercises production-shaped entrypoint ownership. [1]

### Repo-Internal References

- The fixture installs the repository profile and declares a changed candidate. [2]
- Task-document and route declaration are performed before execution. [3]
- The executor uses isolated preparation and real report publication owners. [4]

### Cross-Repo References

None; the suite uses repository-local fixtures and owners.
