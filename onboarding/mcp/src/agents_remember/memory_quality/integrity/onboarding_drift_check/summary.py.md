# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T02:47+02:00                     |
| lastVerifiedCommitHash | `b25d52f2b445554bb64115db2f27fd156954bcf3` |
| lastVerifiedCommitDate | 2026-05-24T02:36:33+02:00|
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
  missing, orphaned, and unsupported rows.
- The report path stays temporary; drift reports are not durable memory content.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Context packets and skill-facing drift tools call this summary helper. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py); [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| The memory quality runner wraps actionable rows from this summary as integrity findings. | [check.py](agents-remember-md/mcp/src/agents_remember/memory_quality/check.py) |

## Update History

- 2026-05-24T02:47+02:00: Created after drift summary moved under `memory_quality.integrity`.
