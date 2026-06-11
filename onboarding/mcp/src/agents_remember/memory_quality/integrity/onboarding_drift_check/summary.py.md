# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`summary.py` runs a bounded onboarding drift summary for context packets,
`drift_check`, and the closeout memory quality gate.

## Code Commentary

### Logic

The helper discovers sidecar onboarding, inline onboarding, and entity catalog
rows through `drift.py`, writes the normal Markdown report under coordination
temp, and returns counts plus a bounded actionable sample. `not_checked()`
provides the stable context-packet response when callers do not request drift.

### Invariants And Boundaries

- Summary generation delegates classification to `drift.py`.
- Actionable classifications are limited to drifted, missing verification,
  missing, orphaned, and unsupported rows; the `ACTIONABLE_CLASSIFICATIONS` set
  is now imported from the shared `models.py`, not defined locally here.
- The report path stays temporary; drift reports are not durable memory content.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Context packets and skill-facing drift tools call this summary helper. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py); [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| The memory quality runner wraps actionable rows from this summary as integrity findings. | [check.py](agents-remember/mcp/src/agents_remember/memory_quality/check.py) |
| `ACTIONABLE_CLASSIFICATIONS` is sourced from the shared models module. | [models.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py) |

## Update History

- 2026-05-31T12:50+02:00 — Dropped the local `ACTIONABLE_CLASSIFICATIONS` set literal and now import it from the shared `models.py`; behavior-preserving. Noted the new source in Invariants And Boundaries and added the `models.py` reference (1.0.0 review remediation).
- 2026-05-24T02:47+02:00: Created after drift summary moved under `memory_quality.integrity`.
