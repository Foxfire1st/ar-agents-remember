# mcp/src/agents_remember/tasks/semantic_topology.py

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Defines `semantic-topology/v2`, the canonical candidate-local scheduling identity used by closeout
doors and projection currentness. It includes only structural task facts and deliberately excludes
delivery, progress, evidence, lifecycle, and prose state.

## Code Commentary

### Logic

`SemanticTopologyV2` binds exact sprint, master, and leaf refs; the uniquely matching structural
parent row; the effective master execution nature; and either an atomic-sequential placement or one
DAG node plus its incident relevant edges. Projection validates the field-effect taxonomy and
canonical composite leaf binding, then reads the candidate slice from the shared graph index.
Canonical JSON bytes produce the fingerprint. Typed `SemanticTopologyError` statuses preserve
missing, ambiguous, malformed, unsupported-version, and graph-index refusals.

### Conventions

- Topology projections are frozen strict models with extra fields forbidden.
- Aliases are explicit, and canonical serialization sorts keys before hashing.

### Invariants And Boundaries

- The schema version is exactly `semantic-topology/v2`; no v1 or whole-document fallback exists.
- Non-structural task fields never enter the projection or fingerprint.
- Parent-row identity is composite and exact, not inferred from a stem alone.
- DAG projection consumes the prevalidated graph index; graphless atomic mode is explicit.
- Canonical sorting makes equivalent structural facts byte- and hash-stable.

### Todos

None.

## Evidence

### Docs References

No external source is needed for this repository-owned semantic identity.

### Repo-Internal References

- Strict frozen models define the complete v2 identity and its two placement modes. [1]
- Projection and fingerprint share one canonical structural value and exact work report. [2]
- Version, taxonomy, composite binding, execution nature, and placement all fail closed. [3]

### Cross-Repo References

None.
