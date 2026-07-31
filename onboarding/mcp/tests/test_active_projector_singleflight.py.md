# mcp/tests/test_active_projector_singleflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_active_projector_singleflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 widened the in-test `_Projected`
  double's constructor from `(**_kwargs)` to `(*_args, **_kwargs)` so it still absorbs the
  now-positional parameter object `ActiveSessionProjector` is constructed with, and reflowed the
  three gathered `_projector_for` calls onto single lines. The arguments passed to
  `_projector_for` are unchanged and this card names neither the projector constructor nor the
  call shape, so the retired-projector, singleflight-at-the-service-boundary, and
  one-shared-live-projector claims all still hold.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  concurrent projector-replacement regression. Verification metadata remains blank until commit.
