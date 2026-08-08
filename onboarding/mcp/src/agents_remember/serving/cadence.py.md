# mcp/src/agents_remember/serving/cadence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/cadence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af` |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Holds `ProjectionCadence` — the one pacing decision every dashboard process shares — in its own
stdlib-only module. New at 260731-EFA-L2.

The module exists to be importable by the import-light daemon agent-notifier: `daemon.py` needs to name
the cadence it hands a spawned child without importing `projector.py` and, through it, the whole
serving stack. Anything added here must keep that property (stdlib only, no `agents_remember`
imports).

## Code Commentary

### Logic

`ProjectionCadence` is a frozen dataclass with two fields that describe **one** decision:

- `interval: float = 1.0` — the floor between projector ticks.
- `heartbeat: float | None = None` — the ceiling on staleness when nothing in the world changes.

The pairing is the point: setting one without the other is how a "fast" projector ends up serving
hour-old state. `DEFAULT_PROJECTION_CADENCE = ProjectionCadence()` is the module's default value and
is what `create_app` and `Projector` take when the caller says nothing.

`__all__` exports `DEFAULT_PROJECTION_CADENCE` and `ProjectionCadence`.

### Invariants And Boundaries

- Stdlib-only by design. Importing anything from the serving stack here re-couples the daemon
  supervisor to the projector and defeats the module's reason to exist.
- The two bounds move together. A change that exposes `interval` without `heartbeat` (or vice
  versa) at any call site reintroduces the half-configured cadence this type was extracted to stop.

## Docs References

No domain documentation source is configured for this repository.

## Repo-Internal References

- [projector.py](projector.py.md) takes the cadence as `Projector(config, cadence=...)`.
- [app.py](app.py.md) takes it as `create_app(config, cadence=...)`.
- [daemon.py](daemon.py.md) names a child's cadence without importing the projector.

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: created for the new module. Verification metadata stays
  pinned to the pre-commit source history until closeout.
