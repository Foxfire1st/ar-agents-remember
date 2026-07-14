# test_harness_control_claude_smoke.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude_smoke.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `../overview.md` |

## Governing Overview
[tests overview](../overview.md)

## Purpose
Opt-in credential-safe live smoke for exact Claude Code 2.1.207.

## Code Commentary
Starts the real adapter, submits the advertised local `/cost` command through the correlated path,
requires completed terminal evidence, and shuts down without printing model, credential, environment,
or settings content.

## Invariants And Boundaries
Pinned and opt-in. `/cost` avoids an API request; it does not weaken production 429 handling.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Adapter exercised. | `L1-L25` | [harness_control_claude.py](../src/agents_remember/serving/harness_control_claude.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
