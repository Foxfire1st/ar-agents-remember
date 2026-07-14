# harness_control_factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b` |
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
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

### 260713-PHA-L6 Factory Boundary

Factories no longer inject a synthetic or pinned vendor version. Each built-in adapter owns its
structured startup evidence; unknown harness ids retain the loud unsupported result.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free factory construction and the
  unchanged explicit custom-harness boundary.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: recorded built-in adapter selection and explicit unsupported custom behavior.
