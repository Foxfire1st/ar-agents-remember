# hosted_control_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/hosted_control_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Projects adapter snapshots into additive terminal catalog fields and converts protocol activity
to the serving turn-state vocabulary.

## Code Commentary
### Logic
Snapshot projection preserves existing catalog schema members while adding control state,
activity, acceptance, vendor identity, pending interaction, sequence, and raw vendor detail.
Legacy raw-TUI harness rows are explicitly marked unsupported. Turn state is derived from adapter
activity and control, not pane text.
### Invariants And Boundaries
Projection is evidence storage, not delivery or consumption. `paneDiagnostic` remains diagnostic
detail and cannot authorize readiness, delivery, or supervisor action.

## Docs References
No relevant external/domain documentation was configured; catalog and projection tests are authoritative.

## Repo-Internal References
- [terminal_catalog.py](terminal_catalog.py) owns persisted additive fields.
- [terminal_liveness.py](terminal_liveness.py) supplies live snapshots.
- [turn_state.py](turn_state.py) retains diagnostic classification boundaries.

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented additive adapter projection, legacy unsupported
  labeling, and protocol-derived turn state.
