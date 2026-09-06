# mcp/src/agents_remember/worktrees/modules/quality/execution/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/execution/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:15:01+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Carries one selected certificate-reuse decision and its exact original predecessor objects into the code executor, with canonical launch-boundary validation.

## Code Commentary

### Logic

`RetainedGateExecution` holds the original certificate, result and publication and serializes all three. `CodeCertificationExecution` holds the frozen run, selected reuse plan, actual input changes, supplied certificate chain and retained reused prefix.

`validate` reparses the frozen run, reuse plan, input changes and certificates through their canonical models, then requires exact equality with `plan_certificate_reuse`. The retained certificate sequence must equal the complete lower prefix preceding `first_gate`. Every retained result and publication is reparsed and cross-bound to its certificate, and each original result must be green.

`first_gate` accepts only 1–4. Gate-5-only or finalization-only decisions refuse code-executor launch. `payload` validates the execution, requires a nonblank unpadded comparison reference, serializes the original records and adds a digest of the complete execution payload.

### Conventions

The lifecycle journal owner supplies selected authority. This transport validates its own inputs but does not replace journal CAS, live-owner checks, physical publication reads or comparison-commit resolution.

### Invariants And Boundaries

- R21 determines the suffix; a caller cannot append a hand-picked reused prefix.
- Gate-5 and finalization-only reuse have zero code starts and cannot enter this code transport.
- Payload digest identity includes the supplied comparison reference and serialized originals.
- Original result/publication authority is checked; no success is reconstructed from a summary.

### Todos

None recorded for this file's bounded responsibility.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Retained transport serializes the complete original objects. | `RetainedGateExecution` | mcp/src/agents_remember/worktrees/modules/quality/execution/models.py:28-38 |
| The execution contract recomputes canonical reuse and validates its exact prefix. | `CodeCertificationExecution` | mcp/src/agents_remember/worktrees/modules/quality/execution/models.py:42-100 |
| Only code gates may launch through this transport. | `first_gate` | mcp/src/agents_remember/worktrees/modules/quality/execution/models.py:81-85 |
| Validation reparses canonical objects and checks original green publication authority. | `validate` | mcp/src/agents_remember/worktrees/modules/quality/execution/models.py:51-78 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |

## Update History

- 2026-09-06T15:15:01+00:00 — Created from the complete source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented the selected-original, terminal or transport responsibility and its actual neighboring owners. Source verification is not execution or acceptance evidence.
