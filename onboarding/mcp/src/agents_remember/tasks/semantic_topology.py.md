# mcp/src/agents_remember/tasks/semantic_topology.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/semantic_topology.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external source is needed for this repository-owned semantic identity.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict frozen models define the complete v2 identity and its two placement modes. | `SemanticTopologyV2`; `SemanticTopologyDagPlacement`; `SemanticTopologyAtomicPlacement` | mcp/src/agents_remember/tasks/semantic_topology.py:53-122 |
| Projection and fingerprint share one canonical structural value and exact work report. | `semantic_topology_projection_with_work`; `semantic_topology_fingerprint_with_work` | mcp/src/agents_remember/tasks/semantic_topology.py:148-238 |
| Version, taxonomy, composite binding, execution nature, and placement all fail closed. | `_require_schema_version`; `_owning_parent_row`; `_dag_placement` | mcp/src/agents_remember/tasks/semantic_topology.py:241-364 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the canonical
  `semantic-topology/v2` file card. Verification remains closeout-owned.
