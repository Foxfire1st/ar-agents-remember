# claude_stream_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_protocol.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b` |
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Encodes and parses the structured Claude Code stream-json protocol used for capability negotiation.
Exact package strings belong only to fixtures and smoke baselines.

## Code Commentary
Builds launch flags, validates initialization and capabilities, and extracts safe terminal metadata. A
`success` subtype with `is_error=true` and API 429 remains failed; result text and credentials are not retained.

## Invariants And Boundaries
Structured initialization evidence is authoritative: required commands, models, account/session,
cwd, model, permission, tools, slash commands, and bootstrap fields must validate. Reported CLI
version is opaque evidence; there is no exact-version gate, semver guess, or pane/log/timing
fallback. `/cost` is a local advertised command.

### 260713-PHA-L6 Capability Negotiation

Claude compatibility is decided from the correlated `control_request/initialize` and
`system/init` contract consumed by the adapter. Missing required capabilities fail loudly.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| 429 normalization regression. | `L1-L40` | [test_harness_control_claude.py](../../../tests/test_harness_control_claude.py) |

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: replaced the stale exact-version description with the
  structured Claude capability contract; fixture versions remain non-production evidence.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
