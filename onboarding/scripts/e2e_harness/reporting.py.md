# reporting.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/reporting.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:20:19+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Defines the structured checkpoint contract and deterministic JSON writer used by every harness run.

## Code Commentary

### Logic

A frozen `CheckpointDefinition` owns stable requirement, expectation, and evidence-owner meaning.
`CheckpointRecorder.check` appends actual candidate evidence and raises only after preserving the
failed record; diagnostics remain non-acceptance context.

### Conventions

Definitions are separate from observations so report meaning cannot drift with incidental payload
assembly. JSON output is indented, key-sorted, UTF-8, and newline-terminated.

### Invariants And Boundaries

- Every failed checkpoint is recorded before `CheckpointFailure` escapes.
- Diagnostic rows never count as acceptance proof.
- Report assembly is deterministic and carries the scenario name.

### Todos

None.

## Docs References

No Domain Documentation source is configured or needed for this repository-owned evidence shape.

| Finding | Anchor | Source |
| --- | --- | --- |
| Stable checkpoint meaning and observed evidence are separate records. | `CheckpointDefinition` | scripts/e2e_harness/reporting.py:11-68 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Failure is raised only after the structured checkpoint is appended. | `CheckpointRecorder` | scripts/e2e_harness/reporting.py:25-56 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The report contract is wholly repository-owned. | `write_json` | scripts/e2e_harness/reporting.py:15-72 |

## Update History

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for candidate-bound checkpoint reporting. Verification metadata remains closeout-owned.
