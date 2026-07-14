# harness_control_factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Maps the three built-in hosted harness ids to their protocol adapters and deliberately maps
settings-defined or unknown ids to an explicit unsupported adapter.

## Code Commentary
### Logic
Claude, Codex, and Pi receive their adapter-specific settings and supported version selection.
Codex receives model/effort environment values; Pi uses the pinned supported RPC version. No
custom harness receives a regex, timing, or paste compatibility path.
### Invariants And Boundaries
This is the single factory used by the hosted runner. Unsupported is a truthful capability state,
not an exception that invites a legacy fallback.

## Docs References
No relevant external/domain documentation was configured; adapter implementations and tests are authoritative.

## Repo-Internal References
- [harness_control_runner.py](harness_control_runner.py) owns runner composition.
- [harness_adapters.py](harness_adapters.py) defines adapter contracts.

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: recorded built-in adapter selection and explicit unsupported custom behavior.
