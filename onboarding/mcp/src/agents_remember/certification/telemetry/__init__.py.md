# mcp/src/agents_remember/certification/telemetry/__init__.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing documentary
artifacts for this change scope are the CCR-R16@v3 requirement packet
(`requirements/CCR-R16-v3-durable-phase-telemetry.md`) and the 260831-CCR-L16 leaf task doc
(`16_durable-gate-and-rail-telemetry.md`). Task artifact paths are not repo-relative citations, so
those facts are recorded as prose here: the packet normatively requires one execution-coherent
durable stream whose cost, order, zero-start barriers, recovery, and public state are
reconstructable without ephemeral-log parsing, and the leaf owns exactly that manifestation.

### Repo-Internal References

- The package re-exports the public telemetry surface from five owning modules. [1]
- `__all__` fixes the complete public telemetry surface. [2]
- The certification facade imports the telemetry surface through this package. [3]

### Cross-Repo References

No cross-repository implementation boundary is owned here.
