# mcp/src/agents_remember/serving/cadence.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository.

### Repo-Internal References

- [projector.py](projector.py.md) takes the cadence as `Projector(config, cadence=...)`.
- [app.py](app.py.md) takes it as `create_app(config, cadence=...)`.
- [daemon.py](daemon.py.md) names a child's cadence without importing the projector.

### Cross-Repo References

No meaningful cross-repo references.
