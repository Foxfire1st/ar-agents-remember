# mcp/src/agents_remember/certification/telemetry/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/telemetry/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T07:08:26+00:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

The package surface for the CCR-R16@v3 durable boundary, gate, and rail telemetry
manifestation (leaf 260831-CCR-L16). This module carries no logic of its own: it re-exports the
complete telemetry vocabulary from its four owning modules - the event-compile adapters
(`adapters.py`), the immutable event/payload schema and closed vocabularies (`models.py`), the
durable reconstruction projection (`projection.py`), the content-addressed journal store
(`store.py`), and the never-raising stream validator (`validation.py`) - and fixes the public set
in `__all__`. Consumers of the certification facade import the telemetry surface through this
package rather than reaching into module-private helpers.

## Code Commentary

### Logic

All names are imported from the four owning modules (`telemetry/__init__.py:3-103`):
`TelemetryExecutionContext` plus the twenty `compile_*` adapters and `span` come from `adapters`;
the event/payload models and constants (`TelemetryEvent`, `EVENT_MATRIX`,
`CLOSEOUT_EVENT_KINDS`, `aggregate_span_totals`, ...) come from `models`; the projection models
and fold entry points (`TelemetryProjection`, `project_execution_telemetry`,
`project_gate_history`) come from `projection`; the journal models (`DurableTelemetryStore`,
`TelemetryJournalEntry`, `TelemetryReplay`, `TelemetryStorePolicy`) come from `store`; and the
readiness surface (`TelemetryReadiness`, `TelemetryValidationReport`,
`compile_telemetry_readiness`, `validate_execution_telemetry`) comes from `validation`.
`__all__` (`telemetry/__init__.py:105-197`) fixes the complete public set of roughly ninety
constants, models, adapters, and functions.

### Conventions

The package mirrors the owning modules exactly and adds no parallel declarations; a symbol is
public here only if its owning module defines it.

### Invariants And Boundaries

- The package never instantiates or validates events itself; all contracts live in the four
  owning modules.
- `__all__` is the single public surface used by `certification/__init__.py``'s telemetry import
  block.
- No telemetry logic, store root, or projection default exists at this level.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root. The governing documentary
artifacts for this change scope are the CCR-R16@v3 requirement packet
(`requirements/CCR-R16-v3-durable-phase-telemetry.md`) and the 260831-CCR-L16 leaf task doc
(`16_durable-gate-and-rail-telemetry.md`). Task artifact paths are not repo-relative citations, so
those facts are recorded as prose here: the packet normatively requires one execution-coherent
durable stream whose cost, order, zero-start barriers, recovery, and public state are
reconstructable without ephemeral-log parsing, and the leaf owns exactly that manifestation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package re-exports the public telemetry surface from five owning modules. | `TelemetryExecutionContext`; `TelemetryEvent`; `TelemetryProjection`; `DurableTelemetryStore`; `TelemetryReadiness` | mcp/src/agents_remember/certification/telemetry/__init__.py:3-103 |
| `__all__` fixes the complete public telemetry surface. | `__all__` | mcp/src/agents_remember/certification/telemetry/__init__.py:105-197 |
| The certification facade imports the telemetry surface through this package. | "from agents_remember.certification.telemetry import (" | mcp/src/agents_remember/certification/__init__.py:146-184 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## Update History

- 2026-09-05T07:08:26+00:00 — L31 final residual curation against frozen code `ea35964985f30080488270e71ac81657ac40682b`: Replaced multiply resolved telemetry names with the unique facade import block; telemetry facade claim unchanged. This scoped repair does not promote the card's verification stamp or certify a gate.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired facade anchors and import coordinates; corrected the owning-module count from four to five as directly enumerated by the imports. No runtime behavior claim changed; source verification metadata was not advanced.

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 durable gate and
  rail telemetry package surface (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
