# mcp/tests/test_active_projector_singleflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_active_projector_singleflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Proves concurrent reconnects replace one retired active projector exactly once.

## Code Commentary

### Logic

The async regression drives two callers through the same post-retirement service lookup and
asserts that they converge on one newly constructed projector rather than racing into duplicate
pollers and projection graphs.

### Conventions

The test targets lifecycle ownership, not mapper behavior.

### Invariants And Boundaries

- A retired projector is never reused.
- Concurrent replacement is singleflight at the service boundary.
- The resulting callers share one live projector.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Replacement owner. | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/service.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  concurrent projector-replacement regression. Verification metadata remains blank until commit.
